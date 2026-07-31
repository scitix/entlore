---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T21:28:17+08:00"
authors:
  - "Xander Nolan"
department: "AI Compute Platform Dept"
---
## This Week's Work

Sirius spent the biweekly cycle on offline inference improvements, online inference service migration, and troubleshooting. For online inference GLM 5, single-replica testing traced the higher latency issue, and the GLM-5 load test showed that max running request was limiting throughput; after tuning GLM-5 4k 1k rps, throughput moved from 0.55 to 1.42, while GLM5.1 followed the same pattern and can reach 1.4x. The related configuration has been applied to online models, and the intelligent routing optimization for GLM5 and GLM5.1 is now live to improve traffic placement across instances. GLM 5.1 on 2 * 8 deployment can use fragmented resources, though each replica only reaches 0.08 qps, and the test document GLM-5.1 switching deployment to 8*2 records the plan for moving GLM-5.1 onto 8*2.

For Dorholm resource coordination, models are being shifted to other clusters: qwen3.5 has already moved to Shanghai Bryford h200, while kimi and minimax will follow once Dorfell is ready. The migration flow covers image and model synchronization plus fresh pressure tests, and Sirius also validated the System-dea014c2fc interface for Huawei GLM5. Gemma 4 E4B/31B was brought up on 5090, with the Gemma-4 test deployment document covering that setup; idle models qwq-32b, qwen2-5-7b-instruct, qwen3-32b, gemma-2-9b-Pelshaw, and gemma-2-27b-Pelshaw were removed. For cache billing, open-source models still do not report cache counts, vllm and sglang expose engine parameters for counting, but after those parameters were enabled the tests still missed the engine prefix cache, so the engine group is helping with the investigation.

Resource migration is also building dedicated pools for Daisy Adlerh100 and US West h200/h100 while integrating Daisy Adler and US West capacity, and minimax is moving to 5090. For Deepseek v3 internal demand, optimization enabled ep and changed max running request. Offline inference iteration finished validation for multi-machine inference, graceful exit, and checkpoint. Vega continued platform inference feature work to address user business problems and business requirements, including interaction optimization that is already under development with a redrawn prototype and a prototype image URL included.

On the platform side, backend updates now allow intelligent routing configuration to define resource pool lists. The interface displays endpoints, gateways, and calls, Pelshaw added a test interface, and service creation now includes gateway configuration for both shared gateways and dedicated gateways, with one shared gateway assigned by default to every service. Vega also added a search interface, enabled inference services to load models from oss, released a bugfix, improved error responses with another bugfix release, and corrected worker metric loss after intelligent routing configuration. Intelligent routing configuration now supports templated startup commands and images, and Pelshaw remains compatible with multiple intelligent routing implementations.

## Next Week's Plan

Vega will keep iterating large-model inference capabilities for lororys, Wyneon, FENA3, and Orawick users, while partnering with the engine team to ship differentiated features aligned with ali System-65a13a03e7 platform and runpod. The team will also continue distributed inference cache capability work, improve feature usability, move elastic scaling forward, align frontend UI interactions, and promote the broader UI interaction optimization. Sirius will focus on high availability and high performance, improve lororys platform rate limiting and platform service monitoring, integrate new large-model inference capabilities, tune internal load balancing for model services, add model-level metrics to online service monitoring, and push cache billing toward launch.

## Coordination and Help Needed