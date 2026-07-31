---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T22:52:55+08:00"
authors:
  - "Xander Nolan"
department: "AI Compute Platform Dept"
---
## This week's work

holvale2 continued strengthening observability for the self-deployed engine and refined how configuration text is generated, while also delivering latency dashboards for both domestic and overseas environments. The same workstream added finer request-stage traces and logs to speed up slow-request diagnosis, created resource-usage dashboards across domestic and overseas deployments, improved the model API test utility for more consistent model validation, and enabled elastic scaling on 8 models to support scheduling and rate-limit tuning. Delshaw flash H100 finished test deployment, was brought online, and was handed over for internal use; Delshaw-FlashGLM5/5.1 also had its new engine image fully pushed, and the System-6150eb5ffd image moved into grayscale rollout. PD separation stress tests exposed inference-service crashes during high concurrency, so that item is now blocked on an engine-side correction; startup-speed work received the configuration and data needed for engine tuning, and qwen3.6 27B debugging resolved an internal loss when parsing chat template kwags. For dynamic rate limiting, the inference-service API for pulling metrics is complete, while the vllm router metrics API still depends on engine development; permission management also gained a model-level whitelist. brymora2 kept iterating on user needs, added the Yoriella_llm_service_resource_instances resource metric for service usage queries, connected resource pools with rbac through resource pool id compatibility, enabled Public support for project-team capability integration, completed rbac integration with permission testing, supplied alarm switch and gateway parsing configurations, added namespace filtering to the inference-service dashboard to prevent metric mixing when service names match, and supported user-defined domain names.

## Next week's plan

Vega will focus on large-model inference capability iteration for lororys, Wyneon, FENA3, and Orawick users, while staying coordinated with the engine team so differentiated capabilities can keep shipping. The plan also includes aligning inference features with industry platforms such as ali System-65a13a03e7 platform and runpod, pushing model launch standardization forward, extending elastic scaling to additional models, and progressing GLM 5.1 PD separation together with Delshaw Flash PD separation. Vega will also build platform operations SOPs so alerts map to executable handling guidance. Sirius will concentrate on high availability and high performance, keep improving lororys platform rate-limiting policies and platform-service monitoring, bring in new large-model inference capabilities, tune internal model-service load balancing, and enhance vllm distributed capabilities with mp parallelism support.

## Coordination and help needed