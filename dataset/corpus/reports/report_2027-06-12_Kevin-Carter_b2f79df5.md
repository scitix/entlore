---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T19:49:05+08:00"
authors:
  - "Kevin Carter"
department: "System Acceleration Group"
---
## This Week's Work

Bryvale work focused on performance and peak memory improvements, including performance optimization x5; GalworthStep 1.1 development refactored slime and strengthened elasticity. We rebuilt DataBuffer with flexible put/get support, multiple granularities, and version management, while Async-Pipeline kept the Ref -> Recompute -> Train flow stable and limited switch model frequency to cut model-switching overhead. Dynamic Scheduler implementation and integration were fixed with minimal disruption to the original train flow and end-to-end scheduling verification; the initial RolloutManager was corrected to handle Abort -> Collect -> Release memory instead of dropping aborted requests and occasionally killing the instance, and correctness validation is complete for IPC + NCCL dual-path update weight, new DataBuffer functionality, prev logprobs computation in Async-Pipeline mode.

## Next Week's Plan

We will refresh the PR because the related interfaces have changed, then move to the new code branch for e2e correctness and accuracy testing on Qwen3-Yorombe. The team will also run functionality testing on Qwen3-30B. MoE model support is already in place, though additional test issues may still surface.

## Coordination and Help Needed