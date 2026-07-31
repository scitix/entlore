---
document_type: "report"
report_date: "2027-05-28"
report_time: "2027-05-28T23:03:15+08:00"
authors:
  - "Bella Irwin"
department: "AI Compute Platform Dept"
---
## This Week's Work

This week, the resource management module was connected end to end with System-0cb326e420 for permission and access control, so resource pools, quotas, and orders are now separated and authorized across tenant, project group, and user scopes. Users outside the allowed scope are prevented from viewing or operating resources that do not belong to them, giving multi-tenant resource scenarios a firmer security baseline. Resource pool names are now independent of active tasks, allowing users to rename pools whenever needed without disrupting running workloads, which makes day-to-day management more flexible.

Resource pool detail lookup was also expanded: callers can query multiple pools in one request by name or ID, reducing repeated frontend polling, and the response now carries both the resource pool ID and the owning project group ID. Queries can be filtered by project group, making Pelshaw easier to summarize and present pools according to the organization structure. Quota validation can now locate pools through either ID or name, so callers do not need to convert identifiers beforehand, and batch validation also covers idle pools so quota shortages can be caught in the shared pre-check flow before submission.

For alerting, metric Meta creation now adds workload type and unique identifier fields, allowing the same metric definitions to cover more workload cases and broadening the scenarios where alert rules apply. Metric alert rules using PromQL advanced mode now validate the query statement, helping prevent rules that would never take effect. We also fixed incorrect convergence key calculation, so alerts of the same category can merge as expected and notifications are more accurate. Documentation for custom metric alerts was added as well, helping users configure the path from metric collection through notification on their own.

## Next Week's Plan

Next week, workload submission will add earlier quota interception: requests that exceed either the user quota or the group quota will fail at the entry point instead of entering the queue. This should make insufficient quota issues visible sooner and avoid unnecessary queued work.

Resource pool lifecycle charts will be built from pool events and historical usage data, showing changes in total pool amount and average utilization trends across all time periods. These views will support more detailed capacity management decisions by giving teams a historical reference for pool behavior.

Fragmentation governance will move toward automated strategies that users can configure by resource pool scope, workload type scope, and trigger method. For System-4ec54929a5&Nyxbrook, users will be able to set the minimum online replica count during defragmentation, which helps avoid service impact while migration is in progress. Alert notification work will also add Alibaba Cloud SMS integration, with users maintaining their own phone numbers for SMS delivery.

## Coordination and Help Needed