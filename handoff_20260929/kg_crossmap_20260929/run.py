"""Offline semantic and typed local-neighborhood retrieval, with evidence-preserving grouping.

Not entity identity merging, causal inference, supervised training, or calibrated transfer probability.
"""
import os
os.environ['HF_HUB_OFFLINE']='1'
os.environ['TRANSFORMERS_OFFLINE']='1'
os.environ['TOKENIZERS_PARALLELISM']='false'
import collections as C
import gzip, hashlib, json, re, time
from pathlib import Path
import numpy as np
from scipy import sparse
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import normalize

OUT=Path(__file__).resolve().parent
ROOT=OUT.parent
INPUT=ROOT/'kg_crossmap_readiness_20260929/repair_snapshot'
MODEL='sentence-transformers/all-MiniLM-L6-v2'
K=20
CORE={'intrinsic_material_mechanism','thermodynamics','ion_mass_transport','electrode_interface_kinetics'}
MECHANISM_ROLES={'mechanism_process','interaction','design_strategy','state_structure'}
GENERIC={'property','description','use','characterization','measurement','prediction','classification','representation'}

def read(p):return json.loads(p.read_text())
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def log(s):print(time.strftime('%H:%M:%S'),s,flush=True)
def compact(s):return ' '.join(str(s).split())
def lexical(s):return re.sub(r'\s+',' ',s.casefold().replace('_',' ').replace('−','-')).strip()
def checksum_texts(texts):return hashlib.sha256(json.dumps(texts,ensure_ascii=False).encode()).hexdigest()

def incidence(e, center):
    """Retain orientation of the stored predicate, not assumed physical causation."""
    r=e['normalization']['relation'];direction='out' if e['source']==center else 'in'
    neighbor=e['target'] if direction=='out' else e['source']
    family=r['relation_family']
    # Unresolved or residual predicates are distinct types, not a generic unknown edge.
    predicate=r['relation'] if family!='unresolved' else 'verbatim:'+lexical(e['predicate'])
    if r.get('residual_predicate_text') and family!='unresolved':predicate+='|residual:'+lexical(r['residual_predicate_text'])
    flags='|'.join([str(bool(r['negated'])),e['assertion'],str(bool(e['joint_factors']) or r.get('joint',False)),r['effect_direction']])
    return neighbor, direction+'|'+family+'|'+predicate+'|'+flags

def make_domain(d):
    g=read(INPUT/d/'graph.json');ns={n['id']:n for n in g['nodes']}
    expressions=sorted((n for n in g['nodes'] if n['kind']=='source_expression'),key=lambda n:n['id'])
    assoc={e['source']:e['target'] for e in g['concept_links']}
    adj=C.defaultdict(list);paperadj=C.defaultdict(list)
    for e in g['edges']:
        for side in ['source','target']:
            adj[e[side]].append(e);paperadj[(e['paper_id'],e[side])].append(e)
    features1=[];features2=[];nodes=[];labels=[];contexts=[]
    for n in expressions:
        oid=n['id'];es=sorted(adj[oid],key=lambda e:(e['scope'] not in CORE,e['claim_id']))
        docs=sorted({e['paper_id'] for e in es})
        # Representative context is explicitly capped; all evidence remains indexed.
        selected=[];used=set()
        for e in es:
            if e['paper_id'] not in used:selected.append(e);used.add(e['paper_id'])
            if len(selected)==3:break
        if len(selected)<3:
            for e in es:
                if e not in selected:selected.append(e)
                if len(selected)==3:break
        text=[]
        for e in selected:
            text.append(f"{e['subject']} {e['predicate']} {e['object']}. Assertion: {e['assertion']}. {e['conditions']}")
            # Nearby source evidence; not old material/mechanism annotation columns.
            quotes=e['context_quotes'] or [e['quote']]
            text.append(compact(' '.join(quotes))[:450])
        context=n['label']+'. '+' '.join(text)
        labels.append(n['label']);contexts.append(context)
        one=C.Counter();two=C.Counter();walks=0
        for e in es:
            neighbor,rel=incidence(e,oid)
            roles=','.join(sorted(ns[neighbor]['roles']))
            central=','.join(sorted(n['roles']))
            scale=.35 if e['normalization']['relation']['relation_family'] in GENERIC else 1.
            one['one|'+central+'|'+rel+'|neighbor:'+roles]+=scale
            # State tokens are categorical annotations, not semantic text embeddings.
            side='subject_state' if e['source']==oid else 'object_state'
            states=','.join(sorted(x['kind'] for x in e['normalization'].get(side,[])))
            if states:one['state|'+rel+'|'+states]+=scale
            for e2 in sorted(paperadj[(e['paper_id'],neighbor)],key=lambda z:z['claim_id']):
                if e2['claim_id']==e['claim_id']:continue
                other,rel2=incidence(e2,neighbor)
                if other==oid:continue
                if walks>=256:break
                roles2=','.join(sorted(ns[other]['roles']))
                two['two|'+central+'|'+rel+'|'+roles+'|'+rel2+'|'+roles2]+=scale
                walks+=1
        features1.append(dict(one));features2.append(dict(two))
        nongeneric=sum(e['normalization']['relation']['relation_family'] not in GENERIC|{'unresolved'} for e in es)
        nodes.append({'id':oid,'label':n['label'],'roles':n['roles'],'concept_id':assoc.get(oid),
          'concept_label':ns[assoc[oid]]['label'] if oid in assoc else None,
          'paper_ids':n['source_record']['paper_ids'],'accepted_paper_ids':docs,
          'claim_ids':[e['claim_id'] for e in es], 'core_claim_ids':[e['claim_id'] for e in es if e['scope'] in CORE],
          'context_claim_ids':[e['claim_id'] for e in selected],
          'degree':len(es),'non_generic_relations':nongeneric,'two_hop_walks':walks,
          'two_hop_cap_reached':walks==256,'one_features':len(one),'two_features':len(two),
          'group_key':assoc.get(oid) or d+':label:'+lexical(n['label'])})
    log(f'{d}: {len(nodes)} expressions, {len(g["edges"])} accepted edges')
    write(OUT/d/'nodes.json',nodes)
    return g,nodes,labels,contexts,features1,features2

def feature_matrix(dicts,name):
    v=DictVectorizer(dtype=np.float32);x=v.fit_transform(dicts).tocsr()
    # log counts and corpus-frequency weighting in a shared feature space.
    x.data=np.log1p(x.data)
    df=np.asarray((x>0).sum(axis=0)).ravel()
    idf=np.log((len(dicts)+1)/(df+1))+1
    x=normalize(x.multiply(idf).tocsr(),copy=False)
    sparse.save_npz(OUT/(name+'.npz'),x)
    write(OUT/(name+'_vocabulary.json'),v.get_feature_names_out().tolist())
    return x

def encode(texts,name,model):
    target=OUT/(name+'.npy');meta=OUT/(name+'_metadata.json')
    digest=checksum_texts(texts)
    if target.exists() and meta.exists() and read(meta)['text_hash']==digest:
        log('reuse '+name);return np.load(target)
    log('encode '+name+f' ({len(texts)} texts)')
    arr=model.encode(texts,batch_size=128,normalize_embeddings=True,convert_to_numpy=True,show_progress_bar=True).astype('float32')
    assert np.isfinite(arr).all()
    np.save(target,arr);write(meta,{'model':MODEL,'text_hash':digest,'shape':list(arr.shape),'max_seq_length':model.max_seq_length})
    return arr

def topk(a,k):
    ix=np.argpartition(-a,k-1,axis=1)[:,:k]
    val=np.take_along_axis(a,ix,axis=1)
    order=np.argsort(-val,axis=1,kind='stable')
    return np.take_along_axis(ix,order,axis=1),np.take_along_axis(val,order,axis=1)

def main():
    start=time.time();OUT.mkdir(exist_ok=True)
    hashes={str(p.relative_to(ROOT)):sha(p) for p in [INPUT/'iTE/graph.json',INPUT/'TG/graph.json',ROOT/'cleaned_ite_tg/data/ite_clean.csv',ROOT/'cleaned_ite_tg/data/tg_clean.csv']}
    patchmanifest=read(INPUT/'manifest.json')
    for p,h in patchmanifest['outputs'].items():assert sha(ROOT/p)==h
    a=make_domain('iTE');b=make_domain('TG');na,nb=a[1],b[1];split=len(na)
    import torch
    torch.set_num_threads(4)
    from sentence_transformers import SentenceTransformer
    model=SentenceTransformer(MODEL,local_files_only=True,device='cpu')
    model.max_seq_length=192
    labels=encode(a[2]+b[2],'label_embeddings',model)
    contexts=encode(a[3]+b[3],'context_embeddings',model)
    del model
    one=feature_matrix(a[4]+b[4],'one_hop');two=feature_matrix(a[5]+b[5],'two_hop')
    onepresent=np.asarray(one.getnnz(axis=1)>0);twopresent=np.asarray(two.getnnz(axis=1)>0)
    reliability=np.array([min(n['degree']/3,1)*(.3+.7*min(n['non_generic_relations']/2,1)) for n in na+nb],dtype=np.float32)
    # No central role hard exclusion: analogies may cross types. Report compatibility.
    matrices={name:{'indices':np.empty((len(na),K),dtype=np.int32),'scores':np.empty((len(na),K),dtype=np.float32)} for name in ['semantic','structure','combined']}
    groups={};candidate_count=0;overlaps=[]
    log('all-pair blocked retrieval')
    with gzip.open(OUT/'candidate_pairs.jsonl.gz','wt',encoding='utf-8') as f:
        for startrow in range(0,len(na),256):
            end=min(len(na),startrow+256)
            slabel=labels[startrow:end]@labels[split:].T
            scontext=contexts[startrow:end]@contexts[split:].T
            semantic=.75*slabel+.25*scontext
            s1=(one[startrow:end]@one[split:].T).toarray()
            s2=(two[startrow:end]@two[split:].T).toarray()
            both2=twopresent[startrow:end,None]&twopresent[None,split:]
            structure=np.where(both2,.65*s1+.35*s2,s1)
            present=onepresent[startrow:end,None]&onepresent[None,split:]
            weight=.25*np.minimum(reliability[startrow:end,None],reliability[None,split:])
            combined=(1-weight)*semantic+weight*structure
            rankinput=structure.copy();rankinput[~present]=-1
            choices={}
            for name,score in [('semantic',semantic),('structure',rankinput),('combined',combined)]:
                ix,val=topk(score,K);choices[name]=ix
                matrices[name]['indices'][startrow:end]=ix;matrices[name]['scores'][startrow:end]=val
            for row,i in enumerate(range(startrow,end)):
                union=set(choices['semantic'][row])|set(choices['combined'][row])
                if onepresent[i]:union|={int(j) for j in choices['structure'][row] if present[row,j] and structure[row,j]>0}
                rank={name:{int(j):r+1 for r,j in enumerate(ix[row])} for name,ix in choices.items()}
                overlaps.append(len(set(choices['semantic'][row])&set(choices['combined'][row]))/K)
                for j in sorted(map(int,union)):
                    x,y=na[i],nb[j]
                    rec={'i':i,'j':j,'iTE_id':x['id'],'TG_id':y['id'],
                         'label_similarity':round(float(slabel[row,j]),6),'context_similarity':round(float(scontext[row,j]),6),
                         'semantic':round(float(semantic[row,j]),6),'structure':round(float(structure[row,j]),6) if present[row,j] else None,
                         'one_hop':round(float(s1[row,j]),6),'two_hop':round(float(s2[row,j]),6) if both2[row,j] else None,
                         'combined':round(float(combined[row,j]),6),'structure_weight':round(float(weight[row,j]),6),
                         'ranks':{name:rank[name].get(j) for name in rank},
                         'role_overlap':bool(set(x['roles'])&set(y['roles'])),
                         'structure_evidence':'available' if present[row,j] else 'missing_not_dissimilar'}
                    f.write(json.dumps(rec,ensure_ascii=False)+'\n');candidate_count+=1
                    key=x['group_key']+' || '+y['group_key']
                    if key not in groups:
                        groups[key]={'group_id':hashlib.sha256(key.encode()).hexdigest()[:16],
                           'iTE_group':x['group_key'],'TG_group':y['group_key'],
                           'iTE_label':x['concept_label'] or x['label'],'TG_label':y['concept_label'] or y['label'],
                           'pair_count':0,'iTE_nodes':set(),'TG_nodes':set(),'iTE_papers':set(),'TG_papers':set(),
                           'best':{},'core_mechanism_priority':False}
                    gr=groups[key];gr['pair_count']+=1
                    for domain,n in [('iTE',x),('TG',y)]:
                        gr[domain+'_nodes'].add(n['id']);gr[domain+'_papers'].update(n['accepted_paper_ids'])
                    gr['core_mechanism_priority'] |= bool(x['core_claim_ids'] and y['core_claim_ids'] and set(x['roles'])&MECHANISM_ROLES and set(y['roles'])&MECHANISM_ROLES)
                    for name in ['semantic','structure','combined']:
                        score=rec[name]
                        if score is None or name=='structure' and score<=0:continue
                        current=gr['best'].get(name)
                        secondary=0 if name=='structure' else rec['semantic']
                        oldsecondary=0 if name=='structure' or current is None else current['semantic']
                        if current is None or (score,secondary,-i,-j)>(current[name],oldsecondary,-current['i'],-current['j']):
                            gr['best'][name]=rec
            if startrow%2560==0:log(f'{end}/{len(na)} source expressions retrieved')
    for name,vals in matrices.items():np.savez_compressed(OUT/(name+'_top20.npz'),**vals)
    for gr in groups.values():
        for k in ['iTE_nodes','TG_nodes','iTE_papers','TG_papers']:gr[k]=sorted(gr[k])
    log(f'grouping {candidate_count} candidate pairs -> {len(groups)} groups')
    with gzip.open(OUT/'groups.jsonl.gz','wt',encoding='utf-8') as f:
        for gr in sorted(groups.values(),key=lambda g:g['group_id']):f.write(json.dumps(gr,ensure_ascii=False)+'\n')
    top={}
    for name in ['semantic','structure','combined']:
        ranked=sorted((g for g in groups.values() if name in g['best']),key=lambda g:(-g['best'][name][name],0 if name=='structure' else -g['best'][name]['semantic'],g['group_id']))
        top[name]=ranked[:100]
        top[name+'_mechanism']=[g for g in ranked if g['core_mechanism_priority']][:100]
    write(OUT/'top_groups.json',top)
    modeldir=Path.home()/'.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2'
    snapshots=sorted(p.name for p in (modeldir/'snapshots').iterdir()) if (modeldir/'snapshots').exists() else []
    manifest={'inputs':hashes,'script_sha256':sha(Path(__file__)),'model':MODEL,'cached_model_revisions':snapshots,
       'scope':'ALL original source expressions; all accepted claims. Deferred edges retained in input, not used for neighborhoods. No papers removed.',
       'semantic_formula':'.75 cosine(label) + .25 cosine(label + <=3 representative claim contexts); max tokens 192',
       'structure_formula':'shared TF-IDF/log-count cosine of typed 1-hop/2-hop features; .65/.35 if both have 2-hop, otherwise 1-hop; paths restricted to same paper; generic edges downweighted .35 before log',
       'fusion_formula':'(1-w)*semantic+w*structure; w=.25*min(reliability_i,reliability_j); reliability=min(degree/3,1)*(.3+.7*min(non_generic_relations/2,1))',
       'weight_status':'fixed exploratory heuristics, not learned or validated probabilities',
       'tie_policy':'structural retrieval and group ranking use no node-text semantic tie-breaker; equal structural scores may yield arbitrary deterministic candidates',
       'grouping':'existing domain concepts when available, else exact normalized labels. Grouping is display/evidence organization, not identity merging; qualifiers remain in original nodes.',
       'n_iTE':len(na),'n_TG':len(nb),'all_pairs_scored':len(na)*len(nb),'candidate_pairs':candidate_count,'groups':len(groups),
       'mean_semantic_combined_top20_overlap':float(np.mean(overlaps)),
       'no_accepted_neighborhood':{'iTE':sum(n['degree']==0 for n in na),'TG':sum(n['degree']==0 for n in nb)},
       'two_hop_cap_reached':{'iTE':sum(n['two_hop_cap_reached'] for n in na),'TG':sum(n['two_hop_cap_reached'] for n in nb)},
       'elapsed_seconds':time.time()-start,'no_training':True,'no_remote_data_transmission':True,
       'readiness_note':'Supersedes blanket stop wording only for exploratory retrieval. Neither repaired graph nor this run is certified for unreviewed causal transfer.'}
    for p,h in hashes.items():assert sha(ROOT/p)==h
    write(OUT/'manifest.json',manifest)
    log('DONE '+str({k:manifest[k] for k in ['all_pairs_scored','candidate_pairs','groups','elapsed_seconds']}))

if __name__=='__main__':main()
