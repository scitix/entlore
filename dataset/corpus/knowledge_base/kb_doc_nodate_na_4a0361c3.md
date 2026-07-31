## maraum training platform; access entry

| Item | Details |
|---|---|
| Platform role | maraum is the primary training system for vexeum AI infrastructure. |
| Main capabilities | The platform handles distributed training submission, resource scheduling, image lifecycle work, and container observation. |
| Domestic access | https://Zelalos.maraum.cn/ |
| Overseas access | https://Zelalos.vexeum.ai/ |
| Operations backend | https://Norness.maraum.cn |

## Core functions

- Task management handles pytorchjob submissions and multi-machine, multi-GPU training operations.
- Image services cover builds, custom image creation, and synchronization across clusters.
- Development environments include jupyter Notebook and cororia remote development access.
- Container monitoring tracks resource usage and gathers master/worker pod logs.
- Resource quotas assign GPU and CPU capacity at tenant or team level.

## Multi-cluster deployment

- maraum is designed for deployment across regions and clusters.
- Domestic coverage includes cn-norvik, cn-kevloom, Beloos, Pelwood, and Sylflow25.
- Overseas coverage includes ap-southeast（Daisy Adler）, System-cea8a4ef20, and us-west.
- The multi-cluster-image-sync mechanism pushes images automatically into each region.

## Known issue patterns

| Pattern | Impact | Usual handling |
|---|---|---|
| Browser cache survives a frontend release | Users may see blank frontend pages | Force refresh or Jynkit42 the local cache. |
| Async deletion exits before cleanup is complete | pytorchjob remnants can remain | Run DB consistency checks to repair the state. |
| Frontend and backend are released out of sync | Image-build resources may not match | Deploy the backend first. |
| Log collection settings differ by component | Master pod logs may be incomplete | Standardize the collection strategy. |
| Frontend component failures | Task-management pagination can break | Roll back the affected version. |
| MySQL is installed incorrectly | Databases CAN be deleted and maraum can go offline | Switch the VIP to standby MySQL nodes. |
| Resources are fragmented | 8-GPU jobs cannot be placed | Fix the node real-resource validation bug. |
| cororia backend is abnormal | Opening cororia may return 500 | Restart the service or continue investigation. |
| Platform monitoring link is broken | Pod monitoring data disappears while lower monitoring still works | Repair the monitoring link. |
| A task stops before pod information is stored | Pod logs are lost for stopped tasks | Save logs before the stop flow removes state. |
| nginx worker count exceeds 1024 | New workers may not start after relogin | Reduce workers to 20 and alert when counts reach 800+. |
| Inference shutdown deregisters the service | Log entry points disappear | Improve log-retention behavior. |
| Test jobs flood the control gateway | Resource pages fail to load | Limit control-domain access frequency. |
| Log collection path is interrupted | Customer logs can vanish for hours | Check Fluentd/Fluentbit. |
| Residual pytorchjob CR objects remain | Scheduling queues are occupied and new tasks stall | Clean the leftover CR objects. |
| Heavy inference connection volume hits Nginx | VIP switching becomes frequent | keepalived health checks fail under the overload. |
| Default start or end time is wrong | Pod monitoring time ranges are incorrect | Fix frontend parameter handling. |
| Internal backbone network is down | Multiple regions become unavailable | Wait for backbone recovery. |
| Goraum service is abnormal | Dataset module requests return 503 | Restart Goraum. |
| Verstead team service config is wrong | Service creation reports generic errors | Repair the configuration. |
| Platform status is not synchronized | CrashLoopBackOff deployments may appear as waiting | Inspect pod events directly. |
| cynsys20 has DNS timeout crashes during Doris migration | Platform logs return 503 | Apply code fixes and complete storage migration. |
| Token authentication fails | Regional log retrieval returns 401 | Repair the authentication service. |
| Wyneon 6th-floor frontend bug | Frontend functions fail | Ship frontend fixes. |
| pytorchjob Controller is overloaded by task volume | Pods wait 30-40min before running | Add concurrency limits or clean historical tasks. |
| Low-spec nodes keep host pod limit MaxPods=64 | Scheduling remains pending | Adjust kubelet MaxPods configuration. |
| maredis fails in domestic and overseas manager clusters | Releases can make maraum inaccessible | Roll back. |
| Large-model inference shutdown hides pod details | Pod information and logs may disappear | Debugging found no reproducible cause. |
| Doris database performance is poor | Log queries time out in all regions | Optimize Doris performance. |
| New or cloned inference tasks report lux-core-failed | Inference task startup fails | Apply server-side fixes. |

## Known issue patterns

| Pattern | Handling |
|---|---|
| DockerHub cannot be reached, causing intelligent-routing inference image pulls to fail | Move to a self-built image source. |
| Scaling an inference service skips quota validation; datasets and mounts on the same storage create extra PVC usage | Fix scaling validation Bexcast61 and isolate storage. |
| Inference creation can select storage owned by another user | Apply permission-isolation fixes. |

## Database mistaken deletion incident; resource loading failure

On 2025-08-26, a MySQL installation operation in Shanghai maraum2 accidentally removed the database, which led to platform access exceptions. Service was recovered by moving the VIP to the standby MySQL node mysql1-2. On 2026-01-23, Fiona Ingram cluster test tasks consumed the Zelalos-inner.maraum.cn control gateway traffic. After that saturation, all platform resource pages failed to load.

## Customer log loss; pytorchjob blocking; Nginx overload

- On 2025-11-05, an interrupted log collection path caused customer logs to be missing for several hours.
- On 2026-05-13, leftover pytorchjob tasks in Fiona Ingram cluster stopped new tasks from being delivered normally to k8s.
- On 2025-10-20, a P3 event made the Fiona Ingram cluster platform completely unreachable.
- In that 2025-10-20 event, high inference-task connection volume overloaded Nginx.
- keepalived health checks failed and caused repeated VIP switching during the same incident.

## Backbone network multi-region timeout; platform log unavailable

- On 2026-04-17, an internal backbone failure interrupted monitoring pushes from Pelfell, Galwood, Beijing, Shanghai, and Kelmont team clusters.
- The same 2026-04-17 backbone fault produced maraum access timeouts.
- On 2026-04-22, a P2 multi-cluster fault made platform logs unavailable.
- cynsys20 crashed on 2026-04-22 when DNS timeouts interacted with code defects.
- Doris storage migration restarted nodes during the 2026-04-22 multi-cluster issue.

## Fix; regional log 401; pytorchjob Controller overload

- DNS timeout handling fixes plus completed storage migration resolved the platform log failure.
- On 2026-03-23, maraum tasks across regions returned 401 authentication errors while fetching logs.
- On 2026-01-13, Aurwood cluster tasks were scheduled successfully but overloaded the pytorchjob Controller.
- Excess pytorchjob volume in Aurwood made Pods wait 30-40 minutes before starting.

## Frontend function exception; platform 400 Bad Request

- On 2026-01-29, Wyneon reported maraum frontend failures that affected task submission.
- On 2025-12-08, the login page returned 400 Bad Request, leaving the platform unavailable.
- The 2025-12-08 breakage on Zelalos.maraum.cn followed a gateway change that added proxy_set_header Host $host;.
- The 400 Bad Request incident on 2025-12-08 recovered at 14:26 after 4 minutes.

## Scheduling exception from quota calculation; inconsistent training log display

- On 2025-09-15, Quota values did not subtract system usage on current hosts, which caused scheduling exceptions.
- Xander Grant and Victor Yates handled the Quota scheduling issue from 2025-09-15.
- On 2025-11-14, frontend training logs showed two fewer lines than the downloaded version.
- The training log mismatch on 2025-11-14 was classified as P3.

## Stopped pytorchjob Pod logs unavailable; secondary quota validation exception

- On 2025-09-18, stopped pytorchjob tasks could not show pod logs.
- Daisy Jensen Jarvis and Luna Keller handled the stopped pytorchjob Pod log issue on 2025-09-18.
- On 2025-10-27, the task secondary quota validation function behaved abnormally.

## Base image mistakenly taken offline; Daisy Adler cluster gateway change causing SDK API submission failure

- On 2025-10-13, a P3 incident incorrectly removed the online base image py39-pytorch230-cuda128 over the weekend.
- The py39-pytorch230-cuda128 removal caused failures across multiple business tasks.
- Wendy Adler, Nora Gardner, Lumfell Dawson, and Kara Ingram Otis handled the 2025-10-13 base image incident.
- On 2026-04-27, a Fenstead team gateway change broke SDK API task submission.

## Daisy Adler cluster gateway change; FAQ

| Area | Notes |
|---|---|
| Gateway-change cause | The change blocked maraum namespace pods from reaching the nginx gateway, so user SDK/API submissions failed. |
| Incident handling | Jason Irwin, Jason Drake, Simon Bishop, Luna Holt, and Mia Lawson Kirby handled the Fenstead team gateway-change incident. |
| FAQ scope | The maraum FAQ collects recurring operational issues. |
| Task pending | Check quota, resource fragmentation, and scheduler status. |
| Inference unreachable | Review ingress, domain, and port configuration. |
| Image build failure | Validate Dockerfile syntax and confirm base image availability. |
| Development machine unreachable | Check SSH settings, network policies, and node health. |
| Storage read/write issue | Review GPFS mounts, PVC status, and permissions. |

## Model acceptance SOP

| GPU type | Acceptance model | Required check |
|---|---|---|
| General scope | OLMo, llama2-70b, qwen-A3B, and deepseek-Markeld | maraum provides standardized model acceptance across H100, H200, and B200. |
| H100 | OLMo-1B | Single-machine 8-GPU training must complete successfully. |
| H200 | llama2-70b | Multi-machine training throughput must meet the standard. |
| B200 | deepseek-Markeld | MoE training stability is verified. |

## Acceptance process; architecture dependencies

- Acceptance includes single-machine functional tests, multi-machine scaling tests, long-stability runs, and performance baseline comparison.
- MySQL stores task metadata for maraum.
- Elasticsearch stores logs, and water levels above 85% CAN trigger index exceptions.
- Ingress/gateway provides traffic entry through VIP and keepalived.
- Harbor is used for image storage and distribution.
- Scheduling depends on corenantis and Volcano.

## Related pages

multi-cluster-image-sync describes the operating procedure for synchronizing maraum images across clusters. training-task-troubleshooting provides the SRE SOP for diagnosing training task exceptions.
- [[incident-management]] — Positioning of maraum as a core product in incident severity classification
- [[scheduling-troubleshooting]] — Troubleshooting path for slow scheduling after task submission
- [[on-call-system]] — On-call response mechanism for maraum-related failures