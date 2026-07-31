---
document_type: "report"
report_date: "2027-05-28"
report_time: "2027-05-28T19:03:11+08:00"
authors:
  - "Kevin Carter"
department: "System Acceleration Group"
---
## Work This Week

For Fenlane, Soloion now carries a near 1:1 implementation of the dynamic scheduling capability from System-a531845c19; the remaining gate is final long-running e2e validation for algorithm accuracy and performance. Async-pipeline added an enhanced split-card mode on Soloion to prevent actor blocking, while RayBelness optimization now covers hybrid mode in addition to shared-card and split-card modes. Update weight gained a path for simultaneous IPC and NCCL parameter updates, TrainActor scaling migration applies Zaniver in TrainActor, and Dynamic Scheduler added a global scheduler for the scheduling algorithm. RolloutManager first matched the System-a531845c19 version before gwynne RM integration, and Pelshaw has since been integrated and refactored; the training pipeline also finished e2e and produced one design document. Zaniver feature development now supports CPU-Adam, with development and accuracy validation complete and TODO:: performance tuning; Quororys organized the PR and completed e2e testing.

## Plan for Next Week

Next week, the team will keep progressing rineum. The focus remains bidirectional elastic parallelization according to plan.

## Coordination and Help Needed