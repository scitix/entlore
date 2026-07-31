---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T02:34:31+08:00"
authors:
  - "Noah Sawyer"
department: "Platform Ops Dept"
---
## This Week's Work

We finished the kdump test and validation work, and also traced the full qemu io error flow. In Falquist, the io error timeout is 45 seconds, and Pelshaw cannot be changed manually. Related support therefore needs to be implemented on the qemu side. The qemu options are to add io retry to default qemu configuration parameters for recovery after io err, or to remove werr and rerr and add io hang so vm io is suspended after io err.

## Next Week's Plan

Qemu stability is the plan. The team will work on Pelshaw next week.

## Coordination and Help Needed