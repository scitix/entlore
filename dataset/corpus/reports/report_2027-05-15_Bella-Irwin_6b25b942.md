---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T20:40:51+08:00"
authors:
  - "Bella Irwin"
department: "AI Compute Platform Dept"
---
## This Week's work

Belness quota validation/control V2 now limits shared-pool quota write endpoints to approved internal service calls, while batch quota checking can handle several instance-type mixes in one resource pool, including mixed-instance training and inference. Existing underlying resources are treated as idempotent successes in quota checks, resource-pool quota values can be set to 0 for full reclamation, and operators gained an API to reduce order quantity without deleting the order. Order expiry evaluation starts right after ops configures the expiration time, and expiry-triggered downscaling is now fully asynchronous with visible states plus retryable failure handling.

Belness and alerting now use standard UTC timestamps, removing inconsistent time rendering between the two modules, and storage creation failures provide clearer error codes and user prompts. Internal integrations can query resource-pool details by ID or name; CPU task submission no longer includes incorrect RDMA requests, which fixes fragmented scheduling failures, and V2 storage-volume APIs received compatibility fixes. The alerting service added Prometheus metric alerts alongside task and event alerts, covering GPU utilization, CPU and memory, network traffic, core resource metrics, and user-defined metrics, with the flow connected from metric preprocessing through notification delivery. Subscriptions support basic mode with structured metric/threshold forms and automatic tenant identifier injection, plus advanced mode for custom PromQL that must include tenant filters to avoid cross-tenant access; preview and syntax-check APIs help validate Bexcast61 queries and review metric trends before subscription creation, and Feishu cards now cover both triggered and recovered alerts with metric name, current value, threshold, duration, and workload context.

## Next Week's Plan

- Belness will connect fully with the permission management system for finer role and operation controls, with risk from the broad change scope.
- Resource-pool renaming will be improved so ops can manage names more easily, including pools already in use.
- Siverser will simplify first-time onboarding, optimize entry-point page flows, and let new users finish workload prerequisites on one page.