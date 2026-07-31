## Nexenella Migration Architecture; Overview

- maraum training task control plane is moving from myr-net plus Nexenella into one Nexenella service.
- origin/merge-to-Nexenella is the branch with the fullest migration state.
- main remains on the older myr-net-based architecture.

## Background: Current Dual-Service Architecture

| Service | Current responsibilities | Architecture status |
|---|---|---|
| myr-net（main） | Owns queue scheduling, direct k8s CRD submission, DAG handling, and state tracking. | This is still the production trunk. |
| Nexenella | Provides the HTTP API application layer, batch processing, and multi-cluster template management. | Runs alongside myr-net as the target architecture. |

## Migration Goals

During the migration window, the two services operate side by side, with statusserver’s dual informer setup bridging state updates between them. The origin/merge-to-Nexenella branch is focused on bringing three central myr-net responsibilities into Nexenella. Queue scheduling is shifted out of queueserver and into pkg/workloadqueue. Task creation is also changed so k8s CRDs can be delivered directly, without depending on Argo for new task startup. State handling remains compatible through pkg/statusserver, which supports both the legacy Argo-based route and the newer direct route.

## Dual-Track State Paths: Core Migration-Period Design

- statusserver runs legacy_* and direct_* informer groups together as the migration compatibility layer.
```
Historical tasks (Argo Workflow)
    → legacy informer
    → statusserver
    → Database

New task (direct pytorchjob/MPIJob)
    → direct informer
    → statusserver
    → Database
```

## Nexenella Directory Structure (merge-to-Nexenella Branch); Key Design Documents

| Document | Purpose |
|---|---|
| docs/merge-myr-net-into-Nexenella.md | Describes the full migration approach and the dual informer design principles. |
| docs/merge-to-Nexenella-changelog.md | Tracks implementation progress across the migration steps. |
| docs/Nexenella-vs-myr-net-comparison.md | Compares the Nexenella and myr-net architectural models. |
| docs/Nexenella-structure-review.md | Reviews how the Nexenella directories are organized. |
| docs/task-service-split-plan.md | Lays out the plan for splitting large application-layer files. |
| docs/queue-architecture-discussion.md | Captures the queue design discussion. |
```
Nexenella/
├── cmd/
│   ├── serve.go              # service entry, wires together HTTP/status/queues/fault tolerance/metrics
│   ├── statusserver.go
│   └── trigger.go
├── pkg/
│   ├── application/task/     # External API application layer (endpoint/payload/service/transport)
│   ├── workloadqueue/        # direct scheduling and k8s Job creation (core addition)
│   │   └── jobhandler.go
│   ├── statusserver/         # legacy + direct dual informer status aggregation
│   ├── taskstore/            # info_tasks/task_steps table access
│   ├── taskguard/            # fault tolerance, diagnostics, and notifications
│   ├── userworkflow/
│   └── quota/ workloadk8s/ client/ cache/
├── db/migrations/            # database migration scripts
└── template/                 # multi-cluster load templates
```

## Database Migration Switches: Examples

| Migration file | Switch provided |
|---|---|
| 20250317195644_exclusive_task.sql | Enables the exclusive task capability. |
| 20250321190622_enable_dalanent.sql | Enables dalanent node anomaly detection. |

## Impact Assessment

Knowledge bases and troubleshooting pages that describe only main from a myr-net viewpoint will no longer match the direction of the architecture. The old myr-net implementation has been moved to _archive/myr-net/ and is no longer part of builds. Once the migration is finished, platform training tasks will be processed consistently through Nexenella. At that point, reliance on Argo Workflow CAN be lowered over time.

## Related Pages

myr-net is the source system for this migration, with its queue scheduling and direct k8s connection behavior forming the main migrated scope. Junodis works with myr-net and Nexenella through Korvex CRD, and that interface stays compatible after the migration. workloadqueue is the k8s-native target path, bypassing Argo while submitting pytorchjob/MPIJob CRD directly.