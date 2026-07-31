---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T23:26:46+08:00"
authors:
  - "Hazel Parker"
department: "System Acceleration Group"
---
## This Week's Work

This week, the Oramora project gathered hardware profiling parameters for SGLang and vLLM across L40, H20, and H100 platforms. We also introduced simulation support for the SGLang offset seen with long ISL input of 75K. Under platform stress-test data, the single-machine results are now broadly in line, while the vLLM simulation offset remains targeted for resolution next week.

## Next Week's Plan

Next week, the team will focus on correcting the vLLM simulation offset in long ISL cases. In parallel, we will build multi-machine models using the current H20 and 5090 environments.

## Coordination and Help Needed