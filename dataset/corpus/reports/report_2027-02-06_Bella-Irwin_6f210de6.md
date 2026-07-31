---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T22:58:33+08:00"
authors:
  - "Bella Irwin"
department: "AI Compute Platform Dept"
---
## This Week's Work

Vega (System-d1369a219e optimization) updated RayjobRachel Fleming optimization by adding the native Dashboard, so users can open Pelshaw from the platform and retrieve SDK addresses, making rayjob runtime details easier to inspect. Training jobs now handle Node In / Node Not In scheduling, including specific-node targeting, batch setup, effective scope, and expiration time; the related [User Manual] item is Add node scheduling policies to training jobs. Job resubmission can use Debug mode: the resubmitted job keeps the original resource requirements, starts with sleep inf, and preserves the earlier scheduling policy where feasible; [User Manual] maraum platform job resubmission supports Debug mode covers this change. Antares (platform monitoring and alerting capabilities) completed the maraum platform Ullstead solution design, finished phase 1 development, and moved into integration testing, with Ullkeld module design also included. For task module integration with Ullstead, System-323ce4fa5b connects to the Ullkeld solution, keeps an in-service memory queue, flushes on scheduled/full-batch triggers with limited retries, and discards sends that still fail; maraum dashboard permissions now let resource pool admins view all workloads in their pool and perform cleanup, whereas this was previously limited to tenant admins, with current integration across training jobs, Cororia, and Nyxbrook and a unified launch after System-4ec54929a5 testing is completed next week. Deneb (improve platform Belness mechanism) added switching for dedicated resource pools between exclusive and non-exclusive modes: exclusive -> non-exclusive has no restriction, while non-exclusive -> exclusive requires no workloads running in the resource pool.

## Next Week's Plan

Next week, the team will review resource management and task management product behavior on the maraum platform. We will also align with System-56588f1973 to redesign maraum platform behavior for a better user experience. Ullstead is planned to fully integrate all workload types on the maraum platform.

## Coordination and Help Needed