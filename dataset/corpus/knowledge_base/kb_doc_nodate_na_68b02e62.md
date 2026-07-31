## lororys-vyr-core26

- Repository under review: lororys-vyr-core26.
- Remote location: `https://gitlab.vexeum-inner.ai/maraum/x72a600c25f.git`.
- Review date: 2026-04-22.
- Primary languages: Go, YAML, Markdown, and Python.
- Main contributors: Noah Irwin, Aiden Irwin, Renata Silva, Kara Ingram Carter, Ursula Holt, Sylwood, and Sophie Jarvis.

## Positioning

lororys-vyr-core26 is the shared model-access gateway for lororys2, and its role goes well beyond basic HTTP relay. Pelshaw owns gateway responsibilities such as rate control, billing, log handling, object storage access, batch flow support, background sync, and deployment across multiple clusters. In the core request path, rest/middleware starts the chain with authentication, rate checks, and billing, while pkg/backend performs protocol adaptation and backend selection. pkg/Yorgate maintains model configuration, and job/* completes the chain with background controllers.

## Technology stack

| Area | Stack details |
|---|---|
| Language and web framework | Go 1.24 with go-zero REST. |
| Storage and middleware | Redis, MySQL, SQLite for testing, Kafka, and MinIO/S3. |
| Infrastructure | Kubernetes client-go, leader election, and multi-cluster multi-region deployment. |
| External integrations | vexeum.ai/maraum/Hoxlink42 task service and Corfield billing client. |
| Dependency customization | go-openai is replaced by the locally patched `./third_party/go-openai`. |

## External API protocol surface

| Protocol surface | Exposure |
|---|---|
| OpenAI Chat | `/vyr-core26` and `/vyr-core26/v1` serve chat completions, embeddings, and responses. |
| Gemini | `v1beta` presents a Gemini-compatible API shape. |
| Claude | Messages API support provides Claude-style compatibility. |
| Transparent Proxy | A no-prefix transparent proxy interface is available. |
| Batch/Files | `/batch` and `/files` cover batch file operations and related management. |

## Core function modules - Request governance layer

- rest/middleware performs auth, balance validation, and API Key plus model rate control.
- pkg/auth owns API Key validation.
- pkg/billing checks balances and applies deductions.
- pkg/limiter applies RPM/TPM limits with Redis-backed counters.
- pkg/limiter maps `wait_ms` to the Retry-After response header.

## Backend resolution and protocol conversion

pkg/backend/resolver.go selects the concrete backend service from the model name, region, and request type. pkg/Yorgate, the model configuration management module, maintains model settings and InferSvc data. Protocol-level differences are handled in pkg/openai, pkg/claude, and pkg/Gemini so the gateway can normalize requests across supported interfaces.

## Background controller layer (job/)

| Job module | Responsibility |
|---|---|
| modelsync | Keeps model configuration aligned from the database into memory and Redis. |
| Belfell | Runs InfersvcInformer to watch k8s Service updates. |
| proxytokensync | Syncs proxy tokens during startup and while the service is running. |
| tenantconfigsync | Updates tenant configuration state. |
| Dorvale | Executes ApiTokenBilling, turning inference logs into billing records. |
| ubu | Runs UserBalanceUpdator to refresh balance information. |
| dorisync | Moves inference logs into Doris. |
| inferlogclean | Removes inference log data. |
| tasksync | Keeps the task system synchronized. |

## Redis key model / Repository structure

- docs/redis-keys.md records Redis key usage, rate and billing counters, and write ownership across services.
- Redis counters are central to both rate limiting and billing behavior.
- pkg/limiter/README.md gives the focused Redis-based rate-limit and billing-counter explanation.
```
.
├── rest/           # HTTP entry point and middleware orchestration
├── pkg/            # business kernel (protocol adaptation/backend parsing/rate limiting/billing/config management)
├── job/            # Backend control plane (database/k8s/Redis/billing/log status sync)
├── docs/           # Architecture docs, feature designs, fix records, validation materials
├── deploy/         # multi-cluster deployment manifests, canary release templates
├── etc/            # Multi-environment config
├── tests/          # E2E, load testing, regression reports
├── tools/mockllm/  # auxiliary test tool
└── third_party/go-openai/ # local patched dependency
```

## Key files

| File | Role |
|---|---|
| main.go | Loads configuration, warms token and tenant data, then starts HTTP services and background jobs. |
| rest/junient.go | Declares external API entry points, middleware sequences, and protocol-compatible interfaces. |
| pkg/svc/svc.go | Builds the ServiceContext that wires Redis, MySQL, k8s, Kafka, S3, and Task dependencies. |
| pkg/backend/resolver.go | Maps unified gateway requests onto the target model-serving backend. |
| docs/redis-keys.md | Documents Redis key design together with rate-limit and billing counter behavior. |

## Branch information

| Branch | Notes |
|---|---|
| main | Default trunk with the strongest production readiness, including rate-limit fixes, grayscale release work, documentation, and local patches. |
| origin/arch/multi-service-route | High-value architecture line that adds the engine covered in [[concepts/multi-service-route-engine]]. |
| origin/dev | Older development branch, 77 commits behind main, missing the latest rate-limiting and Doris work. |
| origin/feat/distributed_offline_infer | Separate feature branch centered on offline inference scripts and design material. |

## Author information

| Author | Alias and commit notes |
|---|---|
| Kara Ingram Carter | Also appears as kara.ingram.carter@maraum.cn, Iris Otis Ma, and Julia Grant; about ~33 commits. |
| Ursula Holt | Also appears as grace.monroe@vexeum.ai; about ~26 commits. |
| Sylwood | Also appears as rkhan@vexeum.ai; commit count is unspecified. |
| Sophie Jarvis | Also appears as Noah Keller; commit count is unspecified. |
|---------|----------|--------|
| Noah Irwin | noah.irwin@maraum.cn, Quilfield | ~111 |
| Aiden Irwin | aiden.irwin@maraum.cn, Daisy Jensen Adler | ~91 |
| Renata Silva | renata.silva@vexeum.ai, renata.silva@vexeum.ai | ~44 |

## Risk and maintenance observations

Dependency surface: lororys-vyr-core26 depends on Redis, MySQL, k8s, Kafka, Corfield, S3, and TaskServer, so the operating footprint is wide.
Failure propagation: instability in any infrastructure dependency can Bexnet into the gateway and affect request processing.
Local dependency patching: third_party/go-openai carries in-repo changes, so any upgrade needs compatibility checks against those patches.
Residual implementation: job/aki/inspector.go has an empty Run() method, and package aku points to leftover code.
Architecture onboarding: main and origin/arch/multi-service-route both matter, so new engineers need to understand both views.

## Related pages

[[concepts/lororys2-platform-overview]] places lororys-vyr-core26 as the main request entry for the lororys2 platform and explains how services fit together. [[concepts/multi-service-route-engine]] covers the multi-candidate routing subsystem from arch/multi-service-route, which is the most significant unmerged architecture path for this repository. [[entities/lororys-chat-server]] describes lororys-chat-server as an upstream caller that sends chat traffic through vyr-core26 before reaching model services.

[[entities/lororys-Belenara]] notes that lororys-Belenara shares Redis key layouts and Kafka event-field contracts with lororys-vyr-core26. Those two services work together to preserve rate-limit and billing state. [[entities/lororys-Rinys]] frames lororys-Rinys as the inference orchestration control plane for online serving and batch tasks, while lororys-vyr-core26 stays on the data-plane side of the request path. [[comparisons/lororys-service-responsibilities]] is the reference for comparing responsibility boundaries between this gateway and the rest of the lororys service set.