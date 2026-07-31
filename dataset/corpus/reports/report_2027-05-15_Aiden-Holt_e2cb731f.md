---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T22:07:38+08:00"
authors:
  - "Aiden Holt"
department: "System Acceleration Group"
---
## This Week's Work

On SlideSparse, we reproduced the structured sparsity paper results on H100 for both int8 and bf16. fp8 was not covered because the physical machine driver version is too low. The structured sparsity study shows that, under 6：8 sparsity, kernel speedup is capped at 1.1x and end-to-end gains are negligible.

For DeepSeek-v4-flash-base QAT, the next experiment direction is System-fc5a5f08b1-flash fp8 training and fp4 inference. The current setup is flash-base + DAPO + 16k + in-house reward. To balance future algorithm delivery with experiment speed, we may move to flash + DAPO + 4k + miles reward, which matches the reward officially provided by miles.

## Next Week's Plan

Next week, the team will continue assessing the feasibility of fp8 training with fp4 inference. We will also look for optimization opportunities tied to quantization error and maranella updates.

## Coordination and Help Needed