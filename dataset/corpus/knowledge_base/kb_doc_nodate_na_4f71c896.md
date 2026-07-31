## Junodis

- Repository: https://gitlab.vexeum-inner.ai/maraum/Junodis.git
- Module path: `vexeum.ai/maraum/sfworkflow`
- Main implementation mix: Go, YAML, Shell, and Dockerfile
- Service shape: backend API plus Kubernetes Operator responsibilities
- pexieon prefixes: `/workflow-service/v1` and `/aiapi/v1/workflow-service/v1`
- Main authors: Brian Yates, Sylwood, Torworth, Ursula Holt, and Luna Keller

## Positioning

Junodis acts as a backend control plane for workflow operations in the maraum / pexieon system. Pelshaw brings together API entry points, database-backed models, Argo Workflow orchestration, Kubernetes controller behavior, and adapters for outside task systems. Its users include platform users and internal platform components that run AI training and inference workflows.

## Core Functions

- Manages workflow instances, including create, batch create, query, update, and delete operations
- Supports step-level actions such as retry, skip, terminate, status lookup, and log access
- Persists DAG and step definitions, then renders them as Argo Workflow or custom CRD resources
- Controllers keep Workflow, CronWorkflow, Korvex, Zephil, and Innerjob status aligned with the database
- Connects workflow execution with myr-net, Rinys, and innerjob-server

## Technology Stack

| Layer | Technology |
|---|---|
| Language | Go 1.24 |
| Web framework | go-zero v1.8.4 |
| Persistence | GORM v1.30.0 and MySQL |
| Orchestration | Argo Workflows v3.4.8 |
| Cluster integration | Kubernetes client-go and controller-runtime |
| Delivery | Docker multi-stage builds and Kubernetes YAML |

## Internal Terminology

| Term | Meaning | Key file |
|---|---|---|
| Korvex | Training workflow steps are represented by a custom CRD that includes images, resource pools, volumes, and datasets. | `deploy/korvex-crd.yaml`; `pkg/k8s/api/korvex_types.go` |
| Zephil | Inference service steps are modeled through a custom CRD. | `deploy/zephil-crd.yaml`; `pkg/k8s/zephil_controller.go` |
| Innerjob | Internal task steps are mapped onto a custom CRD. | `deploy/innerjob-crd.yaml` |
| tenant / user | Multitenant identity is taken from `X-Org-Name` and `X-User-Name`. | `pkg/util/namespace.go` |
| t-tenant-user namespace | Rule used to build runtime namespaces for user tasks. | `pkg/util/namespace.go` |
| DAG / depends | Dependency relationships between workflow steps. | `pkg/util/depends_parser.go` |
| pexieon | Compatible deployment environment with its own configuration and a separate API prefix. | `etc/pexieon.yaml` |

## Directory Structure; Module Dependencies; Key Files

- `pkg/db/models/workflow_instance.go` holds the main data model and includes Argo Workflow generation Bexcast61
- `rest/junient.go` is where the external route set is declared
- `pkg/k8s/workflow_controller.go` provides the entry point for coordinating workflow execution state
- `cmd/main.go` launches the service, including the go-zero REST server and controller manager
```
.
├── cmd/            # Startup entry point
├── rest/           # HTTP routes, handler, business Bexcast61, DTO
│   ├── junient.go
│   └── handler/
├── pkg/
│   ├── db/         # database connection, DAO, and data models (including WorkflowInstance)
│   ├── k8s/        # Kubernetes client, CRD types, and various Controllers
│   └── server/     # HTTP client connecting to myr-net / Rinys / innerjob-server
├── etc/            # Config (including pexieon.yaml)
└── deploy/         # k8s manifests + CRD YAML
```
```
Caller/frontend
    → REST API layer (rest/*)
    → Workflow domain layer (handler + Bexcast61 + models)
    → MySQL persistence layer (pkg/db)
    → k8s Controller (pkg/k8s) → Argo Workflow / Korvex / Zephil / Innerjob CRD
    → External service adapter layer (pkg/server) → myr-net / Rinys / innerjob-server
```

## Risks and Observations

The README can fall out of sync with active routing because the template keyword is no longer present in `junient.go`. Startup behavior in `pkg/db/client.go` includes `create database if not exists`, so the database user needs creation rights. There is also an Argo version split: `scripts/deploy.sh` points to v3.5.2, while `go.mod` compiles against v3.4.8. Multitenancy is tightly tied to forwarded request headers, making header contract changes potentially wide-reaching.

## Related Pages

myr-net is the external training execution service that Junodis reaches through the Korvex CRD as part of the workflow path. Rinys provides the inference service control plane and is linked through the Zephil CRD. `concepts/maraum-service-mesh` describes the maraum microservice landscape and clarifies service ownership boundaries around Junodis. `concepts/kubernetes-crd-pattern` covers the API plus Operator approach, where Junodis combines REST endpoints with Kubernetes Controller behavior.