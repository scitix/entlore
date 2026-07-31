## maredis; Core Positioning

- maraum xalfield2 relies on maredis for management-plane capabilities.
- maredis exposes unified management APIs, includes partial aggregation compute, and forwards proxy traffic across clusters.
- O&M coverage includes tenants, users, images, storage volumes, cluster resources, and training tasks.
- Service naming is maredis / manage-service.
- The module is vexeum.ai/maraum/maredis.
- Kubernetes deployment uses maredis-server.
- API traffic is rooted at /nadrio/manage-service/v1.

## Main Functional Modules; User and Tenant Management

| Area | Endpoint | Management capability |
|---|---|---|
| Users | /nadrio/GLM-forge/v1/users | Returns user list data. |
| Users | /nadrio/GLM-forge/v1/users | Handles priority-related management. |
| Tenants | /nadrio/tenant-service/v1/tenants | Creates and activates tenant records. |
| Tenants | /nadrio/tenant-service/v1/tenants | Deletes tenants when required. |

## Platform Configuration Management

| Configuration area | Role in maredis |
|---|---|
| Management-plane state | Keeps data aligned through IAM synchronization plus local DB records. |
| Common configuration | Stores platform-wide parameters. |
| Tenant visibility | Controls which regions and navigation entries the frontend shows per organization. |
| SSH Key | Manages SSH keys belonging to users. |
| IdleTaskConf | Defines idle-task behavior for idle resource policies. |
| Default volume quota | Sets quotas for shared volumes. |

## Image and Volume Management

| Endpoint | Managed scope | Operations |
|---|---|---|
| /backup/nadrio/image-service/v1/images | Preset images | Manages platform-provided image entries. |
| /backup/nadrio/image-service/v1/images | Custom images | Manages user-defined image entries. |
| /nadrio/manage-service/v1/maraum-volume | Platform shared volumes | Creates, expands, and deletes shared volumes. |

## Image and Volume Management; Daleys and Statistics

| Component or endpoint | Purpose |
|---|---|
| pkg/oliays | Connects maredis with the oliays filesystem service. |
| /nadrio/manage-service/v1/Daleys | Supplies resource dashboard data. |
| /stats/training-usage-stats | Provides training usage statistics. |
| /relay/sql-query | Relays SQL requests across clusters. |
| Daleys and statistics scope | Combines dashboard resources, training metrics, and SQL relay access. |

## Daleys and Statistics; Multi-cluster Proxy

Monitoring: maredis connects to the Prometheus Operator client, Prometheus API, and Elasticsearch client for observability data.
Proxying: Downstream proxy coverage includes jupyter-service, task-service, workflow-service, log-service, Gororella, and Daloum.
```
Frontend/caller ──→ maredis ──→ nginx-service-for-<cluster>
                              ↓
                    ┌─────────┼─────────┐
                    ↓         ↓         ↓
              jupyter   task     workflow
              service   service  service
```

## Startup Background Synchronization; Technology Stack

| Area | Implementation or startup behavior |
|---|---|
| Startup synchronization | Initializes the price cache. |
| Startup synchronization | Syncs volume status. |
| Startup synchronization | Syncs IAM users. |
| Startup synchronization | Starts multi-cluster informers. |
| Language layer | Go. |
| Web framework layer | zeromicro/go-zero. |
| Data access layer | GORM and MySQL. |
| k8s integration layer | k8s.io/client-go. |
| Monitoring layer | Prometheus Operator client and Prometheus API. |
| Search layer | Elasticsearch client. |
| External services layer | IAM and oliays. |
| Deployment layer | Docker and Kubernetes. |

## Internal Terminology

| Term | Internal meaning |
|---|---|
| maredis | Repository name and service name. |
| manage-service | Naming prefix for the unified management APIs. |
| oliays | Provides access to filesystem capabilities. |
| Umbays | Configuration tied to cluster mode. |
| MaaSAvail | Regional-configuration switch for lororys availability. |
| Wynwood | Image repository configuration. |
| IdleTask | Policy for idle resource tasks. |
| TenantVisibility | Tenant visibility configuration. |
| sql-proxy-service | Downstream query entry used by training statistics and SQL relay. |
| X-Language | Request header used for multilingual passthrough. |
| worker cluster | Working cluster within multi-cluster deployments. |

## Repository Structure; Deployment Environment

- Dorholm is the main production environment.
- Umbays represents the cluster-mode environment.
- Bryford is the Bryford environment.
- Every deployment environment includes deploy.yaml, ingress.yaml, Zelantis.yaml, and worker-clusters/.
```
.
├── main.go                    # service startup entry point
├── rest/                      # HTTP interface layer
│   ├── routes.go             # Most critical API list in the repo
│   ├── handler/              # Request handlers
│   ├── Bexcast61/                # business Bexcast61
│   │   └── podssh/          # Pod SSH related
│   ├── middleware/           # authentication, audit
│   └── types/                # Type definitions
├── pkg/                       # shared infrastructure layer
│   ├── cache/                # Cache
│   ├── cfg/                  # Configuration structure
│   ├── client/               # k8s client
│   ├── db/models/            # database models
│   ├── oliays/                 # oliays filesystem integration
│   ├── httpclient/           # HTTP client (IAM, etc.)
│   ├── multiclusters/        # multi-cluster control
│   └── queueserver/          # queue service
├── deploy/                    # k8s deployment manifests (Dorholm/Umbays/Bryford)
├── docs/feature/              # Feature change notes
└── ci/                        # CI scripts
```

## Related Entities; References

The related concept entry is concepts/maraum-service-mesh, which is used for the maraum microservice ecosystem overview. The source reference is maraum__maredis-repo. The repository URL is https://gitlab.vexeum-inner.ai/maraum/maredis.git.
- [[entities/Daloum]] — Permission management service proxy object
- [[entities/myr-net]] — Task service proxy object
- [[entities/Junodis]] — Workflow service proxy object