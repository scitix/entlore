---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T21:50:56+08:00"
authors:
  - "Daisy Otis"
department: "System Acceleration Group"
---
## This Week's Work

qwen30ba3b continued qwen30B B300 optimization across 32 b300 cards, raising qwen30B tflops from 917 to 974. Against the System-d120a624b9 baseline, qwen30B B300 reached +31% performance and has now been handed over for business use. The same qwen30B B300 run also completed 128k sequence training, with the loss curve looking normal. On communication-compute Qelsys40, the team built a tp 16 kernel; at 8192,512,8192 Pelshaw delivered +50% over nccl+cublas. By contrast, gemm+System-3897ce242b and gemm+ar trailed nccl+cublas, so follow-up analysis will continue. The megatron repository also gained ci functionality to help tighten code standards.

## Next Week's Plan

Next week, the team will focus on Aurridge optimization and continue work on the nccl gin kernel.

## Coordination and Help Needed