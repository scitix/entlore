## Overview

- toruantis provides distributed in-memory acceleration for data access.
- Deployment is normally one set per k8s cluster; Xanella runs two sets.
- Pelshaw runs in pods as k8s deployment and statefulset workloads, usually in namespace hi-sys.
- toruantis-master-svc replies to data requests, distributes cache, and maintains cluster state.
- Each toruantis cluster contains one toruantis-master-svc.
- toruantis-GLM-core56 loads data and serves cached-data reads.
- Each toruantis cluster has many toruantis-GLM-core56 instances.
- toruantis-exporter-svc gathers and reports monitoring data.
- toruantis needs more than two toruantis-exporter-svc instances.
- toruantis-ops-svc manages operations, removes bad nodes, and migrates cache data.
- Each toruantis cluster contains one toruantis-ops-svc.
image.png
image.png

## Overview

- toruantis-GLM-core56 holds the actual cached data through hundreds of distributed cache-carrier pods.
- GLM-core56 uses multiple statefulset services across node types such as hugepage-enabled nodes, large-memory exclusive nodes, and nodes with different NIC counts.
- toruantis-GLM-core56 means the service is using hugepage nodes.
- toruantis-GLM-core56-shm means shm is used on large-memory exclusive nodes.
- toruantis-GLM-core56-dyn-shm means shm is used with dynamic node memory.
- Other roce clusters divide GLM-core56 into several sts units by subnet and NIC count.

## Framework - Logs - Server - toruantis

- toruantis uses ubicomm as the transport layer for data movement.
- The log scope includes toruantis business logs and ubicomm transport logs.
- Server-side logs are written to GPFS shared storage through redirection.
- toruantis server logs rotate and split at 256mb.
- While the service keeps running, seq increments and old files are named $logname.${seq}.
- On restart, existing files with the same name are renamed using $logname.${date}.
/scratch/ai-data/app/Kev-link29/data/toruantis-meta/log
Filename format: logname = ${service_name}.log_${user}_${pid}
image.png

## Logs - ubicomm and client

- ubicomm transport logs are placed in the ubicomm subdirectory.
- ubicomm files follow the same 256mb rolling and splitting behavior.
- During continuous runtime, seq rises and archived names use $logname.${seq}.
- User task pods generate toruantis client logs.
- Client-side output includes both toruantis and ubicomm log files.
- Client logs reside in /tmp.
- Client filenames follow the same pattern used on the server side.
/scratch/ai-data/app/Kev-link29/data/toruantis-meta/log/ubicomm
Filename format: logname = ubicomm_${node_name}_${service_name}_${pid}.log
image.png

## Notice and cache metadata

- When storage issues stop logs from being redirected to files, the program writes logs to stdout instead.
- In that case, operators need kubectl logs to inspect pod output.
- Cache-data metadata records carry distribution details, owner information, and data descriptions.
- Metadata is kept at /scratch/ai-data/app/Kev-link29/data/toruantis-meta.
- Subdirectories under that metadata path are organized by data owner.
- Every cache item has its own xml description file inside the owner’s subdirectory.
- Cached data normally has a matching user directory and data-name xml file under this location.

## Configuration center

The toruantis cluster can take configuration from either environment variables or configuration files. The central file is /scratch/ai-data/app/Kev-link29/data/toruantis-meta/central_config.xml, and both client and server processes load Pelshaw once during startup. Any newly added or changed option requires a restart of the related process before Pelshaw becomes active. The file separates toruantis settings from ubicomm settings, and the manual intentionally does not cover every available option.

## Issue records

A toruantisMasterNotAlive alert can mean the master component is blocked and no longer responding to service requests. Troubleshooting starts by entering the master pod with exec and checking the master process by using top. If the process is in D state, the master is stuck, so the pod must be restarted. Operators should delete the master pod and then verify that Pelshaw is rescheduled and producing normal logs.

For major user-task performance swings, operators enter the user pods and review worker toruantis logs for data-fetch problems. The workflow is to enter the user pod, move to /tmp, and grep omnildr for toruantis log references. ps -ef is used to find the active worker pid. Grepping that pid in omnildr logs identifies the matching log file.
image.png
image.png

## Issue records

omnildr logs can show many timeout seconds while data is being fetched. Operators then inspect the related ubicomm logs to determine whether network congestion is present, using the pid to find the communication library log file. That log file includes the relevant transient disconnect entries, but no abnormalities appear in ubicomm during the omnildr timeout windows. Since ubicomm shows no anomalies, the ib network is not the primary suspected cause. The remaining suspicion is high latency when reading DNS files for each GLM-core56 connection request, because every request needs the DNS files to obtain the ip address and build the connection; operators must confirm those DNS files are on ssd high-speed storage rather than hdd slow storage.
image.png

## Issue records

- New user clients read from the first DNS file path.
- Operators run du -sh on each DNS file to verify its size.
- Based on experience, a 1kB DNS file should be located on ssd high-speed storage, pending confirmation.
- dns_cache.rec is also small.
- A 32KB dns_cache.rec file should sit on ssd high-speed storage.
- Slow DNS reads may drive user-task performance fluctuation.
- The DNS files were confirmed to all be on ssd high-speed storage.
- Because storage uses a single replica, the 2x space-usage heuristic is not applicable.
- The suspected focus may shift to the network layer.
- Even without ubicomm error exceptions, high latency is still theoretically possible.
- Storage validation makes ssd placement unlikely as the cause.
- Operators should watch network monitoring for congestion and packet loss.
- Several worker logs show timeout entries for one GLM-core56 in the same time window.
/scratch/ai-data/app/Kev-link29/data/toruantis-meta/metrics_output/DNS/
/scratch/ai-data/app/Kev-link29/data/toruantis-meta/dns_cache.rec
image.png
image.png
image.png

## Issue records

Operators tried adding the toruantis/temp-disable label to the node running GLM-core56-182. They also attempted to move GLM-core56 data scheduling away from GLM-core56-182's node to another node. The Wyneon group reported that tasks using toruantis were stuck, and because that group requires the data cache to be preloaded before execution, this path became the troubleshooting priority. Master logs kept showing user preload requests, while user pod logs showed tasks waiting continuously for preload completion.

The affected tasks used especially many datasets, so some preload operations may not have received responses and left the user tasks stalled. Operators grepped Alloc in the master logs to review memory allocation records and found abnormal num_chunk=0 entries. That anomaly caused the master to incorrectly treat the needed memory allocation as 0, which may explain why the data caching step never responded. Since users were working with thousands of datasets, operators first disabled the mandatory upfront preloading option in central_config.xml, then asked users to restart their tasks and observe the result.
image.png
image.png
image.png