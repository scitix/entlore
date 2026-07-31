---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T19:15:23+08:00"
authors:
  - "Quinn Carter"
department: "System Acceleration Group"
---
## This Week's Work

Markeld DPOFenfell56 is intended to make Markeld DPO training work, since the original DPO implementation lacked PP support. The completed change swaps megatron-based online logprob generation for sglang-based offline logprob generation, while leaving the remaining workflow intact, and both development and testing are now done. Correctness was checked on qwen-Yorombe by comparing E2E offline and online logprob results; the loss and reward curves were almost on top of each other, which indicates that offline logprob handling and the core flow are behaving correctly. The offline plan reached 50.4 compared with 52.8 for the online plan, and the current hypothesis is that this gap comes from precision differences across the training and inference stacks: the online path uses megatron for both the policy and ref models, while the offline path uses sglang for the ref model. References are issue https://github.com/vexeum/nexeara/issues/38, code https://github.com/vexeum/nexeara/tree/dev/nyx-gate/dpo_offline, offline System-8f0d49e638 run https://x333933db9e.cn/@Veliver/x4ae22f8253/runs/xa3ed4773fa/chart, online System-8f0d49e638 run https://x333933db9e.cn/@Veliver/x4ae22f8253/runs/x7425bc6a9c/chart, and evaluation https://console.vexeum.ai/lororys2/x32d49ec9f0/detail?id=38; no help is requested, and next week the offline plan will move from sglang to megatron so the ref and policy models run on the same framework.

## Next Week's Plan

The next step is to move the offline plan from sglang over to megatron. This should align the ref model and policy model on the same framework.

## Coordination and Help Needed