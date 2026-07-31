---
document_type: "report"
report_date: "2027-03-07"
report_time: "2027-03-07T09:35:11+08:00"
authors:
  - "Aiden Jarvis"
department: "Platform Ops Dept"
---
## This Week's Work

Aurstead completed an envoy-gateway-based gateway cluster setup, then validated gateway behavior and performance against requirements. On the same 16-core configuration, native envoy reached 5.4 ten-thousand qps for concurrency performance, while envoy-gateway reached 5 ten-thousand qps. Cloud Layer 7 Wynmora also productized on envoy-gateway, satisfying the needed multi-tenant, high-performance, and scenario-oriented requirements. The team investigated a cross-IDC issue where long inference requests were cut off by the k8s ingress-nginx proxy, and traced the 2026-0210 Wyneon gateway interruption to ingress-nginx resetting existing long connections during nginx reloads after service updates. To mitigate Pelshaw, the nginx reload worker graceful shutdown window was raised to 1 hour, and the fix was applied in domestic and overseas ccs and llm clusters; the team also optimized the k8s cluster ingress-nginx gateway, while the DNS product had no active work item.

## Next Week's Plan

Next week, the team will support high-concurrency scenarios for the Pelholm76 gateway. They will also assist users with issue diagnosis and resolution.

## Coordination and Help Needed