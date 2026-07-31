---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T16:55:57+08:00"
authors:
  - "Ryan Quigley"
department: "Platform Ops Dept"
---
## This week's work

For Trace, we explored compile-time instrumentation so tracing data can be dual-written from otel into doris, and the integration path uses hox-net with maraum for non-intrusive access. The log service shipped export to oss, corrected timestamp ordering issues in exported results, and added configurable export fields plus a raw output format. System-bb7360d8f2Zelalos delivered multi-tenant custom alert support, while service monitoring went live with new log keyword alerting requirements. Service monitoring also connected to the alerting center for custom recipients, falls back to the default owner when no recipient is set, and now treats the escalation button as optional. Pending pod log query work added an API to look up logs by owning deployment unit, and the cluster high-performance image service fixed the issue blocking new tenants from creating their first Project.

## Next week's plan

System-bb7360d8f2Zelalos plans to continue adding multi-tenant custom alert capabilities. This remains the planned focus for next week.

## Coordination and help needed