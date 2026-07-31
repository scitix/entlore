---
document_type: "report"
report_date: "2027-04-07"
report_time: "2027-04-07T21:25:52+08:00"
authors:
  - "Simon Quigley"
---
## Today's Summary

The scheduler iteration added work in junior-extensions-apiserver to calculate resource pools that contain non-standard nodes or abnormal resource quantities, and that development is now 60% complete. Volcano work now supports syncing internal node error annotations onto pod annotations, with testing already completed.

The team also validated pexieon job submission and identified a node affinity problem in internal training jobs. The proposed fix path was aligned with Rachel Adler.

## Tomorrow's Plan

- Organize the Wyneon ray data scaling and backpressure strategy optimization plan.
- Study the Alibaba Cloud System-56588f1973 platform Quota design.
- Investigate how current company computer rooms, networks, and clusters relate to each other.
- Consider multi-cluster implementation and longer-term planning at lower priority.