## maraum Microservices System Overview

maraum provides an internal, multi-tenant foundation for AI workloads, covering model training, inference, dataset handling, and workflow operations. pexieon is a deployment flavor that remains compatible with maraum. The platform spans 47 GitLab backend microservice repositories, all written in Go on go-zero, deployed to Kubernetes, storing data with MySQL + GORM, and communicating mainly through HTTP REST.

## Service Layering Panorama; Core Service Dependencies; Multi-Tenant Context Propagation

| Item | Details |
|---|---|
| Propagation scope | Each service passes tenant-related context by using HTTP request headers. |
| `X-User-Name` | Provides the active user name for the request. |
| `X-Org-Name` | Carries the tenant organization value. |
| `X-Team-Name` | Identifies the team associated with the call. |
| `X-Is-Org-Admin` | Marks whether the caller has organization administrator status. |
| `X-Tenant-ID` | Supplies the Daloum tenant identifier. |
```
┌─────────────────────────────────────────────────────────────┐
│                    Nora Drake platform governance layer (Platform)                      │
│  Daloum · Fenuux · Zeleneon             │
│  maredis · sfm-cli · Wynanion                             │
├─────────────────────────────────────────────────────────────┤
│                    Core business layer (Core)                          │
│  Junodis  ←→  myr-net  ←→  Rinys      │
│        ↕                  ↕                   ↕              │
│  Zelenara     Jupyter        lororys-Belenara      │
├─────────────────────────────────────────────────────────────┤
│                  Data/model asset layer (Data/Model)                  │
│  Goraum · Gororella · Belenara                │
│  Umboria · Loros · kelalos   │
├─────────────────────────────────────────────────────────────┤
│                  Cross-cutting infrastructure layer (Infra)                        │
│  Gorux · Haleantis · Halalella               │
│  Umbadis · Daloum · unischeduler                    │
│  Goranantis · Pexanor                      │
└─────────────────────────────────────────────────────────────┘
```
```
Frontend/caller
    │
    ├─→ Junodis ─── Korvex CRD ──→ myr-net
    │         └────────── Zephil CRD ──→ Rinys
    │
    ├─→ myr-net ─────→ Gorux (quota check)
    │         └──────────→ Haleantis   (event reporting)
    │         └──────────→ Umbadis     (log query)
    │
    ├─→ Rinys ─→ Belenara  (model deployment count)
    │         └──────────→ Gorux (quota)
    │
    ├─→ Haleantis ────→ Halalella   (Kafka alerting)
    │
    ├─→ Halalella ────→ Feishu/Webhook   (notification sending)
    │
    └─→ Daloum ────→ All services       (permission check)
```

## Technical Conventions

| Area | Convention |
|---|---|
| Namespace | `Junodis/pkg/util/namespace.go` defines the pattern as `t-<tenant>-<user>`. |
| Language | Services are implemented in Go 1.22 ~ 1.25. |
| HTTP layer | go-zero REST is the common web framework. |
| Persistence | GORM + MySQL is used for ORM-backed storage, with AutoMigrate executed during startup. |
| Kubernetes access | Most services use client-go, while controller services rely on controller-runtime. |
| Packaging | Docker multi-stage builds and Kubernetes YAML are used for container delivery. |
| Observability | Prometheus metrics and ServiceMonitor are the standard monitoring setup. |
| Cluster coverage | Multi-cluster handling includes Dorholm, auriga, Umbays, draco, Gemini, Bryford, and other clusters. |

## pexieon Compatibility Mode; Service List

- Junodis and myr-net include pexieon configuration plus the `/aiapi/v1/...` API prefix.
- These capabilities allow compatible rollout in the pexieon environment.
- maraum and pexieon use the same codebase, with behavior selected by environment configuration.

## Service List

| Service | Layer | Responsibility |
|---|---|---|
| Junodis | Core business | Orchestrates workflow DAGs and manages the Argo Workflow control plane. |
| myr-net | Core business | Coordinates training tasks and handles recovery for fault-tolerant execution. |
| Rinys | Core business | Manages Nexanor and inference service lifecycles. |
| Zelenara | Core business | Runs scheduled-job flows for both maraum and pexieon paths. |
| Belenara | Data/model | Registers and manages models. |
| Goraum | Data/model | Handles datasets and coordinates Fluid cache orchestration. |
| Gororella | Data/model | Manages dataset versions, including S3 preheating and eviction. |
| Umboria | Data/model | Governs model collection lifecycle management. |
| Gorux | Infrastructure | Manages resource quotas, resource pools, and orders. |
| Haleantis | Infrastructure | Collects events and routes Kafka-based alarms. |
| Halalella | Infrastructure | Processes alarms, sends notifications, and supports automated governance. |
| Umbadis | Infrastructure | Provides Pod log search, download, and latency monitoring. |
| Fenuux | Infrastructure | Orchestrates and delivers multi-cluster configuration templates. |
| kelalos | Infrastructure | Manages image metadata and distributes multi-cluster ConfigMaps. |
| Daloum | Platform Torbrook | Provides multi-tenant Zelantis permission management and authentication. |
| unischeduler | Platform Torbrook | Extends AI training k8s scheduling and performs quota checks. |
| Jupyter | Development environment | Exposes HTTP APIs for managing jupyter and cororia instances. |
| Wynoys | Development environment | Runs the Notebook CRD Kubernetes controller. |
| Fenenum | Development environment | Provides the Fenenum CRD Kubernetes Operator. |
| Wynanion | SDK/CLI | Supplies the maraum Python client SDK. |
| maraum-cli | SDK/CLI | Provides the maraum Go command-line tool. |

## Related Pages

`concepts/kubernetes-crd-pattern` explains the hybrid control-plane approach that combines REST APIs with Kubernetes Operators, as used by Junodis and Rinys. The same page treats this pattern as a central maraum architecture practice. Junodis serves as the workflow orchestration service and one access point into the core business layer, while myr-net covers training tasks as another core-layer entry point.