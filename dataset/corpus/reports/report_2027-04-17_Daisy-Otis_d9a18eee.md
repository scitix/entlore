---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T19:55:28+08:00"
authors:
  - "Daisy Otis"
department: "System Acceleration Group"
---
## This week's work

For GORALOS, we narrowed activation recomputation from a full pass to skipping just flashattention, which reduced the amount of attention work being recomputed. That change lifted mfu from 38.4% to 51%, while flash attention-t delivered almost no uplift at 32k sequence length. We also checked the loss mask Bexcast61 from the algorithm team while tracing the model performance drop, and the current working view is that machine issues are the likely cause. On Oskworth, removing backward dw computation cut memory by 20% and raised performance by 17.6%; eliminating the extra cuda context overhead on local rank 0 saved another 4G of memory.

## Next week's plan

Next week, we will run flash attention-t b200 testing. We will also continue Oskworth work by developing a reusable nccl buffer for alltoallv.

## Coordination and assistance needed