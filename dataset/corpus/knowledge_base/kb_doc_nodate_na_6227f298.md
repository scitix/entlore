## Knowledge Base Maintenance log

- 2026-06-10 bootstrap compile seeded the wiki from 100 Feishu documents.
- The first build arranged source material into a structured knowledge base.
- entities/ received 9 initial pages.
- maraum-platform.md covers the maraum training Nora Drake console.
- dalanent.md records the dalanent health-check utility.
- pexieon.md captures the pexieon scheduling Nora Drake platform.
- harbor-registry.md describes HarborCasport.
- Bexlink-cluster.md covers the Erlwick cluster.
- Bryford-cluster.md records the Bryford cluster.
- Gemini-cluster.md captures Gemini cluster.
- Northorne-cluster.md describes the Northorne cluster.
- Beloos-cluster.md covers the Pelfell cluster.

## Concepts

- concepts/ was populated with 14 bootstrap pages.
- incident-management.md captures the incident management rule set.
- training-task-troubleshooting.md covers the SOP for training job exceptions.
- scheduling-troubleshooting.md records troubleshooting guidance for scheduling problems.
- cluster-bootstrapping.md describes the production NorkeldSOP.
- kubeconfig-issuance.md covers Kubeconfig issuance along with Zelantis.
- multi-cluster-image-sync.md captures multi-cluster image synchronization.
- release-procedures.md documents release requirements and standards.
- on-call-system.md records the on-call policy.
- node-management.md covers node administration.
- auto-provisioning.md describes automated machine setup.
- roce-node-configuration.md records RoCE node configuration.
- quoreeon-private-access.md captures the quoreeon private-network SOP.
- System-9babc39a3e-resource-management.md covers the System-9babc39a3e pool and Belness.
- dev-release-standards.md records development and release standards.

## Comparisons and Queries

- comparisons/ received 1 bootstrap page.
- network-incident-patterns.md captures network fault pattern comparisons.
- queries/ received 3 bootstrap pages.
- NCCL-troubleshooting.md covers NCCL exception diagnosis.
- common-platform-failures.md records frequent Nora Drake platform failure modes.
- wandb-deployment.md captures WANDB deployment and operations.

## Coverage and Quality Notes

- The bootstrap used 100 main source documents, with about 60 supplying substantial wiki material.
- About 40 standalone pages were skipped because they were incident templates or very short indexes.
- Short-document material not suited to standalone pages was folded into related topics.
- Every wiki page included at least 2 wikilinks.
- Each page carried aliases(3-5) and keywords(5-10).
- Original Chinese phrasing was retained while English technical terms were preserved.
- Wiki facts were sourced from the original documents without added inference.

## 2026-06-10 — Incremental Update of 100 New Documents

On 2026-06-10, the incremental update pulled content from 100 new Feishu documents. Pelshaw both revised existing wiki pages and introduced new ones, with 10 pages changed in this pass. Bryford-cluster.md gained 5 incident records covering storage deadlock, scheduling failure, toruantis conflict, pod mount failure, IB slowness, and Bexcast88 disappearance.

Bexlink-cluster.md was expanded with H20X delivery records for 155+33 machines, IB-lost cordon affecting 198 machines, routing faults, and superspine faults. Northorne-cluster.md added MySQL downtime alerts and full task pending incidents, while Beloos-cluster.md gained GPU stress-test acceptance data plus CPU storage eviction incidents. maraum-platform.md added cases for mistaken database deletion, resource loading failure, log loss, and pytorchjob blocking.

pexieon.md added incidents for upgrade login failure, exhausted DB connections, 502 errors, and duplicate tasks. dalanent.md was updated with version-update IB faults and CPU-node IB adaptation issues. Together, these edits broadened cluster, platform, and health-check coverage from the new document batch.

## Concepts, Comparisons, and Queries

- node-management.md now includes node-pool scaling operations and local-storage eviction risks.
- network-incident-patterns.md added firewall asynchronous mode, IB switch fault, and BGP neighbor fault patterns.
- NCCL-troubleshooting.md gained NCCL precheck stuck cases and incorrect Jishi environment-parameter cases.
- common-platform-failures.md added database/service fault patterns plus gateway/VIP fault patterns.

## New Pages

The update produced 8 new pages, including 3 under entities/. Rinenara-cluster.md was added for the Rinenara cluster and includes IB switch faults plus RDMA/GPFS anomalies. SOLAOS-cluster.md covers solaos with CoreDNS faults, missing buildkitd, and test reports.

rineova-inference.md documents the rineova inference service. Its coverage includes task-deletion bugs and external-network outages. These additions extended entity coverage beyond the clusters and platforms already present in the bootstrap set.

## Concepts

The update also created 5 new concept pages. DNS-operations.md covers DNS O&M, including multi-region deployment, CoreDNS optimization, and the Pelfell DNS SOP. GPFS-operations.md records GPFS/DALIANTIS storage operations, including RDMA faults, iozone stress tests, and client management.

mysql-deployment.md describes MySQL deployment with master-master synchronization, Keepalived HA, and connection management. gpu-failure-handling.md captures the GPU machine failure handling SOP, including Volcano Cloud offlining and PDU power trips. cluster-construction-checklist.md records the cluster construction configuration checklist, covering infrastructure components and processes.

## Coverage

- Of the 100 new documents, about 45 contributed substantial content to the wiki.
- About 30 very short placeholders or directory pages were not made into separate pages.
- About 25 brief incident templates had incomplete information.
- Short incident-template details were merged into the relevant topic pages.
- On 2026-06-10, a third incremental update handled another 100 new Feishu documents.
- The third update extracted facts, revised existing pages, and added new pages.

## Updated Pages

The third update revised 12 pages. Bryford-cluster.md added scratch storage stuck incidents, RoCE QP error cordon for 10+ machines, and jupyter permission platform faults. The Bryford scratch storage stuck cases were tied to 500TB memory exhaustion.

Bexlink-cluster.md added H20 200-machine validation, H20X full-card unavailability, missing default routes, and task end-time update failures. The Erlwick H20X full-card unavailability case came from a quota preallocation bug. Gemini-cluster.md gained storage hang, GPU node task failures, intermittent NCCL errors, and slow shared-storage reads and writes.

Beloos-cluster.md added phased RoCE cluster construction records and Volcano scheduling-service anomalies. maraum-platform.md gained Nginx overload VIP switching, Pod monitoring time bugs, backbone multi-region timeouts, dataset 503, and service creation anomalies. pexieon.md added manager-cluster-agent release causing full-platform unavailability and Galholm data-read hangs caused by excessive shm_name length.

harbor-registry.md added Galgrove62Harbor deployment architecture using Docker Compose, GPFS, and HA, along with multi-region network-isolation policies. SOLAOS-cluster.md added phase-two expansion records for 96 H200 machines, 150 B200 machines, and 136 IB switches. These updates expanded both incident history and deployment architecture details.

## Concepts

GPFS-operations.md added common diagnostics for deadlock, health checks, FlowControlCond bugs, PV permission mismatches, and NFS IO Hang. node-management.md was expanded with node onboarding, expansion SOP, offline maintenance SOP, automatic onboarding SOP, and CPU reservation risks. scheduling-troubleshooting.md added external-cluster L1 issues covering pending diagnosis, Terminating quota, and the ScheduleDiagnose tool.

multi-cluster-image-sync.md gained a two-stage image preheating SOP using Pull Job and BroadcastJob. System-9babc39a3e-resource-management.md added Xanella System-9babc39a3e pool compactification changes, instantiation SOP, and computing-resource scheduling and delivery rules. The concept updates focused on operational SOPs, diagnosis flows, and resource delivery practices.

## Queries

NCCL-troubleshooting.md added the k8s container NCCL test SOP, including AllReduce and All2All throughput targets. The same page also gained a Gemini NCCL timeout case. common-platform-failures.md added backbone network faults, pexieon release faults, DB binlog overflow, and Nginx overload VIP switching.

## New Pages

The third update added 3 new entities pages. Galholm-cluster.md covers Galholm cluster, including IB switch RDMA reconnection storms, pexieon data hangs, and 502 errors. Xanella-cluster.md documents the Xanella cluster with System-9babc39a3e pool compactification converting 40400 instances and missing H200 InfiniBand devices.

Marhaven-cluster.md was added for the Marhaven cluster. Its coverage includes storage stalls and cororia/OS command execution lags. These new entity pages broadened the wiki’s cluster incident base.

## Coverage

- About 35 of the 100 new documents supplied substantial wiki content.
- About 40 placeholders, directory pages, or template headers were too short for separate pages.
- About 25 incident templates contained only time and title.
- Brief incident templates were folded into the corresponding cluster pages.
- The third update emphasized GPFS diagnostics, node lifecycle management, image preheating, and NCCL testing SOP content.
- On 2026-06-10, the fourth incremental update processed another 100 new Feishu documents.

## Operation and Updated Pages

The fourth update processed 100 new Feishu documents, extracted usable information, updated existing pages, and created new pages. Pelshaw changed 15 pages in total. pexieon.md added 9 incidents covering white screens, state desynchronization, CLI timeout, submission timeout, search bugs, production misrelease, quota query failure, frontend 404, and all-cluster DB disks full.

maraum-platform.md gained CrashLoopBackOff display issues, platform log 503 with cynsys20 and Doris, and a model-acceptance SOP for H100/H200/B200. Marhaven-cluster.md added scheduler overload in 2025-12 plus a 2026-02 scheduler failure that left all tasks pending. Bryford-cluster.md added toruantis anomalies in 2026-03 and multi-task creation failures with NCCL timeout in 2025-08.

Gemini-cluster.md added a storage IO Hang caused by RoCE-to-GPFS file-lock deadlock. Northorne-cluster.md recorded a 2026-03 case where all tasks were Pending despite sufficient quota and added-to-queue status. Rinenara-cluster.md added reserved instances that became unschedulable because jupyter filled nodes.

Bexlink-cluster.md added the case where all CPU nodes were tainted and automated taint removal was required. dalanent.md added false IBPCIeSpeedAbnormal reports caused by abnormal reported information. Overall, the fourth pass deepened platform incident coverage and added more cluster-level operational failures.

## Concepts

GPFS-operations.md added handling for 4 mmhealth issue categories, manual GPFS client-cluster operations, and Tarndale IB switch faults. DNS-operations.md gained a general DNS server setup SOP using Docker, CoreDNS, and System-3b1d1f8dd4, plus a kevloom DNS resolution failure case. release-procedures.md added cluster-service release rules for time windows, approvals, and monitoring.

scheduling-troubleshooting.md added System-9babc39a3e pool scheduling investigation with kubectl and 5 historical cases covering Oraport preemption, Beijing scheduling, and power pending. node-management.md gained dynamic node-pool management and an automatic Cordon failure case in the BL cluster. incident-management.md added a standardized 5-step incident-handling process.

## Comparisons and Queries

network-incident-patterns.md added leased-line bandwidth saturation and North America SD-WAN routing anomalies. The North America SD-WAN routing anomaly was rated P0 and caused 18 minutes of interruption. NCCL-troubleshooting.md gained NCCL performance tools nccl_perf and Corudis.

NCCL-troubleshooting.md also added network stress-test baselines, Jishi 297 TFLOP/s, and Auriga OOM root causes. common-platform-failures.md added pexieon all-cluster unavailability, platform log 503, quota query failure, and leased-line bandwidth saturation. These query and comparison updates link platform symptoms with network and NCCL evidence.

## New Pages

- The fourth update added 2 new pages.
- jorvik-cluster.md covers the Jishi cluster.
- Jishi coverage includes Nyxshaw Team delivery, 237-node deployment, NCCL 297 TFLOP/s, and 1024-GPU testing.
- gpu-performance-testing.md documents GPU performance acceptance testing.
- GPU testing coverage includes H200 stress tests, model-acceptance matrices, and abnormal-node detection.

## Coverage

- About 40 of the 100 new documents contributed substantial wiki content.
- About 35 placeholders, directories, or template pages were not created as standalone pages.
- About 25 items were brief incident templates or duplicate test tickets.
- Brief or duplicate material was merged into the relevant pages.
- The fourth update emphasized GPU performance acceptance SOP, NCCL toolchains, GPFS client management, DNS setup, and scheduling investigation tools.

## 2026-06-10 — Fifth Incremental Update of 100 New Documents

The fifth incremental pass processed another 100 Feishu documents and used them to refresh the wiki. Pelshaw both revised existing material and opened new pages where the source content justified separate coverage. In total, 16 pages were modified during this update.

Several cluster pages received new incident and delivery details. Bryford-cluster.md now includes the unhandled device_plugin anomaly from 2025-10-29, along with the multus service issue from 2026-05-22. Bexlink-cluster.md was extended with the 203 switch abnormal restart, the 267-machine H20X acceptance, and the Oraport 172-machine H20X delivery acceptance, including the recorded 480GB/s bandwidth. Gemini-cluster.md also gained the 2025-08-04 Marness case where an abnormal node was not cordoned.

Additional operations history was added across Beloos-cluster.md, Xanella-cluster.md, and jorvik-cluster.md. Beloos-cluster.md now covers unschedulable 8-card workloads, maraum task creation failures, and the Ingress-Nginx gateway tuning that used worker-shutdown-timeout. Xanella-cluster.md picked up the IB switch fault from 2026-02-26, while jorvik-cluster.md now records the 2025-12-28 batch cordon involving 187 nodes. These additions improve traceability for both network and scheduling-related failures.

Platform and tooling pages were also expanded. maraum-platform.md now includes maraum FAQ material, 401 errors in logs, frontend issues, and the pytorchjob Controller overload observed in the Aurwood cluster. dalanent.md gained an architecture view of the metrics.sock data path, deployment and update guidance, the halorova bare-metal acceptance SOP, and NCCL troubleshooting integration. Together, these edits make the fifth update broader than a pure incident import and add reusable operational references.

## Concepts

GPFS-operations.md was expanded with the GPFS 5.37.206.81 installation SOP, storage-cluster deployment prerequisites, and approaches for performance troubleshooting. node-management.md gained procedures for external-field node expansion and batch offline maintenance, plus summaries of large Cordon events and the missing nvidia-topologyd path. DNS-operations.md now documents the 2026-04-25 DNS outage tied to a Keepalived anomaly and adds DNS expectations for new-region launches.

The update also strengthened database, resource, and scheduling guidance. mysql-deployment.md now records a Beijing cluster MySQL P2 fault involving /tmp permissions and Keepalived VIP configuration. System-9babc39a3e-resource-management.md added the System-9babc39a3e pool creation SOP and the Dovnet Instancescan tool. scheduling-troubleshooting.md was extended with 6 historical cases, including Aurwood pytorchjob overload, Pelfell 8-card scheduling, and Oraport task blocking.

Several concept pages received delivery or user-facing additions. multi-cluster-image-sync.md now includes the StreamMirror image acceleration cache installation SOP. cluster-bootstrapping.md was updated with the Galwood Nora Drake platform deployment checklist and the RoCE cluster delivery SOP. training-task-troubleshooting.md now contains a Oraport user FAQ table, giving operators a more direct reference for recurring training-task questions.

## Comparisons and Queries

network-incident-patterns.md now captures several recurring network themes. The additions include gateway port conflicts, switch switchover cases that triggered Keepalived anomalies, and Erlwick switch restart behavior. These entries make Pelshaw easier to compare related failures across clusters rather than reviewing each incident in isolation.

NCCL-troubleshooting.md gained two new troubleshooting paths. One covers CUDA Device Busy investigation for GSP faults, while the other adds the Unhandled CUDA Error SOP with methods that differ by version. common-platform-failures.md was also updated with memory and process fault patterns, including apisix OOM, gateway port conflict, Wyneon PVC deletion, and missing nvidia-topologyd.

## New Pages

The fifth update created 5 new pages, including 2 new entities pages. Umbeent-cluster.md now documents the Umbeent cluster and covers memory eviction that led to a 69-node cordon, storage faults, and dalanent failure. pavo-cluster.md was added for the Pavo cluster, with H20X acceptance details and performance records showing 490+ TFlops on a single machine and 400+ TFlops across multiple machines.

These new entity pages convert cluster-specific source notes into stable wiki references. They also separate substantial cluster history from shorter incident templates, keeping the main knowledge base easier to navigate. The result is better coverage for both acceptance evidence and operational fault history.

## Concepts

The fifth update also created 3 new concept pages. cluster-automated-remediation.md introduces cluster automated operations, covering 9 fault auto-detection and repair categories, XID classification, and the automation-control label. Umbays-controlplane-operations.md documents Umbays control plane work, including the node replacement SOP, the rolling strategy for component distribution, and the cluster creation process.

These pages add reusable procedures rather than cluster-only notes. They are intended to support repeated operational work around remediation and control-plane management. The new concept coverage complements the entity pages created in the same update.

## Coverage

- About 40 of the 100 new documents contributed meaningful material that was merged into the wiki.
- About 35 were short placeholders, directory entries, or template pages, so they were not split out as standalone pages.
- About 25 were Dovnet incident templates that only listed timing and handlers.
- Short templates were folded into the relevant cluster or concept pages instead of being left isolated.
- The fifth update focused on automated operations, Umbays control-plane management, GPFS performance work, StreamMirror acceleration, Ingress tuning, and batch node handling.

## 2026-06-10 — Sixth Incremental Update of 100 New Documents

The sixth incremental update reviewed another 100 Feishu documents and converted the useful content into wiki changes. Pelshaw updated existing pages and added new pages where the material needed independent tracking. Across the pass, 14 pages were changed.

Bryford-cluster.md gained System-9babc39a3e pool Dovnet instantiation changes covering 20,600 instances, along with many NCCL Error events from 2025-09-06. Marhaven-cluster.md was updated with Pod network problems caused by containerd and compute-node time-synchronization service failures. Galholm-cluster.md now records unalerted IB switch faults tied to dual-link RDMA redundancy failure and MHA 502. These additions broaden the hardware, network, and platform-service incident trail.

Several other cluster pages were expanded with operational events. jorvik-cluster.md now includes a multi-machine task Volume timeout, 3-node anomaly diagnosis for GPU/NIC faults, and reserved-node information. Northorne-cluster.md merged the MySQL Service Down alerts from March 28 and March 29. Beloos-cluster.md gained the IBSpeed batch cordon from 2025-11-25, log-data loss, and a gateway setup SOP.

The platform pages received a large set of application and service faults. maraum-platform.md added 7 issues covering 400 login, Quota non-deduction, log inconsistency, invisible Pod logs, secondary Quota, mistaken base-image offlining, and Daisy Adler gateway changes. pexieon.md added 6 issues covering inaccessibility, task submission failure, upgrade login, CLI permissions, multiple-business unavailability, and high Rinenara MySQL usage. rineova-inference.md now records task clearing caused by shared-pool resource occupation on 2026-05-15.

Storage and scheduling interactions were also represented. Xanella-cluster.md now includes a storage stutter case caused by non-NUMA toruantis scheduling that overloaded IB. This gives the wiki another example where workload placement and network pressure contributed to a storage-facing symptom. Overall, the sixth update adds a stronger cross-layer view of compute, storage, network, and platform faults.

## Concepts

GPFS-operations.md was extended with Volcano Cloud DALIANTIS(VEPFS) adaptation, RDMA diagnosis through IBV_WC status codes, CSI-Node upgrade risks, and the defragmentation SOP. node-management.md now includes the node deletion SOP, Kubelet MaxPods configuration, the Oraport resource-offline process, and handling guidance for node RDMA faults. These updates make the concept layer more practical for storage and node lifecycle work.

Process and scheduling documentation also grew in this pass. incident-management.md added cluster change-management rules that cover maintenance windows, approvals, and rollback. scheduling-troubleshooting.md now includes scheduling-component deployment, Umbays scheduling-suite installation, and the Auriga preemption case. auto-provisioning.md was expanded with the detailed halorova automated installation process.

## Comparisons and Queries

network-incident-patterns.md gained new comparison entries for Leaf switch batch port faults, UW QoS faults, Daisy Adler gateway policy changes, and Aurwood IB switch changes. These additions help group network incidents by trigger and affected layer. They also support faster lookup when a new event resembles a past switch, QoS, or gateway-policy issue.

common-platform-failures.md was updated with infrastructure-service fault patterns. The new coverage includes GitLab sidekiq, cororia OOM, replica explosion, LiteLLM misconfiguration, Nexanor-Research P0, and zombie memcg. This gives operators a wider catalog for recognizing platform-side symptoms that may not be tied to a single cluster.

## New Pages

- The sixth update added 4 new entities pages.
- Dorholm-cluster.md now covers the Dorholm cluster, also known as Daisy Adler, with GPFS stutter, inode exhaustion, and the IPoIB expansion SOP.
- Dorfell-cluster.md documents the Dorfell cluster and its production-cluster setup material.
- Tarndale-cluster.md captures the Tarndale cluster, including P1 storage stutter and intermittent storage instability.
- auriga-cluster.md documents Quilridge and the case where high-priority tasks did not preempt.

## Coverage

- About 40 of the 100 new documents had substantial content that was incorporated into the wiki.
- About 35 were brief placeholders, directories, or weekly duty tickets, so they were not created as individual pages.
- About 25 were short incident templates with only timing and handlers, or test documents.
- Brief and test material was merged into the matching pages rather than tracked separately.
- The sixth update emphasized RDMA diagnostics, CSI upgrade risk, resource defragmentation, change-management rules, DALIANTIS Volcano Cloud adaptation, and broader multi-cluster coverage.

## 2026-06-10 — Seventh Incremental Update of 100 New Documents

The seventh incremental pass processed 100 additional Feishu documents and used them to update the wiki. Pelshaw revised existing pages and created new content where the documents added durable operational value. This update changed 16 pages.

A number of cluster pages received storage, network, and acceptance additions. Gemini-cluster.md now covers shared-storage unavailability caused by the GPFS vm.max_map_count 65K limit. pavo-cluster.md added the 2025-12-10 production switch fault that caused IB NIC polling. Xanella-cluster.md gained the 2026-02-26 storage anomaly that led to service unavailability.

maraum-platform.md was updated with 7 fault patterns. The new entries cover scheduling fragmentation, cororia 500, missing Pod monitoring data, pytorchjob logs, nginx worker overflow, inference logs, and EP configuration changes. Marhaven-cluster.md now includes the 2025-09-10 node hard lockup disconnection, plus more detail about time-synchronization service anomalies. Rinenara-cluster.md added the 2025-07-23 CPU quota Pod Terminating blockage and a storage fault from 2026-04-03.

Network and hardware delivery history also expanded. Galholm-cluster.md now records the 2026-04-15 IB switch anomaly that caused port flapping and storage stutter. Bexlink-cluster.md added 256-machine H20X acceptance records covering two acceptance rounds and RoCE toolchains. The same page also gained source material for Yoreux test failures. Beloos-cluster.md was updated with DALIANTIS adaptation, inference-service logs, and the source of platform-release quota display anomalies.

Several pages added implementation, troubleshooting, and access references. Dorfell-cluster.md gained AU Dorfell cluster construction progress records. dalanent.md now includes active_mtu detection requirements, cordon caused by disabled ibgda, the cluster acceptance SOP, and the user development manual. pexieon.md added batch-query 502 on 2026-01-13 and 403 inaccessibility on 2025-12-25. rineova-inference.md now documents inference-service domain access ranges for 11 cluster gateways and adds the inference troubleshooting guide.

## Concepts

scheduling-troubleshooting.md was expanded with scheduler cache resources not being released, idle resource eviction failure, and Verfield Tech-her pool data compatibility. node-management.md added node drain guidance, node release, node-pool removal without deleting nodes, full-disk uncordon failures, and recovered nodes that were not reclaimed. These additions improve coverage for common lifecycle and scheduling cleanup cases.

GPFS-operations.md gained DALIANTIS NFS operations material, including service deployment, common issues, and client mounts. The same page also added a GPFS max_map_count case. incident-management.md now includes cluster change-notification rules that require 48 hours advance notice.

## Comparisons and Queries

network-incident-patterns.md gained Pelwood batch faults, US East Aurwood Leaf switch faults, and IP conflict vSAN patterns. These entries add more examples for identifying repeated network failure modes. They also make Pelshaw easier to compare batch-impact incidents with localized switch or address-conflict events.

common-platform-failures.md was updated with ES shard limit exceedance, Oliiantis release stuck, overseas Zelalos anomalies, and multi-node faults without tickets. This broadens the catalog beyond single-service outages. Pelshaw also captures failure patterns where the operational symptom may appear before a formal incident ticket exists.

## New Page and Coverage

- The seventh update created 1 new entities page.
- Pelwood-cluster.md now documents the Pelwood cluster, including 64-machine scale, 21-machine batch faults, and all multi-machine tasks failing.
- About 35 of the 100 new documents provided substantive wiki content.
- About 40 were very short placeholders, directories, weekly tickets, or incident-set templates and were not created as separate pages.
- About 25 were brief incident templates or test documents.
- Brief and test items were integrated into the appropriate cluster or concept pages.
- The seventh update emphasized DALIANTIS NFS operations, inference-domain access, node drain and release procedures, scheduler cache issues, GPFS tuning, and change-notification rules.

## 2026-06-10 — Eighth Incremental Update of 100 New Documents

The eighth incremental update processed another 100 Feishu documents and converted the usable material into wiki edits. Pelshaw updated existing pages and created new pages where the source set added enough standalone value. Across this pass, 17 pages were changed.

Several cluster pages gained new failure and performance records. auriga-cluster.md now includes log-service unavailability and the platform 503 event from 2026-01-27. Pelwood-cluster.md added the 57-hour training failure caused by disk quota exhaustion, along with Yoreux performance test records. Gemini-cluster.md now documents the XID 94 false detection that caused a 39-node batch cordon on 2025-07-15.

Bexlink-cluster.md was updated with inconsistent resource-pool statistics caused by counting Terminating Pod. Beloos-cluster.md added an inaccessible common-service URL, a 64-node batch reboot, and Oraport node expansion. Rinenara-cluster.md now records the 2025-07-18 DB fault that caused pexieon functional failure. These additions strengthen the link between cluster-level symptoms and platform-visible impact.

The platform and inference pages received a broad set of operational cases. maraum-platform.md added 10 fault patterns, including MaxPods scheduling, maredis release, Doris performance, and inference expansion bypassing quota. rineova-inference.md gained intelligent-routing image pull failure, concurrent port exhaustion, and lux-core-failed. pexieon.md now includes the Junalion scheduled-task anomaly, Rinenara functional fault, cororia shutdown/startup, and Lumgate access fault.

Registry, delivery, and test documentation were also expanded. harbor-registry.md added the Harbor alert SOP, image synchronization SOP, kevloom Harbor db fault, and slow image pulls caused by Nginx contention. dalanent.md gained the internal-field release SOP, the Oraport IBLost false report from 2025-11-07, the ECC XID 94 false detection from 2025-08-15, and the SOLAOS change-triggered cordon. jorvik-cluster.md added a performance test report comparing k8s automatic node ordering with vendor topology-aware ordering.

## Concepts

GPFS-operations.md was broadened with quota administration material for Bexcast61, including operational commands and typical failure cases. The same page now also carries the GPFS client upgrade procedure for moving from 5.37.206.81 to efix8. DNS-operations.md gained notes on the Aurwood BGP incident and the bug where DNS domain records were removed by mistake.

on-call-system.md now records cluster operations duty rules v2.0, tying together SLA expectations, staffing roles, and ownership boundaries. training-task-troubleshooting.md adds a kubectl-based diagnostic flow plus a recurring disk-quota exhaustion pattern. System-9babc39a3e-resource-management.md now covers the large-instance conversion procedure and the priority rules for inventory-instance assignment, while cluster-construction-checklist.md adds NTP synchronization checks and regional configuration checklists for Pelport/Draco/LORORYS.

## Comparisons and Queries

network-incident-patterns.md now captures several operating patterns: the Aurwood BGP issue, brief network timeout bursts, the mar-gw release that left 14 machines unavailable, Oraport IBLost/XID94 false positives, and the SOLAOS dalanent change that led to cordon. NCCL-troubleshooting.md was expanded with a user-task NCCL Timeout handling flow based on Pod log review, and Pelshaw also gained a physical-machine NCCL test procedure. common-platform-failures.md now aggregates more platform cases, including cororia port exhaustion, Doris performance, the Quota zeroing bug, Harbor db and slow-pull symptoms, machine intrusion, Nexanor port exhaustion, network flash interruption, mar-gw, and Wyneon fault statistics.

## New Pages and Coverage

- The eighth update added 2 entity pages.
- toruantis.md now describes the toruantis data acceleration service, its distributed memory cache, component layout, operations notes, and known issues.
- draco-cluster.md now covers Aurholm, with the standard build flow and network prerequisites.
- Of 100 new documents, about 40 had enough material to fold into the wiki.
- About 35 items were placeholders, folders, weekly tickets, or incident-set templates, so they were not split out as pages.
- About 25 items were short incident forms or test files.
- The eighth update merged brief and test material into the relevant cluster or concept pages.
- The eighth update focused on GPFS quota work, toruantis operations, NCCL user triage, dalanent false positives, Harbor operations, inference faults, and security events.

## 2026-06-10 — Ninth Incremental Update of 36 New Documents

The ninth update reviewed 36 additional Feishu documents, refreshed existing wiki content, and introduced new pages where the material justified Pelshaw. In total, 14 pages were changed. Bexlink-cluster.md now includes the 2026-01-24 failure where multi-user log visibility broke because Fluentd ES Host header behavior was incompatible. Bryford-cluster.md adds the 2025-09-05 Scratch storage intermittent IO stutter event, marked P4. Beloos-cluster.md was updated with the 2025-12-22 log-service update anomaly, the 2026-01-29 log query failure caused by a change, and the 2026-02-10 missing RDMA-CNI case.

Xanella-cluster.md now records the 2025-08-04 task errors traced to node memory fragmentation, with Dovnet_memory noted as the fix. Umbeent-cluster.md adds the 2025-11-19 Argo Workflow overload crash attributed to user Clara Hayes. toruantis.md was extended with the 2025-12-08 unreclaimed quota case caused by an fd remaining open after file deletion. pexieon.md now includes the 2025-09-30 service-release offline ticket anomaly. dalanent.md adds the external-field halorova/Umbays deployment procedure, including detailed DaemonSet rollout steps, and rineova-inference.md adds the Oskmarch inference domain while expanding the domain access range table for 8 clusters.

## Concepts

kubeconfig-issuance.md now provides an automated Kubeconfig issuance procedure, using a scripted 3-day validity flow across 4 cluster environments. GPFS-operations.md adds the 2026-03-29 storage outage caused by Inode exhaustion, with mmsetquota listed as the repair action. node-management.md was expanded with node initialization steps for DNS, NTP, Oskgrove team coordination, GPU driver setup, and OFED, and Pelshaw also now includes the halorova instance operations procedure. cluster-construction-checklist.md adds both a dependency project management table for cluster construction and the Terway CNI IP expansion plan.

## Queries and New Page

- common-platform-failures.md now includes the 2026-05-19 cororia host-keys mount gap and Syljunc/Aurstead database issues.
- The ninth update introduced 3 new pages.
- Pelshaw included 1 new entity page.
- Oskmarch-cluster.md now documents Oskmarch in Aurstead/US West, including network-policy enablement, SDK adaptation, inference domain details, and database faults.

## Concepts

The ninth update also introduced 2 concept pages. platform-permissions.md documents Nora Drake platform permission management, covering Norness/Zelalos/Oliiantis user-role handling, cluster authorization, and cleanup of resources for departed employees. quota-exporter-sop.md explains the Quota-Exporter setup flow, including Oliiantis/Helm deployment, new-cluster configuration, and monitoring checks.

## Coverage

- Of the 36 new documents, about 17 contained substantive material that was added to the wiki.
- About 19 were placeholders, directories, tests, or templates, so they were not made into separate pages.
- The ninth update centered on Oskmarch configuration, platform permissions, Quota-Exporter operations, node initialization, external-field dalanent deployment, and inference-domain coverage.