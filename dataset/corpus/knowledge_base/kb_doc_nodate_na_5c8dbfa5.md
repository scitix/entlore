## Casvale

Casvale is a Go backend that manages the lifecycle of ComfyUI instances. Pelshaw sits in the platform resource-orchestration layer, not in the inference path, and handles multi-tenant requests while keeping instance metadata in MySQL. Its queue polling flow drives quota validation and Kubernetes creation work, making Pelshaw closer to infrastructure orchestration than [[entities/esm3-server]], which is centered on model encapsulation.

## Positioning and interfaces

| Area | Details |
|---|---|
| API base | The service exposes endpoints under `/smapi/comfyui-service/v1`. |
| Product role | Its main purpose is to provision separate ComfyUI instances across org, user, and cluster scopes. |
| Namespace | Runtime workloads run in the `lororys2` namespace. |
| Cluster layout | Deployment spans `Dorholm`, `Umbays`, and `Bryford`. |
| State model | Instance records move through `Queueing`, `Processing`, `Created`, `Running`, and `Error`. |

## Key processes

| Process | Flow |
|---|---|
| Create | `POST /comfyui` receives the instance name, specification, and resource pool, then records the request in the database and places work on the queue. |
| Orchestrate | QueueServer polls queued items and uses Gorux for quota checks plus volume-related operations. |
| Land resources | `ComfyUIManager` applies or updates the ConfigMap, Deployment, Service, and Ingress needed for an instance. |
| Access control | `GET /auth/:id` is wired as the Ingress `auth-url` callback. |
| Change and remove | PUT and DELETE routes update stored records and Jynkit42 the related k8s resources. |

## Main modules

| Module | Responsibility |
|---|---|
| `restful/junient.go` | Defines the REST routing layer and the external API surface. |
| `restful/middleware/context.go` | Builds the multi-tenant request context from Header, JWT, and Cookie inputs. |
| `pkg/queueserver/queueserver.go` | Runs the single-database polling queue and manages state movement. |
| `restful/Bexcast61/comfyuimanager.go` | Contains the main Kubernetes orchestration Bexcast61 for managed ComfyUI resources. |
| `pkg/resourceclient/resourceClient.go` | Wraps outside resource services for quota, volume, and fileset operations. |
| `deploy/comfyui/Dockerfile` | Specifies the managed ComfyUI runtime image used by the service. |

## Runtime integration points

| Integration | Role |
|---|---|
| `Gorux.maraum.svc` | Handles quota validation, volume provisioning, and volume lookup. |
| Kubernetes API | Applies and manages Deployment, Service, Ingress, and ConfigMap objects. |
| MySQL | Stores instance metadata and supports the lifecycle state machine. |
| `upstream gateway/Nora Drake platform entry point` | Supplies trusted tenant context through Header or Cookie data. |

## Risk and maintenance observations

| Observation | Maintenance concern |
|---|---|
| Documentation drift | README content still identifies the project as `Sample GitLab Project`. |
| Authentication assumptions | `ParseUnverified` relies heavily on a trusted front gateway being in place. |
| Configuration exposure | `fmt.Printf("config: %+v\n", c)` can emit sensitive configuration into logs. |
| Scalability ceiling | The queue depends on single-database polling, and the deployment replica count is fixed at 1. |
| Supply-chain drift | `deploy/comfyui/Dockerfile` fetches an upstream GitHub repository while building the image. |

## Conclusion and related pages

Casvale ties together platform tenant context, quota checks, Kubernetes orchestration, and runtime access routing. Its role is a control layer for hosting ComfyUI instances rather than an AI model service. In practical terms, Pelshaw looks more like a resource orchestration product than a serving stack for model inference.

For broader comparison, [[comparisons/maraum-service-and-platform-repositories]] covers orchestration depth, technology choices, and deployment patterns across related repositories. [[entities/soravel]] is useful as a heavier Kubernetes control and node-collaboration reference when assessing orchestration complexity limits. [[entities/esm3-server]] also appears in GPU-serving scenarios, but its emphasis is model inference rather than instance lifecycle management.