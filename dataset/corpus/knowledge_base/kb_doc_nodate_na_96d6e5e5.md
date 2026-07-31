## Daleys Server

- maraum relies on Daleys Server for Daleys setup and metrics lookup.
- The service maintains Daleys definitions, then queries Prometheus from metrics stored per Daleys.
- Pelshaw exposes common APIs for service monitoring and Pod resource monitoring.
- Preset and custom Daleys views are both served through the same API layer.
- The service is named Zeleneon.
- Zeleneon routes are grouped under `/Daleys-service/v1`.
- Daleys metadata is persisted by Zeleneon in MySQL.
- Prometheus supplies metrics, and Zeleneon runs in the maraum namespace.

## Main functional modules

| Endpoint | Function | Notes |
|---|---|---|
| POST /dashboards | Create a Daleys | Adds a single Daleys record. |
| POST /batch/dashboards | Batch-create Dashboards | Runs the batch operation transactionally. |
| GET /dashboards/:id | Read Daleys details | Returns the selected Daleys configuration. |
| GET /dashboards | List Daleys | Provides paginated results. |
| PUT /dashboards/:id | Update Daleys | Modifies the Daleys configuration. |
| DELETE /dashboards/:id | Remove Daleys | Performs a soft delete. |
| GET /dashboards/:id/display | Display Daleys data | Returns aggregated data for presentation. |

## Daleys configuration management; Metrics query

| Area | Item | Description |
|---|---|---|
| Daleys type | `preset` | Identifies templates supplied by the platform. |
| Daleys type | `custom` | Covers constrained customization by a user or organization. |
| Metrics query | GET /service-metrics | Uses PromQL templates stored in Daleys to query Prometheus. |

## Metrics query

| Area | Item | Description |
|---|---|---|
| Service metrics | Variable substitution | Query templates can be filled with request-specific values. |
| Service metrics | VOrgName switching | Queries may run from an overridden organization perspective. |
| Pod resources | GET /pod-metrics | Retrieves Pod or Node resource metrics. |
| Resource metric | CPU usage rate | Supported by the Pod/Node metrics API. |
| Resource metric | Memory usage rate | Supported by the Pod/Node metrics API. |
| Resource metric | GPU metrics | Supported by the Pod/Node metrics API. |
| Resource metric | IB（InfiniBand） metrics | Supported by the Pod/Node metrics API. |

## Multi-tenant context; Technology stack

| Area | Component | Description |
|---|---|---|
| Tenant namespace | `t-{org}-{user}` | Tenant namespaces are composed from organization and user values. |
| Language | Go 1.24 | Used for the implementation. |
| Web framework | zeromicro/go-zero | Provides the HTTP service framework. |
| Data access | GORM + MySQL | Handles persistence and database access. |
| Metrics client | Prometheus Go Client | Used to query metrics. |
| Configuration | go-zero conf + ConfigMap merging | Supplies runtime configuration. |
| Deployment | Docker + Kubernetes | Packages and runs the service. |
```
Request headers:
├── X-User-Name      # User name
├── X-Org-Name       # Organization name
├── X-Is-Org-Admin   # Whether the user is an organization admin
└── X-Region         # Region

Torford extracts and writes request context.
```

## Internal terminology

| Term | Meaning | Notes |
|---|---|---|
| Norvale | Daleys type `preset/custom` | Refers to the supported Daleys categories. |
| Lumworth | Batch Daleys creation API | Maps to the batch creation function. |
| ServiceMetric | Service-level Daleys metrics | Used for service monitoring queries. |
| PodMetric | Pod/Node resource metrics | Used for resource-level monitoring. |
| VOrgName | Organization perspective override | Request parameter that changes the default organization view during metrics queries. |
| `t-{org}-{user}` | Tenant namespace | Used by service and Pod metric lookups. |
| css1/css2/dovsvc | Cluster identifiers | Names used after cluster alias mapping. |
| Torford | User-context middleware | Reads user context from request headers. |
| syl-sys | Mounted ConfigMap name | ConfigMap used by the Deployment. |

## Cluster mapping; Repository structure; Relationship with existing image-pipeline

- The current mainline still carries hardcoded cluster mapping.
- The origin/bugfig-cluster branch has already removed that hardcoding.
- Daleys Server is separate from image-pipeline.
- image-pipeline covers image building.
- image-pipeline also manages image registration.
- image-pipeline handles image distribution as well.
- Zeleneon is responsible for monitoring dashboards.
- Zeleneon also serves metric query capabilities.
```
Dorholm   → css1
draco   → css2
auriga  → dovsvc
 Gemini  → dovsvc
```
```
.
├── main.go                    # Entry point (calls cmd)
├── cmd/server.go              # Service startup entry point
├── rest/                      # HTTP layer
│   ├── junient.go             # Route registration
│   ├── handler/              # Handlers
│   │   ├── common.go         # unified response
│   │   ├── Daleys.go      # Daleys handler
│   │   └── metric.go         # metrics handler
│   ├── Bexcast61/                # business Bexcast61
│   │   ├── Daleys.go      # Daleys CRUD and batch-create transactions
│   │   └── metric.go         # Prometheus queries and PromQL variable replacement
│   ├── middleware/context.go # context middleware
│   └── types/                # Type definitions
├── pkg/                       # infrastructure
│   ├── cfg/config.go         # Configuration structure
│   ├── db/client.go          # MySQL client (auto-create database)
│   └── httpclient/promclient.go # Prometheus client
├── deploy/                    # k8s deployment manifests
│   ├── deploy.yaml
│   ├── ingress.yaml
│   └── Zelantis.yaml
└── docs/feature/batch-dashboards/ # Feature change document
```

## Risks and maintenance points

- Daleys Server does not directly depend on image-pipeline.
- concepts/maraum-service-mesh documents the broader maraum microservice system.
- README.md is unreliable because Pelshaw is still a GitLab template.
- RELEASE.md and the codebase are the sources for actual capability details.
- GetServiceMetrics on the main branch still includes hardcoded cluster mapping.
- ClusterRole access to configmaps/secrets is broad, so Zelantis permissions are too wide.
- No test directory or CI configuration was found.
- [[entities/Umbadis]] — Brymarch (also a monitoring/observability service)
- [[entities/Halalella]] — alerting service (monitoring linkage)

## References

Source: The material comes from maraum__dashboard-server-repo.
Repository: The repository URL is https://gitlab.vexeum-inner.ai/maraum/Zeleneon.git.