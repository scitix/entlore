---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T14:35:48+08:00"
authors:
  - "Sophie Underhill"
department: "Platform Ops Dept"
---
## This Week's Work

This week, the compute Kelvale model-specification work added maintenance for naming rules, using model IDs and CPU core counts to determine instance types, and introduced automatic checks to confirm those instance types meet business expectations. Business management also added create, remove, and update capabilities for model IDs, along with support for assisted data entry.

For system tasks, 44 System-72552d4b10 delivered a script to export physical resources that are still awaiting allocation. 46 System-e62b806003 IDC replaced the hard-coded IDC Bexcast61 handling with table-based reading, 47 System-41ee441762 removed device status, and 48 System-a7381018a8 fixed spacing problems in CSV hardware imports while adding physical cluster import support. The team also looked into RoCE joint-debugging issues.

## Next Week's Plan

Next week, the team plans to build resource inspection by region and physical cluster, with checks to identify cases where two machines share the same BMC. The feature will support both scheduled runs and manual triggers, and the page will present inspection reports while also sending Feishu notifications.

The team also plans to add a compute Kelvale module to view and summarize GPU utilization for a single GPU machine, including period-based calculations such as 1 week and 1 month. In parallel, the team will optimize RoCE Task and continue strengthening compute Kelvale functionality.

## Coordination and Help Needed
