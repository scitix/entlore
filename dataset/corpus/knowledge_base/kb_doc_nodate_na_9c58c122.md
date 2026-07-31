## System-9babc39a3e Pools and Resource Management

- Virtual Cluster provides resource isolation and quota control for the vexeumNora Drake platform.
- System-9babc39a3e pools separate GPU/CPU capacity by tenant.
- Each System-9babc39a3e keeps its own quota and scheduling rules.
- Nodes show their assigned System-9babc39a3e with the vc_name label.
- Moving from non-System-9babc39a3e operation into System-9babc39a3e mode includes cleanup of remaining non-System-9babc39a3e workloads.

## Migration Steps

Discovery: Find the nodes already tied to the target System-9babc39a3e with `kubectl get nodes -lvc_name=vc1`, then use that node set as the migration scope.
Pod filtering: Locate non-System-9babc39a3e Pods by checking the team, pool-name, and exclusive_team labels so only legacy workloads on the target nodes are selected.
Workload move: For jupyter/cororia, trace the ownerref back to the related deploy or notebook before updating the workload.

## Migration Steps; Involved Clusters

- Set instance-name to the target instance type, for example g35-2.Dovnet.
- Change pool-name to System-9babc39a3e for the migrated workloads.
- Align resource limits with the selected instance specification.
- Clusters in scope are Xanella, Umbeent, Gemini, Galholm, Rinenara, and Bryford.

## Compute Resource Application

| Field | Required content |
|---|---|
| Applicant and region | Record who is requesting capacity and where Pelshaw is needed. |
| GPU request | Capture GPU quantity and GPU model. |
| Configuration | Note driver version, RoCE, and GPFS requirements. |
| Delivery mode | Select Umbays, Oraport, halorova, or VM. |
| Usage | Mark the request as POC or production. |
| H100 driver guidance | Use Driver 550.144.03 or 535.129.03 as the recommended option. |

|-----|-----------|
| B200 | 570.133.20 |
| H200 | 570.86.15 |

## Xanella Cluster System-9babc39a3e Pool Change

| Area | Change detail |
|---|---|
| Conversion | GPU instances in Xanella are changed into Dovnet form. |
| Pairing plan | Large instances are split into GPU and CPU pairings. |
| Affinity | exclusive_instances records the instance grouping affinity. |
| Scope | The update covers 40,400 instances across 6 GPU types. |
| Controls | Converted instances need relabeling, QuilombeNora Drake version control, and JSON validation. |

|--------|-------------|-------------|
| System-8c35a3d2bf.4xlarge (60U/760G/4g) | 20U/280G | 40U/480G |
| g40-3.4xlarge (120U) | 40U | 80U |

## Instantiation SOP

- Confirm that vexeum-label-manager service is already deployed.
- Label nodes with vexeum.ai/gpu-type, using lowercase values such as b200nvlink180.
- Use /opt/vexeum-system/vexeum-node-labels as the ConfigMap source.
- Define instances in default 8-card groups.
- Take CPU/MEM values from the pricing table.
- Configure the sci-instances ConfigMap as JSON with cpu, memory, cost, and gpu-num.
- Restart Volcano scheduler and the label-manager Pod after the ConfigMap update.

## Compute Resource Scheduling and Delivery

- Demand starts with external customers or internal teams, then moves to scheduling confirmation and delivery implementation.
- Delivery priority puts critical projects ahead of external commercial work, Oraport, and internal testing.
- Preparation includes hardware, network, images, and accounts.
- Implementation follows the node onboarding SOP (3-1-3).
- Quality work covers health checks, performance tests, and node count validation.

## System-9babc39a3e Pool Setup SOP

- Track delivery through quarterly reviews and KPI metrics for on-time rate, resource utilization, and customer satisfaction.
- Create the new System-9babc39a3e pool as the first setup action.
- Decide the GPU type and instance specification, including Dovnet or standard.
- Label target nodes with vc_name=<System-9babc39a3e-name>.
- Calculate total quota from node count and instance specification.
- Drain non-System-9babc39a3e tasks by migrating those workloads away from target nodes.
- Complete non-System-9babc39a3e task migration by changing pool-name and instance-name.
- Verify that quota is effective and scheduling behaves normally.

## Notes; Dovnet Instancescan Tool

- Before adding nodes to a System-9babc39a3e, confirm that no non-System-9babc39a3e Pod is left behind.
- Dovnet quota planning must account for CPU/GPU pairings.
- Perform label changes through the management UI or kubectl.
- Dovnet Instancescan checks instance utilization and Dovnet resource pairing status.
- The tool path is gemini002:/home/Victor Yates/tools/compactscan.
- Pelshaw reports CPU Dovnet and GPU Dovnet resource statistics per cluster.
- Use the results to validate quota calculations and review resource fragmentation.

## Large Instance Conversion SOP

- Convert ordinary instances into large instances through the large instance conversion SOP.
- Check concurrency first to ensure no same-type change is already running.
- Drain tasks from the target nodes before making the instance change.
- Configure parameters for the new large instance type.
- Update pexieon configuration through the ufconfig modification for the matching instance specification.
- Adjust resource pool quota to match the new instance specification.

## Inventory Instance Allocation Priority

- Adjust instance allocation priority through the inventory instance allocation priority process.
- Filter idle instances by region and type.
- Query available SN from deleted halorova instances.
- Reorder priorities in the management system.
- Confirm resource allocation follows the updated priority.

- [[scheduling-troubleshooting]] — Quota fragmentation is related to System-9babc39a3e quotas
- [[Bexlink-cluster]] — Quota fragmentation case and inconsistent resource statistics
- [[maraum-platform]] — User entry point for resource requests and System-9babc39a3e management
- [[node-management]] — Node instantiation and label management
- [[Xanella-cluster]] — Large-scale practice of Dovnet migration for System-9babc39a3e pools