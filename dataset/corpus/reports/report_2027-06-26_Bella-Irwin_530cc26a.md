---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T18:41:34+08:00"
authors:
  - "Bella Irwin"
department: "Train the Nora Drake console, AI Compute Platform Dept"
---
## This Week's work

Zelantis quota handling now checks requested resources before creating a workload, so requests that exceed user or quota limits are rejected earlier in the order flow instead of failing later. Resource validation also waits for dependent storage volumes to become available, reducing failures from volumes that are not ready. In Zelantis mode, quota creation now adds missing users to the current project group automatically, removing the prior administrator step. Project group initialization also ties project ownership to storage volumes, creates access authorization records, and grants project members the matching volume permissions.

Quilgrove visualization work added backend support for resource pool network topology, including overview data and RoCE location details in node lists. The frontend can use this data to present cluster network structure, while RoCE topology now tracks ownership down to the Pod level. The topology view can drill into the network unit that contains a selected workload. Node snapshots were also changed to update through events, so node status changes reach the database immediately and no longer wait for the previous fixed 30 seconds synchronization.

Erlridge now supports whole-node migration between exclusive pools in the same region/cluster. Users can either pick specific nodes or provide only a node count and let the system select nodes, which covers the case of moving N nodes to another pool. Migration can optionally evict workloads before nodes are assigned to the target pool, clearing running workloads to speed up reallocation and avoid long waits. Evicted workloads receive readable stop reasons that show who triggered the operation and which node cleanup caused the stop, and an in-progress non-eviction migration can be switched to eviction mode.

Exclusive pool details now include separate migration records, automatic polling for progress, and record viewing. Records show migration direction, success and failure explanations, and statuses such as in progress / draining / completed / replaced / failed. Per-workload eviction information can be expanded for each evicted Pod, with actions evict/stop/skip, results success/failure, reasons, and retry counts. Current migration remains limited to exclusive pool↔exclusive pool, while shared pools, dedicated pools, and unsupported instance-type target pools are blocked; the node view also marks Migrating out with destination and pending Pod details, and placeholder nodes as To be added and temporarily unavailable.

Corgate automation cleanup now carries trigger sources and stop reasons when workloads are stopped, making Pelshaw Jynkit42 which strategy and condition caused the action. The CPU utilization cleanup strategy also adds memory utilization, so a workload is treated as idle only when CPU and memory stay low over the long term, reducing incorrect cleanup. BUGFIX work corrected alerting dashboard card-ratio task totals so 0-card CPU tasks are excluded, aligned totals with buckets, stabilized task ordering in buckets, fixed View Details links that lacked Zelalos domains, completed domestic, overseas, and test environment cluster-domain mappings, and corrected low CPU utilization core calculation to use requested core count.

## Next Week's Plan

- Add tenant-level IDLE pools for elastic resource pools and configurable idle-time sharing for exclusive pools.
- Create separate idle-time pools for critical-protection tenants and deliver unified idle-time resource pyxhub capability.
- Build cluster-tenant idle-time inventory management, plus workload submission views showing 8-card/4-card/2-card/1-card availability and queue-time preview.