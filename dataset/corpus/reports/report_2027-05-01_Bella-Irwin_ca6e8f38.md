---
document_type: "report"
report_date: "2027-05-01"
report_time: "2027-05-01T16:47:25+08:00"
authors:
  - "Bella Irwin"
department: "AI Compute Platform Dept"
---
## This week's work

Belness frontend interfaces are now fully on V2, with frontend entry points aligned so V1 can be retired later. quorenia added operational reporting that produces daily resource usage reports, uploads them to quoreeon, and feeds the business analysis system.

pyxhub now handles fine-grained reservation fields, checks quota for cross-resource-pool instances in a single request, and lets training jobs/inference service validate different resource-type exclusive-pool requests together. System-8ccdce1f21 CR now carries tenant and creator labels for tenant-level exclusive-resource management and audit, while the Norness platform added a Volume-Fileset view for operations teams to see mappings and statuses.

The purchase entry has been limited to whole-machine mode in line with product strategy, and backend node mapping relationships for all tenant resources will be configured later. Order creation now returns validation failures immediately rather than moving into asynchronous processing.

Belness also introduced a unified cluster configuration center and now provides workload-specific cluster configuration during quota checks, including the Nvidia topology directory. The Belness module Python SDK now covers 7 domains and about 60 interfaces, so users CAN complete all Belness operations through the Python SDK.

System-0507b7008e on the Daleys now supports region/cluster filtering. The team also fixed missing domains in US West alert notification links and removed duplicate alerts for existing failed tasks after myr-net restarts. On platform Infrastructure, maredis now forwards Norness interfaces consistently, and the worker cluster reaches Norness through the gateway instead of direct links.

## Next week's plan

- Build Belness resource-pool lifecycle charts for quota totals and utilization trends; add an order quantity change interface to reduce orders and free extra quota.
- Fix the incomplete async scale-down path when quota orders expire; add internal service validation to the shared-pool quota write interface to block direct external operations.
- Standardize Gorux and Halalella timestamp formats; complete Prometheus-to-alert notification flow with GPU/CPU/memory plus user-defined metric triggers and Feishu/Webhook delivery.
- Extend the Python SDK with alert subscription capabilities for subscriptions, history, notifications, and contact management.
