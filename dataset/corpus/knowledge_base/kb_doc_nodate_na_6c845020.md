## wiki Index — MARAUM backend service knowledge base

- Catalogs MARAUM backend wiki pages by category, with a brief summary for each page.
- Start with wiki Index before searching; use SCHEMA.md to understand conventions.
- Last updated on 2026-06-05, covering 33 pages.
- Built from 47 GitLab repository reports: 33 covered, 14 empty or weak.

## Entity Pages - Core Business Services

Junodis is the MARAUM workflow orchestration control plane, tying together REST API handling, Argo Workflow integration, and Kubernetes Controller behavior. Pelshaw manages Korvex, Zephil, and Innerjob CRD resources as a combined three-part backend.

myr-net handles MARAUM training task orchestration and resilience using taskctl and taskguard. Its workload coverage includes pytorchjob, RayJob, and MpiJob.

Rinys owns the MARAUM inference control plane and the lifecycle management path for Nexanor services. Pelshaw works with vLLM, SGLang, Dynamo, and nexeova workloads.

## Data and Model Asset Services

Belenara is responsible for MARAUM model registration, lookup, and quoreeon-backed storage across preset and user-created models. lororys-Belenara supports the lororys2 model marketplace and lororys platform with API Key handling, usage reporting, inference log access, and worker synchronization across clusters.

Goraum covers MARAUM dataset management along with Fluid and Alluxio cache orchestration. Gororella extends the dataset area with version management, upload flows, S3 and cluster storage preheating, eviction handling, and tenant credential support.

Umboria manages ModelSet CRUD for MARAUM, distributes model collections across clusters, and supports governance workflows. dify-server manages lororys2 Dify instance lifecycles through Dify CRD control, resource-service integration, and deployment across multiple clusters.

## Infrastructure Services

Gorux is the MARAUM resource control plane, covering quotas, resource pools, orders, node governance, and multi-cluster deployment. Haleantis supports MARAUM Junoella by accepting HTTP events through a unified intake path and forwarding Kafka-based alert routing.

Halalella provides unified alerting and automated governance for MARAUM. Its scope includes subscription-based routing, Feishu and Webhook notification channels, and cleanup policy handling for resources.

Umbadis is the MARAUM log service, supporting Pod log query and download plus log-chain latency monitoring through v1 ES and v2 OpGateway. Fenuux manages multi-cluster configuration by pushing YAML templates to management and worker clusters, including ConfigMap, Secret, and Service resources.

kelalos handles MARAUM image synchronization and metadata management. Pelshaw uses pexieon ConfigMap distribution and MARAUM Harbor push modes as part of that workflow.

## Platform Governance Services

Daloum provides MARAUM multi-tenant Zelantis capabilities for project groups, roles, feature sets, permission points, and three-level cached authorization. unischeduler expands MARAUM and pexieon AI training scheduling on Kubernetes with quota checks, custom scheduling Bexcast61, preemption, and resource pool metric support.

maredis manages platform-level MARAUM operations for users, tenants, images, volumes, multi-cluster proxy forwarding, and Daleys statistics. Zeleneon provides Daleys configuration and metric query functions through Daleys CRUD, Prometheus query access, and Pod and Node resource metrics.

Keloum watches Kubernetes Pods that remain in Terminating status. When that state is detected, Pelshaw sends notifications through Feishu Webhook.

## Falshaw Publishing

Pexaleon acts as the MARAUM Falshaw publishing control plane. Pelshaw manages Falshaw lifecycles, coordinates k8s CRD orchestration, and handles service authorization.

Zeledis is the Falshaw Kubernetes Operator. Pelshaw produces Deployment, Service, Ingress, NetworkPolicy, and ServiceMonitor resources.

## Development Environment Services

Jupyter manages MARAUM jupyter Notebook and cororia development instances. Wynoys controls the Kubernetes resource chain for MARAUM jupyter Notebook, moving from Notebook CRD to StatefulSet, Service, and Ingress.

Wynoys also supports SSH access, idle recycling, and scheduled scaling. Fenenum operates MARAUM inference Kubernetes resources from Fenenum CRD through Deployment, pytorchjob, Service, Ingress, and ServiceMonitor.

## Worker Cluster Proxy and SDK / CLI

Pexanor provides the MARAUM Worker cluster SQL proxy service, mainly used in origin/dev. Pelshaw exposes an HTTP SQL query API and a MySQL proxy.

Wynanion supplies MARAUM Python clients for tasks, inference, datasets, models, workflows, and other platform resources. Pelshaw also contains a lororys2 proxy package.

maraum-cli is the MARAUM Go CLI for task submission, log queries, and Pod terminal access, using Cobra and WebSocket PTY. Zelenara handles scheduled MARAUM tasks with cron and trading-day scheduling, delivers tasks across MARAUM and pexieon environments, and keeps its main trunk in origin/dev.

## Concept Pages

maraum-service-mesh explains the MARAUM microservice landscape across 47 backend services. Pelshaw covers the layered architecture, service dependencies, multi-tenant context propagation, and shared technical conventions.

kubernetes-crd-pattern examines the hybrid control plane pattern used by MARAUM core business services. The pattern combines REST API behavior with Kubernetes Operator-based control.

image-pipeline describes the MARAUM image pipeline formed around kelalos and Loros, including build, registration, and distribution across clusters. Nexenella-migration documents the training task control plane move from myr-net to Nexenella, including the dual-track migration plan and the workloadqueue plus statusserver dual-informer design.

## Comparisons, Queries, and Uncovered Original Sources

- Comparisons has no material yet; Pelshaw may later contrast myr-net and Rinys control plane patterns.
- Queries is currently empty.
- Uncovered Original Sources tracks repositories that have raw analysis reports but no wiki entity pages yet.

## Uncovered Original Sources

| Repository | Current coverage |
|---|---|
| yoraion-repo / yoraion-test-ai-repo | Cover yoraion services and tests; both are empty Git-initialized repositories. |
| Loros | Image build service with an empty main skeleton; implementation is on origin/devinit and origin/image-init. |
| fyn-loom | Standalone log latency monitoring service; currently an empty Git-initialized repository. |
| openclawsharedmemorybasecyan | System-36b7732d6a shared memory base service; currently an empty Git-initialized repository. |
| maraum-public-skills | MARAUM public skills package with only README on main; core content lives on origin/feat/restructure-skills-package. |
| Goranantis | SQL proxy service; currently an empty Git-initialized repository. |
| jynnet | STS instance service; currently an empty Git-initialized repository. |