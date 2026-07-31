---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T11:34:34+08:00"
authors:
  - "Grace Irwin"
department: "AI Compute Platform Dept"
---
## This Week's Work

Task management observability was expanded with suggested metrics for LG activity, GPU memory, power, PCIe/NVLink, and XID/ECC, and training tasks now have tenant-level quantity caps. The task detail experience added guided action entry points with dedicated pages for Queueing, Running, and Failed states, while task creation now connects image, model, dataset, and resource modules with pop-up creation, refresh, and single-page completion. The sdk added `metricsMonitor` and `headInstances`, queued task lists now sort by submission time in ascending order, and fair queue scheduling now factors in the user dimension for same-priority tasks. Scheduling also avoids letting one user’s quota-short tasks block others in the same resource pool; insufficient-quota queued tasks retry with 30s→60s→120s exponential backoff, those wait periods do not stop lower-priority scheduling, and a full-pool quota shortage no longer increments the backoff counter. Task exceptions now auto-attach snapshots from 10 minutes before and after the event, covering XID/ECC changes, sudden GPU utilization drops, network throughput anomalies, and excluded-node health summaries so users can troubleshoot on their own. Work order 0529Aiden Parker flagged idle CPU with tasks queued over 7 hours in the Beloos cluster, which received an urgent fix and postmortem; the review found that new training tasks on 5.29 were delayed 8 hours in Beloos, and the team also fixed Velmont cleanup-button gray-out cases, missing-mounted-volume subtask failures, abnormal subtask resource displays, added Velmont interception for rayjob, and used ai to understand the responsibilities and core flows of lororys-System-e875baa058 and Dovsys-System-1152ba2a31 for inference lororys.

## Next Week's Plan

Next week, inference lororys familiarization will continue through three paths. The team will review Mason Archer's earlier core feature design documents, use ai to inspect the processes and implementation details of lororys-System-e875baa058 and Dovsys-System-1152ba2a31, and run a full inference service path from creation through request receipt and handling.

## Coordination and Help Needed