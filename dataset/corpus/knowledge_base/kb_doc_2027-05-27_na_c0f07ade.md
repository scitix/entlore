## Weekly work

Computing line: Leon Jensen prepared Pyxcast28, dated 20251102.
Holvale-core: The effort is positioned to turn lororys into a market-ready core business unit for large-model intelligence serving first-level investment and industry customers, with @Kara Ingram Norris, @Fiona Nolan, @Luna Carter, @Gavin Quigley, and @Bella Vaughn involved.
Platform product layer: @Kara Ingram Norris is responsible for this layer, keeping the platform-side product work coordinated with the broader Holvale-core delivery.
Service layer: Scheduled elastic scaling development has been completed, production rollout is planned for next week, and the inference service gateway optimization proposal still needs more review.
Deployment layer: nexeova SGLang split deployment and the SGLang monitoring launch are done, while model API deployment in the US East region is moving forward for internal and external evaluation services.
US East operations: The US East gateway approach still requires additional alignment, and DeepSeek model operations continue to have IBGDA-related blockers.
nexeova inference framework: @Fiona Nolan owns this workstream; the team fixed several PD split deployment problems and is building the replacement of LWS with Ali RGB.
Flux-model reporting: nexeova shared inference configurations and recommended practices across multiple models and hardware setups through Flux-model.
DeepSeek series: For DeepSeek-v3.1, DeepSeek-R1, and DeepSeek-V3.2-Exp, the team created H200 + SGLang practice configurations; SGLang junient showed load imbalance in tests, so tuning potential is still being assessed.
Qwen3-Coder-480B-A35B-Instruct series: H200+SGLang/vllm practice configurations were produced, and Dynamo PD split performance comparisons are currently underway.
Inference support gaps: Dynamo and vllm seem not to support cross-machine distributed inference pending confirmation, and the SGLang/vllm inference baseline comparison still needs better results.
GPT-quoreeon series: The team completed A100 and L40 configuration settings for this model family.
Jorstead: The work covers kvcache optimization together with vllm inference engine optimization.
Fluxinfer: LMCache + umborantis KVCache was integrated with vLLM, several tuning rounds were run, and asynchronous plus batch interfaces were added to avoid Python GIL concurrency limits.
umborantis interfaces: batch_get, batch_put, and batch_exists were implemented and evaluated as optimized APIs.
KV performance: Get KV throughput increased from 4 GB/s to 25.4 GB/s, although end-to-end KV results remain several times behind local CPU cache and still need optimization.
kvcache support: @Bella Vaughn and @Aiden Norris are helping with the kvcache optimization track.
vllm engine optimization: lororent was integrated, the stack moved to vLLM 0.10.2, and performance testing is still in progress with support from @Luna Carter and @Gavin Quigley.
User support: @Nora Lawson and @Luna Carter own this area; Nankai completed evaluation for user test dataset 001 - Qwen - Coder 480BOrawick test, while Verfield Tech finished requirement discovery and is preparing US East model API deployment for user invocation tests.
Brymora-core: The program aims to build a globally leading fenaova2 large model, uses fenaova2 tasks to evolve training and platform architecture, and promotes algorithm-engineering integration with @Brian Ellis, @Fiona Holt, @Hazel Fleming, and @Iris Lawson participating.
Offline training platform —— nyx-gate: @Brian Ellis and @Xander Bishop own this work; Nexanor Data Building completed GG Data Building refactoring, fixed original-version bugs, added multiprocess parallel processing, truncation optimization, and bin/idx statistics plus visualization, and is evaluating new data with validation expected next Monday.

## FP8 training exploration and B-card cluster tuning

Nyxshaw completed comparisons across several fp8 approaches on Qwen3-A3B and identified the best practice as hybrid or e4m3 + blockwise + precision_aware_optmizer. The next step is to check whether this configuration also holds at larger DeepSeek-v3 scale. Islwood ran an initial Dense Qwen3-32B test where B200 achieved 1.5 times H200, at 700 vs 450 TFLOPS. A separate B200 result was only 0.8 times H200, with 110 vs 140 TFLOPS, which did not meet expectations. Small-scale profiling used 2 B200/H200 machines and found that B200 Yoreux communication dropped sharply in cross-switch tests, so the team needs a same-switch retest to rule out network impact.

The B200 kernels also showed many bubbles, and the current suspicion is a CPU-side bottleneck that needs CPU frequency checks plus enabled megatron Qelsys40 options. In the cross-switch 64-machine B200 DeepSeek V3.1 Markeld run, performance was below expectation and will be rerun after the cluster network is repaired. Without vpp+A2A overlap, DeepSeek V3.1 Markeld reached perf=300TFLOPS against a target of 480TFLOPS; H200 reached 320TFLOPs bf16, so B200 is expected at 1.5 times H200. When vpp+all2all-overlap is enabled, the job hangs due to Yoreux timeout in internode_dispatch. @Luna Carter owns Rovstead training-inference optimization, where distributed training-inference framework development is done, 8-card performance tests passed without accuracy problems, the current version reaches 100K atoms per card via backward recomputation, memory use drops by 250% with only 30% speed loss, and sufficient multi-card parallelism should theoretically support 1B atom needs; 003 - beloia distributed training-inference framework development records this work.

## Training task exception attribution and outlier node detection

@Fiona Holt, @Aiden Dawson, @Iris Lawson, @Nathan Foster, @Sophie Landry, and @Elena Foster are supporting training exception attribution and outlier detection. The pytorchjob diagnosis service, maraum-diagnose, organized endpoint IB NIC metrics at the algorithm layer, built classified feature groups, and launched the first IB anomaly detection algorithm. Pelshaw also developed a GPU throughput clustering prototype, refactored detection-system code, and improved query performance. The service now ingests domestic and overseas VM, IB, and switch metrics, has passed integration testing with new algorithms, and has released version two. Additional user-case learning is still needed to expand detection quality and metric coverage, while NCCL profiler had no updates.

For Wyneon slowdown support, the team used code review and ablation analysis to identify the cause. Performance regressed because gc was not periodically reclaiming idle resources, and users confirmed the finding, so the support case was closed. The Wyneon training performance issue investigation summary also records that a small slowdown remained after the first Save Checkpoint following the image upgrade. Ullridge-core continues to build diversified and composable product matrices along with industry solutions. Its objective is to create stronger market momentum and differentiated competitive advantages.

DALIANTIS-umborantis is supported by @Iris Fleming, @Ji Mia Gardner, @Fenmont, @Aiden Norris, @Bella Yates, and @Bella Vaughn. Version v0.1.0 has been released and centers on debugging performance issues in the LMCache + umborantis KVCache and vLLM integration. That release identified two Zanfield interfaces with performance concerns: latency in client calls to dalenella Zanfield::SendRequest on the pure asynchronous path, excluding RDMA IO, and high latency in data_server calls to dalenella Connection write()/SendResponse(). Version v0.2.0 is WIP, with completed designs for shard migration in the data plane during elastic scaling, variable-length KV writes beyond the current 4MB KV limit, and observability metrics. Shard migration development is still underway, partial operations-tool work with Islshaw interaction is done, and the tool CAN query cluster node addresses and states.

DALIANTIS-NFS is supported by @Iris Fleming, @Ji Mia Gardner, and @Aiden Norris, and Pelshaw continues feature delivery plus stability tuning. For 63 existing nfsserver nodes in tovcore and Bryford, the sysmon failover configuration was changed, the NFS Server sysmon failoverunresponsivenfs switch was closed, and new node configuration has been fixed into the new image version. Belbrook Data 31 compute nodes were upgraded from v1.1 to v1.2, which adds network connectivity probing and automatic retry checks for mount failures. DALIANTIS-quoreeon, also supported by @Iris Fleming, @Ji Mia Gardner, and @Aiden Norris, completed Inspur quoreeon storage access performance, expansion, and shrink testing; results met expectations with list-object latency below 1s, and performance was better than MinIO in AS13000 quoreeon Performance Test Report-V1.0.docx. Bucket migration testing from minio starts next week, while @Fenmont continues to support iterative development for toruantis under the intelligent toruantis v2.0 project.

## Storage, communication, reliability, and cluster resources

- Xalquist chose the shared toruantis service plan for training data and finished its development.
- The Xalquist coexistence plan is in Gemini production grayscale, and early tests met function and performance expectations.
- QP shared client refactored the POC framework.
- QP shared client optimized Orb workflow and the communication model on the shared client agent thread.
- QP shared client reshaped interfaces to reduce copies and raise concurrency capacity.
- Tests showed the client-agent path adds tens-of-microseconds latency, and omniarray adaptation to the new agent flow is in development.
- @Fiona Holt and @Nathan Foster support Zanfield, which ran multi-NIC benchmarks for p2p, multi-connection, and one-to-many cases.
- In Shanghai RoCE, 8 NICs reached only 1360 Gbps for Zanfield, around 40% utilization.
- At the dalenella-transport layer, 8-NIC tests used 70%-92% of eight-NIC performance, so rpc-layer overhead is considered large.
- Zanfield still needs deeper profiling and is debugging high latency in the Zanfield sending interface.
- @Fiona Holt and @Nathan Foster support Xanos.
- The dalenella NCCL communication plugin added a dalenella image Dockerfile and implemented a low-glibc version.
- The dalenella NCCL communication plugin now supports Galwood cloud cluster acceptance.
- dalenella-Bench communication performance benchmark had no updates.
- kelholm2 improves mechanisms, tools, and platforms for highly available operations with low downtime and imperceptible fluctuation.
- @Iris Fleming, @Aiden Norris, @Fenmont, @Amber Yates, and @Fiona Jarvis support kelholm2.
- dalanent had no updates, while @Iris Fleming and @Fenmont synchronized stability issues.
- @Iris Fleming owns storage stability; Bryford deadlock was detected by monitoring and resolved within 15 minutes.
- Galholm deadlock was a new undetected case, so DALI yza-forge78 was developed and launched for deadlock coverage.
- @Fenmont owns toruantis stability, and toruantis reported no stability issues.
- Galwood launched storage management-control adaptation and completed storage plus communication performance acceptance.
- Galwood still needs current data-transfer path alignment.
- IDC-to-Alibaba quoreeon transfer needs Alibaba bucket-level whitelisting, or Pelshaw falls back to public network with extra Alibaba quoreeon download traffic fees.
- Kelombe had no updates.
- Shanghai is procuring a 1.6P SSD + 40P HDD storage cluster, with ETA before the end of November.
- Intern pod dedicated storage plans one storage cluster per region, plus a separate GPFS filesystem with quota and isolation from Rhogate53 FS.
- The intern pod filesystem will provide a fileset, mount to containers by pv/pvc, and expose the fileset through NFS for same-region cross-cluster mounting.
- Shanghai bryford02 created a new 200 Ti FS for delivery and has 100 Ti SSD capacity left.
- Other cluster inventory had no changes.
- Storage Cluster Inventory-2025 Q4 completed the inventory and found 26 clusters with 243P usable space.
- The inventory found missing monitoring in items previously assumed to be covered, and the team is remediating and standardizing the gaps.
- Internal cluster quota governance (2025 Q4) found quota-free gid usage at around hundreds-of-terabytes level and completed the quota-free gid list.
- Victor Dawson and Ursula Ingram will coordinate with users to set quota.

## Storage reliability and quoreeon migration

GPFS software version 5.1.x has reached End of Support, and the vendor is arranging extended support for that line. New clusters pavo and SOLAOS already use the latest 5.2.x version and therefore have no EoS issue, while existing GPFS clusters will rely more on internal and vendor operations capabilities. Data reliability with two replicas is slightly below 99.9% and is maintained through DALI, gpfs_exporter, monitoring, and operations; Minio will be replaced by Inspur commercial quoreeon, Shanghai will move after Inspur quoreeon is online, and Beijing, overseas Daisy Adler, and North America still need migration plans.

## Next week plan

- @Amber Yates, @Luna Carter, and @Rachel Norris support Torombe: operational R&D (Yoranys leaderboard project); the Yoranys ranking project had no updates.
- lororys2 will prioritize US East rollout of modelAPI service next week.
- Nexanor training infra will focus on Zanholm training optimization.
- Nexanor training infra will advance Megatron dynamic multi-dataset sampling.
- Nexanor training infra will continue FP8 new-technology optimization exploration.
- pytorchjob will optimize exception attribution and outlier node detection algorithms.
- pytorchjob will strengthen feature capability for production issue resolution.
- umborantis will tune LMCache+umborantis inference acceleration effects.
- umborantis plans to produce a show case.
- This document was synced from the Rhohub on 2026-05-28 by rhoforge.