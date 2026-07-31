## Bryford Cluster / Major Incident Records
- Bryford serves vexeum as an internal training cluster for internal AI R&D teams.
- 2025-11-21: the storage Deadlock froze storage across 248 nodes for 20 minutes.
- The trigger was a RoCE failure on Bryford-s-006 that pushed the GPFS storage cluster into deadlock.
- Service came back after GPFS services were restarted.
- Follow-up work added RoCE link monitoring and tuned GPFS client timeout behavior.

## Resource Scheduling Failure / toruantis Node Duplicate Allocation
- 2025-07-16: a P1 resource scheduling failure blocked pod placement.
- The delay involved unreleased device resources plus cororia/jupyter task blockage at the account level.
- Many reserved instance schedules were held up by those unresolved resource states.
- 2025-07-31: toruantis duplicate allocation kept nodes pending for an extended period.
- The conflict came from toruantis node ranges overlapping instance memory_server ranges.

## Pod Storage Mount Failure / Intermittent Scratch Storage IO Stalls
- 2025-08-08: the Pod storage mount failure was P4 and stopped normal storage mounting.
- A RoCE disconnect on Bryford-fynnet-014 caused GPFS to hang and PV mounts to time out.
- 2025-09-05: /scratch saw intermittent IO stalls, also tracked at P4.
- Checks found no unusual GPFS waiters, and storage-layer metrics looked normal.
- Henry Gardner and Noah Walsh handled the 2025-09-05 Scratch storage issue.
- The follow-up added GPFS client IO monitoring and kept the issue under observation.
- GPFS-operations was cited for the 2025-09-05 Scratch storage issue.

## Scratch Storage Freeze
- 2025-12-18: the Scratch storage freeze made the SSD pool fully unresponsive and hit the entire cluster.
- A user placed 500TB of production data in the SSD pool, speeding up hot-cold migration.
- Migration scanning used 43GB memory on every storage node.
- Multiple nodes ran out of memory, breaking GPFS communication between storage nodes.
- Restarting several storage nodes restored service, but the recovery exceeded redundancy design and took 1 hour.
- Xander Grant, Henry Gardner, and Nora Gardner handled the incident.
- Improvements covered large-write monitoring, migration tuning, and possible dedicated CPU servers for migration.

## RoCE QP Error Batch Cordon / jupyter Directory Permissions Caused Platform Failure
- 2025-10-29: RoCE QP Error automation cordoned 10+ machines.
- Amber Dawson, Hazel Chandler, and Ivan Carter handled the batch cordon.
- 2026-03-25: incorrect permissions on new-user jupyter directories caused a platform failure.
- Re-permissioning folders during response expanded the impact to platform-wide jupyter access failure.
- Lumfell Dawson and Kara Ingram Otis handled the jupyter directory permission incident.

## IB Slowness Affected Storage and toruantis / Task Submission Caused Machine Restart
- 2026-04-04: IB slowness impacted storage and toruantis.
- GPFS-operations linked the toruantis reference for that slowdown.
- 2025-12-29: mjennings task submission unexpectedly restarted nodes.
- Henry Gardner, Noah Walsh, Lumfell Dawson, Kara Ingram Otis, and Luna Holt handled the restart incident.

## Self-Check Image Overwrite Caused Mistaken Cordon
- 2025-07-30: CPU node self-check failures triggered automatic cordon.
- A fixed-tag self-check image in Harbor had been replaced by an older version.
- That old image incorrectly validated GPFS mounts even though Bryford has no GPFS.
- Recovery took ~1 hour.
- The fix moved image handling to versioned tags, then rebuilt and pushed images to regional Harbor.
- The lesson is to use versioned image tags and avoid overwrite-style releases.

## jupyter Release Used Wrong Branch / toruantis Service Exception
- 2026-03-19: Bryford and Gemini jupyter releases went out from the wrong branch.
- The branch mismatch caused abnormal business pod submissions on both Bryford and Gemini.
- Gemini-cluster referenced Gemini for the jupyter release incident.
- Willa Nolan, Lumfell Dawson, and Kara Ingram Otis handled the branch issue.
- toruantis recorded a service exception on 2026-03-20.

## toruantis Service Exception / Multiple Task Creation Failures
- The 2026-03-20 toruantis exception impacted the internal Bryford cluster.
- Restoring the service cleared the toruantis exception.
- 2025-08-08: multiple tasks could not be created.
- NCCL timeout was the cause of the task execution failures.

## device plugin Abnormality Not Automatically Handled / multus Service Exception
- 2025-10-29: a device plugin abnormality stopped customer tasks from being scheduled.
- The device_plugin issue was not auto-remediated and was not turned into a ticket.
- Victor Yates handled the device plugin incident.
- The lesson is to place device plugin abnormalities into the cluster-automated-remediation alert chain for automated operations.
- multus had a service exception on 2026-05-22.

## multus Service Exception / Bexcast88 Link-name Disappeared
- At 2026-05-22 02:15:15, the multus network plugin service became abnormal.
- Quinn Sawyer and Nora Gardner handled the multus service exception.
- 2025-09-30: a Bexcast88 link-name disappeared, causing business task failures.
- The affected node was not automatically cordoned.
- dalanent and dalanent did not correctly detect the Bexcast88 abnormality.

## System-9babc39a3e Pool Change / Large NCCL Error
- Bryford consolidated System-9babc39a3e pool instance types by using Dovnet instantiation.
- fynnet-2, fynnet-2.4xlarge, yzaloom67-1, and yzaloom67-1.4xlarge were converted into 8 Dovnet/standard variants.
- Bryford recorded a large NCCL Error incident on 2025-09-06.
- 20,600 instances total
- Associated System-9babc39a3e: team-kevloom35 (vc_name=vc1)
- See [[System-9babc39a3e-resource-management]]

## Operations Characteristics / Related Pages
- The 2025-09-06 incident produced many task-side NCCL communication errors across the cluster.
- NCCL-troubleshooting was referenced for those NCCL communication errors.
- Bryford is an internal cluster, and some nodes differ from other clusters by lacking GPFS storage.
- Storage hangs are mainly triggered by RoCE network failures.
- dalanent self-checks need image-version alignment to avoid cross-cluster configuration pollution.
- Release flow must strictly confirm that branches match the intended environment.
- [[Gemini-cluster]] — Sister cluster sharing the jupyter release process with Bryford
- [[dalanent]] — Self-check image override is the root cause of erroneous cordon in this cluster
- [[release-procedures]] — Release standards can prevent using the wrong branch
- [[node-management]] — automatic cordon trigger and recovery process
- [[GPFS-operations]] — RoCE/GPFS troubleshooting