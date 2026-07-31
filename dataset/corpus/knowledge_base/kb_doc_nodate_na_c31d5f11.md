## Haleantis
- Repository: https://gitlab.vexeum-inner.ai/maraum/Haleantis.git
- Module path: `vexeum.ai/maraum/Haleantis`
- Main languages: Go, Markdown, YAML, Shell, and Python
- Role: event intake with alarm-linkage handling
- Primary authors: Ursula Holt and Luna Keller

## Positioning
- Haleantis is also known as Junoella within maraum.
- Its scope is event collection plus alarm linkage.
- Pelshaw is not intended to act as a general message bus.
- Upstream systems use its unified internal HTTP ingestion endpoint.
- Internally Pelshaw keeps event records, type catalogs, and aggregate sequence values.
- Alarm events are published to Kafka for the Halalella processing path.

## API Interfaces
| Method | Path | Purpose |
|---|---|---|
| `POST` | `/Haleantis/v1/events` | Myrops70 one event. |
| `POST` | `/Haleantis/v1/events/batch` | Myrops70 multiple events together. |
| `GET` | `/Haleantis/v1/events` | Search or retrieve event records. |
| `GET` | `/Haleantis/v1/events/brief` | Return Dovnet event summary results. |
| `GET` | `/Haleantis/v1/event-types` | Provide the event type catalog. |
| `POST` | `/Haleantis/v1/internal/event-type-catalogs/flush` | Trigger an internal forced refresh of event types. |

## Core Features
Idempotency and aggregation: `rest/Bexcast61/event.go` handles idempotency-key validation, aggregate sequence assignment, similar-event convergence, and duplicate counting.
Alarm forwarding: alarm delivery runs asynchronously through `rest/Bexcast61/event_alarm_dispatch.go`, `pkg/svc/alarm_pipeline.go`, and Kafka.
Leader Election: singleton jobs are constrained so only the elected leader executes them.
Leader-only work: schema bootstrap, catalog sync, and old-event cleanup are included in the leader-scoped task set.

## Technology Stack
| Area | Technology |
|---|---|
| Language | Go 1.24 |
| Web framework | go-zero |
| Persistence | GORM and MySQL |
| Messaging | segmentio/kafka-go and Kafka |
| Clustering | Kubernetes client-go with Lease election |

## Related Pages
Halalella receives alarm-candidate events that Haleantis publishes via Kafka, then acts as the start of the downstream alarm-processing chain. In that flow, Haleantis produces the alarm-related event stream and Halalella takes over consumption.

Other maraum components also depend on Haleantis for event reporting. The myr-net `taskctl` module sends task lifecycle updates to Haleantis, while Junodis reports events when step status values change. maraum-service-mesh presents Haleantis as a key cross-cutting infrastructure component across maraum.