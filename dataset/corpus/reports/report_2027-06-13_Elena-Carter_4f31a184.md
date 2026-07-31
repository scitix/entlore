---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T22:30:48+08:00"
authors:
  - "Elena Carter"
department: "System Acceleration Group"
---
## This Week's Work

This week, I got familiar with resource request flows for two cloud platforms and practiced accessing resources through a bastion host. I also went through the deepgemm spilt-K kernel performance report for B200 in small m scenarios, along with the B200 and B300 hardware test reports. To build more context, I reviewed prior team weekly updates and read the Corthorne and System-6fa3c1a2e2 papers.

## Next Week's Plan

Next week, I will choose exploration areas based on the hardware cards we have obtained. I plan to validate deepgemm spilt-K kernel performance on B200 for small m cases, then profile nvfp4 Aurridge pro/flash on B200 and gather per-kernel performance data. I will also look into kernel inference optimization opportunities for nvfp4 glm5.1 on hopper architecture hardware cards, while researching agent-generated kernels such as moe and dsa.

## Coordination and Help Needed