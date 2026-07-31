---
document_type: "report"
report_date: "2027-03-13"
report_time: "2027-03-13T22:48:13+08:00"
authors:
  - "Owen Tucker"
department: "Platform Ops Dept"
---
## This Week's work

I built the list and insert APIs for the US region service-launch API so data can be added without direct database changes, then added frontend-facing APIs, integration notes, and test validation. I also corrected related behavior by adding nameservers configuration plus sales type and disk size limits, and I consolidated configuration handling from separate maps into one centralized abstraction. The query tool was updated for better efficiency, with usage documentation added, while API integration and installation process optimization documents were also completed. Authentication still needs a later move toward a more standard model.

For installation work, I organized the install flow and created an all-purpose Go installer with HTTP static file service, embed file handling, API interfaces, TFTP service, and ISO file support. The PXE approach uses dnsmasq for DNS and DHCP, and I bought 3 virtual machines in the domestic production environment for testing. I tested API calls with ak/sk under tenant restrictions, wrote a Go remote-API caller with help from Falwood, and prepared scripts to gather details for 13 cluster expansion nodes, where 2 nodes were still Failed and need follow-up. I also studied CPU lag troubleshooting, reviewed a sched_setaffinity-based CPU monitor, used top, htop, ps, and perf for system checks, traced periodic high CPU sys% to kubelet, found an issue in memcg_numa_stat_show, diagnosed zombie memcg references held by page cache, compared long-connection and short-connection tradeoffs, and researched a machine command execution channel solution.

## Next Week's Plan

- Define 3-month and 6-month okr.
- Work with @Kara Monroe and @Elena Ellis on defense quality.
- Continue learning how to troubleshoot the 2 failed cluster expansion machines.
- No coordination or help is needed right now.