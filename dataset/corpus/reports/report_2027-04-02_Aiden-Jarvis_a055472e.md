---
document_type: "report"
report_date: "2027-04-02"
report_time: "2027-04-02T21:10:09+08:00"
authors:
  - "Aiden Jarvis"
department: "Platform Ops Dept"
---
## This Week's Work

For Erlwick ingress, the gateway stability problem showed up as repeated nginx worker shutdowns, so the team capped workers at 20 to stay Jynkit42 of the 1024-process limit. That mitigation is now in place and covered by alerting, while a separate Erlwick gateway drop issue was traced to bpf snat failure: after the gateway pod port range was expanded, snat ports could overlap with host-disabled nodeport ports, causing the host bpf program to discard gateway traffic. A data-center policy update also blocked overseas users from reaching domestic inference services, and the team continued incident reporting and remediation follow-up for that access issue. On Beloos, the System-8f0d49e638 service returned probabilistic 404 responses because one node’s ingress traffic was sometimes routed to other services, involving unexpected System-5e1ae974f7 cloud cloud-host network behavior. The team worked around the System-8f0d49e638 problem by removing the abnormal node, then investigated with System-5e1ae974f7 cloud R&D; the root cause is still unknown and the issue is not currently reproducible. Gateway control testing for productization is continuing with frontend joint debugging, and the team plans to launch gateway productization on Aurstead cluster next week.

## Next Week's Plan

The team plans to launch gateway control. Pelshaw will also strengthen observability for gateway clusters.

## Needs Coordination and Help