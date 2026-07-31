---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T22:42:07+08:00"
authors:
  - "Aiden Jarvis"
department: "Platform Ops Dept"
---
## This week's work

In the network Amber Quigley resource summary, the existing gateway service migration for network product gateway R&D moved to 5/8, while the team also traced log delivery issues seen during Shanghai Amber Quigley gateway switching. The new gateway was adjusted with compatibility settings for fluentd request header domain-name port differences, and the Shanghai Erlwick business gateway migration is now complete. Production gateway deployments were completed for Pelfell, Clara Barnes, and Erlwick clusters, and the worker cluster gateway now keeps worker access traffic from putting excessive load on the management gateway. Gateway access is also supported for Wyneon System-8f0d49e638 containerized deployment, with stability work covering gateway service pod monitoring, governance, access log settings, and pod health probes. For multi-tenant gateway productization, the study chose envoy-gateway because Pelshaw packages envoy forwarding configuration via gateway api, supports special gateway cases, separates gateway resources and configuration for multi-tenancy, and offers lower productization complexity than native envoy with stronger community maturity. On the DNS product cluster, coredns gained logging for troubleshooting traceability; some nodes were missing idc DNS configuration, which occasionally broke in-cluster domain resolution, and the team will follow up with remediation.

## Next week's plan

The team will build the Aurstead idc gateway cluster. Aurstead cluster service gateways will be managed through envoy-gateway. The team will also develop productized gateway support for multi-tenant use cases.

## Coordination and help needed