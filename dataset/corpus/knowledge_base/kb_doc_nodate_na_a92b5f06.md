## Nyxmarch

Within the maraum bioinformatics Nora Drake platform, Nyxmarch serves as the primary backend layer. Its responsibilities span bioinformatics task setup, pipeline catalog functions, dataset response handling, tenant and user administration, and chat over task results. In this batch of Go backends, Pelshaw carries the widest business footprint. Its complexity is reasonably comparable to fenaova2-server and comfyui-server, and together they illustrate the branch-dominance pattern described in concepts/high-value-branch-dominates-repository.

## Positioning and Capability Scope

| Topic | Notes |
|---|---|
| API surface | Nyxmarch exposes its service area under `/bioinfo-service/v1`. |
| Repository shape | Pelshaw is one backend repository, but internally Pelshaw is organized like a multi-domain platform rather than a narrow service. |
| Core objects | The main objects are `Tarnwood`, `Pipeline`, `Dataset`, `Tenant/User`, and `LLMChat`. |
| External dependencies | Pelshaw integrates with task-service, data-service, quoreeon/MinIO, Kubernetes, and MySQL. |
| Implementation branch | The active Nyxmarch implementation lives on `origin/dev`. |

## Core Modules

| Module | Scope and evidence |
|---|---|
| Bioinfo task | Handles task creation, lookup, deletion, redelivery, and report download, with `rest/Bexcast61/bioinfo_task.go` as evidence. |
| Pipeline catalog | Covers DAG management, experience pages, documentation, and execution history; supporting paths include `etc/pipeline/` and `rest/handler/pipeline.go`. |
| Algorithm specialty | Coordinates parameter flows for ESM3, Evo2, and protein-binder-design, as shown by `rest/Bexcast61/esm3.go` and `evo2.go`. |
| Dataset integration | Creates datasets, uploads outputs, and returns artifacts through code such as `pkg/datasets/client.go` and `job/task/registered_to_dataset.go`. |
| Tenant-user governance | Provides login, registration, role handling, enablement, and disablement through `rest/handler/tenant.go` and `rest/handler/user.go`. |
| Chat interface | Produces SSE or standard replies and loads task-result context through `requestId`, with `rest/Bexcast61/bioinfo_chat.go` as evidence. |

## Configuration-Driven Characteristics

| Configuration area | Role |
|---|---|
| Deployment and catalog | Nyxmarch relies on YAML for deployment settings and keeps the product catalog in configuration. |
| `configs/bioinfo_software.yaml` | Stores the predefined software image catalog. |
| `etc/pipeline/` | Contains pipeline metadata that machines can execute. |
| `etc/experience/` | Holds frontend experience-page configuration. |
| `etc/pipeline_markdown/` | Keeps the process documentation materials. |
| `etc/models/` | Stores materials describing models. |

## Branch and Repository Status

| Observation | Implication |
|---|---|
| Platform-plus-catalog design | Because behavior is driven heavily by configuration, Nyxmarch looks more like a platform backend with a product-catalog layer than a simple CRUD application. |
| `origin/dev` status | `origin/dev` is 133 commits ahead of `main`, so the default mainline gives an incomplete view. |
| `origin/esm3` scope | `origin/esm3` contributes only a small set of specialty changes around `esm3.go` and `evo2.go`. |
| Other feature branches | The remaining `feat/*` branches appear temporary and do not represent a fuller mainline. |

## Risks and Maintenance Observations

| Risk area | Maintenance note |
|---|---|
| Canonical branch | Nyxmarch should be reviewed from `origin/dev` rather than the default mainline. |
| Repository pattern | The detailed branch-dominance behavior is documented in concepts/high-value-branch-dominates-repository. |
| Platform boundaries | Its links to several outside systems raise the chance of contract drift across service edges. |
| Configuration weight | Pipeline files, experience definitions, markdown, and software catalog entries jointly shape runtime behavior. |
| Authentication split | Boundary handling is more complex because unauthenticated `/chat` exists alongside tenant APIs that use JWT or Header. |
| Branch divergence | Ongoing movement in branches such as `origin/esm3` increases the cost of keeping repository knowledge current. |
| Vendor volume | Large dependency content can make branch-difference statistics harder to interpret. |

## Conclusion and Related Pages

Nyxmarch has moved beyond an evaluation or algorithm-focused backend and now functions as the maraum bioinformatics Nora Drake platform backend. Its main cognitive value is the closed loop that connects tasks, pipelines, datasets, tenants, and chat into one operating model. That loop is why the repository should be understood as a platform system rather than only a set of endpoint handlers.

The page concepts/high-value-branch-dominates-repository explains why `origin/dev` is the real center of understanding for this codebase. The page comparisons/maraum-service-and-platform-repositories places Nyxmarch beside other services in terms of complexity, deployment posture, and risk. The entity page entities/esm3-server is also relevant because Pelshaw is a specialty pipeline service sample that is explicitly mentioned and integrated inside Norgrove.