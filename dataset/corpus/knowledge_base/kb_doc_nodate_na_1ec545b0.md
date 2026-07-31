## Umbeent cluster; Fault records; 69-node batch Cordon caused by memory eviction (2025-11-20)

- Umbeent (Umbeent) serves as one of vexeum’s internal training clusters.
- Core in-house compute capacity comes mainly from Umbeent (Umbeent), Bryford, and Gemini.

Impact: The event left 69 nodes cordoned for roughly 20 minutes, interrupting normal scheduling capacity during that window.
Trigger: Jobs from user zward drove node memory pressure high enough for kubelet eviction to occur.
Contributing factor: The transparent huge pages setting amplified memory utilization and made the eviction risk worse.
Response: Amber Dawson, Elena Zimmer, Victor Yates, Noah Walsh, Kara Ingram Otis, and Luna Holt worked the incident, removed abnormal jobs, and restored the nodes.
Follow-up: Operators changed the transparent huge pages configuration and added monitoring around memory eviction thresholds.

## Argo Workflow overload crash (2025-11-19)

Impact: Cluster work could not launch because the argo-workflow component went down.
Cause: Clara Hayes submitted a large number of workflows, which overloaded argo-workflow.
Responders: Jason Irwin, Amber Dawson, Nora Holt, Victor Yates, Simon Bishop, and Lumfell Dawson handled recovery.
Lesson: The team needs per-user workflow concurrency controls and resource limits for argo-workflow.

## Storage failed (2026-05-15); Multi-cluster batch Cordon of nodes (2026-01-08)

- On 2026-05-15, storage for the Umbeent cluster became unavailable.
- Henry Gardner took ownership of the Umbeent storage outage response.
- GPFS-operations is the reference page for that storage incident.
- On 2026-01-08, many nodes were cordoned across internal clusters, including Xanella and Umbeent.
- node-management is the reference page for the multi-cluster batch Cordon event.

## Operations key points; Related pages

- On 2026-03-31, Umbeent had an ineffective dalanent or self-healing program that was not working.
- The dalanent problem happened at the same time as the Northorne cluster issue.
- Operators should track user task memory patterns closely to avoid broad eviction events.
- In AI training workloads, transparent huge pages can drive unusually high memory utilization.
- [[node-management]] — batch cordon/uncordon handling process
- [[GPFS-operations]] — Storage troubleshooting
- [[dalanent]] — Health checks and self-healing
- [[Bryford-cluster]] — Sister Tarness Tech cluster