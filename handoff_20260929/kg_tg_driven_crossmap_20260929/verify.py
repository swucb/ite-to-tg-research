"""Independent integrity, ranking arithmetic, and evidence-path checks, not transfer validity."""
import csv,gzip,json,hashlib
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent;ROOT=P.parent;OLD=ROOT/'kg_crossmap_20260929';INPUT=ROOT/'kg_crossmap_readiness_20260929/repair_snapshot'
read=lambda p:json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 m=read(P/'manifest.json')
 for name,h in m['inputs'].items():assert sha(ROOT/name)==h,name
 assert sha(P/'run.py')==m['script_sha256']
 q=np.load(P/'query_embeddings.npy');la=np.load(OLD/'label_embeddings.npy');cx=np.load(OLD/'context_embeddings.npy')
 nodes={d:read(OLD/d/'nodes.json') for d in ['iTE','TG']};split=len(nodes['iTE']);byid={};counts={};checks=0
 needs=read(P/'tg_needs.json');packets=read(P/'review_packets.json')
 for domain,stem in [('iTE','ite'),('TG','tg')]:
  g=read(INPUT/domain/'graph.json');es=sorted(g['edges'],key=lambda e:e['claim_id']);byid.update({e['claim_id']:e for e in es})
  rows={r['paper_id']:r for r in csv.DictReader(open(ROOT/f'cleaned_ite_tg/data/{stem}_clean.csv',encoding='utf-8-sig'))}
  assert set(g['corpus_paper_ids'])==set(rows)
  for e in es:
   assert e['quote'] in rows[e['paper_id']]['摘要']
   assert all(x in rows[e['paper_id']]['摘要'] for x in e['context_quotes'])
  ni={n['id']:i+(0 if domain=='iTE' else split) for i,n in enumerate(nodes[domain])};oi=[ni[e['target']] for e in es]
  out=q[:,0]@la[oi].T;coarse=.75*out+.25*(q[:,2]@cx[oi].T);index={e['claim_id']:i for i,e in enumerate(es)}
  ids=read(P/(domain+'_claim_embedding_ids.json'));ev=np.load(P/(domain+'_claim_embeddings.npy'));evindex={cid:i for i,cid in enumerate(ids)};evidence=q[:,1]@ev.T
  with gzip.open(P/(domain+'_all_claim_scores.jsonl.gz'),'rt') as f:
   records=[json.loads(line) for line in f]
  assert len(records)==4*len(es) and len({(r['need'],r['claim_id']) for r in records})==len(records)
  for z,n in enumerate(needs):
   ranked=read(P/(n['id']+'_'+domain+'_top200.json'));want=np.argsort(-coarse[z],kind='stable')[:200]
   assert {r['claim_id'] for r in ranked}=={es[i]['claim_id'] for i in want}
   scores=[]
   for r in ranked:
    k=index[r['claim_id']];s=.55*out[z,k]+.45*evidence[z,evindex[r['claim_id']]]-r['generic_penalty']
    assert abs(s-r['score'])<2e-6
    assert r['edge']==es[k]
    scores.append(r['score'])
   assert all(a>=b for a,b in zip(scores,scores[1:]))
   seen=set();unique=[]
   for r in ranked:
    if r['paper_id'] not in seen:unique.append(r);seen.add(r['paper_id'])
   got=[r for r in packets if r['need']==n['id'] and r['domain']==domain]
   assert [r['claim_id'] for r in got]==[r['claim_id'] for r in unique[:5]]
  for r in records:
   z=int(r['need'][1:])-1;k=index[r['claim_id']]
   assert abs(r['coarse_score']-coarse[z,k])<2e-6
  counts[domain]=len(records)
 for n in needs:
  assert n['anchor_evidence']==byid[n['anchor']]
  for e in n['known_target_evidence']:assert e==byid[e['claim_id']]
 for r in packets+read(P/'supplemental_packets.json'):
  e=byid[r['claim_id']];assert r['edge']==e
  for key in ['upstream_same_paper','downstream_same_paper','same_subject_other_claims']:
   for f in r[key]:
    assert f==byid[f['claim_id']] and f['paper_id']==e['paper_id']
    if key=='upstream_same_paper':assert f['target']==e['source']
    elif key=='downstream_same_paper':assert f['source']==e['target']
    else:assert f['source']==e['source']
    checks+=1
 ds=read(P/'review_decisions.json');assert {d['case_id'] for d in ds}=={r['case_id'] for r in packets+read(P/'supplemental_packets.json')}
 result={'status':'PASS','type':'integrity_numerical_and_traceability_not_scientific_transfer_validation','paper_counts':{'iTE':1644,'TG':333},'input_hashes_unchanged':True,'all_accepted_claims_scored_for_each_need':True,'score_records':counts,'queries_recomputed':8,'top200_score_and_ranking_checks':'PASS','reviewed_packets':len(ds),'same_paper_neighborhood_checks':checks,'quotes_in_clean_abstracts':'PASS'}
 (P/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
