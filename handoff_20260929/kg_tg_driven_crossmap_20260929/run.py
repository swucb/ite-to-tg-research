"""TG-need-driven, evidence-linked retrieval pilot. No training or causal certification."""
import os
os.environ['HF_HUB_OFFLINE']='1';os.environ['TRANSFORMERS_OFFLINE']='1';os.environ['TOKENIZERS_PARALLELISM']='false'
import json,hashlib,gzip,time,collections as C
from pathlib import Path
import numpy as np
import torch
from sentence_transformers import SentenceTransformer
P=Path(__file__).resolve().parent;ROOT=P.parent;INPUT=ROOT/'kg_crossmap_readiness_20260929/repair_snapshot';OLD=ROOT/'kg_crossmap_20260929'
def read(p):return json.loads(p.read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def log(x):print(time.strftime('%H:%M:%S'),x,flush=True)
NEEDS=[
 dict(id='N01',title='凝胶中离子扩散慢，限制输出',anchor='TG:P0046:complete_v1_cr004',
 outcome='Fast ion diffusion and ion mass transport through polymer hydrogel electrolyte',
 query='How can a material design or molecular interaction increase ion diffusion and mass transport through a hydrogel electrolyte? Seek a stated intervention and a supported transport effect.',
 context='Quasi-solid thermogalvanic hydrogel cell; slow diffusion and limited redox reaction rates jointly reduce power output.',
 target_conditions='凝胶电解质中的氧化还原物种传输；扩散和反应速率共同限制输出。',
 known=['TG:P0046:r005','TG:P0046:r007','TG:P0046:r009']),
 dict(id='N02',title='离子配对妨碍浓度梯度建立',anchor='TG:P0021:complete_v1_cr001',
 outcome='Ion dissociation, suppression of ion pairing, release of free mobile ions',
 query='Which molecular or material intervention suppresses ion association or promotes dissociation and releases mobile ions to establish an ion concentration gradient?',
 context='Thermogalvanic redox electrolyte; ion pairing hinders substantial ion concentration gradients.',
 target_conditions='需区分普通载流离子和氧化还原电对；配对减弱不自动等于浓度梯度或热电势提高。',
 known=['TG:P0021:r001','TG:P0021:r002']),
 dict(id='N03',title='失水与冻结限制凝胶耐久性',anchor='TG:P0061:complete_v1_cr002',
 outcome='Water retention, resistance to dehydration, anti-drying and anti-freezing of hydrogel electrolyte',
 query='Which hydrogel material design retains water and resists dehydration or freezing while preserving ionic conduction?',
 context='PVA gelatin thermogalvanic gel with ferricyanide ferrocyanide redox ions; practical durability requires resistance to drying and freezing.',
 target_conditions='保水/抗冻与电导、氧化还原物种传输需同时满足，不能只改善一个指标。',
 known=['TG:P0061:r003','TG:P0061:r004','TG:P0061:r005']),
 dict(id='N04',title='电子转移动力学受限，催化改进还要稳定',anchor='TG:P0107:complete_v1_cr001',
 outcome='Fast electrochemical redox reaction kinetics and reduced electrode charge transfer resistance',
 query='Which electrode material or interface design improves electrochemical redox kinetics or lowers charge transfer resistance, with stable operation in electrolyte?',
 context='Ferricyanide ferrocyanide gel thermogalvanic cell; Au nanoparticles reduce electron transfer resistance but dissolution and passivation offset short term gains.',
 target_conditions='铁氰化物/亚铁氰化物电对环境；降低电荷转移阻力不保证持续功率，须检查溶解与钝化。',
 known=['TG:P0107:r001','TG:P0107:r005','TG:P0107:r006','TG:P0107:r007','TG:P0107:r008'])]
def main():
 torch.set_num_threads(4)
 graphs={d:read(INPUT/d/'graph.json') for d in ['iTE','TG']}
 nodes={d:read(OLD/d/'nodes.json') for d in graphs};ni={d:{n['id']:i for i,n in enumerate(nodes[d])} for d in graphs}
 labels=np.load(OLD/'label_embeddings.npy');contexts=np.load(OLD/'context_embeddings.npy');split=len(nodes['iTE'])
 model=SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2',local_files_only=True,device='cpu');model.max_seq_length=256
 texts=[n[k] for n in NEEDS for k in ['outcome','query','context']]
 q=model.encode(texts,normalize_embeddings=True,show_progress_bar=False).reshape(len(NEEDS),3,-1)
 np.save(P/'query_embeddings.npy',q)
 allpack=[];stats={};byid={e['claim_id']:e for g in graphs.values() for e in g['edges']}
 for n in NEEDS:
  assert byid[n['anchor']]['status']=='accepted'
  n['anchor_evidence']=byid[n['anchor']];n['known_target_evidence']=[byid[k] for k in n['known']]
 write(P/'tg_needs.json',NEEDS)
 for domain,g in graphs.items():
  es=sorted(g['edges'],key=lambda e:e['claim_id']);offset=0 if domain=='iTE' else split
  oi=np.array([offset+ni[domain][e['target']] for e in es]);si=np.array([offset+ni[domain][e['source']] for e in es])
  # Every accepted claim scored; no paper, scope or material exclusion.
  outcome=q[:,0]@labels[oi].T
  context=q[:,2]@contexts[oi].T
  coarse=.75*outcome+.25*context
  ix=np.argsort(-coarse,axis=1,kind='stable')[:,:200];selected=sorted(set(ix.ravel().tolist()))
  claimtexts=[]
  for k in selected:
   e=es[k];claimtexts.append(f"{e['subject']} {e['predicate']} {e['object']}. "+' '.join([e['quote']]+e['context_quotes'])+' Conditions: '+e['conditions'])
  log(f'{domain}: all {len(es)} claims scored; encoding {len(selected)} shortlisted claim evidence texts')
  ev=model.encode(claimtexts,normalize_embeddings=True,batch_size=64,show_progress_bar=False)
  np.save(P/(domain+'_claim_embeddings.npy'),ev);write(P/(domain+'_claim_embedding_ids.json'),[es[k]['claim_id'] for k in selected])
  sem=q[:,1]@ev.T;selindex={k:j for j,k in enumerate(selected)}
  paper=C.defaultdict(list)
  for e in es:paper[e['paper_id']].append(e)
  with gzip.open(P/(domain+'_all_claim_scores.jsonl.gz'),'wt',encoding='utf-8') as f:
   for z,n in enumerate(NEEDS):
    shortlist=set(ix[z].tolist())
    for k,e in enumerate(es):
     f.write(json.dumps({'need':n['id'],'claim_id':e['claim_id'],'outcome_similarity':float(outcome[z,k]),'coarse_score':float(coarse[z,k]),'reranked':k in shortlist})+'\n')
  for z,n in enumerate(NEEDS):
   ranked=[]
   for k in ix[z]:
    k=int(k);e=es[k];rel=e['normalization']['relation']
    # Explicit low information penalty; no structural-shape similarity score.
    generic=rel['relation_family'] in {'property','description','use','measurement','characterization','classification','representation'}
    score=.55*float(outcome[z,k])+.45*float(sem[z,selindex[k]])-(.10 if generic else 0)
    incoming=[f for f in paper[e['paper_id']] if f['target']==e['source'] and f['claim_id']!=e['claim_id'] and f['source']!=e['target']]
    outgoing=[f for f in paper[e['paper_id']] if f['source']==e['target'] and f['claim_id']!=e['claim_id'] and f['target']!=e['source']]
    same_subject=[f for f in paper[e['paper_id']] if f['source']==e['source'] and f['claim_id']!=e['claim_id']]
    ranked.append({'need':n['id'],'domain':domain,'claim_id':e['claim_id'],'paper_id':e['paper_id'],'score':round(score,6),
      'outcome_similarity':round(float(outcome[z,k]),6),'evidence_similarity':round(float(sem[z,selindex[k]]),6),
      'generic_penalty':.10 if generic else 0,'edge':e,'upstream_same_paper':incoming,'downstream_same_paper':outgoing,
      'same_subject_other_claims':same_subject,'negated':rel['negated'],'effect_direction':rel['effect_direction'],
      'assertion':e['assertion'],'joint_factors':e['joint_factors'],
      'path_warning':'Stored directed adjacency, not proof of causation; alternative conditions and joint factors require source review.'})
   ranked.sort(key=lambda r:(-r['score'],r['claim_id']))
   for rank,r in enumerate(ranked,1):r['rank_before_paper_grouping']=rank
   unique=[];seen=set()
   for r in ranked:
    if r['paper_id'] in seen:continue
    seen.add(r['paper_id']);unique.append(r)
   write(P/(n['id']+'_'+domain+'_top200.json'),ranked)
   for rank,r in enumerate(unique[:5],1):
    r['paper_rank']=rank;r['case_id']=n['id']+'_'+domain+f'_{rank:02d}';allpack.append(r)
  stats[domain]={'registered_papers':len(g['corpus_paper_ids']),'scored_claims':len(es),'scored_need_claim_pairs':len(es)*len(NEEDS),'encoded_claims':len(selected)}
 write(P/'review_packets.json',allpack)
 lines=[]
 for r in allpack:
  e=r['edge'];lines.extend([f"\n{r['case_id']} {r['score']} {e['paper_title']}",f"{e['claim_id']} {e['subject']} --{e['predicate']}--> {e['object']}",'QUOTE '+e['quote']+' '.join(e['context_quotes']),f"CONDITIONS {e['conditions']} JOINT {e['joint_factors']} ASSERTION {e['assertion']}"])
  for key in ['upstream_same_paper','downstream_same_paper','same_subject_other_claims']:
   lines.append(key+':')
   for f in r[key]:lines.append(f"  {f['claim_id']} {f['subject']} --{f['predicate']}--> {f['object']}")
 (P/'review_readable.txt').write_text('\n'.join(lines)+'\n')
 write(P/'manifest.json',{'inputs':{str(p.relative_to(ROOT)):sha(p) for p in [INPUT/d/'graph.json' for d in graphs]+[ROOT/'cleaned_ite_tg/data'/f for f in ['ite_clean.csv','tg_clean.csv']]+[OLD/f for f in ['label_embeddings.npy','context_embeddings.npy','iTE/nodes.json','TG/nodes.json']]},
  'script_sha256':sha(Path(__file__)),'model':'sentence-transformers/all-MiniLM-L6-v2','new_query_and_claim_max_tokens':256,'cached_model_revision':'1110a243fdf4706b3f48f1d95db1a4f5529b4d41','no_training':True,'no_remote_transmission':True,'stats':stats,
  'scope':'Four explicitly selected TG needs; all registered papers retained, all accepted source and target claims scored. Need selection is not an exhaustive inventory of TG problems.',
  'coarse_formula':'.75 desired-outcome / object label cosine + .25 TG context / object context cosine; top200 per need and domain',
  'rerank_formula':'.55 outcome cosine + .45 query / claim evidence cosine - .10 generic property/description penalty',
  'structure_use':'Actual same-paper directed upstream/downstream neighborhoods attached for evidence review; no bonus for mere graph shape; no automatic causal transfer inference.',
  'grouping':'Best ranked claim per paper; top5 papers per need and domain for assistant review. No score confidence threshold; all candidates may be rejected.',
  'limitations':'Not exhaustive retrieval; MiniLM general model; query formulation and assistant labels not independent gold; novelty not established; no quantitative improvement claim over different first-run task.'})
 log('DONE 20 iTE candidate papers + 20 TG existing-work comparison packets')
if __name__=='__main__':main()
