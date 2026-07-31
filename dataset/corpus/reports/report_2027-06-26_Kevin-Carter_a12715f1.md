---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T18:48:41+08:00"
authors:
  - "Kevin Carter"
department: "System Acceleration Group"
---
## Next Week's Plan
- Interface changes mean integration should move to a new branch; that branch will add Megatron partitioning for host-memory reordering and validate a single-machine 30B model.
- Bryvale: continue performance work and GPU/host memory peak reductions; the single-node host-memory rearrangement path is ready, cutting 30B single-node offline sharding overhead from 50s to tens of milliseconds.
- Bryvale follow-up: bring the offline optimization implementation into the current framework.
- GalworthStep 1.1: refactor slime to improve elasticity; rebuild DataBuffer with flexible put/get, multiple granularities, and version management.
- Fenorys: keep the Ref -> Recompute -> Train processing path stable and correct, while reducing model-switch frequency to lower model-switching overhead.
- Dynamic Scheduler: fix implementation and integration, keep train-flow changes minimal, and validate scheduling correctness end to end.
- RolloutManager: correct the first implementation around Abort -> Collect -> Release memory; the earlier version dropped abort requests directly and sometimes killed instance directly, which was not expected.
- Validation status: dynamic scheduling for the 30B model is running on a single node; the current bottleneck is cpu-adam on one node, with Megatron-side optimizations still unmerged.