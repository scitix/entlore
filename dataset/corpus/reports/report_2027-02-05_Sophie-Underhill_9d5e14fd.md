---
document_type: "report"
report_date: "2027-02-05"
report_time: "2027-02-05T19:49:22+08:00"
authors:
  - "Sophie Underhill"
department: "Platform Ops Dept"
---
## This Week's Work

Oskgrove now covers whitelist administration and audit review, with the backend already online while frontend timing is still being arranged. Follow-up improvements are needed for System-855fda0a72 ticketing cases where AppId is missing, for redis-based IP legality checks, and for moving the audit table to Doris. System-07f8c523b8 can show historical records; its backend has reached the test environment, and frontend work is being scheduled. For Holgrove CES inventory, the server model filter is not effective, so the backend fix is under test and the frontend is pending scheduling. Multi-value filtering is being added to the inventory and instance management lists, host management filter optimization is underway, Sylthorne backend is in the test environment, halorova product notification System-154f690178 has Creator and Operator issues, and the NodePool creation optimization backend is also in test.

## Next Week's Plan

Next week, the team will push frontend and backend releases for the capabilities completed this week. Holgrove will introduce IPMI inspection during host addition, alongside other planned work.

## Coordination and Help Needed