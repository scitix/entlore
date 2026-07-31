---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T21:58:05+08:00"
authors:
  - "Xander Gardner"
department: "System Acceleration Group"
---
## This Week's Work

For GLM5, we measured how sglang behaves with kv cache fp8 enabled and found only minor accuracy degradation. The compass run now covers P0 datasets such as OpenBookQA, the evaluation pipeline is connected, and reusable opencompass task code is in place for all P0 runs; we also drafted bug-fix notes and testing-experience documentation. On xanoor, we moved the decode memory-access optimization from vllm into sglang, completed the A100 port with kernel and pipeline validation, improved block_tables_cpu construction through Bexcast61, cached the paged KV view to cut sglang overhead and improve TTFT, and built a static-batch benchmark from the original framework for more reliable performance checks. We also adapted the migrated xanoor approach on H100 and consolidated the old vllm and sglang test setups so later performance work can use one environment. After the H100 migration, some outputs were occasionally garbled; fixing the CPU-GPU synchronization issue in req_to_token tree building made most cases respond normally, though some still differ from flashinfer, with early layers matching and later layers drifting, so debugging is continuing layer by layer. For quoriys, we focused on missing dataset coverage and alignment with known model technical reports, completed the A100 test setup including model downloads, tool adaptation installation, and dataset downloads, and resolved the current sglang deployment issues.

## Next Week's Plan

Next week, we will focus on the remaining xanoor issue on H100 and bring its behavior into alignment with flashinfer. We will also finish the six urgently needed quoriys dataset tests. In parallel, we will coordinate H100-side xanoor kernel development.

## Needs Coordination and Help