---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T12:51:00+08:00"
authors:
  - "Yvonne Carter"
department: "Platform Ops Dept"
---
## This Week's Work

We built a team-specific distribution on Ubuntu 2404 and finished tailoring sysctl, kernel boot settings, related parameters, and required software packages. We also reviewed why installation is currently slow and failure-prone, then started focused tuning to reduce install time and improve success rates. In parallel, we are merging custom content with the Nvidia driver and ofed driver into the OS base image for offline deployment. This offline base-image approach should help speed up the overall installation flow.

## Next Week's Plan

Next week, we plan to finish creating the OS base image. After that, we will begin Linux kernel customization.

## Coordination and Help Needed