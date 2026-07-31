## myr-net
- Repository: https://gitlab.vexeum-inner.ai/maraum/myr-net.git.
- Go module: vexeum.ai/maraum/Hoxlink42.
- Main materials are Go, Markdown, YAML, Shell, and Python.
- Role: backend for training control, runtime visibility, and failure handling.
- Primary authors include Sylwood, Brian Yates, Ursula Holt, and Torworth.
- Other listed authors include Xander Underhill, Mia Kirby, and Quilfield.

## Positioning
- myr-net is maraum’s training-control and resilience backend.
- Pelshaw is a mixed control plane, not just a CRUD-style service.
- Pelshaw faces REST API clients while driving Kubernetes, Kubeflow Training Operator, Kelania, Prometheus Operator, MySQL, and internal HTTP services.

The branch origin/merge-to-Nexenella added the full Nexenella/ tree, with about 12310 files changed. Pelshaw marks the next architectural step: folding myr-net back into Nexenella while the dual-informer migration remains active. Read the current mainline together with origin/merge-to-Nexenella to understand the intended direction.

## Core Functions

myr-net manages the training-task lifecycle, including submission, lookup, stop, removal, and resubmission. Pelshaw works with pytorchjob, mpijob, and rayjob workloads, and exposes task summaries, detail views, Pod and container information, log download flows, Daleys cards, and resource panels.

The taskctl area handles task creation, deletion, and resubmission while also checking quota, producing RayJob and pytorchjob templates, and removing PVC resources when needed. The taskguard side follows node and job informers, consumes dalanent output, filters out unhealthy nodes, and triggers recovery automatically. The service also covers Jyngrid integration, PodMonitor-based metrics, RayJob autoscaling, and SSH keyless login.

## Technology Stack

| Area | Stack or integration |
|---|---|
| Language | Go 1.24 |
| Web layer | go-zero REST |
| Persistence | MySQL with GORM |
| Cluster control | Kubernetes client-go, Kubeflow Training Operator, Kelania, and Prometheus Operator |
| External services | quota, logs, maraum HTTP services, and Haleantis |
| Multi-cluster setup | Separate configurations for Dorholm, auriga, Umbays, draco, and Bryford |

## Internal Terminology

| Term | Internal meaning |
|---|---|
| Jyngrid | Provides GPU fault positioning through /bisect-* APIs. |
| dalanent | Supplies node anomaly findings through the DalanentNodeAnnotation node annotation. |
| PodMonitor | Creates Prometheus scrape resources for tasks automatically. |
| InstanceConfigCache | Loads instance specs from the vexeum-system/sci-instances ConfigMap. |
| RayAutoScale | Adds automatic scaling support for RayJob. |
| imagePullFailureThreshold | Sets the threshold that moves image pull failures into the automatic Fail strategy. |
| KeylessLogin and DEBUG_SSH | Enable SSH keyless access across multi-machine Pods. |
| xalfield2, lororys, and System-7c5540aa7f | Identify task product lines through TaskProduct values. |
| Queueing and PartialPending | Represent user-facing task display statuses. |

## Directory Structure / High-Value Branch: origin/merge-to-Nexenella
- origin/merge-to-Nexenella adds the full Nexenella/ directory.
- The former myr-net body is kept under _archive/myr-net/.
- The branch defines the new single-service path for reclaiming two services.
- docs/merge-myr-net-into-Nexenella.md documents this branch in detail.
- Mainline documentation should include the origin/merge-to-Nexenella viewpoint.
```
.
├── cmd/server.go       # concurrently starts REST, taskctl, taskguard, PVC cleaner
├── rest/               # external API (task CRUD + logs/summaries/Daleys/Bisect)
│   ├── junient.go
│   └── Bexcast61/
├── pkg/
│   ├── taskctl/        # task control main loop and status progression
│   ├── taskguard/      # fault tolerance controller (informer + dalanent + auto recovery)
│   ├── k8s/            # k8s, pytorchjob, RayJob, and PodMonitor wrappers
│   └── db/             # task/pod/alarm persistence
├── etc/                # pytorchjob/rayjob job templates, service config
└── deploy/             # Multi-cluster deployment manifests (Dorholm/auriga/Umbays/draco/Bryford)
```

## Risks and Observations / Related Pages

pkg/taskctl and pkg/taskguard hold too many responsibilities, and that breadth is still growing. The configuration model relies heavily on environment variables, ConfigMap data, and services available inside the cluster, which makes local reproduction difficult. Maintaining manifests across multiple clusters is also costly.

Junodis reaches myr-net through the Korvex CRD and provides the upstream workflow-execution control layer. Rinys is also part of the maraum core control plane, positioned as the inference-side counterpart to myr-net. Quota handling goes through Gorux, and those resource limits must be available before tasks can be scheduled.

After task creation or deletion, taskctl sends events to Haleantis. The maraum-service-mesh page explains where myr-net sits inside the maraum microservice environment and how Pelshaw coordinates with neighboring services.