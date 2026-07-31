---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T19:53:56+08:00"
authors:
  - "Ryan Quigley"
department: "Platform Ops Dept"
---
## This Week's Work

Arvops redesign and observability - Logs redesign both finished testing and validation. For observability - alerting management, the alert subscription API changes are complete; orgname is now auto-injected, data is written directly to n9e, and validation has passed. Soluor now highlights upstream and downstream dependencies for the selected service, supports selectable hierarchy levels, completed n9e rule import and prometheus rule import, moved log, event, and trace query capabilities to query-gateway, and added a performance analysis page. System-eb97735ecf remains under iterative development in the test environment, while System-cfaa3270bf added ebpf-instrument for traces and ebpf-profiler for CPU profiles with optional pprof profile integration. Oliiantis automatic service registration to Wynwick is still progressing and is expected to finish by next month-end; Wynwick dynamic multi-parameter alert configuration is online, https certificate alerts now fire 30 days early and have been released, and casport2 now has a pre-deletion image sync-rule risk check API with release still pending.

## Next Week's Plan

Next week will continue work on the Arvops redesign, observability - Logs redesign, and observability - alerting management redesign. Soluor data ingestion is also planned to add diagnostic functionality.

## Coordination and Help Needed