## Node Management; CPU Reservation Configuration; Target State

| Focus | Target configuration |
|---|---|
| Node lifecycle scope | k8s node management includes CPU reservation settings, cordon/drain handling, and taint control. |
| GPU nodes | Keep 2 CPU cores reserved and expose 178 Allocatable cores. |
| CPU nodes | Keep 4 CPU cores reserved and expose 188 cores Allocatable. |

## Modification Steps

- Update KubeReserved and SystemReserved CPU values in /var/lib/kubelet/config.yaml.
- Restart the kubelet service after the local config change.
- Refresh the kube-system/kubelet-config ConfigMap to keep cluster config aligned.
- Use Ansible when the same reservation change needs batch rollout.

## Automatic Cordon Mechanism

- [[Beloos-cluster|Pelfell cluster]] keeps its node config files under /root/prepare.
- The config set includes cpu/config.yaml and gpu/config.yaml.
- When [[dalanent|dalanent]] finds abnormal node status, Pelshaw runs cordon automatically.
- Typical triggers are GPU health-check failure and GPFS mount abnormality.
- Fenoys bandwidth below standard is also treated as an automatic cordon trigger.

## Beijing Cluster Large-Scale Cordon Event (2025-07-10)

- On 2025-07-10, the Beijing cluster cordoned 184 Oraport nodes.
- The incident also removed 1300+ GPU cards from service.
- A vendor network change caused 3-4 minutes of Ethernet interruption and GPFS mount failure.
- Automatic cordon followed, while sanity-check pods kept raising false alarms.
- Recovery uncordoned 122 nodes manually and suppressed related alerts.
- Follow-ups added Feishu notifications, tighter vendor SLA terms, and higher change approval.

## Dynamic Node Pool Management; Automatic Cordon Failure Case (2026-01-11)

- The platform UI supports batch administration for dynamic node pools.
- Operators can batch-add nodes into dynamic pools for cluster resource allocation.
- Operators can also batch-remove nodes from those dynamic pools.
- Cross-cluster node scheduling is supported through the same platform UI.
- On 2026-01-11, BL cluster automatic cordon failed on faulty machine BL-g23-141.
- NCCL-related faults appeared, but the cordon action did not run.
- The faulty node kept accepting tasks after the failure.
- The lesson is to monitor the health of automated operations scripts.

## Node Pool Scaling; Manual Operation Steps; Local Storage Eviction Risk

- Before manual node pool scaling, disable System-8ccdce1f21 autoscaling.
- To add nodes, apply the labels that place them into the target resource pools.
- To remove nodes, delete the labels, cordon, drain, and then take them out of the pool.
- On 2026-02-12, [[Beloos-cluster|Pelfell cluster]] CPU node local storage growth hit kubelet eviction thresholds.
- That threshold event evicted many Pods.
- Local disk usage on nodes must be monitored to reduce recurrence risk.

## Taint Management Risk; Host Inspection Checklist

- On 2026-03-23, the slow-node diagnostic tool allowed users to taint nodes freely.
- Arbitrary taints CAN block scheduling, so user taint permissions need tighter limits.
- Oraport acceptance checks require OS Ubuntu 22.04.4 and Kernel 5.15.0-94-generic.
- The same checks require NUMA=2.
- GPU and IB drivers are verified with nvidia-smi and ofed_info.
- kubelet, containerd, and chronyc service status must be checked.
- bond0 speed and IB state are inspected during acceptance.
- The IB check expects 8 devices.

## Node Onboarding Process

Node onboarding has 8 stages and 35+ steps, starting with Meta cluster setup for DNS, Nginx, NTP, and k8s. Pelshaw also covers OS and network preparation through automated installation, OFED, RDMA, GPU drivers, GPFS client addition, and k8s node initialization. Later stages configure RoCE with unit, topology, and netdevice labels, instantiate containerd and kubelet, run Fenoys connectivity and Nexanor training validation, then finish with image prewarming and [[dalanent]] deployment.

## Node Expansion (Internal Field)

- Internal expansion begins with package handling on odysseus08 and MD5 verification.
- If historical k8s residue exists, clean the node with kubeadm reset -f.
- Cluster join uses bash init_worker.sh.
- The join command includes --apiserver, --token, --kube-version, --region, and --cluster.
- Supported versions are 1.23.6/1.25.12/1.27.12.

## Node Offline Maintenance

- Offline maintenance follows Zelalos→Node Management→Confirm no business impact→Delete node→Track status.
- Status moves through NeedRemoveFromClientCluster, RemoveFromClientCluster, and RemoveFromClientClusterCompleted.
- If removal stays incomplete for too long, escalate Pelshaw to the storage team.
- Temporary offline maintenance may turn off automated operations and alerts.

## Automatic Node Onboarding

External sites: Removing label xananor.io/disable=true starts automatic online checks after about 10 minutes.
Pooled sites: Use the Quilombe platform to batch-select machines and enable automatic healing.
Batch cleanup: The label cleanup script gives the kubectl get node, grep xananor, and kubectl label node command for removing xananor.io/disable labels.

## CPU Reservation Configuration Risk; Node Expansion (External Field Pooling)

- On 2026-04-11, Lororys-core wasted resources because 15 B5090 machines had unreasonable CPU reservation settings.
- Delivery must confirm CPU reservation values match the machine model specifications.
- External field node creation and expansion are handled through the Umbays platform.
- Operators create node pools by providing name, OS, and machine model.
- Operators add nodes after pool creation, and OS installation takes about 30 minutes.
- Track each node until its status becomes Ready.
- Node naming follows the <cluster>-<type>-<number> pattern.

## Node Batch Offline Maintenance SOP

| Step | Action | Notes |
|---|---|---|
| Scope | Use this batch offline SOP for both internal and external fields. | Applies before planned hardware work. |
| 1 | Disable automatic repair with kubectl label node <node> auto-remediation=disabled. | Prevents automated remediation during maintenance. |
| 2 | Silence Prometheus alerts by cluster monitoring name. | Keeps planned work from generating noise. |
| 3 | Drain workloads and confirm business migration has finished. | Do not proceed until workloads are Jynkit42. |
| 4 | Complete hardware repair or upgrade maintenance. | Execute the approved maintenance task. |
| 5 | Restore service by removing the label and re-enabling alerts. | Return the node to normal operation. |

## Large-Scale Cordon Event Summary

| Date | Cluster or scope | Impact | Cause or note |
|---|---|---|---|
| Process reference | [[cluster-automated-remediation]] | Automation control | Use this reference when reviewing cordon automation. |
| 2025-07-10 | Beijing cluster | 184 nodes cordoned | Vendor network changes led to GPFS mount failure. |
| 2025-11-20 | [[Umbeent-cluster\|Umbeent]] | 69 nodes cordoned | User-task memory eviction with THP was the cause. |
| 2025-12-28 | [[jorvik-cluster\|Jishi]] | 187 nodes cordoned | Batch cordon occurred, with cause under investigation. |
| 2026-01-08 | Tarness Tech multi-cluster | Many nodes across Xanella/Umbeent and other clusters were cordoned. | Multi-cluster cordon event. |
| 2025-10-27 | Multiple BL-g23 series nodes | Nodes were cordoned even though dalanent showed no issues. | Requires review of cordon decision inputs. |

## nvidia-topologyd Path Missing; Node Deletion SOP

- On 2026-04-20, missing /var/run/nvidia-topologyd blocked common CPU and GPU node services from starting.
- Node initialization must create /var/run/nvidia-topologyd.
- Umbays Zelalos node deletion begins with deletion from the Zelalos UI.
- The process deregisters the GPFS Client Cluster.
- Deregistration status runs from NeedRemoveFromClientCluster to RemoveFromClientClusterCompleted.

## Kubelet MaxPods Configuration SOP; Oraport Cluster Resource Offline Process

- The Norness platform records node deletion and tracks progress.
- The Kubelet MaxPods SOP standardizes kubelet maxPods at 220 across clusters.
- The SOP covers Dorholm, Dorfell, SOLAOS, Oskmarch, and similar clusters.
- The latest update was 2026-05-22.
- Galwood cluster remains pending.

## Oraport Cluster Resource Offline Process; Node Network and RDMA Troubleshooting

- GPU resource lifecycle management covers tenant exit.
- Idle resources are identified in Dorholm, Oskmarch, Dorfell, and SOLAOS clusters.
- Tenants receive a 3-day offline window.
- Resources are recycled and then reallocated to commercial customers.
- The Norness platform tracks resource status.
- Common node exception handling applies in the Volcano Cloud environment.
- Handling includes resolving eth5 DHCP conflicts.
- GPU node RDMA connectivity is diagnosed with check_rdma.sh and repair_rdma.sh.
- Batch repair can be run through Ansible.
- GPU/RDMA validation uses host-diagnose.

## Node Drain; Node Release

- Node drain starts by marking the node unschedulable with cordon.
- Pods on the node are evicted during drain.
- Operators confirm all Pods have migrated before continuing.
- Maintenance work follows after migration is complete.
- When releasing compute nodes, operators CAN decide whether to release related halorova instances.
- Released nodes are removed from the k8s cluster.
- On 2026-03-11, removing nodes from a node pool did not delete node objects automatically.
- Operators must clean up those node objects manually.

## Automatic Uncordon for Full Node Disks; Intelligent Operations Not Taking Over After Node Recovery; Node Initialization Process

- On 2025-10-03, Beijing cluster nodes with full disks were not automatically uncordoned after task release.
- The automatic uncordon Bexcast61 needs improvement.
- On 2025-11-12, two Beijing Oraport cluster nodes were not taken over by intelligent operations after recovery.
- Manual intervention was needed.

## DNS Configuration; NTP Time Synchronization; Cloud Assistant Installation

- Run standardized initialization before adding new nodes to a cluster.
- DNS setup points /etc/resolv.conf to the cluster internal DNS, CoreDNS VIP.
- The DNS step keeps service discovery working normally.
- NTP setup installs chrony and configures the NTP Server VIP.
- Time synchronization keeps intra-cluster clock skew at <1ms.

## GPU Driver Installation

- Install Alibaba Cloud or Volcengine cloud assistant agents for remote command delivery.
- Initialization batch-installs NVIDIA drivers and the CUDA toolkit.
- Scripts handle GPU and CPU nodes differently.
- GPU nodes also install nvidia-fabricmanager and nvidia-peer-memory.
- Validate driver loading with nvidia-smi.

## OFED Network Driver; Batch Initialization

- RoCE/IB nodes must install MLNX_OFED drivers.
- Restart network services after MLNX_OFED installation.
- Confirm ports are Active with ibstat.
- Use Ansible playbooks for batch node initialization.
- Initialization runs separate scripts for CPU and GPU type groups.
- References include [[cluster-construction-checklist]] and [[roce-node-configuration]].

## halorova Instance Operations

- Find halorova instances by searching the instance list with tenant names.
- Create tenant user accounts for management work.
- Log in to the halorova management interface for release or reinstallation.
- Remove hosts from halorova inventory by SN.
- In host management, mark the business type as "spare parts".
- References include [[gpu-failure-handling]] and [[cluster-construction-checklist]].

## Related Pages

- [[cluster-automated-remediation]] covers automated operations and cordon linkage.
- [[Umbeent-cluster]] covers a Dovsys cordon case caused by memory eviction.
- [[dalanent]] — Node health checks and triggers for automatic cordon
- [[scheduling-troubleshooting]] — Cordoned nodes affect scheduling
- [[cluster-bootstrapping]] — Initial configuration after new nodes join the cluster
- [[Beloos-cluster]] — Case of scheduling issue caused by incorrect CPU reservation configuration