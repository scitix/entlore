---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T21:55:59+08:00"
authors:
  - "Owen Osborn"
department: "Platform Ops Dept"
---
## This Week's Work

We advanced the node stability work by splitting system disks from data disks and by placing kubelet and containerd data in separate directories, reducing shared failure points for node components. The resource reservation track also progressed, with node capacity held back and CPU cores pinned to make core services more predictable. For container storage control, the RootFS limit design uses NRI to restrict rootfs usage inside containers, helping stop business Pods from consuming disk space enough to cause Pod eviction. Monitoring work focused on reviewing kubelet metrics and refining the related dashboards. In operations, we replaced problematic master-node machines in the Dorholm cluster, though the Dorholm stability plan still needs more refinement; on 20260306, the tov-kit machine showed abnormal behavior and Daisy AdlerMARAUM was unavailable. Umbays product development resolved plugin installation authentication issues for newly created clusters and also fixed failures caused by missing namespaces.

## Next Week's Plan

Next week, we will continue fixing stability problems in existing K8S clusters. We will also strengthen the plan used for newly created K8S clusters.

## Coordination and Help Needed