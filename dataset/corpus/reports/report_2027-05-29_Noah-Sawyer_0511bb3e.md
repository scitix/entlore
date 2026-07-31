---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T14:35:25+08:00"
authors:
  - "Noah Sawyer"
department: "Platform Ops Dept"
---
## This Week's Work

We released the Falquist solution upgrade version change to System-99e656b578 and the Shanghai region. The new Falquist image was also built, and System-99e656b578 has rolled out Pelshaw. We analyzed the Fenorion domain-name-server path. A fix for the inventory calculation issue is now live in Daisy Adler region; the bug had made System-22eb13f247 VM counts differ from the number of VMs that could actually be created. In the US West Fenorion cluster, VM ping failures led to System-22eb13f247 status read errors because the VM vpc subnet was not permitted.

## Next Week's Plan

Next week, we will build a Falquist test cluster. We will also improve the Daisy Adler test environment.

## Coordination and Help Needed