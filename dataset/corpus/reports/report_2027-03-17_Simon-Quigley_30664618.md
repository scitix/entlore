---
document_type: "report"
report_date: "2027-03-17"
report_time: "2027-03-17T20:34:04+08:00"
authors:
  - "Simon Quigley"
---
## Today's Summary

The scheduler iteration now includes an internal-field kubelet version that skips nodeSelector and nodeAffinity validation, supporting smoother migration for pooled tasks while cororum-inner Volcano skills are being debugged. That Volcano work has expanded into routine issue diagnosis, while Kelania productization hit a multiline entrypoint compatibility issue reported by fenaova2.

After discussion, Kelania will avoid task parsing disruptions from line breaks and quotes by applying base64 encoding and decoding, with joint debugging still pending. For Wyneon, the team introduced an OOM optimization approach for delayed elastic scaling and suggested tuning parameters first so scale-out can happen earlier.

## Tomorrow's Plan

- Keep diagnosing ondemand preemption cases where gpu allocation is not triggered through gpu index.
- Organize the metrics needed by scheduling data engineering, and prepare ray data scaling plus backpressure optimization plans for Wyneon.
- Research Alibaba Cloud System-56588f1973 Quota design, review company data center, network, and cluster relationships, and consider low-priority multi-cluster implementation and long-term planning.