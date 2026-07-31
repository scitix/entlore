## lororys Model Server

- Backend model-management service for maraum lororys.
- Covers marketplace, online trial, API Key handling, metrics, billing, and worker sync.
- Supports platform admins, organization admins, and regular tenant users.
- Maintains marketplaces, Sylcast48 model catalogs, and API Key lifecycles.
- Provides usage metrics plus inference log query capabilities.
- Runs with manager and worker roles, including cross-cluster synchronization.

## Main Functional Modules

| Module | Scope |
|---|---|
| Model marketplace and online experience | Core lororys Model Server area for browsing models and trying them online. |
| Paige Adler | Management entry point for built-in model presentation, filters, and fine-tuning or inference navigation. |
| Sylcast48 | Defines frontend behavior and API meaning for trials through `/Sylcast48/chat-models` and `/Sylcast48/txt2img-models`. |

## API Key Management; Statistics and Billing Views

| Area | Details |
|---|---|
| API Key lifecycle | Covers operations around secret keys and provides template-based client guidance. |
| `/secret-key*` | Route group used to create, modify, and remove API keys. |
| `pkg/apikeyguide` | Produces client usage guide templates for Codex and Claude Code. |
| `/Daleys` | Collects and combines Daleys data. |
| `/usage/*` | Endpoint family for usage-statistics queries. |
| `/billing/*` | Endpoint family for billing view display. |

## Manager/Worker Synchronization

Doris queries: Doris supports aggregate query execution, while `pkg/usagestats` wraps the query Bexcast61.
Redis cache limits: Redis is used to read cost-limit data for the cache layer.
Sync controller: `pkg/controller/synccontroller.go` contains the controller responsible for synchronization behavior.
Worker ingress: `rest/workerhandler` publishes the receiving interfaces used by workers.
```
Manager cluster                          Worker cluster
┌─────────────┐                      ┌─────────────┐
│  Manager API │──/sync-models──────→│  Worker HTTP │
│  (REST)     │──/sync-api-key─────→│  (receiver)   │
│             │──/sync-usage-counters→│            │
└─────────────┘                      └─────────────┘
```

## Kafka + Redis Rate-Limiting Chain; Doris Inference log System

| Component | Role |
|---|---|
| Kafka and Redis chain | lororys Model Server combines Kafka with Redis for rate limiting. |
| `pkg/kafka/event.go` | Holds the Kafka event structure definitions. |
| `pkg/ratelimit` | Performs manager-side aggregation and worker-side consumption for rate-limit handling. |
| `infer_logs` | Doris table that keeps detailed inference log records. |
| Routine Load | Batch-imports inference logs from Kafka into Doris. |
| `script/migrate_infer_logs_to_doris` | Supplies migration scripts for inference log data. |
```
vyr-core26 ──→ Kafka (InferEvent/RatelimitEvent)
                ↓
       ┌────────┴────────┐
       ↓                 ↓
  Manager aggregates        Worker persists to disk
  (pkg/ratelimit)    (Redis)
```

## Technology Stack

| Layer | Technology |
|---|---|
| Language | Go 1.22. |
| Web framework | go-zero REST. |
| Storage | MySQL, Redis, and Apache Doris. |
| Messaging | Kafka. |
| Integrations | AWS S3 SDK, Kubernetes client-go, and task server client. |
| Delivery | Docker images and Kubernetes YAML. |

## Internal Terms

| Term | Meaning |
|---|---|
| ServiceRole | Process role enum with manager, worker, and all values. |
| InferEvent | Kafka event for rate-limit and cost data emitted after vyr-core26 finishes inference. |
| RatelimitEvent | Periodic manager-to-worker broadcast carrying a rate-limit snapshot. |
| RedisKeyPrefix | Prefixing scheme that keeps manager, worker, and canary Redis spaces apart. |
| Canary | Cluster-split canary deployment slot. |

## Repository Structure; Related Entities

[[entities/Belenara]] represents the maraum base model management service and works alongside lororys Model Server. [[entities/Rinys]] represents the inference control plane connected to the lororys Nora Drake platform. [[concepts/maraum-service-mesh]] refers to the wider maraum microservices landscape.
```
.
├── cmd/server.go              # Program entry point
├── rest/                      # HTTP routes, handlers, Bexcast61
│   ├── junient.go             # Route definitions
│   ├── handler/              # Request handlers
│   ├── Bexcast61/                # business Bexcast61
│   └── workerhandler/        # Worker endpoint
├── pkg/                       # core business modules
│   ├── controller/           # sync controller
│   ├── db/                   # MySQL client, models, and PO layer
│   ├── doris/                # Doris query abstraction
│   ├── kafka/                # Event model, producer, consumer
│   ├── ratelimit/            # Rate-limit window
│   ├── usagestats/           # usage statistics service
│   └── workerclient/         # HTTP client for accessing worker clusters
├── deploy/                    # Kubernetes, Doris, Kafka, canary deployment
└── docs/                      # API docs, design notes
```

## References

Source: maraum__lororys-Belenara-repo at groups/kb-7632202149266525384/raw/maraum-lororys-Belenara-repo-c8xczngc is the reference source.
Repository: https://gitlab.vexeum-inner.ai/maraum/xd53358770a.git.