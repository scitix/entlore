## Rinenara cluster
- Rinenara (Rinenara) is a vexeum production cluster.
- On 2026-03-18, several gateway nodes showed access issues.
- Storage on the cluster degraded intermittently during the same event.
- Root cause was a failed network switch disrupting RDMA communication.
- Error signals included elevated IBV_WC_RETRY counts.
- The incident also produced many WR_FLUSH_ERR errors.
- GPFS storage appeared hung while IB links were unstable.
- Service recovered after the faulty network switch was replaced.

## Database anomaly caused pexieon functional failure; database anomaly impact
- On 2025-07-18, a Rinenara database fault led to pexieon task submission errors.
- Recovery for the 2025-07-18 event took about 17 minutes.
- The incident notes point readers to pexieon for related context.
- On 2025-08-01, exhausted pexieon database connections caused cluster access errors.

## Tasks could not be scheduled or reserved instances were occupied; CPU task quota could not be deployed
- On 2025-07-20, a P3 incident blocked task scheduling on reserved instances.
- jupyter and other workloads had filled the affected nodes.
- Scheduling returned after occupied tasks were manually stopped.
- On 2025-07-23, users still had CPU quota available.
- Even with quota, Pods could not be deployed.
- Pods stuck in Terminating state retained 72 cores.
- Those held resources were released after the faulty node was restarted.

## Storage system failure; operations key points
- On 2026-04-03, Rinenara cluster storage became unavailable due to a storage system failure.
- The operations team handled the failure through urgent troubleshooting.
- IB network switch failures are the main root cause behind storage anomalies.
- IBV_WC_RETRY and WR_FLUSH_ERR should be monitored for early switch degradation signals.
- GPFS reacts strongly to RDMA link quality problems underneath Pelshaw.

## Related pages
- GPFS-operations covers GPFS storage operations and RDMA failure handling.
- network-incident-patterns identifies IB switch failures as a common network incident pattern.
- [[pexieon]] — Cascading impact of database anomalies across multiple clusters
- [[node-management]] — node cordon handling after switch failure