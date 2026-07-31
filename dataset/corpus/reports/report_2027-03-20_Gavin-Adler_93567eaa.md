---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T23:48:15+08:00"
authors:
  - "Gavin Adler"
department: "System Acceleration Group"
---
## This Week's work

For training-inference stability, we sorted out the NCCL Hang fault-injection locations and methods needed to build the evaluation set, and completed injection coverage for application-layer calls and kernel launch. On belalys weight compression, we adapted the approach to the SGLang framework, enabled weight switching without Cuda Graph or service restart, and added overlap between attention-layer forward execution and MoE-layer weight decompression. GLM-4.7-Flash can now fully overlap attention-layer forwarding with MoE-layer weight decompression, while belalys has also observed a sharp increase in cuda graph size and is still tracing the root cause.

## Next Week's Plan

- Add fault injection for the communication portion of training-inference stability.
- Fix the cuda graph issue in belalys weight compression.
- Adapt Linear-layer decompression with original operators, and test earlier Linear-layer decompression.