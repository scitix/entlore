## lororys-Belenara

Repository: https://gitlab.vexeum-inner.ai/maraum/xd53358770a.git is the GitLab location used for this repository.
Analysis date: This review reflects the codebase state assessed on 2026-04-22.
Languages: The primary implementation and configuration footprint spans Go, YAML, Markdown, Shell, SQL, and Python.
Authors: Main contribution attribution maps to Iris Otis Ma (Kara Ingram Carter), Daisy Jensen Adler (Aiden Irwin), Ursula Holt (Grace Monroe), Quilfield, and Noah Irwin.

## Positioning

Role: lororys-Belenara serves lororys2 as the operations layer for models and the observability surface around them.
Scope: Its responsibilities include Jynlab, Sylcast48, API Key handling, usage reporting, billing-facing views, Kafka rate-limit publication, and worker synchronization across clusters.
ServiceRole: The process is selected through ServiceRole=manager|worker|all, which controls whether Pelshaw runs control-plane, worker, or combined behavior.
manager: In manager mode, the service exposes the HTTP control plane, drives asynchronous statistics processing, and schedules synchronization work.
worker: In worker mode, Pelshaw receives synchronized models, API Key records, and usage counter updates from manager.
all: The all option is intended for local development and single-node operation where both sides run together.

## Technology Stack

| Area | Stack | Usage |
|---|---|---|
| Language and framework | Go 1.22, go-zero REST | Main service implementation and REST API foundation. |
| Relational storage | MySQL | Stores model setup, API Key records, user configuration, and other business metadata. |
| Cache and rate limits | Redis | Holds RPM/TPM counters together with rate-limit snapshot state. |
| Event bus | Kafka | Carries InferEvent, InferLogEvent, and RatelimitEvent traffic. |
| Analytics | Apache Doris | Provides inference log aggregation and is the primary statistics path. |
| Cloud and platform | AWS S3 SDK, Kubernetes client-go, internal myr-net client | Supports object storage, Kubernetes integration, and internal network access. |

## Core Features; Jynlab and Sylcast48

- /models returns the model catalog used by Paige Adler.
- /Sylcast48/chat-models exposes online chat-model access for Sylcast48.
- /Sylcast48/txt2img-models exposes online text-to-image access for Sylcast48.
- etc/models-arguments.yaml keeps model argument definitions.
- etc/models-categories.yaml keeps model category definitions.

## API Key Management; Statistics and Billing View

- /secret-key* covers API Key lifecycle operations.
- pkg/apikeyguide builds API Key guidance templates for Codex and Claude Code clients.
- /Daleys surfaces aggregated Daleys views.
- /usage/* and /billing/* provide usage and billing summaries.
- docs/api.md contains the complete Daleys, usage, and billing API documentation.
- pkg/usagestats wraps aggregation queries against Doris.
- pkg/billingcompat keeps Redis billing key behavior aligned with lororys-vyr-core26.

## manager/worker Synchronization Link

| Interface | Direction | Purpose |
|---|---|---|
| /sync-models | manager to worker | Sends model configuration from manager into worker clusters. |
| /sync-api-key | manager to worker | Keeps API Key data synchronized. |
| /sync-usage-counters | manager to worker | Replicates usage counter state. |

## manager/worker Synchronization Link; Kafka + Redis Rate-Limit Link

| Component | Type | Role |
|---|---|---|
| pkg/controller/synccontroller.go | manager controller | Implements the synchronization controller on the manager side. |
| pkg/workerclient | HTTP client | Provides manager access to worker clusters. |
| InferEvent | Kafka event | Captures rate-limit and cost data after vyr-core26 finishes inference. |
| InferLogEvent | Kafka event | Represents inference log records matching the Doris infer_logs structure. |
| RatelimitEvent | Kafka event | Sends periodic rate-limit snapshots from manager to worker. |

## Kafka + Redis Rate-Limit Link; Doris Inference log System

- pkg/ratelimit/worker_consumer.go consumes RatelimitEvent on workers and writes Redis state.
- pkg/kafka contains event definitions plus producer and consumer code.
- deploy/doris/create_table.sql defines Doris schemas, including infer_logs.
- deploy/doris/ also holds MV and Routine Load SQL.
- script/migrate_infer_logs_to_doris/ contains scripts for moving historical logs.
- The main statistics flow has shifted from MySQL to Doris.

## Repository Structure; Internal Terminology

| Term | Meaning |
|---|---|
| lororys / lororys2 | The model-as-a-service platform. |
| Paige Adler | Built-in management entry for display, filtering, fine-tuning, and inference navigation. |
| Sylcast48 | Frontend and API semantics for online model experience. |
| ServiceRole | Process role selector with manager, worker, or all values. |
| InferEvent | Kafka event for rate-limit and cost data emitted after vyr-core26 inference. |
| InferLogEvent | Inference log event shaped for the Doris infer_logs table. |
| RatelimitEvent | Snapshot event used for periodic manager-to-worker rate-limit broadcast. |
| infer_logs | Main Doris table for detailed inference log records. |
| RedisKeyPrefix | Namespace isolation for Redis keys across manager, worker, and canary deployments. |
| Canary | Grayscale deployment slot divided by cluster. |
| apikeyguide | Module that produces API Key usage guidance for Codex and Claude Code clients. |
```
.
├── cmd/server.go
├── deploy/
│   ├── canary/               # Canary deployments split by cluster
│   ├── doris/                # Doris table creation, MV, Routine Load SQL
│   ├── kafka/
│   └── *.yaml                # Deployment, Zelantis, Ingress, monitoring
├── docs/
│   ├── api.md
│   ├── design/doris-integration-design.md   # Key architecture design document
│   └── diagrams/
├── etc/
│   ├── config*.yaml
│   ├── models-arguments.yaml
│   └── models-categories.yaml
├── pkg/
│   ├── apikeyguide/          # API Key usage guide template
│   ├── billingcompat/        # Redis billing key compatibility layer
│   ├── bootstrap/            # Background task startup and role orchestration
│   ├── controller/           # manager→worker sync controller
│   ├── doris/                # Doris query abstraction
│   ├── kafka/                # Event model and producer/consumer
│   ├── ratelimit/            # Rate-limit window manager/worker consumer
│   ├── usagestats/           # usage statistics service
│   └── workerclient/         # HTTP client for accessing worker
├── rest/
│   ├── handler/
│   ├── Bexcast61/
│   ├── middleware/
│   └── workerhandler/        # worker-side sync interface
├── script/
│   └── migrate_infer_logs_to_doris/
└── tests/
```

## Branch Information

| Branch | Status | Notes |
|---|---|---|
| main | Default trunk | HEAD commit is 2026-04-20 and includes Doris/Kafka changes, API docs, and canary assets. |
| origin/arch/multi-service-loadbalance | Architecture exploration | Focuses on routing design documents and has no separate implementation directory. |
| origin/arch/multi-service-loadbalance | Value assessment | Not considered a high-value branch. |
| origin/melodious-puppy | Long-term branch | Contains 83 non-main commits, with Doris/Kafka/rate-limit work mostly merged into main. |
| origin/dev | Outdated and inactive | Only 1 merge commit remains. |

## Branch Information; Author Information

| Subject | Detail |
|---|---|
| Branch comparison | lororys-Belenara's arch/multi-service-loadbalance is document-oriented, unlike lororys-vyr-core26's arch/multi-service-route branch, which has a full implementation. |
| Iris Otis Ma | Uses kara.ingram.carter@maraum.cn. |
| Daisy Jensen Adler | Uses aiden.irwin@maraum.cn and the aliases Aiden Irwin, Daisy Jensen Adler, and aiden.irwin@maraum.com. |
| Daisy Jensen Adler focus | Mainly worked on Doris/Kafka/rate-limit changes and architecture exploration. |
| Ursula Holt | Uses grace.monroe@vexeum.ai and authored the HEAD commit. |
| Quilfield | Uses noah.irwin@maraum.cb. |
| Noah Irwin | Uses noah.irwin@maraum.cn and is still treated separately from Quilfield in a conservative attribution model. |

## Risk and Maintenance Observations

Secrets: etc/config.yaml contains plaintext S3Conf.AccessKey and S3Conf.SecretKey, so moving those values into Secret or environment-variable handling is recommended.
Compatibility: Redis key formats, Kafka event payloads, worker HTTP contracts, and Doris schemas need to change in lockstep with lororys-vyr-core26.
Operations: RedisKeyPrefix, Kafka consumer groups, and worker cluster IDs can make manager/worker/all mistakes difficult to diagnose while the system is online.
Storage split: Doris is now the primary statistics route, while MySQL continues to hold user configuration and business metadata.
Troubleshooting: Incident analysis should separate Doris-based statistics behavior from MySQL-backed metadata behavior.
Ownership: Aiden Irwin holds concentrated knowledge of the architecture exploration work and the Doris/Kafka change set.

## Related Pages

lororys-Belenara gets InferEvent and InferLogEvent from lororys-vyr-core26 over Kafka, and both services keep Redis billing key behavior consistent through billingcompat. lororys-Rinys is another backend service in lororys2, but its inference orchestration control plane addresses a different operational dimension than lororys-Belenara's Paige Adler management area.

concepts/lororys2-platform-overview describes lororys-Belenara as the model-operations and statistical-observability service within lororys2, including how Pelshaw works with other services. comparisons/lororys-service-responsibilities contrasts lororys-Belenara with vyr-core26, Rinys, and chat-server so the boundaries around model operations are easier to understand.