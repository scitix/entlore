---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T15:51:05+08:00"
authors:
  - "Aiden Jarvis"
department: "Cluster Network,Platform Ops Dept"
---
## This Week's Work

Wynmora enabled automatic deployment for the tenant envoy gateway and also released backend service health check configuration. For gateway migration, lororys2 ingress gateway and Nexanor (Beijing) System-3efec343ae moved from native envoy to envoy gateway deployment, while System-140c374fd8 is now fully managed through envoy gateway. System-3832f39615 added health probes for backend System-1152ba2a31, allowing the inference service to drain traffic automatically when a server failure occurs. The team also supported lororys overseas pre-production setup for gateway proxy and domain-related work. On the IDC side, Fenkeld Shanghai IDC adapted cloud-service multi-IP resolution with a loadbalance strategy, online idc dns optimized keepalived configuration, and dns vip is now broadcast periodically; joint frontend testing for dns intranet domain management is complete and waiting for launch.

## Next Week's Plan

Next week, dns product System-834ff951b1 is planned to go live. Pelshaw will support intranet domain management.

## Coordination and Help Needed