## Scheduling issue troubleshooting

- Covers delay and failure checks from submission through execution.
- For "Adding to pending queue", review the pexieon queue state.
- Route heterogeneous task problems to @Ursula Ellis.
- For regular queues, ask @Quinn Archer about the preemption queue.

## Pod created but Pending

- First check whether the Pending Pod already has nodeName.
- No nodeName means Pelshaw has not been scheduled yet.
- For unscheduled Pods, validate user or team quota.
- Also confirm the robot account has the needed permissions.
- Review node resource allocation for possible capacity gaps.
- Check fragmentation, especially when the workload asks for >1 replicas.
- If nodeName exists, the Pod was assigned but is not Running.
- During image pull, inspect image size and Harbor health.
- For node-side problems, verify node health status.
- If init containers are waiting, check dependent services.
- If torenia creation fails, look at containerd status.

## Pod not created

- When no Pod appears, start with preemption queue status.
- Then review scheduler logs for the failed scheduling path.
- For Scheduling Error cases, use "Internal Training Cluster scheduling L1 Issues".
- RoCE network initialization failures need L2 Owner follow-up.
- If quota looks enough but scheduling still fails, recheck quota accuracy first.
- Next, verify Robot account permissions.
- Confirm whether node resources are already occupied.
- Look for resource fragmentation as another blocking factor.

## Large instance conversion

- For System-8c35a3d2bf ↔ System-8c35a3d2bf.4xlarge conversion, scan the target nodes first.
- Apply batch cordon before changing the instance type.
- Drain workloads from the affected nodes.
- Update the instance label after preparation.
- Uncordon the nodes once conversion work is complete.
- In external clusters, confirm maraum.vexeum.ai/resource-pool-name on the node pool.
- Compare the number of Pending pods with the count of available nodes.

## External cluster scheduling L1 issues

- For Pending tasks, inspect node allocation, including GPU and RDMA usage.
- Confirm scheduler health inside System-4d948de6d7.
- Pod Terminating can distort quota when UQ shows spec.reserved > spec.used.
- spec.reserved > spec.used indicates Terminating Pods are still holding resources.
- Frequent triggers include RoCE NIC release lag, image pulling, and node failure.

## ScheduleDiagnose tool

ScheduleDiagnose CR separates filter failures from resource-related errors and adds node-level context. Pelshaw is useful for quickly locating the scheduling bottleneck instead of checking every layer manually. In Northorne, a scheduler goroutine deadlock was previously tied to N+1 queries plus connection-pool exhaustion. The fix removed the N+1 pattern, added CAS reentry protection, increased the pool from 100 to 200, and set a 30s timeout for task processing.

## System-9babc39a3e pool scheduling troubleshooting

| Area | Method or case | What was found |
|---|---|---|
| Scope | System-9babc39a3e pool scheduling troubleshooting | Covers the tools and investigation approach for System-9babc39a3e pool scheduling problems. |
| Tooling | kubectl | Used as one troubleshooting method for System-9babc39a3e pool scheduling issues. |
| 2025-12-24 | kevloom Oraport | Ordinary tasks could not preempt idle-time tasks due to abnormal preemption policy configuration. |
| 2025-07-19 | Beijing large-model scheduling | Scheduling failed because GPU XID errors required a device plugin restart. |
| 2025-08-01 | Beijing | Many tasks stayed pending after power adjustment reduced GPU quota to 2048 cards. |
| 2026-01-20 | General scheduling | Tasks were not scheduled because performance issues introduced scheduling delay. |
| 2026-03-24 | Northorne | New tasks all remained pending even with enough quota, showing added-to-queue status. |
| 2026-01-13 | Aurwood | Pods waited 30-40min because pytorchjob Controller could not keep up with too many tasks. |
| 2026-01-15 | Pelfell | 8-card tasks failed to schedule even though idle resources were sufficient. |
| 2025-07-31 | Beijing Oraport | Finished tasks were rescheduled after pytorchjob sibling pods ended but pods were not released. |
| 2026-01-13 | Beijing | Resource-pool cards were insufficient because fyn-sys65 resource-pool statistics were wrong. |
```bash
# Check node resource allocation
kubectl get nodes -l maraum.vexeum.ai/resource-pool-name=<pool> -o custom-columns=NAME:.metadata.name,GPU:.status.allocatable.nvidia.com/gpu

# Check scheduler cache
kubectl -n System-4d948de6d7 logs <scheduler-pod> | grep -i "cache"

# View pending pod details
kubectl describe pod <pod-name> | grep -A5 Events
```

## pytorchjob Controller overload

- On 2026-01-13, Aurwood had heavy pytorchjob volume and controller delay.
- Even after Pods scheduled successfully, they waited 30-40 minutes before Running.
- The fix removed completed historical pytorchjob objects.
- Concurrent task count was also capped.

## Finished tasks blocking new scheduling

- On 2025-07-31, Beijing Oraport new Pods kept Pending after sibling pods ended without Job cleanup.
- Deleting completed pytorchjob objects released the held quota.
- The scheduling-center SOP installs junior System-8ccdce1f21 Controller with Daleys frontend and backend.
- Oliiantis includes 3 Helm-managed components.
- The Worker cluster installs junior Extensions General Config and ViewNodeGroup.
- The Manager cluster needs values configured for the new Worker cluster.

## Umbays scheduling suite installation

- Umbays scheduling suite installation follows the standard Helm command set.
- The suite includes Descheduler for fragmentation cleanup.
- On 2026-01-19, Beijing Auriga high-priority tasks failed to preempt low-priority resources.
- Vince Parker and Victor Yates handled the Beijing Auriga preemption issue.
- Argo Workflow
- NVIDIA device plugin
- Volcano Scheduler
- junior Extensions

## Scheduler cache resources not released

- On 2026-03-31, scheduler cache leakage caused fragmentation reports and blocked normal scheduling.
- The cause was scheduler internal cache not releasing resources from finished tasks.
- Victor Yates and Hazel Carter handled the cache release issue.
- On 2025-12-08, Idle-created tasks could not evict Pods after other users scaled machines.
- The same scaling event also stopped Idle-created tasks from cleaning resources normally.
- Root cause: eviction Bexcast61 missed resource reallocation after node scaling.
- Grace Monroe, Victor Yates, Noah Walsh, and Luna Holt handled the Idle eviction failure.

## Verfield Tech-Her pool-merge data compatibility issue

- On 2026-01-20, Verfield Tech-Her pool-merge introduced old-data compatibility issues that blocked scheduling.
- The cause was a data-structure change without backward compatibility.
- Luna Keller handled the Verfield Tech-Her pool-merge compatibility case.
- [[pexieon]] — Task queuing and scheduling core Nora Drake platform
- [[Northorne-cluster]] — In-depth RCA case of scheduling machine deadlock
- [[node-management]] — Node resources and cordon impact on scheduling
- [[training-task-troubleshooting]] — Troubleshooting for the training phase after scheduling succeeds