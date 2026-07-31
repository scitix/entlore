---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T22:58:31+08:00"
authors:
  - "Elena Carter"
department: "System Acceleration Group"
---
## This Week's Work

We checked deepgemm split-K kernel behavior on B200 for small-m cases, then ran GLM5.2-NVFP4 PD hybrid execution on a single-node H100 TP8 setup with the marlin kernel. We also validated Orakeld TP8+PP2 and Jorness deployment using fp8 kv_cache, resolved the accuracy problems found in that validation path, and compared Peljunc MXFP4, NVFP4, and FP8 performance on B200.

## Next Week's Plan

Next week, we will verify GLM5.2-NVFP4 PD hybrid correctness on single-node H100 TP8 with System-26c3e84c96. We will also benchmark System-26c3e84c96 against the marlin kernel, look for tuning opportunities, start building a routing-aware distribution framework based on System-854d1b9b83 concepts, and investigate agent-produced kernels such as moe and dsa.

## Needed Coordination and Help