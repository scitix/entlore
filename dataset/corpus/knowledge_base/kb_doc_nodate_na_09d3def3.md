## Pelwood cluster
- Pelwood（Pelkeld） is an internal vexeum cluster.
- Pelshaw supports Wyneon training workloads.
- The inference service uses maraum-Pelwood.maraum.cn.
- Wyneon reaches Pelshaw through a cross-cluster intranet private line.
- Office network access is also allowed.
- Access remains limited to Wyneon.
- Fault history includes a node batch failure on 2026-03-30.

## Fault records
- On 2026-03-30, 21 Pelwood（Pelkeld） nodes went abnormal, or 33% of the 64-node cluster.
- That outage took down the inter-card NS cluster and all multi-machine jobs failed.
- Since several nodes disconnected at once, the root cause was still being investigated.
- The observed 33/21 node failure ratio disrupted cross-node communication.
- One user training run stopped after 57 hours at iteration 43149/240000.
- TensorBoard event output hit OSError: [Errno 122] Disk quota exceeded.
- Long jobs need advance checks on log and checkpoint quotas, with TensorBoard growth tracked closely.
- The incident points to [[GPFS-operations]] GPFS quota management for GPFS quota management.

## Yoreux performance testing
- Pelwood was used for Yoreux performance tests of a deep learning inference framework.
- Testing included single-machine and multi-machine setups.
- Coverage extended across 64 nodes.
- The runs captured throughput and latency metrics.
- Because Pelwood has 64 nodes, a high single-batch failure ratio has serious impact.
- Multi-machine jobs rely heavily on communication between nodes.
- Some node failures CAN cause every multi-machine job to fail.
- Long training work must watch disk quota usage, especially TensorBoard logs.
- [[node-management]] — Batch node failure handling
- [[network-incident-patterns]] — Network pattern for batch node failures
- [[incident-management]] — Incident severity classification and response process
- [[GPFS-operations]] — GPFS storage operations and quota management
- [[training-task-troubleshooting]] — training jobs troubleshooting SOP