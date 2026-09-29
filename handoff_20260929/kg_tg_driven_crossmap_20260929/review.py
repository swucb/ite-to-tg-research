"""Explicit assistant review of fixed candidate evidence, not automated expert validation."""
import json,hashlib,re,csv,collections as C
from pathlib import Path
P=Path(__file__).resolve().parent;ROOT=P.parent
read=lambda p:json.loads(p.read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def md(x):return str(x).replace('\\','\\\\').replace('[','\\[').replace(']','\\]').replace('|','\\|')
SOURCE={
'N01_iTE_01':('排除','调节温差导致表面迁移，目标应用为摩擦电；并未提供加快 TG 凝胶体相红氧物种扩散的材料改进。'),
'N01_iTE_02':('待定参考','冠醚增强热扩散有原文依据，但热扩散不等同于氧化还原物种补给；该源本身含红氧电极，须先区分已有混合机制。'),
'N01_iTE_03':('排除','建立解释模型不是解决扩散瓶颈的材料调控办法。'),
'N01_iTE_04':('待定参考','有明确溶剂比例调控，但所选证据只说 regulate，未给方向和目标红氧物种；TG 已有共溶剂策略。'),
'N01_iTE_05':('排除','整合电子与离子通路不直接证明红氧物种扩散加快，不能按 integrated conduction 判为解决方案。'),
'N02_iTE_01':('排除','源策略促进聚集并增强离子相互作用，与当前“减弱配对/促进解离”的目标方向相反；不能凭相似词接受。'),
'N02_iTE_02':('保留假设','局部电场与选择性锚定位点共同促进解离，方向与需求相符；源为电容式离子热电，目标为红氧凝胶，适用性尚未建立。'),
'N02_iTE_03':('已有机制参考','促进输运不等于解除配对；重分配到 N01 后有比较价值，但 TG 已有定向网络与通道，不能笼统列为新迁移。'),
'N02_iTE_04':('保留假设（低证据）','源将聚合物链/离子液体作用引起的聚集体解离作为电导改善解释；是作者的模型归因，不能当作独立实测解离证据。'),
'N02_iTE_05':('排除','固态超离子导体晶格模型里浓度过高增加排斥并降低电导，不是 TG 解配对方案。'),
'N03_iTE_01':('排除','电导改善没有证明保水或抗冻；同源还指出无机填料可能损伤其他性质。'),
'N03_iTE_02':('排除','升温导致失水是反例/问题描述，不是保水方案。'),
'N03_iTE_03':('已有机制参考','LiCl 水合促进吸湿恢复和抗冻有依据；TG 已有 LiBr 吸湿盐与空气吸水恢复，不应把吸湿盐原则包装成新方向。'),
'N03_iTE_04':('排除','这条边描述失水限制功能，重复了需求，没有提供解决措施。'),
'N03_iTE_05':('排除','低输出限制应用是宽泛问题，不是失水/冻结的解决措施。'),
'N04_iTE_01':('已有机制参考','源本身为 Fe2+/3+ 液体热电化学体系。增厚降低阻力可作电极参考，但不是从纯离子热扩散迁入 TG 的新机制。'),
'N04_iTE_02':('已有机制参考','源已使用铁氰化物/亚铁氰化物电对；注意上升的是阻力倒数，且只在 t≤40 μm 区间成立，不能无限增厚。'),
'N04_iTE_03':('待定参考','源本身含红氧和热扩散，体积相变增熵对反应效率的贡献不能直接换算为电荷转移速率或抗钝化。'),
'N04_iTE_04':('排除','优于单金属硒化物的宽泛电化学表现，不足以证明在目标铁氰化物凝胶中的动力学和稳定性。'),
'N04_iTE_05':('排除','EIS–TEM 为表征关联方法，不是改善电极的调控措施。')}
TARGET={
'N01_TG_01':('直接相关既有方案','共溶剂同时改善红氧物种输运和溶剂化；已是 TG 原生方案。'),
'N01_TG_02':('直接相关既有方案','破坏水结构的盐改善扩散，是需求原论文给出的方案。'),
'N01_TG_03':('其他体系参考','缩短扩散路径有证据，但源为锌热充电超级电容器；TG 语料归属不等于目标器件机制。'),
'N01_TG_04':('问题描述','冻结/干燥损失输运能力，所选边不是解决措施。'),
'N01_TG_05':('不充分','高浓度引入改善输出不直接证明扩散加快；不能替代目标机制证据。'),
'N02_TG_01':('相关既有方案（电对不同）','高氯酸根弱配位抑制 Fe(III/II) 电解液配对；不能不加区分移植到铁氰化物电对。'),
'N02_TG_02':('不充分','界面促进反应/输运，没有给出抑制配对的直接证据。'),
'N02_TG_03':('问题描述','原需求本身；本论文的双层分隔方案另由锚点扩展保留。'),
'N02_TG_04':('相关既有方案','选择性结合保留反离子移动，与离子选择性有关，但不等于减弱所有配对。'),
'N02_TG_05':('表征信息','测定迁移熵，不是解配对调控办法。'),
'N03_TG_01':('不充分','所选边谈浓度与输出，不能据此认定保水机理；论文标题中的 retainability 也不能替代机制证据。'),
'N03_TG_02':('问题描述','所选边是冻干限制，需另读同论文方案，不能计作解决证据。'),
'N03_TG_03':('不充分','盐析限域影响热电表现，没有给出保水/抗冻证据。'),
'N03_TG_04':('直接相关既有方案','从空气吸水恢复水分，说明自主补水这一原则在 TG 已有。'),
'N03_TG_05':('其他功能','破坏水结构改善反应和扩散；不能自动推出防干燥。'),
'N04_TG_01':('相关既有方案（电对不同）','FeNC 催化改善 Fe2+/3+ 内球反应，可作对照但与铁氰化物体系不同。'),
'N04_TG_02':('相关既有方案（电对不同）','MXene 结构/端基改善动力学，主要为 Fe2+/3+，需要电对兼容性检查。'),
'N04_TG_03':('相关关联证据','PEDOT 电子输运与铁氰化物电子转移相关；原文为相关性，不单独推出某改性必然有效。'),
'N04_TG_04':('背景机制','熵驱动电极红氧过程是背景，并非新催化方案。'),
'N04_TG_05':('背景机制','温差驱动有利反应，不是解除动力学/稳定性瓶颈的调控措施。')}
def main():
 packets=read(P/'review_packets.json');expected=(P/'review_packets.sha256').read_text().strip()
 assert hashlib.sha256((P/'review_packets.json').read_bytes()).hexdigest()==expected
 decisions=[]
 for r in packets:
  status,reason=(SOURCE if r['domain']=='iTE' else TARGET)[r['case_id']]
  decisions.append({'case_id':r['case_id'],'claim_id':r['claim_id'],'status':status,'reason':reason,'reviewer':'assistant_reading_local_abstract_evidence','independent_gold_standard':False})
 supplemental=[]
 for need,cid,status,reason in [
  ('N01','iTE:P0376:r007','已有机制参考','桥状石墨烯加速扩散有依据，但同篇明确为明胶/铁氰化物红氧凝胶热电池，是已有 TG 机制，不是新跨域迁移。'),
  ('N03','iTE:P0621:r010','保留假设','MOF-801/水凝胶外层维持湿度和开路电压有摘要依据；借用外部水分管理架构，目标连续红氧输出仍需验证。')]:
  r=next(r for r in read(P/(need+'_iTE_top200.json')) if r['claim_id']==cid)
  r['case_id']=need+'_iTE_supplemental';r['selection']='Assistant selected after inspecting outcome-related triples in the saved top200; not a top5 result.'
  supplemental.append(r);decisions.append({'case_id':r['case_id'],'claim_id':cid,'status':status,'reason':reason,'reviewer':'assistant_reading_local_abstract_evidence','independent_gold_standard':False})
 write(P/'supplemental_packets.json',supplemental);write(P/'review_decisions.json',decisions)
 ds={d['case_id']:d for d in decisions};lines=['# TG 需求驱动检索：逐项审查','',
 '前 40 项为每个需求在 iTE 和 TG 中各取前 5 篇不同论文。另有 2 项来自保存的前 200 条关系助手扩展查看，已标明原排名。审查人为本助手；不是独立专家评审，也不是效果准确率。','']
 for r in packets+supplemental:
  e=r['edge'];d=ds[r['case_id']]
  lines.extend([f"## {r['case_id']}",'',f"**{d['status']}**：{d['reason']}",'',f"原关系排名 {r['rank_before_paper_grouping']}；检索分数 {r['score']:.3f}（非迁移概率）。",'',f"[{md(e['paper_title'])}](https://doi.org/{e['doi']})",'',f"`{e['claim_id']}`：{md(e['subject'])} → {md(e['predicate'])} → {md(e['object'])}",''])
  for q in dict.fromkeys([e['quote']]+e['context_quotes']):lines.extend(['> '+md(q),''])
  lines.extend([f"条件：{e['conditions']}；断言：{e['assertion']}；联合因素：{e['joint_factors']}。",''])
  for key,title in [('upstream_same_paper','同论文上游'),('downstream_same_paper','同论文下游'),('same_subject_other_claims','同一主体的其他主张')]:
   if r[key]:
    lines.extend([title+'：',''])
    for f in r[key]:lines.append(f"- `{f['claim_id']}`：{md(f['subject'])} → {md(f['predicate'])} → {md(f['object'])}；联合因素：{f['joint_factors']}")
    lines.append('')
 (P/'REVIEW.md').write_text('\n'.join(lines))
 print('Reviewed',len(decisions),'packets;',dict(C.Counter(d['status'] for d in decisions if '_iTE_' in d['case_id'])))
if __name__=='__main__':main()
