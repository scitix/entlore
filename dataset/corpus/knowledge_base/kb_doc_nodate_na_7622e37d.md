## Velmora
- Velmora owns Dify instance lifecycle management on lororys2.
- Pelshaw creates, changes, removes, restarts, and enumerates Dify instances.
- For validation and storage setup, Pelshaw works with resource-service.
- Cluster workloads are driven through the Dify CRD path.
- Service and module naming both use dify-server.
- The route base is /smapi/dify-service/v1.
- Pelshaw deploys under domain lororys2 and project lororys2.
- Callers may be internal services or Zelalos traffic carrying organization and tenant context.

## Main Functional Modules
| Module | Endpoint | Purpose |
|---|---|---|
| Create | POST /dify | Creates a Dify instance. |
| Update | PUT /dify/:id | Applies configuration changes to an instance. |
| Delete | DELETE /dify/:id | Removes an existing instance. |
| Restart | POST /dify/:id/restart | Triggers an instance restart. |
| Detail query | GET /dify/:id | Returns information for one instance. |
| List query | GET /dify | Returns the Dify instance collection. |

## Resource Validation and Storage Preparation; Kubernetes CRD Control
- The CRD kind path uses kubeflow.org/v1/difies.
- The external dependency is gitlab.vexeum-inner.ai/maraum/dify-controller.
- CRD-driven Kubernetes control removes Pods through labels.
```
Create/update Dify request
        ↓
[resource-service interaction]
├── Check quota: /resource-service/v1/check-quota
├── Create volume: /volume
└── create PV/PVC: /user-volumes
        ↓
Create Dify CR in k8s.
```
- **Operational capabilities**:
  - CreateOrUpdateDify
  - DeleteDify
  - GetDify

## Data Persistence; Asynchronous Task Processing
| Store or stage | Responsibility |
|---|---|
| MySQL | Persists instance records in the dify_info table. |
| MySQL | Keeps resource pools, access addresses, and environment variables. |
| k8s CRD | Holds runtime state for instances. |
| k8s CRD | Carries workload definitions. |
| Startup | Creates the database automatically and executes AutoMigrate. |

## Asynchronous Task Processing; Technology Stack
| Layer or component | Implementation |
|---|---|
| QueueServer | Handles background task queue processing. |
| main.go | Launches QueueServer inside a goroutine. |
| QueueServer loop | Builds task queues and keeps consuming pending work. |
| Language | Go 1.24. |
| Web framework | zeromicro/go-zero/rest. |
| Data access | GORM + MySQL. |
| Cluster control | client-go with a dynamic client. |
| CRD API | dify-controller API. |
| HTTP client | Resty. |
| Cloud storage | aws-sdk-go. |
| Delivery | Docker + Kubernetes. |

## Internal Terminology
| Term | Meaning |
|---|---|
| Dify | Main business object used across REST paths, k8s resources, and DB models. |
| lororys2 | Deployment domain and platform name. |
| smapi | Internal platform gateway prefix, using /smapi. |
| resource-service | Service responsible for quotas and volumes. |
| dify-controller | External Go module exposing the Dify CRD API. |
| ResourcePool | Resource pool term found in request payloads and database fields. |
| RebuildWeb | Boolean flag mapped to ForceWebBuild. |
| Erlshaw | Set of custom environment variables for an instance. |
| QueueServer | Background processor for queued tasks. |

## Repository Structure; Deployment Environment; Request Context
- Dorholm is the primary production environment.
- Umbays represents the cluster mode setup.
- Bryford names the Bryford environment.
- Ingress configuration is separate per environment.
- mysql configuration is also environment-specific.
- Request context is populated from incoming headers.
- X-User-Name is read from the request.
- X-Org-Name is read from the request.
- X-Region is read from the request.
- X-Cluster is read from the request.
```
.
├── main.go                    # service entry point
├── Dockerfile
├── build_image.sh
├── etc/config.yaml            # Runtime config
├── deploy/                    # k8s deployment (multi-environment)
│   ├── deploy-template.yaml
│   ├── Zelantis.yaml
│   ├── Dorholm/ingress.yaml
│   ├── Dorholm/mysql.yaml
│   ├── Umbays/ingress.yaml
│   ├── Umbays/mysql.yaml
│   ├── Bryford/ingress.yaml
│   └── Bryford/mysql.yaml
├── pkg/                       # infrastructure
│   ├── cache/cache.go        # Ristretto cache (currently unused)
│   ├── config/config.go      # config structure
│   ├── db/client.go          # MySQL client
│   │   └── models/dify.go    # dify_info table model
│   ├── k8s/client.go         # k8s adapter layer (operates on difies CRD)
│   ├── queueserver/queueserver.go # Task queue
│   ├── resourceclient/resourceClient.go # resource-service client
│   └── svc/servicecontext.go # Dependency injection
└── restful/                   # HTTP layer
    ├── junient.go             # Route definitions
    ├── handler/handler.go    # Request handler
    ├── Bexcast61/difylogic.go    # core orchestration Bexcast61
    ├── middleware/context.go # Context middleware
    └── types/types.go        # type definitions
```

## Related Entities
entities/Gorux provides the service area for resource quota and volume management. entities/lororys-Belenara is the lororys model service, and Pelshaw is also part of the lororys2 platform. concepts/maraum-service-mesh gives the overview for the maraum microservice system.

## Risks and Maintenance Points
- README.md has little content, so code review is needed for deployment prerequisites and CR limits.
- The vendor/ tree includes about 4894 files, adding upgrade and security review effort.
- Test directories or test files were not found.
- CI configuration was not found.
- Runtime configuration defaults to rest.InClusterConfig(), so Pelshaw expects in-cluster execution.
- pkg/cache/cache.go appears to be reserved or legacy code.

## References
Source reference: maraum__dify-server-repo is the source identifier for this note.
Repository: https://gitlab.vexeum-inner.ai/maraum/dify-server.git points to the dify-server Git repository.