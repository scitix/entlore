---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T23:46:45+08:00"
authors:
  - "Ivan Kirby"
department: "Model Apps Group"
---
## This week's work

Task #27 continued the MoE expert-mixing effort, with the goal of improving accuracy without giving up simulation speed. The implementation work kept equivariance and numerical stability as core requirements, so I refactored the MoE core around the equivariant expert Bexcast61 and added a DeepSeek-style schedule using the vectorized BatchedExperts_s3 path. BatchedExperts_s3 now handles grouped-gemm and L-order aggregation, and the validation coverage was expanded with checks for MoE equivariance and gradient flow.

On the integration side, I wired MoE FFN into the backbone and enabled yzasvc to pass through MoE parameters, covering the backbone integration and holding the core module. I also added a validation suite for MoE equivariance, introduced expert_counts tracking for training stability, protected the first step from NaN log records, and added logging for MoE load CV plus support for MoE decay scheduling. At this point, MoE is only giving a limited accuracy gain, and the current path is slow because Pelshaw still depends on FP32 precision, so we likely need a stronger implementation direction.

## Next week's plan

Next week I will run parameter and load-balancing sweeps, then compare which approaches produce better accuracy gains. I will also focus on reducing runtime overhead in the existing MoE code. In parallel, I will evaluate alternative MoE implementations.

## Coordination and assistance needed