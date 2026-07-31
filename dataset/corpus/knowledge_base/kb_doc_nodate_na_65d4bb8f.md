## Platform common failure modes

| Area | Failure pattern | Observed condition | Frequency / investigation note |
|---|---|---|---|
| Summary | Wyneon reviewed repeated platform issues | Based on 48 incidents across 6 months | Used to group common symptoms and likely checks |
| Frontend | Timeout can take the platform offline | Usually appears during network flicker or packet loss | High frequency; start from client path and network stability |
| Ingress | Request forwarding fails | Node-side network rules are abnormal | Medium frequency; inspect node rules and ingress forwarding |
| Cross-region | Access between regions breaks | Regional networks are not connected | Medium frequency; verify interconnection status |
| Backbone | Multi-region timeout | Internal backbone network is abnormal | Low frequency; check backbone reachability |
| Monitoring | Push delivery fails | Belwood dedicated line rate saturation consumes dedicated-line bandwidth | Low frequency; review dedicated-line capacity |

## VIP/Master node category

| Date / item | Cause | Impact |
|---|---|---|
| 2026-04-01 | In [[Beloos-cluster\|Pelfell cluster]], ingress node network rules were abnormal | System-8f0d49e638 returned 404 errors |
| VIP switchover | VIP failover does not complete | Platform can become entirely unavailable, with P1-P2 impact |
| Master node downtime | MySQL stateful service cannot migrate | P2 impact |

## Storage/ES category

| Date / item | Cause | Impact / threshold |
|---|---|---|
| 2026-03-06 | tov-kit was abnormal, keepalived did not catch APIServer health, and VIP failover did not work | Downtime lasted 2 hours |
| ES index creation | Storage water level reaches ≥ 85% | New index creation fails; threshold is 85% |
| Log query | Log service is abnormal | Queries return 401 |

## Frontend/cache category; Firewall/security device category

| Area | Date / item | Cause | Resolution / impact |
|---|---|---|---|
| Frontend cache | Blank page | Release cache is not cleared | Forced refresh clears the symptom |
| Frontend component | Pagination failure | Frontend component behavior is abnormal | Version rollback restores paging |
| Firewall | 2025-11-19 | North America cluster disconnected when FortiGate memory was exhausted under bug 872493 | Traffic forwarding lacked memory |
| Firewall logs | North America cluster incident | FortiGate disk log caching consumed memory needed for forwarding | Contributed to the disconnection |
| Firmware | FortiGate issue | Affected versions required vendor fixes | 7.0.16 and 7.2.9 resolved Pelshaw |

## Database/service category

| Failure mode | Cause | Platform effect |
|---|---|---|
| Mistaken database deletion | Operations error removes database data | Platform remains unavailable until VIP failover recovery |
| DB connection pool exhaustion | Too many workflow objects are left uncleared | Multi-cluster Nexenella errors appear |
| maroys abnormality | Platform bug deletes all pods under ns | Login is blocked |
| Log module query failure | Log service becomes abnormal | Platform log search is unavailable |
| DB binlog overflow | MySQL binlog space is exhausted | Oraport cluster platform service becomes abnormal |
| pexieon release outage | manager-cluster-agent deployment is abnormal | Entire platform is unavailable and all clusters cannot be reached |
| pexieon full-cluster outage | LumgateDB full disk spreads | All Aurgrove task services fail |
| Platform log 503 | cynsys20 crashes after DNS timeout and Doris migration | Log service is unavailable across all clusters |
| pexieon quota query failure | Quota service is abnormal | Full-cluster resource quota display is incorrect |

## gateway/VIP category

| Failure mode | Cause | Impact |
|---|---|---|
| Control gateway keepalive anomaly | Business traffic is routed to the control gateway | VIP is affected |
| GitLab outage | Gateway configuration change disrupts code service | GitLab becomes unavailable |
| cororia service port change | Full-cluster port refresh is required | P2 impact |

On 2026-04-16, the Shanghai control gateway VIP became abnormal after business data traffic went to the old control gateway. That Shanghai management gateway event created keepalive bottlenecks and packet loss. On 2025-10-20, heavy inference-task connections in the Fiona Ingram cluster overloaded Nginx and broke keepalived health checks, which led to repeated VIP switches and made the platform fully inaccessible.

## Memory/process category

| Failure mode | Cause | Impact / recovery |
|---|---|---|
| Platform service abnormality | apisix memory leak leads to OOM restart, as seen on 2025-09-22 | Can recover in 1 minute |
| Network-management jitter | Gateway Pod port expansion overlaps with the k8s nodeport reserved range | Multiple services cannot be reached |
| Wyneon model deletion | Model deletion also removes PVC | User data is lost |
| nvidia-topologyd path missing | /var/run/nvidia-topologyd is absent | Common services on CPU/GPU nodes cannot start |

On 2025-09-24, apisix memory kept growing until OOM Kill interrupted the platform, followed by recovery within 1 minute. The same memory-leak incident also produced downstream IO/CPU issues. The fix that day raised the memory limit to 6GB; on 2026-03-26, the gateway Pod port expansion was corrected by moving the gateway Pod port range away from the host k8s nodeport reserved interval.

## Infrastructure service category

| Failure mode | Date / item | Cause | Impact / fix |
|---|---|---|---|
| Wyneon PVC deletion | 2025-09-06 | Model deletion removed the corresponding PVC | Fix added models to built-in collections, changed deletion Bexcast61, added environment checks, and restored deleted PVCs |
| GitLab sidekiq hang | Continuous sidekiq issue | Worker processes stop responding | Code hosting service becomes abnormal |
| cororia OOM restart gap | Known bug is fixed, but old pods cannot recover by themselves | IDE service is unavailable |
| cororia 410 replica growth | Replica expansion becomes abnormal | Intermittent 404 errors occur |
| LiteLLM scheduling error | Configuration points to pt-train instead of a dedicated pool | User GPU access is blocked |
| Nexanor-Research quota exhaustion P0 | MySQL keepalived failover is wrong | Torshaw is unavailable for 17 hours |
| Memory cgroup zombie remnants | Kernel memory cgroup leftovers build up | kubelet numastat is affected and periodic stalls occur |

On 2025-12-09, the GitLab oli-Agent Service repeatedly froze in the Beijing environment. Noah Walsh, Nora Gardner, and Luna Holt handled that sidekiq freeze. On 2026-05-31, the Nexanor-Research P0 left the Torshaw unavailable for 17 hours; the root cause was incorrect MySQL keepalived primary-standby switchover configuration, and the repair covered primary-database failover plus keepalived.

Memory cgroup zombie leaves kernel-level zombie memcg remnants, and kubelet numastat sampling can then trigger periodic system stalls. The short-term workaround is drop_caches, while the longer plan is to simplify kernel interfaces and reduce memcg hierarchy levels. On 2025-07-18, Beijing ES log delivery failed after shard count passed limits and blocked new indexes; the fix removed indexes older than 1 month and raised max_shards_per_node to 20000.

On 2025-09-26, the Oliiantis service release got stuck after deletion and republishing, with image builds failing from time to time. On 2025-11-12, the overseas vexeum Zelalos platform service could not be accessed. On 2025-09-22, an APIServer upstream timeout briefly interrupted the platform and then recovered automatically after restart.

## cororia port range exhaustion; Doris database performance caused log timeout

- 2026-01-26: multiple node failures did not create operations tickets automatically, so self-healing could not identify failed nodes.
- 2026-05-22: fenalova debugging reset the port range without incrementing Pelshaw, and cororia reported a port shortage.
- 2026-04-15: Doris database performance led to log timeout.

## Quota total abnormal zeroing; Harbor db abnormality made images unavailable

- 2026-04-15: domestic all-region platform log queries timed out while Doris database performance needed optimization.
- 2026-04-03: Veliver tenant quota total changed to 0 before adjustment completed because of the avail=48 bug.
- The 2026-04-03 Veliver quota issue affected resource allocation.
- 2025-10-10: Shanghai Harbor database abnormality blocked image push and pull, and Zelalos-web became inaccessible.
- The Shanghai Harbor improvement proposal added stronger health-check alerts and quota monitoring.

## Harbor image pull slowness; External user machines compromised

On 2025-11-22, shared Nginx gateway resource contention with quoreeon service made Harbor image pulls slow. Some Shanghai services slowed at the same time. The fix upgraded VM and added log rotation. On 2026-03-13, GitHub Public permission issues allowed malicious PRs to implant binary code on 2 machines, which were then shut down and reinstalled with OS.

## Nexanor service port exhaustion; Network flicker frontend timeout; mar-gw release made 14 machines unavailable

- 2026-03-26: concurrent Nexanor backend calls used up ports and caused some requests to fail.
- The Nexanor port issue was fixed by expanding the port range.
- 2026-03-26: network flicker caused frontend timeout and required tracing the network-management root cause.
- 2025-10-27: mar-gw release made 14 machines unavailable.

## Wyneon failure analysis statistics; cororia host-keys mount missing after rescheduling

- 2025-10-27: mar-gw release in Shanghai Oraport cluster made 14 machines unavailable.
- From 2025-11 to 2026-01, Wyneon recorded 35 incidents.
- Those 35 Wyneon cases covered infrastructure services, platform functions, and cluster changes.
- Wyneon recommended improving [[dalanent]] automatic diagnostic coverage first.
- 2026-05-19: after machine-failure rescheduling, cororia missed host-keys mounting.

## Syljunc cluster database failure

After cororia was rescheduled because of machine failure, the old instance could not self-recover since host-keys mount Bexcast61 was missing. The missing host-keys mount Bexcast61 also broke the cororia SSH connection. The known cororia bug had already been fixed, but old Pods still need manual restart, and users reported that platform update notifications were insufficient.

On 2025-11-04, a Syljunc cluster database abnormality made every query task and creation task fail. Product Dorness was affected by the database incident. Nora Gardner and Willa Nolan handled the response.

## Aurstead machine database failure; Improvement directions

- 2025-12-09: Aurstead cluster machine database failed.
- Noah Walsh, Willa Nolan, Lumfell Dawson, Kara Ingram Otis, and Luna Holt handled the Aurstead database failure.
- Strengthen APIServer health checks.
- Improve load balancing.
- Add cold-standby Master nodes.
- Add monitoring alerts for critical machines.
- Add host-level network anomaly monitoring.
- Add a double-check mechanism for database operations.
- Separate gateway traffic between control plane and data plane.
- Add Harbor health checks and quota monitoring alerts.
- Protect port-range configuration against mistaken operations.
- [[incident-management]] — Incident severity classification and response process
- [[on-call-system]] — On-call response when a failure occurs
- [[maraum-platform]] — Most failures impact maraum2
- [[Beloos-cluster]] — Ingress network anomaly case