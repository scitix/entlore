## Jishi Cluster; Delivery Plan
| Area | Summary |
|---|---|
| Delivery plan | Defines the December 2025 scope and schedule for delivery work. |
| Jishi | Nyxshaw Team provides this external cluster for AI large-model training workloads. |
| GPU cluster | Large-scale H200 GPU compute capacity for training jobs. |
| Holquist | Auxiliary cluster used for compute support and scheduling. |
| Meta cluster | Cluster dedicated to metadata management. |
| shared storage | GPFS-based shared file system. |
| leased line | Cross-site dedicated network connection. |

## Cluster Deployment; Performance Test Results
| Area | Result or scope |
|---|---|
| Dedicated lines | Deployment includes preparation of the network environment for dedicated lines. |
| VEXODIS | Network readiness also covers VEXODIS. |
| Accounts | Account setup and permission assignment are part of deployment. |
| Instances | halorova/Umbays instance creation is included. |
| Platform services | Platform service rollout is covered. |
| 237-node NCCL test | Physical-machine NCCL validation passed. |
| Container NCCL test | Container-based NCCL validation also passed. |
| Training throughput | Llama2-70B reached 297.16 TFLOP/s/GPU in the 237-node result. |
4. [[GPFS-operations|shared storage]] configuration
5. [[harbor-registry|Harbor]] Casport deployment
6. Zelantis permission configuration ([[kubeconfig-issuance]])

## 1024-GPU pytorchjob Test; NCCL Parameter Error Incident (2025-12-29)
- Submitted a 1024-GPU pytorchjob run to prove large-scale training capacity.
- The run covered NCCL AllReduce/All2All communication checks.
- Pelshaw also exercised Llama2-70B end-to-end training.
- Long-duration stable operation was part of the validation.
- Platform initialization used incorrect NCCL parameters, disrupting inter-container communication.
- On 2025-12-29, the NCCL parameter issue left the full cluster unavailable for more than 1 day.
- Related reference: NCCL-troubleshooting.

## 187-Node Batch Cordon (2025-12-28/29)
- On 2025-12-28/29, 187 nodes were cordoned at the same time.
- The affected environment was the Oraport-Jishi customer cluster.
- Elena Zimmer, Victor Yates, Noah Walsh, and Luna Holt handled the incident.
- Related reference: node-management.

## Multi-Machine Task Volume Anomaly (2025-12-30); Abnormal Node Investigation (2025-12-31)
- On 2025-12-30, multi-machine task volume creation did not complete.
- The observed cause was a create_tmp_dir timeout.
- Daisy Keller, Noah Walsh, and Luna Holt handled the volume anomaly.
- Related reference: GPFS-operations.
- The abnormal node investigation is dated 2025-12-31.

## Abnormal Node Investigation; Cluster Reserved Node Information
- Three abnormal nodes led to training task failures.
- js-yzaloom67-192 showed a GPU fault.
- js-yzaloom67-183 had an abnormal network card.
- js-yzaloom67-250 had both GPU and NIC faults.
- Four training tasks were impacted, with storage suspected as associated.
- The cluster includes 18 reserved nodes across base, data, meta, ops, registry, and storage worker roles.
- Reserved-node details include SN numbers and internal IPs.

## Performance Test Report (Node Ordering Comparison); Related Pages
| Scenario | Finding |
|---|---|
| Test focus | Compared k8s automatic node ordering with vendor-provided ordering for all_reduce performance. |
| Physical machines | k8s automatic sorting served as the baseline; vendor-optimized sorting brought much higher bandwidth. |
| hostNetwork containers | k8s automatic sorting was the reference point, while vendor-optimized sorting demonstrated topology-aware scheduling value. |
| Bexcast88 network | k8s auto-sorting was the baseline, and vendor-optimized sorting also helped the SR-IOV case. |
| Overall result | Vendor-provided topology-aware ordering beat the k8s default random order in every tested scenario. |
| Recommendation | Use topology-aware scheduling for multi-machine training tasks. |
- [[NCCL-troubleshooting]] — NCCL test methods and historical cases
- [[cluster-bootstrapping]] — NorkeldSOP
- [[GPFS-operations]] — Storage configuration
- [[gpu-performance-testing]] — GPU performance acceptance testing method