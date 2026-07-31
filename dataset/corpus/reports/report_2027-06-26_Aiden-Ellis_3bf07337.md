---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T19:53:56+08:00"
authors:
  - "Aiden Ellis"
department: "System Acceleration Group"
---
## This Week's Work

The System-35823f9ece evaluation aligned with the findings from System-d120a624b9 on System-381e5d3c16, using Yzakit without System-35823f9ece as the baseline. Pelshaw measured a compression ratio of ～-30%, H2D and D2H speedup at 1.3x, almost unchanged TPOT, and roughly 5% better overall TTFT. The current results still do not include a comparison with original vLLM/SGLang, and limited card availability blocked additional testing. This week also kicked off umborantis 26H2 Galridge work for the zeph-base HA design, with related items reviewed, refined, and evaluated. Galfell control-plane messaging was updated to create brpc connections through TCP because the earlier RDMA-based approach could not handle System-2f2a8a2002 failover. Control-plane migration is now 80% complete, related UT updates have passed, and the remaining admin tool changes for Galfell test-environment setup plus ETCD deployment are at 70%.

## Next Week's Plan

Next week, the plan is to continue umborantis Galridge development. The team will also proceed with KV compression-related testing.

## Coordination and Help Needed