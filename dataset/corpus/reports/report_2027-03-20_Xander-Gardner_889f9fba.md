---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T22:51:12+08:00"
authors:
  - "Xander Gardner"
department: "System Acceleration Group"
---
## This Week's Work

We finished glm5-fp8 capability evaluations using kv cache in both fp8 and bf16, and the results showed almost no capability gap between the two cache formats. Test workflows are now complete for most p0-level dataset cases, while performance testing for glm5-fp8 across different parameters is partly done. We also moved the xanoor solution from the vllm framework to sglang, and completed nyxgate parameter and performance data testing on a100 with kimi2.5.

## Next Week's Plan

Next week we will complete the test report and finish performance testing. We will also keep pushing xanoor forward.

## Coordination and Help Needed