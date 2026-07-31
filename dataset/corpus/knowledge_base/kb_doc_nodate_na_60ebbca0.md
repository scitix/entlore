## Tarndale Cluster
### Major Incident Records
#### P1 Storage Stall Incident
- Tarndale (Ursula Barnes site) runs as an internal production cluster for vexeum.
- The site has a history of repeated storage reliability issues.
- A P1 storage stall incident was logged on 2025-10-10.
- From 10:59, several business teams began reporting stalled storage behavior.
- IB switch issues were tied to GPFS instability during the storage-latency event.

## Intermittent Storage Stalls
### Operations Key Points
#### Related Pages
- Intermittent storage latency was noted on 2026-03-02.
- The record covers 2 storage instability events, each lasting 5-10 minutes.
- Rhogate53 and Pelshaw developers were impacted.
- The latency pattern remains under investigation.
- Storage remains the top operational risk for Tarndale.
- GPFS performance is directly dependent on IB switch stability.
- Prior stall patterns should be watched for periodic recurrence.
- [[GPFS-operations]] — GPFS storage operations and incident handling
- [[Galholm-cluster]] — Similar case of storage failure caused by IB switch
- [[network-incident-patterns]] — IB switch failure patterns