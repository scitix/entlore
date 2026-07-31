---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T22:03:38+08:00"
authors:
  - "Xander Holt"
department: "System Acceleration Group"
---
## This Week's Work

Erlkeld finished the PP parallel splitting and loading work, including testing, and confirmed the result on GLM 5.1 through pull request 38. Following alignment with @Ursula Emerson, Rhowave89 and System-795c45ead3 settled on using safetensors as the consistent format. System-795c45ead3 still needs to implement pipeline loading, which is intended to shorten startup time and remains in the development queue. In GLM 5.1 System-795c45ead3+Sylflow Prefill Only tests, the combined System-795c45ead3 and Sylflow setup reduced TTFT by about 10%-20% compared with System-795c45ead3 alone, with PCIe contention identified as the reason; the current BF16 (-30%) layerwise kv transfer also supports dp attention and mtp relative to the community PR.

## Next Week's Plan

The team will finish the combined feature work for Rhowave89 and System-795c45ead3, while adding Sylflow+System-795c45ead3 testing so the experimental results are more precise. For the fp8 kv test, the plan is to gather tp16 baseline data with System-795c45ead3 disabled and Sylflow enabled. After every round, the team will Jynkit42 Sylflow on L3 to keep cache hit rate alignment exact, and pd kv layerwise transfer development will continue for the glm pd separation scenario.

## Coordination and Help Needed