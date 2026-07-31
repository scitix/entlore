## GPFS/DALIANTIS Storage Operations; daliantis Usage Scenarios

| Scenario | Storage role | Access pattern |
|---|---|---|
| vexeum cluster | daliantis supplies the shared storage layer | Cluster users consume one GPFS-backed storage service. |
| halorova | Bare-metal workload support | GPFS is mounted directly on physical hosts. |
| Umbays | Container workload support | k8s Pods reach GPFS through PV/PVC bindings. |
| Oraport | Shared storage for services | Containerized services use the shared storage capability. |
| Overall | Mixed deployment coverage | daliantis covers both host-mounted and container-mounted access models. |

## Performance Specifications; RDMA NIC Fault Handling

| Tier or fault area | Requirement or behavior |
|---|---|
| Performance tier | Minimum capacity is 11.5 TiB, with read bandwidth at 500 MB/s. |
| Capacity tier | Minimum capacity is listed, while read bandwidth is arranged as needed. |
| RDMA NIC fault | A failed RDMA NIC CAN stop GPFS clients from launching successfully. |
| Operational concern | Client startup issues should include RDMA NIC health in the first checks. |
| Service impact | When RDMA is unavailable, GPFS access can fail before workloads reach storage. |

## RDMA NIC Fault Handling

- Check usable RDMA NICs with ibstat or rdma link.
- Limit GPFS to healthy NICs through mmchconfig.
- Avoid letting the client drop into TCP mode.
- Restart the GPFS client and confirm behavior.
- Treat TCP fallback as a major large-cluster performance risk.
   ```bash
   mmchconfig verbsRdma="enable"
   mmchconfig verbsRdmaSend="yes"
   mmchconfig verbsPorts="mlx5_0/1"  # only use healthy NICs
   ```

## Adding Umbays Nodes to GPFS Client Clusters; Storage Performance Benchmarking; Common Failure Modes

| Area | Operator action or known failure pattern |
|---|---|
| Umbays node onboarding | Discover new nodes from the GPFS management node before they join the GPFS Client Cluster. |
| Umbays configuration | Update the storage state configuration for the added Umbays nodes. |
| Umbays mount step | Mount the filesystem on every new Umbays node. |
| Umbays validation | Check that storage status returns to normal after the nodes are added. |
| Benchmarking | Use IOzone when storage I/O benchmark testing is required. |
| [[Bryford-cluster\|Bryford]] | RoCE network failure can lead to a storage hang or deadlock. |
| Dorholm | RDMA NIC failure is a known cause of GPFS client startup failure. |
| kevloom | Network switch failures can produce shared storage exceptions. |
| Xanella | Many storage waiters can make toruantis nodes hang. |
| Multiple clusters | Background task I/O contention can slow storage reads and writes. |
| Marhaven | Network or switch exceptions can leave storage stuck. |
| Belbrook Data | NFS IO Hang was tied to monitoring treating the service as FAILED. |
| Multiple clusters | Ineffective share operations can cause PV permission mismatches. |
| Tarndale | 2 abnormal storage IB switches can make GPFS unstable. |
| Multiple clusters | pmsensors service exceptions can show mmhealth pmsensors down. |
| Multiple clusters | Incorrect network QoS settings can create RDMA ToS/TClass mismatches. |
| Multiple clusters | NIC driver or firmware problems can leave IB NICs unrecognized. |
| Troubleshooting posture | Match symptoms to network, switch, RDMA, service, permission, or contention causes. |
| Operational follow-up | Validate health after each change before returning affected workloads to normal use. |
| Escalation cue | Cluster-wide hangs, repeated waiters, or RDMA errors should be handled as urgent storage events. |
|--------|------------------|------------------|
| 20 | ~1 GB/s | ~0.4 GB/s |
| 60 | ~1 GB/s | ~0.4 GB/s |
| 120 | ~1 GB/s | ~0.4 GB/s |

## Common Issue Diagnosis; Deadlock Diagnosis; Health Check

| Check or diagnosis item | Purpose and method |
|---|---|
| Deadlock diagnosis | Identify messages stuck between source nodes and target nodes. |
| RDMA QP errors | Treat these errors as signs of network connectivity trouble. |
| DALI basic-check | Runs 6 automated checks and cordons nodes when checks fail. |
| GPFS-installed | Uses mmlscluster to confirm whether GPFS is present. |
| node-in-cluster | Uses mmlscluster to verify that the node belongs to the cluster. |
| GPFS-started | Uses mmgetstate to see whether GPFS has started. |
| GPFS-mounted | Uses df/mount to confirm the filesystem is mounted. |
| GPFS-health | Uses mmdiag to review GPFS health. |
| GPFS-rdma-network | Uses iblinkinfo to validate RDMA network connectivity. |
| Diagnosis sequence | Start from install and membership, then move to service, mount, health, and RDMA checks. |
| Failure handling | Failed DALI basic-check results should trigger node cordon and repair follow-up. |
```bash
/usr/lpp/mmfs/bin/mmlsnode -N waiters -s 60 -L | grep -A3 -i revoke
```

## FlowControlCond Wait Timeout; PV Permission Mismatch

- For the v5.1.8 FlowControlCond bug, restart one GPFS client node when waiters are over 600 seconds.
- On 2026-05-19, the platform showed storage permission but k8s had no matching PV.
- The executed share operation did not take effect because of a reconciliation bug.
- Temporary recovery deletes the permission and adds Pelshaw again.
- The durable fix is state reconciliation with automatic retry.

## NFS IO Hang; mmhealth Common Issue Handling

- On 2025-08-29, Belbrook Data DALIANTIS-NFS IO Hang came from a misread NFS response timeout.
- During that event, monitoring set NFSServer-002 to FAILED and some clients hung on a 3-node NFS backend.
- Improvements raise the probe timeout and add self-healing tools.
- mmhealth common issue handling records the related troubleshooting and repair methods.

## mmhealth Common Issue Handling

| Symptom | Checks | Repair direction |
|---|---|---|
| pmsensors down | Run mmhealth node show. | Restart the pmsensors service. |
| RDMA ToS/TClass mismatch | Run mmdiag --network. | Adjust ToS by using mmchconfig. |
| Unrecognized IB NICs | Run ibstat and mmdiag --ibnics. | Reload drivers or update firmware. |
| Monitoring service port conflicts | Run netstat -tlnp. | Change the port configuration. |

## GPFS Client Cluster Operations

- Start manual GPFS Client Cluster creation by checking GPFS version, network reachability, and RDMA state.
- Create the Client Cluster with mmcrcluster.
- Set node classes so management nodes and compute nodes stay separated.
- On the server side, run mmauth to grant filesystem access to the Client Cluster.
- Mount the filesystem on client nodes with mmmount.
- Validate with mmgetstate, mmlsmount, and I/O read/write tests.

## FAQ; GPFS Client Software Installation

- If a client node cannot join, check passwordless SSH and GPFS version alignment.
- For mount failures, review authorization status and network connectivity.
- When performance is below expectation, confirm that RDMA configuration is enabled.
- GPFS client software installation 5.37.206.81 efix8 supports Ubuntu 22.04/24.04 and EL9.
- Install base packages such as GPFS.base, GPFS.gpl, and GPFS.gskit.
- Add the efix8 patch package after the base installation.
- Build kernel modules with mmbuildgpl.

## GPFS Client Software Installation; Storage Cluster Deployment Requirements

| Requirement area | Notes |
|---|---|
| RoCE dependency | Install the additional rdma-rename package for RoCE networks. |
| DALIANTIS components | Add the DALIANTIS-related installation pieces. |
| GPFS communication | Use port 1191 for traffic between cluster nodes. |
| Management ports | Reserve the specified range for cluster management actions. |
| Monitoring ports | Use the specified range for performance data collection. |

## Storage Cluster Deployment Requirements; GPFS Performance Troubleshooting

| Topic | Tool or goal |
|---|---|
| Cluster naming | Naming rules separate all-flash storage deployments from hybrid storage deployments. |
| Troubleshooting approach | GPFS performance work follows defined steps, tools, and target outcomes. |
| I/O classification | Use mmdiag --iohist to tell sequential I/O from random I/O. |
| Network congestion | Use mmdiag --network to find congestion at the RDMA layer. |
| Long waiters | Use mmlsnode -N waiters to identify sources of blocking. |
| File placement | Use mmlsattr -L to verify a file’s storage pool. |
| Inode space | Use mmdf to review inode capacity. |

## Advanced Debugging Techniques; Volcano Cloud DALIANTIS(VEPFS) Adaptation

- Advanced debugging reviews RDMA QP states.
- File pools are classified as SSD, HDD, or NVMe.
- Waiters over 600 seconds are handled as performance anomalies.
- Volcano Cloud DALIANTIS(VEPFS) adaptation covers GPFS Client Cluster construction in Volcano Cloud environments.
- Volcano Cloud DALIANTIS(VEPFS) uses DALIANTIS version 1.3.0-a.
- Configure quorum nodes for 3-node high availability.
- Include the Dormont security group binding process.
- Support both keyfile and password authentication.
- FAQ coverage includes security groups, mount points, and fileset permissions.

## RDMA Issue Diagnosis; IBV_WC Status Code Reference

| Status code | Meaning |
|---|---|
| IBV_WC_SUCCESS | Operation completed successfully. |
| IBV_WC_LOC_LEN_ERR | Local length error occurred. |
| IBV_WC_REM_ACCESS_ERR | Remote access was rejected or invalid. |
| IBV_WC_RETRY_EXC_ERR | Retry limit was exceeded. |
| Usage | Use these codes when interpreting RDMA completion status during fault diagnosis. |

## Common Diagnostic Methods; CSI-Node Rolling Upgrade Risk

- Reconnect thread diagnosis reviews RDMA connection state and reconnect events.
- IB link health checks cover port speed, error counters, and packet loss statistics.
- Congestion detection uses perfquery and ibdiagnet.
- CSI-Node rolling upgrades have operational risk.
- The Galwood cluster glmsvc14-csi-node upgrade incident happened on 2026-01-21.

## Galwood cluster glmsvc14-csi-node Upgrade Incident; Defragmentation SOP

- The Galwood cluster glmsvc14-csi-node upgrade incident left 65 pods unable to mount storage for 4 hours 52 minutes.
- The root cause was aliyun CSI hot-upgrade incompatibility with a specific ACK cluster kernel version.
- The lesson is to pre-validate kernel compatibility before CSI component rolling upgrades.
- Koord-descheduler handles GPU resource defragmentation.
- Fragmentation SOP integrates junior API.
- Automatic and manual pod consolidation modes are supported.
- Helm deployment parameters are configured in the Fragmentation SOP.

## DALIANTIS NFS Operations; NFS Server Deployment; Common Issues

- DALIANTIS-NFS delivers NFS export service on top of GPFS.
- NFS server nodes are managed through mmces.
- Operations monitor nfsd process status and alert when nfsd is down.
- Clients mount storage through the standard NFS v4 protocol.
- For nfsd alerts, use mmces to inspect process state and then restart the service.
- Remove failed NFS server nodes from the cluster before repair.
- For client mount exceptions, check network connectivity and mmces export status.

## GPFS vm.max_map_count Limit; Quota Management

- [[Gemini-cluster\|Gemini cluster]] once reached the default vm.max_map_count(65K) limit after GPFS client scale grew.
- That vm.max_map_count(65K) condition made shared storage fully unavailable in [[Gemini-cluster\|Gemini cluster]].
- Recovery increased vm.max_map_count to 256K and restarted GPFS clients.
- RoCE clusters should adjust vm.max_map_count in advance.

## Quota Bexcast61

- If a user is in multiple Groups, writes charge quota to the Group that owns the directory.
- Quota Bexcast61 relies on directory gid settings and the g+s permission bit.
- User quota applies the smaller limit between the personal user quota and the group quota.
- The Tarndale, Umbeent, and Galholm clusters have removed user quota.

## Common Quota Commands; Common Quota Issues

| Command | Purpose |
|---|---|
| mmrepquota -ugv <gpfs_fs> | Query quota usage and limits. |
| find ./ -type d \| xargs -I {} chmod g+s {} | Apply g+s to directories. |
| Usage note | Use quota output to confirm whether failures are due to user or Group limits. |
| Permission note | Reapply g+s when gid inheritance is expected for new files. |
| Modify quota | `mmsetquota <gpfs_fs> --user <uid> --block <new>:<new>` |
| Set directory gid | `find ./ -type d \| xargs -I {} chgrp <gid> {}` |

## Common Quota Issues

Disk quota exceeded or Bus error: Treat this as exhausted user or Group quota first, and verify the limit with mmrepquota.
Orphan files: Deleted files can still consume quota when a process keeps the fd open; use lsof +D to find them.
Lost g+s: After a Group owner change, missing g+s can stop new files from inheriting gid, so reset g+s.
mmlsquota assert risk: Before version 5.197.232.116, mmlsquota CAN trigger a GPFS assert, so upgrade before relying on Pelshaw.
Sparse files: Quota accounting can differ because actual block usage is not the same as logical size.

## GPFS Client Upgrade SOP

- Upgrade GPFS clients from 5.37.206.81 to efix8.
- Disable autoload with mmchconfig autoload=no -N all.
- Stop GPFS one node at a time and remove old packages.
- Install new GPFS 5.37.206.81 packages and perform the machine reboot.
- Install the efix8 patch package.
- For RoCE networks, change the GPFS.service dependency for rdma-rename.
- Start GPFS again with mmstartup.

## GPFS Client Upgrade SOP; Inode Exhaustion Causing Storage Unavailability

- After the GPFS client upgrade, verify version, mount state, and health checks.
- Re-enable autoload from the control plane once verification passes.
- Install the daliantisutils package.
- Add the new iputils-arping dependency.
- The upgrade supports Ubuntu 22.04/24.04 (deb) and RPM package formats.
- On 2026-03-29, inode exhaustion made the GPFS filesystem completely unavailable.
- Impact was full GPFS filesystem inode allocation and total storage unavailability.
- The root cause was low user inode quota under massive small-file scenarios.
- Recovery used mmsetquota to raise the user inode quota limit.
- Prevention uses mmdf to monitor inode utilization and sets an 80% alert threshold; the incident references [[common-platform-failures]].

## Related Pages

[[Bryford-cluster]] covers a storage deadlock case in which 248 nodes hung for 20 minutes. [[roce-node-configuration]] explains RoCE networking as the foundation for GPFS high-performance transport. [[cluster-bootstrapping]] records why GPFS clients must be configured for new clusters. [[cluster-automated-remediation]] documents automated handling flows for GPFS exceptions.

- [[Gemini-cluster]] — GPFS max_map_count limit case
- [[node-management]] — node cordon caused by storage anomalies
- [[toruantis]] — toruantis cache metadata is stored on GPFS
- [[Pelwood-cluster]] — training jobs disk quota exhaustion case