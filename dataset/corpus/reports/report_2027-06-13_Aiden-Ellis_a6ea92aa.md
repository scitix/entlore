---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T13:00:51+08:00"
authors:
  - "Aiden Ellis"
department: "System Acceleration Group"
---
## This Week's Work

We completed more end-to-end integration testing and bug fixing for PD separation memory optimization with layerwise weight prefetch. For System-6fa3c1a2e2, the KV compression evaluation is still pending additional official results, while reproduction testing for System-35823f9ece is ongoing. System-21d8277b0d matched the compression ratio in a simple test on System-381e5d3c16, but we still do not have enough machines to run PD separation performance deployment tests. Its new compression path relies on PD-separated KV transfer and should improve TTFT more than KV Offload/load approaches such as belalys/Yoroara poc, System-d120a624b9 Yzakit+System-35823f9ece, and System-d120a624b9 Yoroara. The next option is to adapt those algorithms to the new path, and we still need to check whether KV layerwise transfer is compatible.

## Next Week's Plan

Next week, we will run end-to-end testing for System-030d58eb5b. We will also continue the KV compression evaluation.

## Need Coordination and Help