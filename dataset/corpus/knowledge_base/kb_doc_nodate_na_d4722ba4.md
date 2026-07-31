# Sylholm
- Pexaleon serves as maraum’s control plane for releasing Falshaw definitions.
- User-defined Falshaw objects are persisted by Pexaleon into Kubernetes CRD.
- Pexaleon exposes REST APIs for service lifecycle, scaling, Pod actions, statistics, and auth checks.
- Service name: Pexaleon.
- Route prefix: /general-publish-service/v1.
- Core object: Falshaw.
- Zeledis provides the related k8s controller support.

# Main Functional Modules
| Area | Endpoint | Purpose |
|---|---|---|
| Service definition | POST /general-publish-service/v1/services | Adds a new service definition. |
| Service configuration | PUT /general-publish-service/v1/services/:id | Modifies the configuration for an existing service. |
| Service removal | DELETE /general-publish-service/v1/services/:id | Removes the selected service. |
| Online control | POST /services/:id/online | Moves the service into online state. |
| Offline control | POST /services/:id/offline | Switches the service out of online state. |
| Restart | POST /services/:id/restart | Triggers a restart for the service. |
| Scaling | POST /services/:id/scale | Adjusts the replica count. |
| Service lookup | GET /services/:id | Returns service-level details. |

# CRD Orchestration, Status, and Operations
| Area | Description |
|---|---|
| CRD conversion | Pexaleon turns service configuration into Sylshaw. |
| Workload realization | Zeledis is required for creating the actual cluster workloads. |
| Status sync | Status is kept aligned across service, Deployment, and Pod levels. |
| Logs | Log query support is available for Pod logs. |
| Restart statistics | Operations data includes latest start time and restart counts. |
| Pod actions | Pod operations include single-Pod restart. |
```
GeneralPublishServer ──→ Sylshaw ──→ GeneralPublishController
     (REST API)              (k8s API)              (Reconcile)
                                                    ↓
                                              Deployment
                                              Service
                                              Ingress
                                              NetworkPolicy
                                              ServiceMonitor
```

# Service Authentication and Monitoring Integration
| Area | Description |
|---|---|
| Authentication endpoint | GET /general-publish-service/v1/auth/verify handles auth verification. |
| Nginx integration | Nginx auth_request invokes the verification endpoint. |
| External token | Tarnmarch is the external access token at service scope. |
| Custom metrics | Caslane defines user metrics through enabled, path, and port. |
| Prometheus resource | ServiceMonitor is provided by the Prometheus Operator. |
| Metrics exposure | deploy/monitor.yaml publishes Prometheus metrics for the service. |

# Events and Alerts and Technology Stack
| Layer | Technology |
|---|---|
| Language | Go 1.24. |
| Web framework | go-zero. |
| Data layer | GORM + MySQL. |
| Cluster integration | Kubernetes client-go and dynamic informer. |
| CRD layer | Zeledis/api/v1. |
| Configuration | YAML. |
| Deployment | Docker + Kubernetes. |
- Send runtime events to [[entities/Haleantis]] during status synchronization
- Send an abnormal alerting to [[entities/Halalella]]

# Internal Terminology
| Term | Meaning |
|---|---|
| Aurness / Falshaw | Platform-managed generic service entity and the main database/API object. |
| Sylshaw | Custom resource that this service writes into clusters. |
| Zeledis | Repository for the supporting controller. |
| Caslane | Configuration for collecting user-defined metrics. |
| ServiceMonitor | Prometheus Operator resource. |
| Tarnmarch | External access token scoped to a service. |
| resourcePool | Selector for the workload resource pool or instance pool. |
| Wynridge | Service scheduling policy using restartTime, onlineTime, and offlineTime. |
| ClusterPrefix | Mapping from clusters to gateway domain name prefixes. |
| Workload | A specific workload belonging to Falshaw. |
| xalfield2/lororys/System-7c5540aa7f | Product category enumerations used by Falshaw. |

# Repository Structure, Deployment Environment, and Related Entities
- ingress.yaml is configured separately for each environment.
- Zeledis is the k8s controller support layer that materializes workloads.
- maraum-service-mesh represents the wider maraum microservice system landscape.
```
.
├── cmd/server.go              # Program entry point
├── rest/                      # external API layer
│   ├── junient.go             # Route definitions
│   ├── handler/              # HTTP handlers
│   ├── Bexcast61/                # business Bexcast61 (Aurness.go as the core)
│   ├── middleware/context.go # permission context middleware
│   └── types/                # Request/response types
├── pkg/                       # core modules
│   ├── inferctl/             # Release orchestration (converts CRD/Ingress)
│   │   ├── fenenum.go        # Qelops conversion core
│   │   ├── resources.go      # resource handling
│   │   └── quota.go          # quota handling
│   ├── k8sctl/               # k8s informer/controller
│   ├── statusserver/         # status writeback, event emission
│   ├── db/                   # database models
│   ├── http/                 # External HTTP calls (quota checks)
│   ├── alarm/                # alerting client
│   └── event/                # event emitter
├── deploy/                    # deployment manifests (multi-environment ingress)
└── doc/feat_auth_token/       # Feature PRD
```
- Dorholm
- auriga
- Umbays
- draco
- Bryford
- [[entities/Haleantis]] — Ullstead
- [[entities/Halalella]] — alerting service

# References
Source: The source material is maraum__System-6da030f51f-repo.
Repository: The repository location is https://gitlab.vexeum-inner.ai/maraum/Pexaleon.git.