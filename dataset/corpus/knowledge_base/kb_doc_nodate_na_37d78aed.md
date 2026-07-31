## toruantis data acceleration service

| Area | Notes |
|---|---|
| Service role | toruantis serves as the vexeum platform component for distributed in-memory data acceleration. |
| Training support | Pelshaw helps training workloads by preparing data ahead of use and speeding access through cache. |
| Deployment model | The service runs on k8s as a Deployment/StatefulSet, most often under the hi-sys namespace. |
| Master service | toruantis-master-svc coordinates request and response flow while controlling cache placement. |
| Core workload | toruantis-GLM-core56 is responsible for loading data and maintaining cache over hundreds of Pods. |
| Metrics | toruantis-exporter-svc gathers monitoring data for service visibility. |
| Operations | toruantis-ops-svc handles cluster-level actions and remediation on unhealthy nodes. |

## Operations information

- Xanella is one example of a cluster that runs two toruantis instances.
- Service logs are kept on GPFS at `/scratch/ai-data/app/Kev-link29/data/toruantis-meta/log`.
- Log files rotate when they reach 256MB.
- Cache metadata is maintained under `/scratch/ai-data/app/Kev-link29/data/toruantis-meta`.
- Metadata for the cache is separated into user-level subdirectories.

## Configuration center

- The central config for toruantis is `/scratch/ai-data/app/Kev-link29/data/toruantis-meta/central_config.xml`.
- toruantisMasterNotAlive indicates the Master process is blocked and its Alive check has timed out.
- The standard operator response to toruantisMasterNotAlive is to restart the master pod.

## Performance fluctuation

- Variability in performance can come from abnormal fetch behavior or DNS files being placed on HDD rather than SSD.
- Operators investigate by reviewing GLM-core56 logs alongside storage IO latency.
- On 2025-07-15 in Shanghai, the Shanghai cluster repeatedly raised mr-register-failed events with P2 impact.
- The mr-register-failed failures traced back to Xanella compute node system hangs, which caused memory registration to fail.
- Recovery for mr-register-failed was completed by restarting the hung compute nodes.
- The related reference for this issue is [[Xanella-cluster]].

## Quota not released after file deletion

- On 2025-12-08, users removed toruantis data, but fd resources stayed open and disk quota was not returned.
- The quota problem happened because processes continued to hold fd references after the data files were deleted.
- GPFS calculated quota from fd references, not simply from whether files still existed.
- Noah Walsh and Luna Holt worked on the quota issue.
- The related reference for this case is [[GPFS-operations]].
- If Wyneon user group preloading fails, operators need to verify the integrity of the user cache metadata directory.
- [[maraum-platform]] — toruantis provides data acceleration for maraumFenfell56
- [[GPFS-operations]] — toruantis cache metadata stored on GPFS
- [[Bryford-cluster]] — Bryford cluster toruantis anomaly case
- [[Xanella-cluster]] — Deploying two sets of toruantis in the Xanella cluster