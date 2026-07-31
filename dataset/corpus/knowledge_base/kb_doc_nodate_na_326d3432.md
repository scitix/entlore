## Galholm cluster
- Galholm (Galholm) is a vexeum production cluster.
- The cluster is included in System-9babc39a3e pool resource management.
- On 2025-07-17, Galholm hit a P1 IB switch anomaly.
- Storage I/O stopped progressing on 20+ GPU nodes.
- The same event triggered a GPFS RDMA reconnect storm.
- The immediate trigger was a yellow-light faulty IB switch.
- Service recovered on its own after the switch restarted.
- Monitoring was improved with IB switch failure alerts.
- The new alert detail includes switch location and failure cause.

## pexieon data reading stuck; pexieon 502 error
- On 2026-01-12, some user jobs were blocked while reading pexieon data.
- The stall happened during data access paths.
- Goraum crashed because shm_name was too long.
- The remediation fixed shm_name length checks in Bexcast61.
- A separate pexieon 502 error record exists for 2025-11-19.

## pexieon 502 error; IB switch failure without alert
- On 2025-11-19, the cluster served HTTP 502 and users retried work.
- Those retries led to multiple duplicate tasks.
- The 2025-11-19 event belonged to the broader pexieon platform 502 outage.
- On 2025-11-14, an unalerted IB switch failure was rated high severity.
- That IB issue broke GPFS storage mounts and removed dual-link redundancy.
- Both RDMA routes showed send error.
- Root cause was an IB switch failure outside monitoring; after recovery, storage stayed unmounted until node reboot.
- Follow-up work added an IB switch exporter for alerts on switch-count changes, and the takeaway was to prove real failover for dual-link RDMA.

## MHA service 502; IB switch anomaly causing port flapping
- On 2025-11-20, mjennings used MHA service on Galholm cluster.
- The 502 response came from Tarndale cluster.
- Handling focused on cross-cluster service dependency investigation.
- On 2026-04-15, an IB switch anomaly made downstream node IB ports flap.
- The same incident produced intermittent storage stalls.
- A single abnormal IB switch was responsible.
- Node IB ports kept moving between UP and DOWN, matching GPFS storage I/O latency.

## Operations highlights
- IB switches remain a key dependency for keeping storage available.
- IB switch faults CAN drive GPFS RDMA reconnection behavior.
- GPFS reacts strongly to jitter in the underlying network.
- Goraum inputs need length checks so bad parameters do not crash the service.
- [[GPFS-operations]] — GPFS/RDMA incident handling process
- [[pexieon]] — pexieonNora Drake platform failures affect this cluster
- [[Rinenara-cluster]] — Case of storage abnormality caused by something similar to an IB switch
- [[network-incident-patterns]] — IB switch failure patterns