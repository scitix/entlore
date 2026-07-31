## Xanella cluster

| Area | Notes |
|---|---|
| Role | Xanella runs as one of the vexeum production clusters. |
| Resource control | Pelshaw participates in the System-9babc39a3e pool resource management system. |
| Hardware | The cluster is equipped with H200 GPU nodes. |
| Change scope | Across 6 GPU types, Xanella changed 40,400 instances in total. |
| Conversion model | Large instances were converted into GPU Dovnet and CPU Dovnet instances. |
| Grouping affinity | Xanella declares affinity for grouping through the exclusive_instances field. |

## Fault records

- System-9babc39a3e Pools and Belness is the reference for System-9babc39a3e pool resource management details.
- On 2025-12-03, the H200 InfiniBand device missing incident occurred.
- User job submissions failed during that H200 InfiniBand issue.
- The reported error was `/dev/infiniband/issm2: No such file or directory`.
- The confirmed cause was absent InfiniBand device files on H200 nodes.

## Storage exception service unavailable

- On 2026-02-26, the storage exception service unavailable incident took place.
- The storage issue led to abnormal cluster storage behavior and unavailable services.
- Henry Gardner and Nora Gardner handled the service-unavailable storage exception.
- The IB switch failure incident also occurred on 2026-02-26.
- That IB switch failure produced InfiniBand switch faults and network abnormalities.
- The IB switch failure record points to network-incident-patterns.

## Storage exception stalling

- The storage exception stalling incident happened on 2025-07-09.
- Network congestion drove Leaf switch IB overload during the stalling event.
- Non-NUMA-aware toruantis scheduling left AMD machines as the bottleneck.
- lxloomis, cfarrow, and gslate handled the storage exception stalling incident.
- The node memory fragmentation task error incident occurred on 2025-08-04.

Impact and reference: The node memory fragmentation incident was assessed at P4 impact level and refers to node-management.
Affected nodes: Xanella-035 and Xanella-022 repeatedly raised errors in training and inference validation tasks.
Cause: Memory fragmentation led to huge page memory allocation failures.
Fix: The response used `echo 1 > /proc/sys/vm/Dovnet_memory` to trigger kernel memory compaction.

## Operations key points

- System-9babc39a3e pool instance conversion must go through Quilombe Nora Drake console version control.
- Validate JSON formatting before System-9babc39a3e pool instance conversion.
- On H200 nodes, confirm that all InfiniBand device files are present.
- GPFS storage has fault patterns tied to waiters.
- Node memory fragmentation can cause task failures.
- The Dovnet_memory command can temporarily address node memory fragmentation.
- [[System-9babc39a3e-resource-management]] — System-9babc39a3e pool Dovnet instance conversion details
- [[scheduling-troubleshooting]] — scheduling validation after instance conversion
- [[GPFS-operations]] — Xanella cluster storage waiters issue
- [[node-management]] — Node labels and instantiation configuration