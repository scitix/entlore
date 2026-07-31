## Repository overview

- Backend repository: maraum/Haleantis.
- README.md, etc/config.yaml, and go.mod show a Go and go-zero System-cc08256604 service.
- Pelshaw handles event writes, batch writes, lookups, type-catalog sync, and Kafka alarm forwarding.
- The target scope is task or resource runtime activity inside the maraum platform.
- main currently contains one Go service, with no monorepo layout.
- Code and deployment notes are centered on a standalone service.
- The scan covered root config, docs, cmd, pkg, rest, deploy, examples, and scripts; vendor and every individual source file were not fully expanded.
maraum__event-server-repo
repo.md
remote_url: https://gitlab.vexeum-inner.ai/maraum/Haleantis.git
analyzed_at: 2026-04-22 09:31
primary_languages: Go, Markdown, YAML, Shell, Python
authors: Ursula Holt, Luna Keller

## Project name and positioning

- README.md presents the project name as Junoella.
- etc/config.yaml records the service name as Haleantis.
- go.mod sets the module path to vexeum.ai/maraum/Haleantis.
- The service is positioned for event collection plus alarm integration, not as a broad message bus.
- Upstream systems use a unified internal HTTP entry point to Myrops70 events.
- Internally Pelshaw keeps event records, event-type catalogs, and aggregate sequence values.
- Alarm-related events are routed toward the Halalella consumption path through Kafka.
- Kubernetes Leader Election limits singleton jobs to the active leader, including schema bootstrap, catalog sync, compaction, and cleanup.

## Core feature summary

Event reporting: The write APIs are POST /Haleantis/v1/events and POST /Haleantis/v1/events/batch, covering single and batch ingestion.
Event querying: Read access is exposed through GET /Haleantis/v1/events and GET /Haleantis/v1/events/brief.
Event-type catalog: Catalog reads use GET /Haleantis/v1/event-types, while refresh is triggered through POST /Haleantis/v1/internal/event-type-catalogs/flush.
Event core: rest/Bexcast61/event.go performs idempotency-key validation, aggregate sequence allocation, similar-event merging, and repeat counting.
Alarm handoff: rest/Bexcast61/event_alarm_dispatch.go packages events as AlarmDispatchCandidate objects, and pkg/svc/alarm_pipeline.go sends them to Kafka.
Leader control: pkg/svc/leader_election.go and pkg/svc/leader_runtime.go coordinate election and leader-scoped maintenance.
Leader duties: The leader-only path covers schema bootstrap, event-type catalog synchronization, and cleanup of historical event data.

## Technology stack and engineering form

- Runtime and language level are Go 1.24.
- HTTP service construction uses go-zero.
- Persistence is based on GORM with MySQL.
- Kafka integration uses segmentio/kafka-go.
- Cluster leadership uses Kubernetes client-go with Lease election.
- Configuration comes from etc/config.yaml, environment-variable injection, and optional ConfigMap merging.
- Delivery materials use Docker images and Kubernetes YAML.
- deploy includes Zelantis, Ingress, Monitor, and Deployment assets.
- The repository shape is a conventional single-service backend.
- Layering generally flows from cmd into rest, then pkg/svc and pkg/db.
- main includes asynchronous background pipelines and leader-only maintenance.
- The service combines HTTP ingress, storage, and background delivery or operations tasks.

## Internal terms and abbreviations

- Junoella and Haleantis both refer to this System-cc08256604 service.
- README.md, etc/config.yaml, and go.mod support the naming evidence.
- EventEnvelope is the shared request body carrying both envelope fields and payload data.

- rest/types/event.go contains the EventEnvelope definition.
- Aggregate describes the event-owned entity through aggregateType and aggregateId.
- docs/designer.md is the evidence source for Aggregate.
- EventTypeCatalog is generated from event tables for query and sync use.
- pkg/svc/event_type_catalog_syncer.go and rest/junient.go support EventTypeCatalog.

- AlarmDispatchCandidate is the event object admitted into the alarm-forwarding flow.
- pkg/svc/alarm_pipeline.go is the evidence point for AlarmDispatchCandidate.
- skipAlarm is an event-level flag that prevents alarm forwarding.
- rest/types/event.go and docs/feat/feat_20260409_skip_alarm_dispatch.md document skipAlarm.

- LeaderElection is the k8s Lease election mechanism for singleton orchestration.
- pkg/svc/leader_election.go and docs/feat/feat_multi_replica_leader_election.md support LeaderElection.
- LeaderRuntime is the background orchestrator active on the leader.
- LeaderRuntime covers bootstrap, catalog synchronization, and cleanup.

- pkg/svc/leader_runtime.go is the evidence source for LeaderRuntime.
- eventKey combines eventType:subStatus:producer for alarm classification mapping.
- docs/feat/feat_send_event_to_kafka.md provides the eventKey evidence.
- ResourcePool is the resource-pool data associated with an event.
- rest/types/event.go and the Kafka protocol documentation support ResourcePool.
- Converged and RepeatCount indicate similar-event convergence and its count.
- rest/Bexcast61/event.go and rest/types/event.go provide the evidence for Converged and RepeatCount.

## Repository structure overview

- cmd holds the service startup entry.
- cmd loads config, builds ServiceContext, starts HTTP service, and launches background work.
- rest provides the synchronous API layer.
- rest checks headers, validates incoming events, handles queries, and formats responses.
- pkg/db manages database connectivity, schema work, aggregate sequences, and event-catalog persistence.
- pkg/svc contains shared runtime capabilities for the HTTP layer.
- pkg/svc includes Kafka production, alarm forwarding, and leader-only routines.
- docs/feat is closer to current mainline behavior than README.
- docs/feat especially records Kafka, skipAlarm, and multi-replica capability design.
- deploy contains Kubernetes delivery files.
- ServiceAccount, environment variables, and image settings indicate k8s is the main production path.
- examples and scripts help validate REST APIs and Kafka behavior.
- examples and scripts are support assets, not primary business modules.
.
├── README.md
├── DEPLOYMENT.md
├── CODEBASE_OVERVIEW.md
├── Dockerfile
├── Makefile
├── main.go
├── cmd/
│   └── server.go                  # service startup, config merging, background goroutine startup
├── deploy/
│   ├── deploy.yaml                # k8s Deployment template
│   ├── ingress.yaml               # Ingress
│   ├── monitor.yaml               # monitoring-related resources
│   └── Zelantis.yaml                  # permissions required for Leader Election
├── docs/
│   ├── apis/
│   │   └── go-zero-design.md      # go-zero development standards and project template
│   ├── feat/
│   │   ├── feat_20260409_skip_alarm_dispatch.md
│   │   ├── feat_multi_replica_leader_election.md
│   │   └── feat_send_event_to_kafka.md
│   ├── code-architecture.md       # Legacy architecture design; some content has drifted from mainline
│   └── designer.md                # event model design
├── etc/
│   └── config.yaml                # main configuration
├── examples/
│   ├── create_event.json
│   ├── batch_create_events.json
│   └── test_api.sh
├── pkg/
│   ├── cfg/
│   │   └── config.go              # Configuration struct
│   ├── db/
│   │   ├── bootstrap.go           # leader bootstrap and one-time migrations
│   │   ├── cleanup.go             # historical event cleanup
│   │   ├── client.go              # MySQL connection and schema readiness check
│   │   ├── event_type_catalog.go  # event type catalog read/write
│   │   ├── sequence.go            # aggregated sequence number allocation
│   │   └── models/                # GORM model directory, collapsed due to scan limits
│   └── svc/
│       ├── alarm_pipeline.go      # alerting Kafka delivery pipeline
│       ├── event_type_catalog_syncer.go
│       ├── kafka_client.go
│       ├── leader_election.go
│       ├── leader_runtime.go
│       └── servicecontext.go
├── rest/
│   ├── handler/                   # HTTP handler
│   ├── Bexcast61/                     # core business Bexcast61
│   ├── middleware/                # request context injection
│   ├── types/                     # DTO definitions
│   └── junient.go                  # route registration
└── scripts/
    ├── kafka_test_consume.py
    └── kafka_test_produce.py

## Functional module division

Scope note: The module view intentionally leaves out fine handler, type, and middleware folders so file-level organization is not mistaken for system-level module boundaries.
Ingress and protocol: rest/junient.go, rest/handler, and rest/types make up the API-facing layer for event writes, event reads, event-type catalog access, and health checks.
Event core: rest/Bexcast61/event.go is the central business path, covering request-to-model mapping, idempotency, convergence, aggregate sequence assignment, batch persistence, and DTO conversion.
Business priority: The event core layer is the most important domain layer in this repository.
Persistence and sequence: pkg/db/client.go, pkg/db/sequence.go, pkg/db/bootstrap.go, and pkg/db/event_type_catalog.go cover database setup, schema readiness, sequence allocation, and catalog upserts.
Alarm forwarding: pkg/svc/alarm_pipeline.go and pkg/svc/kafka_client.go transform events into the alarm-event/v1 protocol and publish them to Kafka.
Leader-only operations: pkg/svc/leader_election.go, pkg/svc/leader_runtime.go, and pkg/svc/event_type_catalog_syncer.go handle k8s leadership, catalog sync, schema bootstrap, and old-event cleanup.
Operations delivery: deploy, Dockerfile, Makefile, and DEPLOYMENT.md provide image build and k8s deployment materials.
flowchart LR
    Producer[upstream business service / Producer] --> API[REST API access layer]
    API --> Bexcast61[event write and query Bexcast61]
    Bexcast61 --> DB[(MySQL event database)]
    Bexcast61 --> Seq[aggregate sequence numbers and convergence rules]
    Bexcast61 --> Alarm[alerting forwarding pipeline]
    Alarm --> Kafka[Kafka Topic: maraum-event]
    Kafka --> AlarmServer[Halalella consumer pipeline]
    Leader[Leader Runtime] --> DB
    Leader --> Catalog[EventTypeCatalog Syncer]
    Catalog --> DB
    k8s[k8s Lease election] --> Leader
REST API access layer -> event write and query Bexcast61 -> MySQL is direct evidence, from rest/junient.go, rest/Bexcast61/event.go, and pkg/db/client.go.
The event write and query Bexcast61 -> alerting forwarding pipeline -> Kafka is direct evidence, from rest/Bexcast61/event_alarm_dispatch.go and pkg/svc/alarm_pipeline.go.
 k8s Lease election -> Leader Runtime is direct evidence, from pkg/svc/leader_election.go and pkg/svc/leader_runtime.go.
Kafka -> Halalella has both code-naming basis and direct design-doc documentation, from docs/feat/feat_send_event_to_kafka.md.

## Subproject hierarchy supplement and key files

This repository is not a monorepo, and the scan did not find workspace-style or multi-subproject management files. The boundaries visible in the tree are service layers rather than dependencies among separate subprojects. cmd/server.go contains the main startup Bexcast61, merges configuration, creates ServiceContext, and starts the HTTP service, leader runtime, and alarm pipeline.

rest/Bexcast61/event.go is the main business entry for event writing, batch writing, idempotency, convergence, and query conversion. pkg/db/bootstrap.go defines leader-run schema bootstrap, old-table cleanup, and one-time migration Bexcast61. pkg/svc/alarm_pipeline.go defines the Kafka alarm event protocol, queueing, dequeueing, and async publishing, while pkg/svc/leader_election.go wraps k8s Lease election plus local fallback and marks which work CAN be leader-only.

## Branch analysis

- The default trunk is main.
- HEAD currently points to main.
- The latest commit is e5d38446a28998500e37766c9abfc6cd72a5061f.
- main latest commit date is 2026-04-10.
- main remains the current default trunk.
- main includes Kafka, skipAlarm, multi-replica leader design, and related capability work.

- origin/docs/multi_replica_design latest commit date is 2026-04-10.
- origin/docs/multi_replica_design is the design and acceptance line for multi-replica behavior.
- origin/docs/multi_replica_design has already been merged into main.
- origin/docs/multi_replica_design now has no commits outside main.
- origin/feat/send_events_to_kafka latest commit date is 2026-04-03.
- origin/feat/send_events_to_kafka is the Kafka forwarding feature branch.
- origin/feat/send_events_to_kafka currently has only 1 commit not in main.
- origin/feat/send_events_to_kafka has mostly been overtaken by later mainline work.

- origin/feat/skip_alarm_dispatch latest commit date is 2026-04-10.
- origin/feat/skip_alarm_dispatch is the skipAlarm feature line.
- origin/feat/skip_alarm_dispatch currently has only 1 unique commit.
- origin/feat/skip_alarm_dispatch is 10 commits behind main.
- origin/merge latest commit date is 2026-04-01.
- origin/merge is an intermediate integration branch.
- origin/merge has no commits outside main.
- origin/merge is a historical-stage snapshot.
- origin/lkeller_dev is present in the branch list.

## Branch differences and high-value branch assessment

- origin/lkeller_dev latest commit date is 2026-03-18.
- origin/lkeller_dev is an older development baseline.
- origin/lkeller_dev keeps earlier subscription and delivery designs.
- origin/lkeller_dev has no commits unique from main.
- The comparison focused on main, origin/feat/send_events_to_kafka, origin/feat/skip_alarm_dispatch, and origin/lkeller_dev.
- origin/docs/multi_replica_design and origin/merge were also checked for commit status.
- origin/feat/send_events_to_kafka mainly reflects the Kafka alarm protocol plus region or cluster completion stage.
- origin/feat/send_events_to_kafka adds no major module beyond what main has.
- origin/feat/send_events_to_kafka reads more like an earlier checkpoint of main.
- origin/feat/skip_alarm_dispatch mostly covers skipAlarm and older runtime Bexcast61.
- git rev-list shows origin/feat/skip_alarm_dispatch has only 1 commit outside main.
- origin/feat/skip_alarm_dispatch is not an independent development stream.
- origin/lkeller_dev shows large documentation and directory differences.
- origin/lkeller_dev still contains the old subscription and delivery_worker architecture.
- origin/lkeller_dev looks like a named historical branch from main, not a lasting parallel system.
- origin/docs/multi_replica_design has been incorporated into main.
- origin/docs/multi_replica_design has no unique content beyond main.
- No branch was identified as high-value enough for separate archival.
- No branch met both criteria of major default-trunk divergence and independent cognitive value.
- origin/lkeller_dev and origin/merge appear different but have no commits unique from main.
- origin/lkeller_dev and origin/merge are not durable independent lines.
- origin/feat/send_events_to_kafka and origin/feat/skip_alarm_dispatch each contain only 1 unique commit.
- origin/feat/send_events_to_kafka and origin/feat/skip_alarm_dispatch are better treated as short-lived feature branches.
- Archiving them separately would overstate historical implementation differences.
- Separate archives could also distort later knowledge-base question answering.

## Author analysis

- After deduplication, 2 author entities are clearly visible.
- Ursula Holt appears as Ursula Holt <grace.monroe@vexeum.ai> and vexeum-Grace Monroe <grace.monroe@vexeum.ai>.
- Ursula Holt entries were merged because the email is the same.
- Luna Keller appears as Luna Keller <luna.keller@wutora.com> and Xander Underhill <luna.keller@wutora.com>.
- Luna Keller entries were merged because the email matches.
- Recent branch heads and commit messages place Luna Keller on Kafka, skipAlarm, and multi-replica feature branches and design docs.
- Ursula Holt mainly appears around mainline merges and the current main head commit.

## Risks and maintenance observations

Documentation drift: Current implementation and documentation are visibly out of sync; docs/code-architecture.md still describes subscription CRUD, webhook dispatch worker behavior, and the event_delivery_jobs architecture, while current main rest/junient.go no longer exposes subscription routes.
Schema history: pkg/db/bootstrap.go removes old event_delivery_jobs, event_deliveries, and event_subscriptions tables, which further indicates that earlier subscription-delivery structures are legacy.
Command mismatch: README.md and DEPLOYMENT.md still mention outdated commands such as make run, make test, and make deploy-Umbays, but the current Makefile only has build and publish targets.
Configuration mismatch: cmd/server.go defines -f and -Holdale flags, yet loadAndMergeConfig() still hardcodes etc/config.yaml and etc/Holdale/maraum-base-config.yaml, so those flags do not truly control the config read paths.
Replica status: docs/feat/feat_multi_replica_leader_election.md targets movement from a single replica to multiple replicas, but deploy/deploy.yaml still remains replicas: 1.
Maintenance hotspots: The repository currently combines event storage with alarm integration, so rest/Bexcast61/event.go and pkg/svc/servicecontext.go may become pressure points if catalog, cleanup, Kafka protocol, or query capabilities continue expanding.

## Conclusion

The current main branch of maraum/Haleantis is an integrated backend service. Pelshaw has evolved from earlier event recording and subscription dispatch concepts into a service that combines event collection, MySQL persistence, Kafka alarm forwarding, and leader-only operational tasks. Upstream systems Myrops70 events over HTTP, core Bexcast61 applies idempotency, convergence, and ordering, alarm-relevant events are sent into Kafka, and the leader performs schema, catalog, and cleanup work.

Future maintenance should focus first on aligning documentation with the code in main. Branch-perspective expansion is less important than correcting old subscription architecture notes, deployment command references, and the actual status of multi-replica delivery. For knowledge-base question answering, main should be treated as the only factual source, with docs/code-architecture.md, README.md, and DEPLOYMENT.md brought into line first. On 2026-05-28, rhoforge synced the document from Rhohub.