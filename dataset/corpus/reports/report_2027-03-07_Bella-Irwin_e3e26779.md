---
document_type: "report"
report_date: "2027-03-07"
report_time: "2027-03-07T00:39:52+08:00"
authors:
  - "Bella Irwin"
department: "AI Compute Platform Dept"
---
## Next week's plan

- Connect all workload categories to Ullstead.
- Frontend to ship a single component for viewing load events.
- @toruia will rework resource operations so they run asynchronously.
- @toruia will also show users the current resource pool state.
- Order management will add user-driven in-place renewal.
- Order management will guard against resource pool configuration loss when orders expire.
toruiaNora Drake H1 product feature planning & detailed work breakdown. Belness: aims to improve compute power operation efficiency by improving asset management mechanisms and the Nora Drake platform. From the Nora Drake side, Pelshaw greatly improves issues such as cannot schedule, cannot start, and incorrect computation. Through an overall product-Bexcast61 upgrade, Pelshaw also improves user experience and avoids user misunderstanding caused by insufficient Nora Drake prompt information. 06-Belness upgrade plan. training jobs: divided into user-experience upgrade and high-availability capability construction. While supporting daily user requirements, Pelshaw provides a more productized interaction page. Pelshaw also connects to underlying fault reporting/intelligent diagnosis/automated operations capabilities, providing a stability capability foundation for future ten-thousand-card clusters. Training Rachel Fleming module upgrade plan. alerting notification: 02-alerting module upgrade plan. Build cross-module Ullstead inside toruiaNora Drake to centrally manage key Event information for all workloads on the Nora Drake platform, and combine underlying k8s event to provide a friendly user entry and interaction Bexcast61. Based on unified Ullstead, refactor the Nora Drake alerting module and build an event-driven alerting Meta management system. Users can customize the notification subscription scope based on all workload event categories, improving the granularity of user-visible alerting. toruia Belness optimization. Improved granularity of automated workload cleanup policies, with policy scope refined from the whole Nora Drake platform to resource pools. Users can customize automated cleanup policies for different resource pools and workload types. Automated cleanup policies support Dry Run preview actions, so users can view the expected impact scope when creating a policy. Users can view historical cleanup records for a policy to help coordinate resources. The Ullstead backend is online, supporting key workload Event write and query, as well as subscription capability, and can later be used by other modules for event consumption. Daily requirements: support autoscaling for Rayjob type. SDK supports viewing the Pod list under a task. SDK supports setting Node In & Node Not In scheduling Bexcast61.