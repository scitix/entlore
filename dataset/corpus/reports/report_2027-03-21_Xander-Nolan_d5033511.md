---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T22:49:03+08:00"
authors:
  - "Xander Nolan"
department: "AI Compute Platform Dept"
---
# This Week's Work

Sirius finished the biweekly model-service refresh, covering new model onboarding, stability work, idle-model cleanup, and better resource use. Engine image testing moved ahead, with sglang 0.5.9 umborantis and 5090 sglang 0.5.9 still awaiting validation. On 5090 vllm 0.17.0, mtp OOM and nvfp4 not taking effect were both observed, and the engine-side fix is still pending verification.

GLM 5 bf16 deployment is under validation, but tp 16 currently fails to start because of graph captrue errors. For qwen3.5 122B on 5090, ttff reached 40s and tpot reached 400ms, leaving Qwen/Qwen3.5-122B-A10B close to unusable. The qwen3.5 35B 5090 rollout ran out of memory with mtp enabled, then served normally after mtp was turned off; Qwen/Qwen3.5-35B-System-fc7c4870ff was broadly usable aside from ttft 10s.

System-bd16ce38d0 gpt oss 120B was migrated to 5090 deployment and expanded to 100 replicas for Iris Otis's request. System-abef9091c8 began timing out or returning 502 above 50qps, and the gateway side confirmed the problem was ingress-related. The plan for System-abef9091c8 is to move to nodeport and separate control traffic.

Incorrect overseas gpt 120B responses were traced back to a umborantis engine defect, and switching to an open-source version resolved the issue. System-9a2ab69d97 had abnormal restarts because dp + ep overflowed GPU memory during heavy load. After the setup changed from dp + ep to tp + ep, those abnormal restarts stopped.

Qwen/Qwen3.5-397B-A17B has been launched, but requests concentrating on the same node are driving very long e2e time. Once intelligent routing is available, Qwen/Qwen3.5-397B-A17B will move to that routing path. Separately, shutting down models with no traffic freed 16 h20 cards, 124 h20x cards, and 12 L40 cards, while current online services are using 590 h20 cards, 608 5090 cards, and 63 L40 cards.

For api.vexeum.ai, the shutdown list included qwen2-5-72b-instruct on 8 h20x, qwen3-Fenhaven-2507 on 4 h20x, glm4.6 on 32 h20x, kimi-System-2b9f5c895e-thinking on 64 h20x, and glm-4-6v on 16 h20x. For api.maraum.cn, the list covered gpt-oss-120 on 16 h20 cards, medgemma-27b-text-Pelshaw on 4 L40 cards, and qwen3-8b on 8 L40 cards. Overseas GLM 4.7 was also taken offline.

@Xander Nolan is validating the Glm 5 pd separation configuration to optimize model-service startup. The earlier Glm 5 pd separation transfer did not use ib, so @Xander Nolan is changing Pelshaw to ib and validating that path. @Xander Nolan is also checking whether the non-ib transfer introduced any performance loss after PD separation.

Vega’s biweekly work focused on improving platform inference capabilities while supporting business needs. The team completed vllm/sglang router backend testing for intelligent routing, finished frontend-backend integration, and launched Pelshaw. Vega also released custom dashboard functionality, updated the user manual, added the busy pod metric to the inference service dashboard, and improved inference service events with action events and more detailed messages.

Vega completed frontend and backend integration for inference service events and launched the capability. umborantis platform integration with kv cache support is still in development and has reached 90% progress. The remaining launch dependency is the open-source vllm 0.17.0 release.

Vega fixed ineffective environment variables and mounts that had been breaking nccl communication, including the system-level cases that affected distributed inference. The team also resolved expansion failures caused by configuration changes while expansion was queued, corrected resource mismatches after post-expansion updates, changed service warning messages from error to info to reduce unnecessary alerts, and improved enum values in the large-model inference documentation.

The vllm/sglang router now supports intelligent routing, with backend testing completed. Vega has handed the router prototype and interfaces to frontend, and frontend scheduling is still pending. Large-model inference event categories were adjusted, action events were added, detailed messages were improved, and the updated event prototype has been aligned with frontend while waiting for scheduling.

Vega still needs to launch the open-source vllm 0.17.0 inference engine. The team also investigated why Wyneon user kv cache metrics were not displayed. The finding was that cache was not enabled, leaving every metric at 0 and making hit rate calculation impossible.

# Next Week's Plan

Vega plans to keep iterating large-model inference capabilities for lororys, Wyneon, FENA3, and Orawick users. The team will continue coordinating with the engine side to release distinctive features, compare inference capabilities with industry platforms such as ali System-65a13a03e7 platform and runpod, and launch kv cache capabilities. Vega also plans to optimize inference prefill, improve service alerts and dashboard functions, and optimize resource dashboard s3 loading.

Sirius will focus next week on both high availability and high performance. Planned work includes further improving lororys platform rate-limiting policies, strengthening platform service monitoring, integrating new large-model inference capabilities, and optimizing internal load balancing for model services. Sirius also plans to migrate models to h100 and continue offline evaluation optimization.

# Coordination and Help Needed

No coordination is requested right now. No help is needed at this point.