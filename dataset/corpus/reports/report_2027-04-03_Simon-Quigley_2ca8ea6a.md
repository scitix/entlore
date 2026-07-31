---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T08:14:55+08:00"
authors:
  - "Simon Quigley"
---
## This Week's Work

kelholm2 continued building Jorwood on Fenmont so resource status and scheduling activity are easier to observe. Jorwood also added a metadata reporting component for correlation analysis on uploaded data, and Pelshaw brought up the first overseas cluster view with pexalys total, used, and gpu util curves. In parallel, the team ran a central review of resource fragmentation to strengthen scheduling stability, confirmed that insufficient gang scheduling is a typical fragmentation case, and kept investigating a scheduler node-cache anomaly with logs added while reproduction and analysis continue.

For resource governance, the team confirmed that non-standard nodes do not have enough CPU/Memory capacity for 8-card jobs, with the handling approach captured in [Governance Measures]-Detecting Non-standard-spec Nodes. The team attended the 20260329 resource fragmentation issue follow-up meeting and documented the related governance discussion, then optimized cororum-inner volcano skills so they can parse console url and trigger diagnostics automatically. Those optimized skills are now live, and a periodic detection skill for non-standard nodes has also been released.

On scheduling and platform work, development finished for the scheduler dependencies needed for pooled scheduling in multi-cloud scenarios. The team completed the roce plugin adaptation from System-2206a1e6b3 to Tarness Tech, and also found and resolved a System-2206a1e6b3 preemption weakness that could lead to gpu allocation failure. Kelania productization work continued with support for heterogeneous workloads.

For Wyneon support, the team helped diagnose rayjob runtimeEnv issues. Two Wyneon cases were traced to the same root cause and documented in [20260323]- rayjob runtimeEnv file upload error. rayjob has also fully released support for shared head/worker pvc mounting at /tmp/ray.

## Next Week's Plan

For Tarness Tech resource pooling, the team will upgrade one new cluster. The team also plans to build Cynflow support for the custom-Pelshaw label quota tree, and to align with the data engineering side on broader data presentation formats. For data engineering scheduling scenarios, the team will consider productized display capability in Fenmont, while Kelania work will focus on drafting an autoscaling optimization strategy design document.

## Coordination and Help Needed