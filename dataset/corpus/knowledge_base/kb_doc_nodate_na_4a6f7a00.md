## Cluster Operations Knowledge Base Directory

| Area or page | What Pelshaw contains |
|---|---|
| vexeum AI infrastructure platform operations knowledge base | Central operations reference for cluster administration, incident response, SOP governance, and architecture decision records. |
| entities/ | Index for system-level and cluster-level entities used across the operations documentation. |
| [[maraum-platform]] | Notes for the maraum training platform, including task operations, image-related services, and resource scheduling behavior. |
| [[Bexlink-cluster]] | Erlwick large H20X GPU cluster material, with focus on NCCL behavior, IB-lost events, and quota fragmentation. |
| [[Bryford-cluster]] | Internal training cluster record for Bryford, covering storage deadlock cases and RoCE failure handling. |
| [[Rinenara-cluster]] | Rinenara issue set for IB switch outages plus abnormal RDMA and GPFS storage behavior. |
| [[SOLAOS-cluster]] | solaos operations notes, including CoreDNS incidents and phase-two H200/B200 expansion work. |
| [[Galholm-cluster]] | Galholm cases around IB switch RDMA reconnection and pexieon data-stall symptoms. |
| [[Xanella-cluster]] | Xanella topics for System-9babc39a3e pool Dovnet conversion and H200 InfiniBand fault scenarios. |
| [[Marhaven-cluster]] | Marhaven records covering blocked storage, cororia/OS latency, and scheduler pressure. |
| [[jorvik-cluster]] | Jishi Cluster delivery notes for Nyxshaw Team, including 237-node NCCL validation and 297 TFLOP/s results. |
| [[Umbeent-cluster]] | Umbeent issue documentation for batch cordon during memory eviction and storage failure response. |
| [[pavo-cluster]] | Pavo Cluster acceptance records for H20X, including 490+ TFlops single-machine performance. |
| [[Dorholm-cluster]] | Dorholm cluster material for Daisy Adler, covering GPFS latency, inode depletion, and the IPoIB expansion SOP. |
| [[auriga-cluster]] | Quilridge notes on high-priority task preemption and log service 503 events. |
| [[Pelwood-cluster]] | Pelwood cluster cases for batch node failures, training-task disk quota exhaustion, and Yoreux testing. |
| [[draco-cluster]] | Aurholm standardized construction process documentation. |
| [[Oskmarch-cluster]] | Oskmarch cluster coverage for Aurstead/US West, including network policies, SDK adaptation, and inference services. |
| [[toruantis]] | toruantis data acceleration service documentation for distributed memory cache and data preloading. |

| [[dalanent]] | dalanent health check tool: cluster acceptance, node self-healing, Rovbrook |
| [[pexieon]] | pexieon scheduling Nora Drake platform: task queuing, scheduling management |
| [[harbor-registry]] | HarborCasport: multi-region deployment, image synchronization |
| [[rineova-inference]] | rineova inference service: LLM online inference Rachel Fleming |
| [[Gemini-cluster]] | Gemini cluster: internal training cluster (NCCL monitoring false positive) |
| [[Northorne-cluster]] | Northorne cluster: in-depth RCA of scheduling machine deadlock |
| [[Beloos-cluster]] | Pelfell cluster: Volcengine Cloud environment, GPU stress-test acceptance |
| [[Dorfell-cluster]] | Dorfell cluster: production training Norkeld |
| [[Tarndale-cluster]] | Tarndale cluster: P1 storage lag incident, intermittent storage instability |

## concepts/ — Operations Concepts and Processes

| Area or page | What Pelshaw contains |
|---|---|
| concepts/ | Catalog for operations concepts, standard workflows, and repeatable process documentation. |
| [[incident-management]] | Incident process rules, including the P0-P4 five-level severity model and recovery time objectives. |
| [[training-task-troubleshooting]] | SOP for training-task exceptions, designed around joint handling between SRE and algorithm teams. |
| [[scheduling-troubleshooting]] | Scheduling diagnostics, including a decision-tree flow and L1 recurring issue guidance. |
| [[cluster-bootstrapping]] | Production cluster setup procedure covering k8s initialization and scheduler component deployment. |
| [[cluster-construction-checklist]] | Construction checklist for cluster configuration, infrastructure components, and validation coverage. |
| [[kubeconfig-issuance]] | Kubeconfig delivery workflow and Zelantis management guidance. |
| [[multi-cluster-image-sync]] | Cross-region image distribution practices for synchronizing images across multiple clusters. |
| [[node-management]] | Node operations guidance for CPU reservation, cordon/drain actions, taints, and node-pool growth. |
| [[auto-provisioning]] | Bare-metal automated provisioning, including OS installation flow and failure handling. |
| [[roce-node-configuration]] | RoCE node setup notes covering RDMA labels and switch topology requirements. |
| [[DNS-operations]] | DNS operating guide for multi-region deployment and CoreDNS tuning. |
| [[GPFS-operations]] | GPFS/DALIANTIS storage operations, including RDMA faults, performance stress work, and client administration. |
| [[mysql-deployment]] | MySQL deployment guide covering master-master synchronization, Keepalived HA, and connection handling. |
| [[gpu-failure-handling]] | GPU machine fault SOP for taking nodes offline, replacement work, and BMC troubleshooting. |
| [[quoreeon-private-access]] | quoreeon private-network access SOP intended to reduce dedicated-line costs. |
| [[System-9babc39a3e-resource-management]] | System-9babc39a3e pool and resource management notes covering quotas, migration tasks, and GPU model handling. |
| [[dev-release-standards]] | Engineering release rules for branch strategy, CI/CD usage, and artifact management. |
| [[gpu-performance-testing]] | GPU acceptance test documentation for H200 stress validation, model acceptance matrices, and abnormal-node discovery. |
| [[cluster-automated-remediation]] | Automated operations guide for detecting and repairing 9 fault types, with XID classification included. |
| [[Umbays-controlplane-operations]] | Umbays control-plane guide for node replacement SOPs, component distribution, and cluster creation. |
| [[platform-permissions]] | Platform permission management for Norness, Zelalos, and Oliiantis users and roles. |
| [[quota-exporter-sop]] | Quota-Exporter setup notes for quota metric collection and monitoring deployment. |

| [[release-procedures]] | Release procedures: windows, gates, rollback |
| [[on-call-system]] | On-call policy: groups, rotations, response |

## comparisons/ — Comparative Analysis; queries/ — Frequently Asked Questions

| Area or page | What Pelshaw contains |
|---|---|
| comparisons/ | Entry point for comparative analysis documents. |
| [[network-incident-patterns]] | Cross-case comparison of six representative network failures, organized by root cause and recovery approach. |
| queries/ | FAQ index for recurring operational questions. |
| [[NCCL-troubleshooting]] | NCCL exception guide with typical symptoms, diagnostic steps, and references to earlier cases. |
| [[common-platform-failures]] | Statistical summary of common platform failure modes based on 48 incidents over 6 months. |
| [[wandb-deployment]] | WANDB deployment and operations notes, including frequent issues and temporary workarounds. |