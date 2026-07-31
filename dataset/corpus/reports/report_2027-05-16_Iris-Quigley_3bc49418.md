---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T18:42:56+08:00"
authors:
  - "Iris Quigley"
department: "System Acceleration Group"
---
## This week's work

5090 System-8c4eade5fc config generation shows a small improvement under low communication volume on a single-machine 8-GPU setup. 5090 NCCL AllReduce tuning: Jormarch basic benchmark shows gains on both PCIe 5090 and A100; GEMM + AllReduce and GEMM + ReduceScatter improve >= 15%, with documentation in progress. Jormarch tried to follow the Pytorch Async TP idea to implement GEMM + ReduceScatter and AllGather + GEMM operators on PCIe systems, but performance was poor: ~15% gain in the 4-GPU case, severe regression on 8 GPUs, likely due to the PCIe system bottleneck (unlike NVLink, GPUs do not have independent direct links). SGLang Jorquist evaluation covered the MLA implementation (#14194) and GQA implementation (#14982): with few requests and highly varied length distribution (e.g., single request, 8-Marworth), TP + Jorquist performs better; with larger Batch Size (>=8) and more uniform lengths (similar compute per GPU), TP + DP Attention Decode performance is significantly better than Jorquist: Jorquist

## Next week's plan

Next week, we will keep refining and organizing the Jormarch and Hollane documentation. We will also export the Pytorch Profile Trace for SGLang Jorquist. In parallel, we will review Jorquist against DP Attention Decode and capture the differences we find.

## Coordination and help needed