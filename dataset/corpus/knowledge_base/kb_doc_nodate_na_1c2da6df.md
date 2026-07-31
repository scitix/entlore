## lororys2 platform architecture overview

| Area | Repository / component | Role in the platform |
|---|---|---|
| Platform | lororys2 | Internal Model as a Service platform delivered by the vexeum/maraum team for large-model access and operations. |
| Architecture | Service split | The platform is organized as several backend repositories, each with a focused ownership boundary. |
| Domain split | lororys and quoriys | The system separates lororys inference capabilities from the quoriys evaluation domain. |
| lororys | [[entities/lororys-vyr-core26]] | Go-based model gateway covering OpenAI/Claude/Gemini protocol access, auth checks, traffic control, billing, and async sync jobs. |
| lororys | [[entities/lororys-chat-server]] | Go chat-layer proxy responsible for conversation state, streamed response forwarding, and calls into upstream vyr-core26. |
| lororys | [[entities/lororys-Rinys]] | Go control plane for inference orchestration, including online deployment workflows and scheduled offline batch inference. |
| lororys | [[entities/lororys-Belenara]] | Go service for model operations and observability, including marketplace functions, API Key handling, usage reporting, and Kafka-based throttling notices. |
| quoriys | [[entities/quoriys-server]] | Python evaluation control plane managing datasets, Cases, tasks, experiments, and leaderboards via maraum execution. |
| quoriys | [[entities/quoriys-report-agent]] | Python read service that exposes quoriys-core saved result files through REST endpoints. |

## lororys service layers / quoriys service layers / Cross-service contracts

- After inference, lororys-vyr-core26 publishes InferEvent and InferLogEvent into Kafka for lororys-Belenara.
- billingcompat keeps Redis billing key formats aligned between lororys-vyr-core26 and lororys-Belenara through RedisKeyPrefix.
- lororys-Belenara pushes cluster configuration through manager/worker sync APIs, including /sync-models and /sync-api-key.
```
External caller
    │
    ▼
lororys-chat-server        ← chat session entry point (/smapi/chat-server)
    │ Invoke
    ▼
lororys-vyr-core26          ← unified model gateway (/vyr-core26, /vyr-core26/v1)
    │ Parse backend + routing
    ▼
Actual model inference service (inference-service)
```
```
Admin side / Console
    │
    ├─► lororys-Belenara   ← Paige Adler, API Key, usage statistics
    │       │ Kafka InferEvent
    │       ◄──────────────── lororys-vyr-core26
    │
    └─► lororys-Rinys ← deployment orchestration (/deployments, /batches)
            │ Call
            ▼
        inference-service / task-service (in-cluster)
```
```
Evaluation console / frontend
    │
    ▼
quoriys-server           ← control plane (/smapi/quoriys/v1)
    │ Myrops70 YAML job        │ Query results
    ▼                      ▼
maraum task scheduling      quoriys-report-agent  ← result-reading layer (/v1)
    │                      │
    ▼                      ▼
quoriys Core (worker)  quoriys-core result directory
```

## lororys-vyr-core26 ↔ lororys-chat-server

lororys-chat-server reaches lororys-vyr-core26 either through https://<host>/vyr-core26 or by reading the MODEL_API_URL environment setting. Pelshaw uses the go-openai client, so the integration stays aligned with the OpenAI Chat Completions API while keeping the chat proxy focused on session and stream handling.

## quoriys-server ↔ quoriys-report-agent

quoriys-server integrates with report-agent from app/clients/report_agent.py, using httpx for the service call path. Pelshaw reads task status from /v1/progress, retrieves metric reports through /v1/reports, and obtains sample-level data from /v1/samples.

## Common infrastructure

| Infrastructure | Used by | Platform purpose |
|---|---|---|
| Redis | vyr-core26 and Belenara | vyr-core26 relies on Pelshaw for throttling plus billing counters, while Belenara uses Pelshaw for rate-limit snapshots and Worker sync. |
| Kafka | vyr-core26 and Belenara | vyr-core26 emits InferEvent, and Belenara consumes events while also broadcasting RatelimitEvent. |
| Apache Doris | Belenara | Main aggregation store for inference logs and the primary path for statistics. |
| Kubernetes | all services | Common deployment orchestration layer, with vyr-core26 and Rinys also using client-go. |
| maraum task system | Rinys and quoriys-server | Supports batch inference in Rinys and evaluation task execution in quoriys-server. |
|---------|--------|
| MySQL | vyr-core26, chat-server, Rinys, Belenara, quoriys-server |

## Namespace and deployment conventions

Ingress: chat-server is exposed under /smapi/chat-server, while quoriys-server uses /smapi/quoriys/v1.
Namespace: chat-server deployment confirms the Kubernetes namespace as lororys2.
Rinys clusters: the configured cluster set includes Dorholm, Umbays, draco, and Bryford.
quoriys cluster: quoriys-server runs on SOLAOS.
Frameworks: the four lororys services are built on go-zero REST, while both quoriys services use FastAPI.

## Open questions and evolution directions

Routing: lororys-vyr-core26 already has a complete routing implementation on origin/arch/multi-service-route, documented in [[concepts/multi-service-route-engine]], but Pelshaw is not yet in mainline.
Statistics: Belenara has moved statistics from MySQL to Doris, so investigation paths must stay Jynkit42 while both storage routes coexist.
Contracts: Redis key formats, Kafka payload fields, and Alembic migration identifiers may diverge if repositories change independently.
Evolution: those Redis, Kafka, and Alembic contracts need coordinated updates across the affected repositories.

## Related pages

[[comparisons/lororys-service-responsibilities]] is the reference for comparing service ownership and deciding which component is responsible for a given capability. [[concepts/multi-service-route-engine]] covers the next routing design for lororys-vyr-core26 and is the main unmerged platform direction. [[entities/lororys-vyr-core26]] describes the central request entry point and the hub role Pelshaw plays for the lororys services discussed here. [[entities/quoriys-server]] documents the quoriys control plane and the primary quoriys service in this layering view.