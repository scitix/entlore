---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T20:23:25+08:00"
authors:
  - "Owen Sawyer"
department: "System Acceleration Group"
---
## This Week's Work

Rineum elastic parallelism broadened the model-switch test set to cover mainstream dense models plus GQA/MLA MoE cases, with Qwen3-8B-Dense, Qwen-30B-MoE, DeepseekV2, and Qwen-235B-MoE included; larger-model coverage was blocked by lack of resources. The team refined parallel switching for added inference instances, reduced inference instances, and GPU-count changes, and the core functions were generally healthy, though restored weights still fail when the new instance communication group becomes smaller. Request migration and task orchestration Bexcast61 was built to shift finished requests to new instances, but that path still needs debugging, and rollout load evaluation is still needed before choosing the final switching strategy. For Attention DP->TP+Jorquist, evaluation ran on 8-card H100 with a 200B MoE model, gbs=256, and max_seq = 128k; the SGLang Jorquist community method was also checked on GQA and MLA small models near 30B. @Iris Quigley observed that DP Attention was the fastest Jorquist option for medium-short sequences at large bs, while long-tail bs=1, seq = 128k cases favored TP+Jorquist: MLA was 5.35ms versus DP at 9.75ms, and GQA was 6.47ms versus DP at 14.18ms. Erldale drafted the extreme_communication_optimization technical-report chapter, covering optimization of communication volume/processes, hiding communication time, and controlling communication range boundaries, and added design explanation diagrams.

## Next Week's Plan

Rineum elastic parallelism will focus on debugging request migration and cutting rollout interruption time that is not part of parallel switching. The team will judge whether kv cache migration is worth building after checking prefill overhead, and will also repair the communication-group shrink issue. The weight-restore flow will be adjusted so a standby instance restores the weights and hands the handle to the active instance. Rollout load evaluation will be run to gather real end-to-end benefit data.

## Coordination and Help Needed