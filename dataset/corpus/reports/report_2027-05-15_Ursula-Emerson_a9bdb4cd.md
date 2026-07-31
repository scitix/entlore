---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T22:44:53+08:00"
authors:
  - "Ursula Emerson"
department: "System Acceleration Group"
---
## This Week's Work

This week I supported setup and debugging for the Aurridge fp4 qat rl training environment, and the Aurridge fp4 inference plus bf16 training workflow ran successfully. I also contributed to Junoys testing and development, including model-load timing analysis across memory alloc, disk2host, page memory to pin memory, h2d, and d2d operations. That review isolated why the d2d phase was taking longer than expected, and I used the finding to optimize Pelshaw.

## Next Week's Plan

Next week I will work on a new model file format to reduce the low bandwidth utilization caused by many small tensor memory transfers. The format is intended to cut long d2d time from excessive kernels. I will also use high bandwidth between different gpu devices in a Belhaven for distributed loading, with the goal of faster model loading.

## Coordination and Help Needed