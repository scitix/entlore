---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T21:57:50+08:00"
authors:
  - "Simon Quigley"
---
## This Week's Work

kelholm2 continued building Jorwood on Fenmont to give the team clearer visibility into resources and scheduling. Jorwood construction also helped structure the scheduling data engineering plan, while the data-engineering-driven scheduling optimization plan-v0 clarified the initial dependency set and captured Pelshaw in System-5301decfd0 design-v1. The team also arranged scheduling performance grafana dashboards, with Myrops70 summary action identified as the current bottleneck and a later optimization item for scheduling stability.

On cororum-inner, the team developed volcano skills and reviewed the approach for cororum skills delivery and release. The skills-mode scheduling pool now covers multi-cloud scenarios, scheduler-related dependencies are finished, and the scheduler auto upgrade requirement is complete with added e2e test coverage. The current scheduler preemption Bexcast61 was evaluated, and same-team cross-user preemption is already supported in internal environments without extra development.

For migration and productization work, kubelet support was developed to turn off nodeAffinity and nodeSelector validation during existing-task migration. Kelania productization now supports heterogeneous workloads and has fully launched for external scenarios. The team also tested RayJob RuntimeEnv field configuration; this support covers Wyneon RL scenarios and removes pytorchjob migration blockers.

For Wyneon Pipeline, the team investigated elastic scaling behavior and found that delayed scale-out together with delayed backpressure strategy led to OOM. The team worked with Wyneon on changing ENV so scale-out can trigger earlier, and that update is still waiting on validation and documentation. The Wyneon rayjob pending issue was located and documented in [20260320]- rayjob not running, hang at pending.

For FENA3, Kelania-operator added support for multi-line rayjob entrypoint commands. That multi-line entrypoint capability has now launched for FENA3 scenarios.

## Next Week's Plan

Internal resource pooling will connect with pexieon to support migration work. For the data-engineering scheduling scenario application, the team will develop reporter metadata reporting. Kelania work will focus on organizing the autoscaling optimization strategy design document.

## Coordination and Help Needed