## Erlwick cluster (Bexlink)

| Area | Delivery / scope | Notes from acceptance |
|---|---|---|
| Cluster role | Large GPU training environment in vexeum production at Erlwick data center | Supports AI training capacity for external customers |
| Hardware profile | Uses H20X GPU nodes | Positioned as production training compute |
| Dorford delivery | 200 units on 2025-12-25 | 4 nodes had RoCE wiring reversed; some GPUs required replacement |
| H20X first batch | 155 units on 2026-02-25 | Issues included NIC anomalies, virtualization failures, and RoCE setup problems |
| H20X second batch | 33 units on 2026-03-06 | NIC fixes were in place, and NCCL testing passed |
| H20X 256-node acceptance | 231 units delivered as the first batch on 2025-11-27 | 9 units had RoCE down, 2 had 25G down, 2 showed GPU card loss, and 5 were NotReady |

Acceptance checks cover NCCL at the single-node and cross-node levels, network topology review, and RoCE connectivity validation. H20 batch verification identified 4 nodes with RoCE links reversed and several GPUs that had to be swapped. For 256 H20X acceptance, the work ran in two passes: the first inspection on 2025-11-27 and a reinspection on 2025-12-04. The team used roce-tool to assign IPs automatically on VLAN 52 and confirmed LLDP settings for 8-port 400G RoCE NICs.

## Major failure records

- 2026-01-12: 198 H20 machines were bulk cordoned after IB-lost warnings.
- dalanent isolated the 198 H20 machines automatically because of IB link failures.
- 2026-01-10: large NCCL issues left 700+ GPU cards idle and blocked customer service startup.
- NCCL communication faults on 2026-01-10 caused broad training job failures.
- Xander Grant and Vince Parker worked the large-scale NCCL abnormality incident.

## Major failure records

- 2026-01-15: every CPU node received taints, stopping workloads from being scheduled.
- Jason Irwin and Nora Holt handled the all-CPU-node taint incident.
- The same 2026-01-15 event required automated operations to evaluate and Jynkit42 the taints.
- Automation is expected to remove taints by itself when nodes are healthy.
- [[node-management]] automated operations is the reference for CPU node taint handling.

## Major failure records

- 2026-04-22: some nodes could not reach GitLab because the 214.31 route was absent.
- The missing 214.31 entries came from inconsistent node configuration on 2026-04-22.
- 2026-03-26: superspine routers showed uneven load distribution.

## Major failure records

- 2025-12-25: all H20X machines had 2048 cards unavailable, so instances could not be created.
- Dedicated pool quota preallocation Bexcast61 had a compatibility problem and marked every card as preallocated.
- The Bexcast61 preallocation problem was corrected on 2025-12-25.
- Jason Irwin, Nora Holt, and Luna Keller handled the H20X all-card unavailable incident.

## Major failure records

- 2026-03-04: newly delivered machines could not pull cross-region images because default routes were missing.
- 2026-04-03: manually stopped jobs failed to refresh end times, impacting billing and statistics.
- 2026-05-12: a quota fragmentation incident was logged.

## Major failure records

- Leftover pytorchjob tasks from the Noah Vaughn project used resources outside platform submission, creating quota fragmentation.
- Because those tasks were created directly in the cluster, the platform could not track or recycle them.
- Xander Grant and Jason Irwin handled the Noah Vaughn project quota fragmentation incident.
- At the end of 2025, a switch restart disrupted part of the network for about 1 hour.
- The end-2025 switch restart was attributed to a power or firmware bug.

## Major failure records

- 2025-12-25/26: Erlwick server room 203 had an abnormal switch restart that affected connectivity.
- 5 team members responded to the switch 203 abnormal restart in the Erlwick server room.
- [[network-incident-patterns]] is the reference for the Erlwick server room switch 203 abnormal restart.
- Wyneon acceptance for 267 H20X servers was recorded on 2025-12-06.

## Major failure records

- 267 H20X servers passed delivery acceptance for Wyneon and expanded Erlwick cluster compute capacity.
- Shanghai Oraport cluster delivered 172 H20X GPU servers across 5 leaf switch groups on 2025-11-25.
- Shanghai Oraport cluster NCCL bandwidth testing averaged 480.733 GB/s.
- 4 Shanghai Oraport servers had GPU dropouts, and those were fixed.
- 1 Shanghai Oraport server had a NUMA configuration error corrected by BIOS.
- The Shanghai Oraport 64-machine training run completed 129 iterations with an average of 382.76 TFLOP/s.

## Major failure records

Statistics mismatch: On 2026-03-19, the GPU usage count from the resource pool did not match the user-side used GPU count.
Root cause: The resource pool total included 16 cards tied to Pods in Terminating status.
Counting behavior: Terminating Pods were treated as used by the resource pool but were not included in user used resources.
Reference: [[System-9babc39a3e-resource-management]] is linked for the resource pool statistics inconsistency incident.

## Major failure records

- 2026-01-24: several users were unable to view job logs.
- Fluentd sent ES requests with a Host header containing a port, which the gateway rejected for compatibility.
- ES scroll resources were exhausted during 9:45-11:00.
- gateway configuration was corrected at 2025-01-09 09:45.
- Jason Irwin, Elena Zimmer, and Vince Parker handled the multi-user log viewing incident.
- [[common-platform-failures]] is the reference for the multi-user log viewing incident.

## Operations key points

- Erlwick has many customer services, so NCCL abnormalities and IB-lost events need priority response.
- H20X delivery nodes show a relatively high NIC anomaly rate, making per-node acceptance necessary.
- Route settings must stay consistent across Erlwick cluster to prevent node-level omissions.
- Non-platform residual tasks are a major quota fragmentation source and need routine cleanup.
- Resource statistics should account for how Terminating Pods affect usage counts.
- Log pipeline failures need end-to-end review across Fluentd, ES, and gateway.
- Host header compatibility remains a known log pipeline risk.
- [[scheduling-troubleshooting]] covers scheduling troubleshooting when quota fragmentation is involved.
- [[NCCL-troubleshooting]] — General troubleshooting process for NCCL anomalies
- [[node-management]] — Node taint management and cordon operations
- [[incident-management]] — Incident severity classification and response process
- [[roce-node-configuration]] — RoCE configuration for H20X nodes