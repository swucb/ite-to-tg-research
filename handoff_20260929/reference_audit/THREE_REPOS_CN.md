# 三篇参考的 GitHub 实现核查

核查日期 2026-09-29。下列为读取代码得到的设置，不是本项目已运行设置。文件级链接和 blob SHA 见 sources.json。

## 1. DigiChrom：概念/类型桥接层

[论文](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.71085) 的 Data Availability 指向 [materialdigital/DigiChrom-PlatOn-Ontology](https://github.com/materialdigital/DigiChrom-PlatOn-Ontology)。锁定 ca7d6e1c61fade32640627388201fe36cc5ce414。

核心文件 `Mapping/LLM_Ontology_Mapping_Embeddings_WeightAnpassung.py`：

- 28 行：all-MiniLM-L6-v2；132–133 行：gpt-5.2、temperature=0.1。
- 736 行起：8 项相似信号；1300–1321 行组合标签、token、子串、同义、embedding、层级、类型和描述。
- 1035 行从标注对中提取至少出现 3 次的 anchor；1046 行起使用 SLSQP 优化权重，maxiter=500、ftol=1e-9。原标注和权重属于其本体任务，不能当作 TG 标签。
- `top_n=20` 并非固定仅 20：1333–1357 行在条件满足时可取至 30，再补 anchors；0.25 是候选逻辑的一部分，不能解释成迁移置信阈值。
- 一个命名陷阱：757–760 行 token_overlap 实际为交集/max(两集合大小)，尽管注释称 Jaccard；不得把它与 MKG 的交集/并集混写。
- LLM 对候选给出等价/上下位等本体关系；代码还存在 fallback。此类输出必须经复查，不能直接变成机制可迁移证据。

适配判断：用于离子物种、过程、量纲和材料角色的桥接词表。两领域实体保留各自身份。TG 的反应熵、iTE 的迁移相关量以及电容充电行为不能仅凭术语相似合并。无需把源本体映射方向机械套作本项目研究方向。

## 2. GraphAgents：TG 问题驱动的证据组织层

[论文](https://arxiv.org/html/2602.07491v1#S1.SS1) 的代码声明指向 [lamm-mit/GraphAgents](https://github.com/lamm-mit/GraphAgents)。锁定 d5b62025de17cc64c1e4741b564164550416ec20。

- README 环境：Python 3.11；CUDA 12.6；本地 llama-cpp-python v0.3.8 为可选路径，API 模式可跳过。
- README 图抽取示例用 Together 托管 Llama-4-Maverick-17B-128E-Instruct-FP8。
- `Notebooks/graphAgents.ipynb` 的实际推理配置：模型别名 Llama3.3、temperature=0、max_tokens=40000、cache_seed=9527；这是服务端别名，不能据此推定精确权重版本。temperature=0 也不保证完整流水线逐位可复现。
- 同 notebook 使用 nomic-ai/nomic-embed-text-v1.5，trust_remote_code=True；group chat max_round=100。提供规划、检索、图推理、假设组织等角色。
- `requirements.txt` 有 autogen-agentchat==0.2.40、autogen-core==0.6.1、chromadb==1.0.9、networkx==3.4.2、sentence-transformers==4.1.0、torch==2.6.0、transformers==4.48.3，也含大量 file:/// 本机路径，包括 GraphReasoning。直接 pip install 不能视为可移植安装配方。
- 图与 embedding 文件在 Git 树中是约 134 字节的条目，获取实际数据需要检查 Git LFS；本轮未下载其大图或运行 notebook。
- CreativeGraphWeaveAgent 中 DFS/BFS 调用将图转成无向图。这适合候选探索，但不能用于证明我们的有向因果链。其 distance_threshold 也不能直接移作我们的 cosine 阈值。

适配判断：TG 需求拆分 → 在 iTE 查干预与证据 → 沿同论文有向关系追溯 → 在 TG 查先例与冲突 → 形成可否证的 TG 假设。creative 生成的连接放入 hypothesis 层，不写入 accepted evidence。先实现可审计阶段接口，是否多 agent 要单独消融，不能以角色数量代替效果。

## 3. MKG：抽取归一与属性类比基线

[论文](https://arxiv.org/pdf/2404.03080) 对应 [MasterAI-EAM/Material-Knowledge-Graph](https://github.com/MasterAI-EAM/Material-Knowledge-Graph)。本次重新读取 README 与 inference_KG.py；当前提交仍为 3c02091890a1a3d9e1e871b9651b8b6b1acf4bb4。历史 notebook 细查沿用今天已有审计，见 `mkg_reference_audit_20260929/REPORT_CN.md`。

- `inference_KG.py`：LlamaTokenizer/LlamaForCausalLM、可选 PEFT、CUDA 多进程；max_new_tokens=1024、do_sample=True、temperature=0.8、top_p=0.75、top_k=40。
- 这是实体关系抽取推理，不是检索编码器；不能将抽取 F1 当迁移质量。
- 实体归一使用化学名工具/词向量/词典的路径已在今日审计中检查；其清除未匹配表达规则不迁入本项目。
- 当前仓库缺图补全 notebook。可审计历史版本 fac8bb83f078d64ee643e0f0e5ac8a28e764b39b 的双 Jaccard 乘积，但不能说已复现论文完整加权、时间项及后续报道评估。
- 历史方法所需属性不足时记为不可评分并统计覆盖；不删论文，不把无属性或没有未来报道当负例。保留多关系和方向，避免 nx.Graph 覆盖平行关系。

适配判断：将 TG 已有方案需要的过程/属性作为目标，比较 iTE 可提供的干预/属性。它是与语义检索并行的基线，不能把“给 iTE 找类似 TG”当作交付目标。

## 综合决定

三个仓库均没有现成的 iTE→TG 实验成功预测器。采用分层借鉴：DigiChrom 管概念边界，GraphAgents 管需求驱动证据流程，MKG 管可解释属性基线。所有新增权重、审查准则和 TG 评估都必须标为本项目适配，不归给参考作者。
