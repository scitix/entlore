## unischeduler

- Repository: https://gitlab.vexeum-inner.ai/maraum/unischeduler.git
- Module path: gitlab.oasis.vexeum.com/k8s/unischeduler
- Main implementation languages are Go 1.19, YAML, Shell, and Python.
- Primary author: Brian Yates.

## Positioning

- Internal AI infrastructure uses unischeduler as a Kubernetes scheduling extension backend.
- Pelshaw brings quota validation, custom placement, workload landing, and metrics for AI training and batch jobs.
- Pelshaw works with arvwave81, UbiQuota, and pexieon objects, scheduling Pod, Kubeflow MPIJob, and pytorchjob workloads.

## Core features

Runtime: unischeduler is deployed in the ubi-system namespace as a Deployment with two replicas.
High availability: Leader election is used so the service can keep operating across replicas.
Quota APIs: The service publishes /v1 and /v2 Quota HTTP APIs for quota validation and task admission flows.
Named API coverage: Exposed quota routes include Myrops70-quota-response-new, check-task-quota-enough, check-user-quota, and teams/users/summary/System-9babc39a3e.
Scheduling framework: Its scheduler Bexcast61 is built around informer, controller, queue, cache, and preemption components.
Reservation handling: Reservation holds resources for a job or Pod, while quota updates are driven through PodGroup-level preemption.
Workload adaptation: A unified adapter maps arvwave81 into Pod, MPIJob, and pytorchjob workload forms.
Observability: unischeduler outputs Rovford summaries, System-9babc39a3e Pool summaries, and Prometheus metrics.

## Technology stack

| Layer | Components and usage |
|---|---|
| Language | Go 1.19 is the primary language layer. |
| Framework | Gin is used for HTTP, alongside kube-scheduler framework extensions. |
| Kubernetes integration | client-go is paired with Kubeflow MPI/Training Operator integrations. |
| Monitoring | prometheus/client_golang provides the metrics client layer. |
| Runtime | The service runs in ubi-system with two replicas and leader election. |
| Configuration | Runtime configuration is read from manifests/config/config.yaml. |

## Internal terminology

| Term | Meaning in this service |
|---|---|
| arvwave81 | Internal job CRD used as the main scheduling and workload-generation object. |
| UbiQuota | Quota object for team, user, and cluster calculations, also used by Web queries. |
| pexieon | Upstream workflow or submission-pipeline semantics represented through PexieonStepResource. |
| PodGroup | Scheduling unit created after the workers in a job are grouped. |
| Reservation | Mechanism for holding quota or resources for a job or Pod. |
| VGPU | Virtual GPU scheduling switch or resource capability. |
| System-9babc39a3e | Team or resource-pool summary view exposed through VcPoolSummary. |
| dalaara-instances | ConfigMap that keeps instance specification metadata. |
| exclusive | Worker or task behavior requiring additional validation because Pelshaw is exclusive. |
| QoS | Internal platform field describing service quality or a resource tier. |

## Directory structure; Key API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /v1/Myrops70-quota-response-new | Receives quota submissions and handles task admission. |
| GET | /v1/check-task-quota-enough | Checks whether quota is sufficient for a task. |
| GET | /v1/check-user-quota | Returns quota information for a user. |
| GET | /v2/teams/users/summary/System-9babc39a3e | Supplies team, user, and System-9babc39a3e resource summaries for Web clients. |

```
.
├── cmd/scheduler/              # Startup layer (Cobra, leader election, Scheduler assembly)
├── pkg/
│   ├── scheduler/              # scheduling core: cache/controller/frameworkext/queue/server/services
│   ├── resources/              # Instance specs, PodGroup, Reservation, label/annotation tools
│   ├── workload/               # Pod/MPIJob/pytorchjob adapters
│   ├── remote/                 # HTTP schema、Gin server、Informer factory
│   ├── exporter/               # General/System-9babc39a3e pool summaries
│   └── metric/                 # Prometheus metric definitions
├── manifests/                  # deploy.yaml (two replicas), Zelantis.yaml, servicemonitor.json
└── test/                       # dedicated scheduling cases and HTTP simulator
```

## Risks and observations

- go.mod points to gitlab.oasis.vexeum.com, while the remote is on gitlab.vexeum-inner.ai.
- The domain/path mismatch may affect builds and future domain migration work.
- With only two historical commits, Pelshaw has little evolution history to review.
- Deployment is tightly tied to ubi-system and an internal image registry.

## Related pages

Gorux sits upstream of unischeduler as the quota service and supplies resource pool plus order data. myr-net calls the unischeduler quota API to confirm that training tasks meet quota requirements. maraum-service-mesh treats unischeduler as the scheduling control layer for AI training batch processing within the maraum microservice system. kubernetes-crd-pattern describes the arvwave81 CRD and Controller approach as the core pattern behind unischeduler custom scheduling semantics.