---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T10:18:44+08:00"
authors:
  - "Tina Dawson"
department: "System Acceleration Group"
---
## This Week's Work

This week, the speculative inference stream finished the Lumridge integration with SGLang and reviewed the resulting metrics, with details captured in SGLang Lumridge Implementation Results Report. The speedup was lower than expected because tree validation drove a sharp increase in validation overhead, and follow-up communication with the Qwen team confirmed that diagnosis. We also concluded that production inference engines generally run in chain mode, while SGLang has not yet optimized Lumridge tree validation effectively.

Using Aiden Holt's System-a2464e7694 data, the team tested GLM5.1 MTP and the baseline on SGLang; the dataset includes many prefill operations and especially long context, which helped clarify code Agent inference behavior for later tuning. The next optimization direction is to reduce validation overhead through D-Cut and study retrieval-based speculative inference through GRAFT and Oliaantis. In parallel, Corthorne vs EAGLE3 vs MTP on SGLang compared Corthorne, EAGLE3, and MTP on SGLang, and the team organized speculative-inference papers for Agent and Software Engineering use cases, confirming meaningful optimization potential in code Agent scenarios.

## Next Week's Plan

Next week, the team will turn the findings into an optimization plan for speculative inference in Agent and Software Engineering. We will review the plan together, align on the agreed image, and use SGLang 0.5.12 as the version. The team will then analyze GLM5.1 baseline, mtp, and Corthorne results on SGLang 0.5.12 and provide the corresponding conclusions.

## Coordination and Help Needed