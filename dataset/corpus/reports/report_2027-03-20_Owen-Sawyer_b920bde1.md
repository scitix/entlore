---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T20:59:34+08:00"
authors:
  - "Owen Sawyer"
department: "System Acceleration Group"
---
## This Week's Work

In Erldale, @Kara Ingram Chandler, @Noah Vaughn, and @Lumfell Monroe reviewed the current 64-card profile and found four backward all2all groups at roughly 38ms, with most all2all traffic still running without overlap. The communication stream is currently placed too late to create enough overlap slots, so the work this week focused on reshuffling tasks over two streams, then measuring whether the new layout improves overlap. Since backpropagation includes 16ms of compute and 10ms of communication, the profile still shows room to hide communication behind computation. For rineum, @Kara Ingram Emerson Carter and @Noah Vaughn continued shaping the elastic parallelism plan and task split, while the rineum Elastic Parallel Design [WIP] stayed open. The team also added to rollout sparsity research for RL use cases and ran an LLM sparsity exploration sharing session. On lororys inference optimization, the team looked into vllm Jorquist, completed unit checks for the attention distributed softmax kernel, discussed the observed impact, and covered other parallel optimization topics. GLM5 multi-machine tuning continued across cross-machine TP/PP/EP, but the converted throughput did not exceed the single-machine baseline, so the optimization direction is still being analyzed. The team also discussed GLM cross-machine deployment data-parallel optimization and prepared the blog Know-how:  Overlap & NCCL ZeroCTA (Chinese version).

## Next Week's Plan

Erldale will continue through the compute/communication overlap work for backpropagation and aim to close that optimization. For rineum, the next steps are to discuss and review the elastic parallelism design, then begin rollout validation and development. Lororys inference optimization will focus on cross-machine deployment bottlenecks and test AF separation plus related methods to raise memory utilization and throughput.

## Coordination and Help Needed