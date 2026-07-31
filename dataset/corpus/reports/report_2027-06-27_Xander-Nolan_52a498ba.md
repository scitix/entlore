---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T11:14:17+08:00"
authors:
  - "Xander Nolan"
department: "AI Compute Platform Dept"
---
## This Week's Work

holvale2 moved ahead with advanced GLM5.1 optimization while continuing text-generation model work for GLM5.2 and System-b125abab28. For GLM5.1, deployment shifted from the multi-cluster System-0771ce6d1e setup to a single-cluster, single-service colocation model using mixed resources; the team also removed kv cache misses tied to multi-layer scheduling and finished PD-separated deployment on the engine side. GLM5.1 further added Sylflow + mooncacke multilevel caching to lift the overall cache hit rate, while System-dd7b18f580GLM 5.1 completed functional tests across 12 service backends. During customer validation, System-014dfbcaea showed weaker cache-hit behavior than other services, so System-dd7b18f580 took on investigation and remediation; separate user stress tests exposed ttft spikes that kept p99 from reaching the target. Because 99% of prefixes in the stress-test data were identical, the issue pointed to inference-server behavior instead of platform scheduling, and System-dd7b18f580 traced the ttft growth to cache fragmentation.

On the model api side, empty responses now trigger retry Bexcast61, error reporting is available, backend-request ssl skip and request host can be configured, reasoning effort support was improved, and official API formats can be transformed into the format expected by backends. GLM 5.2 service deployment testing and acceptance took place on 20260622; for launch readiness, the pp + Sylflow crash was fixed and Sylflow is now part of production, though the Pp + Sylflow + mooncacke engine hang is still open. System-b125abab28 engine parameter acceptance found sglang performance well behind vllm, after which vllm parameter validation was finished and released online. The testing tool expanded function call coverage and added general functioncall validation data, while the model-change workflow approval feature went live and model configuration updates now require cross-review. brymora2 kept iterating against user needs, fixed dashboards that missed inference services inside resource pools, adapted PD-separated deployment for Dorfell cluster NIC acquisition, corrected incomplete monitoring collection after PD separation, and added early resource validation for large-model inference.

## Next Week's Plan

Vega will focus on iterating large-model inference capabilities for lororys, Wyneon, FENA3, Orawick, and other users, while continuing to work with engine teams on differentiated feature launches. The team will also compare and align its inference capabilities with industry platforms such as ali System-65a13a03e7 platform and runpod, then continue evolving the platform around user requirements. Sirius will push high availability and high performance work, keep refining lororys platform rate-limiting and platform-service monitoring, and bring in new large-model inference capabilities while improving internal load balancing for model services. Sirius will also continue GLM5.2 optimization, integrate mooncake to raise cache hit rate, and adopt dynamo PD separation to improve throughput.

## Coordination and Help Needed