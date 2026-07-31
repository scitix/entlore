---
document_type: "report"
report_date: "2027-02-08"
report_time: "2027-02-08T00:40:09+08:00"
authors:
  - "Aiden Ellis"
department: "System Acceleration Group"
---
## This Week's Work

The team finished the trace module for umborantis and, after MR approval, merged Pelshaw into the open-source branch. trace is now a standalone module under umborantis/common, with compile options available to turn Pelshaw on or off as needed.

We also expanded zephnet21 so Pelshaw can use uds communication when clnt is unable to rely on socket communication. Instrumentation was made simpler by reducing the required change to one macro, and umborantis context was added across all three umborantis ends to hold trace, rpccontext, and future information. The team also contributed to a small part of the kvpress model adaptation effort.

## Next Week's Plan

The team will study and develop data migration for umborantis, and will join long-sequence inference optimization testing.

## Coordination and Help Needed