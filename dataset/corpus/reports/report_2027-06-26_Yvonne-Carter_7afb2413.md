---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T13:59:24+08:00"
authors:
  - "Yvonne Carter"
department: "Platform Ops Dept"
---
## This Week's work

This week, the vyr-sys hot patch resolved the all-cluster kernel crash identified as BUG_ON kernel BUG at mm/rmap.c:1041!. We also began online OS configuration governance, with follow-up work aimed at making OS configuration more standardized and platform-based. For online kdump, the team investigated the intermittent success pattern and tuned 4 settings; those changes lowered the chance of crashkernel oom and let systems reboot automatically into a normal kernel after oom. Separately, all Oraport-kevloom machines were hit by debian package dependency problems that disrupted both apt install and apt purge, so we completed a repair script and are targeting release next week. The online ulimit value is currently too low and has been causing frequent node FD exhaustion alerts, and next week we plan to ship that fix along with the CVE-2026-46331 remediation for the high-risk issue impacting all ubuntu2204 and 2404 machines.

## Next Week's Plan

- Continue online OS configuration governance.
- Move forward on the xaneent virtual machine product solution for GPFS disconnection.
- Use the xaneent approach to turn IO Error cases into IO hang handling.