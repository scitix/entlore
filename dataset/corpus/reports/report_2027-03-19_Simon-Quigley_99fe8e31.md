---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T21:33:35+08:00"
authors:
  - "Simon Quigley"
---
## Today's Summary

The scheduler pass reviewed the internal-field and external-field roce plugins, and the conclusion was that no special adaptation is required at this point. The team also completed the cleanup of raw data dependencies for scheduler data engineering and captured the results in Data Dashboard Design-v1. In parallel, the team joined cororum development and release conversations focused on skills. For Kelania productization, Wyneon reported that rayjob remained pending, so the issue was analyzed and a fix was provided in [20260320]- rayjob not running, hanging at pending.

## Tomorrow's Plan

- Continue checking why ondemand preemption does not trigger gpu index allocation for gpu.
- Prepare Wyneon’s ray data scaling and backpressure optimization plan, and study Alibaba Cloud System-56588f1973 platform Quota design.
- Investigate data center, network, and cluster relationships for lower-priority, long-term multi-cluster planning; no help requests were stated.