"""Assemble reviewed need-driven hypotheses and existing-work comparisons."""
import csv,json,re,collections as C
from pathlib import Path
from review import md
P=Path(__file__).resolve().parent;ROOT=P.parent;INPUT=ROOT/'kg_crossmap_readiness_20260929/repair_snapshot'
read=lambda p:json.loads(p.read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
CARDS=[
 dict(id='H01',need='N02',title='用缺陷/极化产生的局部电场与锚定位点，尝试调节 TG 中的离子配对',status='保留；优先核查机制适用性',
 source=['iTE:P0589:r001','iTE:P0589:r002','iTE:P0589:r003','iTE:P0589:r004','iTE:P0589:r005','iTE:P0589:r013'],
 target=['TG:P0021:complete_v1_cr001','TG:P0021:r001','TG:P0021:r002','TG:P0285:r004','TG:P0083:r004'],
 provenance='N02_iTE_02，源关系排名 2；不是源、目标节点名称配对。',
 mechanism='SrTiO3 极化与富氧空位表面 → 局部电场及离子选择性锚定位点 → 共同促进离子解离。源还报告迁移不对称性增强，器件采用电容过程。',
 hypothesis='在有配对/浓度梯度限制的 TG 凝胶中，测试这样的局部场与表面位点能否提高目标离子的解离或有效活度，同时保持红氧物种输运。借用的是调控途径，不是把源侧热电系数直接移植。',
 existing='TG 已有双层空间分隔控制梯度，也有在不同 Fe(III/II) 电对中利用弱配位阴离子抑制配对的方案；TG 电极已有氧空位。因此“用氧空位”本身不是新颖性，待查的是凝胶内局部场/锚定位点作用于配对这一具体组合。',
 gap='源为离子热电电容体系，目标含可反应红氧电对。锚定可能提高解离，也可能过度束缚红氧物种；摘要没有给出在目标体系中的净效果。不得把联合因素拆成“氧空位单独有效”。',
 validation='在同组成和含水量条件下比较无填料、缺陷较少/较多的对照，分辨极化、缺陷与表面积影响；测配对/物种状态、红氧物种扩散、电导、热电势、持续功率和电化学稳定性。',
 keyword='SrTiO3|strontium titanate|ferroelectric|local electric field'),
 dict(id='H02',need='N03',title='把 MOF/水凝胶吸水外层用于 TG 的水分管理',status='保留；架构迁移假设，仅覆盖失水部分',
 source=['iTE:P0621:r009','iTE:P0621:r010','iTE:P0621:r011','iTE:P0621:r012','iTE:P0621:complete_v1_cr001'],
 target=['TG:P0061:complete_v1_cr002','TG:P0061:r003','TG:P0061:r005','TG:P0058:r006','TG:P0058:r007','TG:P0048:r006'],
 provenance='N03_iTE_supplemental，源关系排名 105；阅读前 200 条中与水分有关的关系后补选，并非自动前五。',
 mechanism='源将 MOF-801 与水凝胶组成外层，置于质子掺杂 PEDOT:PSS 薄膜上；摘要报告局部相对湿度约 90%，并维持超过 72 h 的开路电压。这里是同论文的结构与表现证据，不把不同主体的边伪装为完整因果链。',
 hypothesis='对易失水的 TG 凝胶，测试相对独立的吸水/缓释水外层能否维持水分与红氧电解质浓度，尽量减少对凝胶本体配方的改动。',
 existing='TG 已有甘油/水抗干燥、吸湿盐以及从空气吸水恢复水分的做法。不能宣称“自主补水”是新机制；待查的差别是 MOF/凝胶外层与 TG 工作层的分离布置及其实际收益。',
 gap='源主要报告湿度和开路电压，未证明 TG 持续负载输出；也未证明抗冻。外层可能改变热阻、温差和水/盐分布，这些都需检查。',
 validation='对照裸 TG、仅水凝胶外层和 MOF/水凝胶外层；在规定温湿度和负载下记录质量、水分/盐浓度、实际两电极温差与持续功率。72 h 开路电压不能替代连续发电证据。',
 keyword='MOF|metal.organic framework|water.harvest'),
 dict(id='H03',need='N02',title='借鉴聚合物链作用促使离子聚集体解离',status='保留备选；机制证据较弱',
 source=['iTE:P0548:r001','iTE:P0548:r002','iTE:P0548:r003','iTE:P0548:r004','iTE:P0548:r005'],
 target=['TG:P0021:complete_v1_cr001','TG:P0285:r004','TG:P0249:r004','TG:P0249:r005'],
 provenance='N02_iTE_04，源关系排名 4。',
 mechanism='MWCNT/聚合物/离子液体体系中，作者用“聚合物链呼吸”模型解释聚集体解离及电导提高；1 wt% 配方的电导增益和 0.25 wt% 的最佳热电表现不能混成同一配方结论。',
 hypothesis='测试 TG 凝胶中可调的聚合物—离子作用，能否改变配对/聚集状态并保持红氧物种移动；不是直接照搬 MWCNT 配方。',
 existing='TG 已有弱配位阴离子抑制配对、聚合物选择性结合保留反离子移动的相关工作。此处的待查差别是动态链作用促进解聚的具体路径。',
 gap='源是非水离子液体凝胶，目标可为水系红氧凝胶。电导增加只是表现，解聚为作者模型归因；不能声称已直接观测并验证了目标机制。',
 validation='先找全文中离子聚集/配对的直接证据，再设计链段作用或交联度对照；同时检查红氧物种扩散、电荷转移及是否引入电子漏电。若只有电导变化，仍不能确认解聚路径。',
 keyword='breathing polymer|dissociation of ion aggregates|polymer.chain.*dissoci')]
def main():
 graphs={d:read(INPUT/d/'graph.json') for d in ['iTE','TG']};edges={e['claim_id']:e for g in graphs.values() for e in g['edges']}
 rows=list(csv.DictReader(open(ROOT/'cleaned_ite_tg/data/tg_clean.csv',encoding='utf-8-sig')))
 lines=['# 从 TG 需求出发的 iTE 迁移候选','',
 '**本轮保留 2 个优先核查假设和 1 个低证据备选。没有一个已被证明可迁移或具有新颖性。**',
 '四个 TG 问题来自原摘要；检索对象是 iTE 的调控关系及同论文邻域。以下为助手回查后的解释，不是模型分数自动生成的结论。','']
 cards=[];checks=[]
 for c in CARDS:
  ev={side:[edges[k] for k in c[side]] for side in ['source','target']}
  assert len({e['paper_id'] for e in ev['source']})==1
  hits=[r['paper_id'] for r in rows if re.search(c['keyword'],r.get('摘要',''),re.I)]
  checks.append({'card':c['id'],'regex':c['keyword'],'searched':'all 333 cleaned TG abstract fields, including retained empty abstract','paper_hits':hits,'limitation':'Keyword non-hit is not semantic absence, full-text search or proof of novelty.'})
  lines.extend([f"## {c['id']}：{c['title']}",'',f"**{c['status']}**。",'',f"检索来源：{c['provenance']}",''])
  for key,title in [('mechanism','iTE 具体提供什么'),('hypothesis','迁移到 TG 要检验什么'),('existing','TG 已经做过什么'),('gap','尚缺什么'),('validation','如何验证')]:lines.extend([f'**{title}：** {c[key]}',''])
  lines.extend([f"本地 TG 摘要定向词检索命中 {len(hits)} 篇。只用于检查明显已有线索，不代表文献中不存在，更不是新颖性证明。",''])
  for side,label in [('source','iTE 源证据'),('target','TG 需求及已有工作证据')]:
   lines.extend([f'### {label}',''])
   papers=C.defaultdict(list)
   for e in ev[side]:papers[e['paper_id']].append(e)
   for paper,es in papers.items():
    f=es[0];lines.extend([f"[{md(f['paper_title'])}](https://doi.org/{f['doi']})",''])
    qs=[]
    for e in es:
     lines.append(f"- `{e['claim_id']}`：{md(e['subject'])} → {md(e['predicate'])} → {md(e['object'])}；条件：{md(e['conditions'])}；联合因素：{md(e['joint_factors'])}")
     qs.extend([e['quote']]+e['context_quotes'])
    lines.append('')
    for quote in dict.fromkeys(qs):lines.extend(['> '+md(quote),''])
  cards.append({**c,'evidence':ev,'transfer_validated':False,'novelty_validated':False})
 write(P/'hypotheses.json',cards);write(P/'target_prior_art_keyword_audit.json',checks)
 (P/'CANDIDATES.md').write_text('\n'.join(lines)+'\n')
 known_ids=['iTE:P0585:r001','iTE:P0585:r002','iTE:P0585:r003','TG:P0096:r002','TG:P0185:r003','TG:P0199:r003','TG:P0199:r006','iTE:P0365:r011','iTE:P0365:r012','TG:P0048:r006','TG:P0048:r007','TG:P0058:r007','iTE:P0376:complete_v1_cr001','iTE:P0376:r007','iTE:P0376:r010','iTE:P1188:r004']
 write(P/'existing_mechanism_evidence.json',[edges[k] for k in known_ids])
 known=['# 降级为已有机制参考的方向','',
 '- 定向/排列通道：iTE P0585 有来源证据，但 TG P0096、P0185、P0199 已有定向网络、排列纳米通道及输运路径。上一版笼统的“把定向通道用于 TG”不再作为新候选。',
 '- 吸湿盐保水：iTE P0365 的 LiCl 水合策略，与 TG P0048 的 LiBr 抗干燥/抗冻及 P0058 的吸水恢复原理重叠。可比较配方，不能当新原理。',
 '- 桥状石墨烯加快扩散：虽然在 iTE 语料中，P0376 原文已经是明胶/铁氰化物红氧凝胶热电池。',
 '- 调整电极厚度降低阻力：iTE P1188 也是铁氰化物液体热电化学器件。它是目标机制的已有参考；t≤40 μm 及阻力倒数限定必须保留。','']
 for k in known_ids:
  e=edges[k];known.extend([f"## {k}",'',f"[{md(e['paper_title'])}](https://doi.org/{e['doi']})",'',f"{md(e['subject'])} → {md(e['predicate'])} → {md(e['object'])}",''])
  for quote in dict.fromkeys([e['quote']]+e['context_quotes']):known.extend(['> '+md(quote),''])
 (P/'EXISTING_WORK.md').write_text('\n'.join(known))
 m=read(P/'manifest.json');v=read(P/'verification.json');ds=read(P/'review_decisions.json')
 count=C.Counter(d['status'] for d in ds if '_iTE_' in d['case_id'])
 report=['# TG 需求驱动的 iTE 机制检索：第二版试跑','',
 '**已经从 TG 的具体问题出发，检索 iTE 可借用的调控关系，并核对 TG 已有工作。结果保留 2 个优先核查假设、1 个低证据备选。**','',
 '| TG 问题 | 本轮结果 |','|---|---|',
 '| 凝胶离子扩散慢 | 找到调控线索，但定向通道等 TG 已有；本轮未保留独立的新迁移假设。 |',
 '| 离子配对阻碍浓度梯度 | 保留局部场/选择性位点促进解离，以及较弱的聚合物链促解聚假设。 |',
 '| 失水/冻结限制耐久性 | 保留 MOF/水凝胶独立外层管理水分的假设；仅针对失水，未证明抗冻。 |',
 '| 电极动力学和稳定性 | 高分结果包括已有红氧热电器件、宽泛电化学性能与表征方法；本轮没有足够证据保留新迁移假设。 |','',
 '先读 [三项候选及原文证据](CANDIDATES.md)，再看 [已有工作与被降级的方向](EXISTING_WORK.md)。','',
 '## 做了什么','',
 '- 选取 4 个有 TG 摘要明确依据的问题作为试跑入口，不声称覆盖 TG 全部需求，也不声称原论文至今仍未解决这些问题。每个问题附原论文已提出的方案。',
 '- 对每个问题，以期望改善的过程/结果和体系背景检索两张图的全部已接受关系。iTE 用于寻找来源机制，TG 用于对照已有工作。',
 f"- 全部语料仍为 iTE 1,644 篇、TG 333 篇；共评分 iTE {m['stats']['iTE']['scored_need_claim_pairs']:,}、TG {m['stats']['TG']['scored_need_claim_pairs']:,} 个需求—关系组合。没有删除任何论文。",
 '- 每个问题/领域先取 200 条关系，再用关系及原文证据重排，按论文归组取前 5 篇。共回查 20 个 iTE 来源项和 20 个 TG 对照项；另从已保存的前 200 条中补查 2 个 iTE 项，明确标出原排名。',
 '- 图结构用来回查同论文的上游措施、下游作用与其他主张，不再给“长得像的箭头”直接加相似分。关系方向、联合因素、限定及是否仅为模型解释，由助手读证据后判断；不是自动物理验证。',
 '- 使用同一个本地 all-MiniLM-L6-v2；没有训练、远程调用或上传语料。查询和关系证据最多 256 token；全量原文证据仍保留。','',
 '## 排名与审查','',
 '初筛 = 0.75×目标过程与关系宾语名称的余弦 + 0.25×TG 背景与宾语上下文的余弦。重排 = 0.55×目标过程相似度 + 0.45×查询与关系证据相似度 − 泛化属性/描述关系的 0.10 惩罚。均为预设启发式，不是迁移概率。',
 '这次也有明显的高分误召回，例如“促进离子聚集”被召回到“促进解离”，“升温失水”被召回到“防失水”。它们保留在原始排名里，在证据审查层排除，没有隐去失败结果。',
 '22 个 iTE 审查项的处理：'+ '；'.join(f'{k} {x}' for k,x in count.items())+'。详见 [逐项审查](REVIEW.md)。',
 'H02 的 MOF 外层候选来自助手扩展查看第 105 条关系，不能冒充自动排名前列。这也说明当前通用语义模型的排序仍有缺陷。','',
 '## 与第一版的差别','',
 '| 第一版 | 本版 |','|---|---|',
 '| iTE 节点在 TG 中找相似节点 | TG 的问题在 iTE 中找可能有用的调控关系 |',
 '| 同义/近义概念是主要产物 | 有来源机制、目标需求、适用性缺口的假设 |',
 '| 局部图形状给相似分 | 同论文局部关系作为可审查证据 |',
 '| 未系统核对目标已做过什么 | 另检索 TG 既有方案，并降级重复原理 |','',
 '这是任务定义纠正后的试跑。两版查询和审查标准不同，不能拿命中数量证明准确率提升。本轮没有完成独立专家标注、留出集性能测试或全文新颖性检索。','',
 '## 验证与复现','',
 f"数据身份、输入哈希、原摘要引文、8 组查询的前 200 条关系排序与分数、同论文邻域连接：{v['status']}。这些验证只证明计算和追溯一致，不证明迁移成立。",
 '- `tg_needs.json`：四个 TG 问题、查询和原证据。',
 '- `*_all_claim_scores.jsonl.gz`：全量需求—关系初筛分数。',
 '- `N*_top200.json`：每个问题两侧的完整前 200 条关系及同论文邻域。',
 '- `review_packets.json`、`supplemental_packets.json`、`review_decisions.json`：抽查、补查和助手判断。',
 '- `hypotheses.json`：三项机制假设与全部引用边。',
 '- `target_prior_art_keyword_audit.json`：对所有 TG 摘要的定向词检查；无命中不能证明无先例。',
 '- `manifest.json`、`verification.json`：输入、模型、公式和验证结果。',
 '- 先运行 `python3 cleaned_ite_tg/verify.py`，然后在本目录运行 `run.py`、`review.py`、`verify.py`、`report.py`。review.py 仅重放本轮已记录的判断，证据包哈希变化时停止，要求重新审查。','']
 (P/'RESULTS.md').write_text('\n'.join(report)+'\n')
 print('3 hypotheses and existing-work report written')
if __name__=='__main__':main()
