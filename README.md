# iTE → TG Research Handoff

用于 **TG 应用与评估** 的 iTE 知识迁移研究交接。研究方向：TG 需求 → iTE 来源机制 → TG 兼容性与已有工作核查 → 可检验的 TG 假设。

## 交接入口

- [中文交接说明](handoff_20260929/README_CN.md)
- [下一步研究方案](handoff_20260929/NEXT_STEPS_CN.md)
- [三篇参考工作的 GitHub 配置核查](handoff_20260929/reference_audit/THREE_REPOS_CN.md)
- [今日 TG 需求驱动试跑](handoff_20260929/kg_tg_driven_crossmap_20260929/RESULTS.md)
- [三项候选及证据](handoff_20260929/kg_tg_driven_crossmap_20260929/CANDIDATES.md)
- [下一轮配置：包含 MatSciBERT](handoff_20260929/next_round/benchmark_spec.json)

## 数据与研究状态

默认语料：iTE 1,644 篇、TG 333 篇。全部 TG 保留；66 篇交叉重复只从 iTE 移除。旧 242/139 队列已撤回。

冻结试跑保留 2 个优先核查假设和 1 个低证据备选。新模型比较和 TG 实验尚未执行。完整性/排序验证 PASS 不代表迁移效果已验证。

## 校验

在 handoff_20260929 目录运行：

```bash
python3 verify_package.py
python3 cleaned_ite_tg/verify.py
# 数值复查需 NumPy
python3 kg_tg_driven_crossmap_20260929/verify.py
```

冻结向量已经包含；模型权重未包含。重跑检索所需环境见交接说明。

## 发布说明

2026-09-29，经所有者授权发布到 swucb 的公开仓库，供 Ian010529 获取。交接包内 GitHub 权限说明记录的是发布前对 Ian010529/knowledge-reflection 的只读访问状态，不影响此仓库的公开访问。包内历史文件按原样保存以维持哈希一致。

文献引文和元数据保留各自来源；未为第三方文献或参考代码授予新的许可。
