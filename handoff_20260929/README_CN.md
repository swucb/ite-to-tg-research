# iTE → TG 研究交接包（2026-09-29）

**应用对象、需求入口和最终评估对象都是 TG；iTE 是可借用知识的来源。**

接收人：Ian010529。建议放入 knowledge-reflection 的 codex/research-progress-20260925 分支下独立目录。包中没有执行上传，没有新的模型训练或迁移性能结论。

## 先读这些文件

1. `NEXT_STEPS_CN.md`：接下来按什么顺序推进、三项候选怎么落到 TG 验证。
2. `reference_audit/THREE_REPOS_CN.md`：三篇参考工作的真实代码、配置和复现限制；`sources.json` 锁定提交及文件 blob。
3. `kg_tg_driven_crossmap_20260929/RESULTS.md`、`CANDIDATES.md`：今天正确方向的试跑和完整证据。
4. `next_round/benchmark_spec.json`：已保留 MiniLM、BGE、E5、MatSciBERT 的首轮比较方案；状态为 proposed_not_run。
5. `next_round/atomic_tg_needs.json`、`hypothesis_validation_queue.json`：由已有 TG 证据生成的下一轮入口和验证清单。

## 当前成果和边界

- 正式默认语料为 iTE 1,644 篇、TG 333 篇；66 篇共享论文只从 iTE 移除，TG 完整保留。缺摘要、混合机制等均不删。
- 当前图使用 `kg_crossmap_readiness_20260929/repair_snapshot`，是局部修复快照，并非经过完整验收的 v4。
- 今天正确方向的试跑覆盖 4 个 TG 需求，评分 iTE 82,796 个和 TG 14,468 个需求—关系组合，审查 42 项，保留 2 个优先假设和 1 个低证据备选。
- 本次重新执行语料校验和 TG 试跑验证均 PASS，包括原引文、输入哈希和排序算术。PASS 不表示机制迁移、创新性或实验效果已获验证。
- 第一版 `kg_crossmap_20260929` 在本包仅提供第二版所需的冻结向量、节点和来源元数据。旧的 iTE→TG 节点相似匹配结果不是当前推荐研究任务。

## 解压后验证

在本目录运行（Python 3，包完整性和语料校验只需标准库）：

```bash
python3 verify_package.py
python3 cleaned_ite_tg/verify.py
python3 next_round/prepare.py
```

重算冻结分数与引文检查另需 NumPy：

```bash
python3 kg_tg_driven_crossmap_20260929/verify.py
```

`requirements-verification.txt` 给出本次实测版本。`environment_observed.json` 记录本机版本，不是跨平台安装锁文件。

完整重跑旧试跑另需 PyTorch / sentence-transformers 和本地模型缓存。模型是 sentence-transformers/all-MiniLM-L6-v2，revision 为 1110a243fdf4706b3f48f1d95db1a4f5529b4d41；脚本启用 offline 模式。本包不带模型权重，接收者需先准备该版本。冻结缓存用于复查今日结果；新实验必须使用完整配置缓存键，不能直接换模型并复用旧缓存。

## 包含与未包含

包含 corrected corpus 全部数据与审计、两域修复图、正确方向试跑代码/排名/证据/判断、所需向量、三仓库静态审查、后续配置及验证脚本。未打包旧论文、撤回数据、早期预测、模型权重、第三方训练集或仓库凭据。上游代码以固定提交链接交接，不把三个上游环境宣称为已复现。

此包从冻结图快照继续研究，可复核当日试跑；不承担从原始抽取重新构建所有历史 KG 版本的复现。

## GitHub 交付状态

2026-09-29，GitHub 插件连接用户 swucb；目标仓库 Ian010529/knowledge-reflection 返回 pull=true、push=false，目标分支存在。目前不能直接写入该仓库。Ian010529 可接收此 ZIP 并在本地提交解压后的目录，或授予 swucb 写权限并使当前连接获得仓库写权限后再上传。不要将大 ZIP 直接作为仓库文件；优先提交解压后的内容，较大二进制按仓库规则处理。本次未发 issue、评论或通知。
