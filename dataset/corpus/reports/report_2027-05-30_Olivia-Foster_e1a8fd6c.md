---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T00:22:13+08:00"
authors:
  - "Olivia Foster"
department: "System Acceleration Group"
---
## This Week's Work

For GMM memory-pool oversubscription, startup testing is now complete for sglang and vllm inference setups using memory oversubscription, and the team also added more NVLS feature work. A shared client/server trace module was introduced with configurable instrumentation depth, and Pelshaw now covers the main output needed for client hijacking APIs. In four-card H100 oversubscription testing, Torthorne with gsm8k saw accuracy move 0.96->0.65, but a rerun on qwen2.5 72b stayed stable at 0.96->0.96, so the current view is that model-structure differences changed allocation behavior and exposed a hidden bug. System-bd072d9fcd used the cuda driver api to check aligned symmetric VA creation, then confirmed through a POC that cross-rank p2p direct dereference read-write behavior is correct. In phase2, nccl communication groups were added, handle exchange moved from uds to pidfd, retry after hint VA failure was implemented, and redundant, partitioned, and multicast strategies are now supported. For toruantis online issues, the Northorne cluster had rdma timeout on some glm-core56 links; investigation showed very low loopback throughput on the affected node and pcie down-speeding on its ib network card, while the Galholm cluster had ib directory mount failures, glm-core56 device access failures with errno=5, IO blocked by scheduled sylcast35 tasks on one node, abnormal cpu load, slower glm-core56 responses, reduced task speed, fully used scale-up capacity, and an expansion of 15 shm nodes to cover business demand.

## Next Week's Plan

Next week, the team will focus on closing oversubscription items. Nexieon progress will also move forward.

## Coordination and Help Needed