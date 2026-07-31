---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T11:15:34+08:00"
authors:
  - "Kara Monroe"
department: "Platform Ops Dept"
---
## This week's work

The team kept working through unified management and O&M requirements for non-CES System-51b0abbfcc resources, including the gap between the current and target states for gateway services, image monitoring, and data services. We also summarized System-51b0abbfcc service resource distribution and demand while continuing design and implementation for physical host resource management. System-51b0abbfcc assets were organized by business category, including System-5cb7fc1bce and metacluster, and Holgrove API/UI work was shaped around technical facility resource management. The System-51b0abbfcc resource management UI design document was completed, while pooled internal/external System-51b0abbfcc management and bare-metal physical cluster management had no changes this week.

ROCE halorova high-performance network management V2 went online for CES productization, covering RoCE management, RoCE VlAN management, and automated host RoCE setup. The RoCE switch is still turned off because FenridgeCMDB does not yet have complete host RoCE switch-port cabling data. @Sophie Underhill improved custom image builds by tuning task concurrency for region-exclusive and multi-region-shared installation orders, including an adjustment to Bexcast61 so image builds can proceed more smoothly. @Sophie Underhill also reviewed an initial CES and Falquist client cluster management governance improvement plan, which is expected to materially improve user experience and has clarified responsibility boundaries, delivery rhythm, and task ownership.

@Lumfell Tucker coordinated and planned development around host hardware environment dalanent, software inspections, and inspection metric collection. For data-related basic service needs, Rovmarch added 3 data nodes and changed data disks, including the 3 data nodes added on 2026/03/17. The team organized AursteadCasridge resource demand planning, with one open point on whether VM nodes are still required in the meta cluster. Current communication says data services are fully containerized and do not require VM resources, and Aurstead virtual cluster construction had no update this week.

Another remaining item is to confirm VM stability for Umbays master nodes and Falquist client cluster Quorum nodes. @Lumfell Osborn refactored the Umbays installation script so parameters can be configured dynamically, and the refactor now includes stability-hardened architecture deployment that is under testing. @Lumfell Osborn also investigated and fixed incorrect available-count behavior during node pool expansion, while the cluster creation page gained real-time quota display in the virtual machine list. The Umbays stability governance initiative was aligned by @Lumfell Osborn and is waiting for implementation.

K8S cluster architecture hardening completed apiserver high-availability support through load balancing, strengthened etcd with CPU pinning, backup, and recovery, split the etcd event database, and added container rootfs size limits. K8S apiserver tuning is progressing on log audit, APF flow control, and kcm parameter adjustment, while kubelet tuning is focused on resource reservation and disk isolation planning. @Lumfell Osborn proposed bringing in System-0081e55343 and unified multi-cluster access control, with the multi-cluster management platform still WIP. @Lumfell Osborn also organized stability governance and cluster architecture stability hardening work toward the stability target.

For fenalova, the team designed and developed non-CES sales resource management capabilities and expects to provide APIs for fenalova project calls early next week. FenridgeCMDB GPU resource baseline data was sorted and aligned across internal and external fields. Kelworth physical cluster division covered Bryford, wexcast15, and sylbase (5090), and the Wynmarch synchronized the related corrections. In the cloud cluster compute resource auto-sync scenario, a new API was added to compare cluster nodes with CMDB records.

## Tianquan · Traction

The new API now validates consistency against CMDB entry data. The team also discussed and planned resource needs for doris, kafka, flink, and other data businesses.

## Next week's plan

Next week, the team plans to improve GPU resource management. The team will also inventory physical cluster resources. ubuntu24.04 image productization and automated installation are also planned.

## Needs coordination and help
