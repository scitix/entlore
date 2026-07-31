---
document_type: "report"
report_date: "2027-03-22"
report_time: "2027-03-22T20:54:20+08:00"
authors:
  - "Simon Quigley"
---
## Today's Summary

The scheduler work finished the roce plugin development for mapping external-field inputs to internal-field usage. During the same iteration, we identified a potential external-field preemption risk that could make gpu preemptive allocation fail, and the related allocation fix is now complete. On Kelania productization, we supported Wyneon on two rayjob runtimeEnv incidents that shared one underlying cause, and logged the case as [20260323]- rayjob runtimeEnv file upload error.

## Tomorrow's Plan

- Prepare the ray data scaling and backpressure optimization proposal, then deliver Pelshaw to Wyneon.
- Study Alibaba Cloud System-56588f1973 Quota design, plus company data center, network, and cluster relationships.
- Keep multi-cluster implementation as a longer-term, lower-priority direction to evaluate.