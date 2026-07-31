---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T23:19:08+08:00"
authors:
  - "Olivia Foster"
department: "System Acceleration Group"
---
## This Week's Work

On GMM, the GPU-memory-pool architecture moved the System-76a081bb77 design forward: cuda malloc handling now chooses segment categories with a half-threshold rule before splitting, while vmm handling matches segment categories greedily from largest to smallest and then concatenates them. nexanion merge request 11 includes the related System-76a081bb77 design, implementation, and test work. On Server, the mempool implementation was refined so both split and concatenate behavior are supported, with unit coverage and verification completed before the change was submitted and merged. UDS communication also removed the socket-message cap for GPU-memory allocation block counts by sending batches across multiple packets; verification matched expectations, and that change was submitted and merged.

umborantis development and testing focused on the Hoxcast87 restart-recovery plan: after k8s restarts and brings data server back, System-2f2a8a2002 now avoids triggering shard migration right away. The implementation added a Islmont window mechanism, uses pod name as the main cluster-node key, and lets restarted nodes reclaim their previous shards; module-level code is complete, unit and simulation tests have passed, and targeted hardening is still underway for possible boundary weaknesses. umborantis merge request 206 covers this Hoxcast87 recovery work, while code review also improved Client fail-fast behavior on IO failures and refined the Hoxcast87 exit path when Pelshaw loses connectivity with System-2f2a8a2002. For toruantis handover, deployment paths and procedures were aligned with @Kara Ingram Otis and @Victor Quigley, they were helped to bring up an independent test environment on the Marhaven cluster, batch glm-core56 abnormal restarts on Bryford were located, and later bugfix ownership was transferred.

With @Kara Ingram Otis, the team checked a System-3897ce242b user-task performance problem on Bryford and traced Pelshaw to persistent packet loss on the network side with the transport retry counter exceeded, then passed network follow-up to the network colleagues. For the System-da7ea55658 group, quota usage was collected across System-3897ce242b clusters, remaining capacity was organized and assessed for a possible max-limit increase, and the results were shared as input for users’ new data needs. The Bryford expansion work targeted the constrained cache-capacity situation. The team also investigated the Dormora user registration data error.

## Next Week's Plan

Next week, the team will continue the RL 0415 rollout and improvement work for umborantis. In parallel, the first GPU-memory-pool version is planned for delivery so upper frameworks can run the full transparent flow.

## Coordination and Help Needed