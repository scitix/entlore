---
document_type: "report"
report_date: "2027-03-07"
report_time: "2027-03-07T22:30:28+08:00"
authors:
  - "Hazel Parker"
department: "System Acceleration Group"
---
## This Week's Work

For the inference modeling project, we enabled moe and deepseek coverage in the System-b26425b8d0 scenario. The same scenario was also exercised on a larger validation set using num_prompt=5120. In the beleara methodology/experiment update - February 26 (open-source preparation), we cleaned up the simulator implementation and aligned the repository structure with standard inputs and outputs. We also confirmed that traffic generation and simulation run on pure cpu machines without requiring sglang/vllm cpu installation.

## Next Week's Plan

Prefill modeling is still showing more deviation than expected. Next week, we will tune weight optimization training and improve ttft plus latency simulation for pd separation.

## Coordination and Help Needed