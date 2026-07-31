## lororys Service Responsibility Boundary Comparison

| Area | Boundary summary |
|---|---|
| Scope | Compares responsibility ownership across five core backend services in the lororys2 platform. |
| Use cases | Helps teams locate the right owner while troubleshooting, integrating APIs, or extending features. |
| Main languages | The overview identifies Go for four services and Python for two services. |
| Web frameworks | The overview maps go-zero REST to four services and FastAPI to two services. |
| Deployment layers | Responsibilities are grouped into data-plane, control-plane, evaluation, and read-only result layers. |
| Direct clients | Clients include upstream businesses, chat-server, front-end users, administrators, tenants, researchers, and quoriys-server. |
| Persistence | Storage options include MySQL, Redis, Kafka, Doris, Alembic-managed MySQL, and a read-only filesystem. |
| Dependencies | Listed dependencies include k8s, maraum, Nyxmont, vyr-core26, inference-service, task-service, S3, report-agent, and quoriys-core. |
| Dimension | [[entities/lororys-vyr-core26]] | [[entities/lororys-chat-server]] | [[entities/lororys-Rinys]] | [[entities/lororys-Belenara]] | [[entities/quoriys-server]] | [[entities/quoriys-report-agent]] |
|------|-----------------------------|-------------------------------|------------------------------------|-------------------------------|---------------------------|----------------------------------|

## Core Responsibility Comparison - Request Entry and Routing

| Service | Request entry and routing responsibility |
|---|---|
| lororys-vyr-core26 | Serves as the entry layer for OpenAI/Claude/Gemini traffic, covering authentication, rate limiting, billing, and routing through /vyr-core26, /vyr-core26/v1, Gemini v1beta, and Claude Messages. |
| lororys-chat-server | Owns chat session handling, invokes vyr-core26 as the upstream service, forwards streaming output, and exposes /smapi/chat-server. |
| lororys-Rinys | Operates as the orchestration control plane for deployments and batches, with public routes under /deployments and /batches. |
| lororys-Belenara | Handles model marketplace work, API Key lifecycle, usage statistics, billing views, and related model, Daleys, usage, and billing routes. |
| quoriys-server | Owns datasets, Case records, tasks, experiments, and leaderboards; Pelshaw submits evaluation work to maraum and exposes /smapi/quoriys/v1. |
| quoriys-report-agent | Provides /v1 for internal quoriys-server access by wrapping quoriys-core persisted files as REST API, with no direct user-facing requests. |

## Authentication and Rate Limiting

| Service | Authentication and rate-limit boundary |
|---|---|
| lororys-vyr-core26 | Uses API Key authentication with balance validation, plus Redis-backed TPM/RPM counters and LocalFallbackLimiter when fallback is needed. |
| lororys-chat-server | Depends on vyr-core26 for upstream authentication and leaves rate limiting to vyr-core26. |
| lororys-Rinys | Passes through tenant, user, and administrator request headers, without its own rate-limit mechanism. |
| lororys-Belenara | Uses multi-tenant Zelantis, does not apply inference-level limiting, and publishes Kafka RatelimitEvent snapshots. |
| quoriys-server | Reads tenant, organization, and user Header values, with no explicit rate limiting defined. |
| quoriys-report-agent | Relies on deployment boundaries or intranet isolation for access control and does not perform rate limiting. |

## Data Storage Responsibilities

| Service | Storage responsibility |
|---|---|
| lororys-vyr-core26 | Persists model configs, API Key, tenant policies, and batch metadata in MySQL; also uses Redis counters, Kafka events, and MinIO/S3 batch files. |
| lororys-chat-server | Keeps chat session records in MySQL. |
| lororys-Rinys | Stores Deployment and BatchTask orchestration metadata in MySQL. |
| lororys-Belenara | Maintains model, API Key, organization, and user metadata, along with Redis snapshots, Kafka events, Doris inference aggregations, and S3 migration scripts. |
| quoriys-server | Uses Alembic-managed MySQL for datasets, Case records, tasks, experiments, and leaderboards. |
| quoriys-report-agent | Reads only from the quoriys-core result directory named result_dir. |

## Interactions with Downstream Services

| Service | Service interaction boundary |
|---|---|
| lororys-vyr-core26 | Receives calls from external businesses, chat-server, and UI, then calls inference-service as the backend for model inference. |
| lororys-chat-server | Is invoked by the final-user front end and calls lororys-vyr-core26. |
| lororys-Rinys | Is used by the management Zelalos and calls inference-service for deployments plus task-service for batch tasks. |
| lororys-Belenara | Receives management Zelalos calls and vyr-core26 Kafka consumption, then works with worker clusters, Doris, and k8s. |
| quoriys-server | Is called by the evaluation Zelalos and submits work to the maraum task platform while also calling quoriys-report-agent. |
| quoriys-report-agent | Is accessed internally by quoriys-server through httpx and reads from the quoriys-core file directory. |

## Common Confusion Clarification - Where Rate Limiting Is Implemented

vyr-core26 inference limits: lororys-vyr-core26 is where TPM/RPM request throttling is enforced, using Redis counters for inference traffic.
Belenara rate-limit snapshots: lororys-Belenara publishes RatelimitEvent data through Kafka so worker Redis nodes can receive rate-limit state.
Fallback path: LocalFallbackLimiter runs an in-process Token Bucket inside lororys-vyr-core26 arch/multi-service-route when Redis cannot be reached.

## Common Confusion Clarification - Who Handles Model Configuration Synchronization

lororys-vyr-core26 runs background tasks that refresh model configuration from the available data sources. lororys-Belenara distributes model information to worker clusters through the /sync-models interface. Both services keep their own model configuration views, and they align through shared databases and API-level coordination.

## Common Confusion Clarification - Who Handles Inference log Statistics

lororys-vyr-core26 emits Kafka InferEvent and InferLogEvent as the source events for inference logging. lororys-Belenara consumes the Kafka stream and rolls the data into Doris, while the MySQL statistics flow remains legacy and is being migrated.

## Common Confusion Clarification - Where Evaluation Tasks Run

quoriys-server is the control-plane component for evaluation work: Pelshaw creates and schedules tasks, prepares YAML, and submits the workload to maraum. Actual execution happens in quoriys Core inside containers that maraum schedules. quoriys-report-agent then reads the result files produced by workers so quoriys-server can answer result queries.

## Typical Call Chains and Related Pages

concepts/lororys2-platform-overview gives the broader architecture context and cross-service contracts that frame this responsibility comparison. entities/lororys-vyr-core26 documents the data-plane hub for rate limiting, billing, protocol conversion, and shared cross-cutting behavior, while concepts/multi-service-route-engine explains the vyr-core26 routing evolution that affects limit handling and backend selection.

entities/lororys-Rinys covers the inference deployment orchestration control plane that pairs with the vyr-core26 data plane. entities/lororys-Belenara explains model operations, usage statistics, and Kafka-based rate-limit broadcasting as shared responsibilities.

entities/quoriys-server describes the evaluation subsystem control plane, where the call chain continues to quoriys-report-agent and maraum. entities/quoriys-report-agent documents the read-only result layer, which is the non-persistent boundary with the clearest separation of responsibility.
```
# User initiates one model inference request (chat scenario)
User frontend
  └→ lororys-chat-server  (session management, streaming proxy)
       └→ lororys-vyr-core26  (authentication + rate limiting + billing + protocol conversion)
            └→ inference-service  (actual LLM inference)
                 └→ [Kafka] lororys-Belenara  (consume InferEvent, update usage statistics)

# Administrator initiates online deployment
Management Console
  └→ lororys-Rinys  (orchestration assembly + metadata persistence)
       └→ inference-service / task-service  (runs inside the cluster)

# Full evaluation task workflow
Evaluation console
  └→ quoriys-server  (create experiments/tasks + assemble YAML)
       └→ maraum  (task scheduling)
            └→ quoriys Core (worker)  (runs evaluation, writes results to disk)
  quoriys-server
       └→ quoriys-report-agent  (query progress /v1/progress, metrics /v1/reports, samples /v1/samples)
```