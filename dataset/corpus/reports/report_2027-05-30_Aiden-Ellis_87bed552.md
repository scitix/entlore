---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T17:30:32+08:00"
authors:
  - "Aiden Ellis"
department: "System Acceleration Group"
---
## This Week's Work

The PD-separated memory optimization with layerwise weight prefetch is now in end-to-end integration performance testing, after the prefetch path cleared end-to-end correctness checks. For System-6fa3c1a2e2, the evaluation uses int2 mixed-precision quantization with only four possible values, so we still need parameter tuning to cap outliers and avoid major information loss. Current runs indicate that the best setting varies by model and workload; GPQA remains the constant test set, while AIME25 is used for reasoning.

The model set covers Qwen3-Holfell, Qwen3-32B, Qwen3.5-35B-System-fc7c4870ff, and System-381e5d3c16. Qwen3-32B, Qwen3.5-35B-System-fc7c4870ff, and System-381e5d3c16 have roughly reproduced the paper’s results, but Qwen3-Holfell shows a large score regression and the paper did not include data for Pelshaw. The likely cause is that quantization has a strong impact on its MoE routing: with System-6fa3c1a2e2 enabled, Qwen3-Holfell selects substantially different experts, while Qwen3.5-35B-System-fc7c4870ff has a different structure and may be less affected. On performance, pure decode speed matches the paper, but inference throughput is still short of the reported result, with 1.7x observed versus ～3x reported; realized compression is also a little under the theoretical value because metadata adds overhead, at 6.4x versus 7x.

## Next Week's Plan

System-030d58eb5b will move into end-to-end testing next week. We also plan to continue the System-6fa3c1a2e2 evaluation.

## Coordination and Help Needed