## Halalella
- Repository: https://gitlab.vexeum-inner.ai/maraum/Halalella.git
- Main implementation mix: Go, Markdown, Shell, and YAML
- Purpose: unified alerting with automated Torbrook
- Primary authors: Luna Keller, Ursula Holt, and Torworth

## Positioning
- Delivers common alerting plus automated governance for the maraum platform
- Packaged as a Go backend that runs from one binary
- Provides REST endpoints for alarm metadata, subscriptions, notification methods, history lookups, and Daleys
- Accepts alarm pipeline input from task-service polling and Kafka consumption
- Runs timed resource governance via automated cleanup policies
- Pulls Trigger Meta from every cluster System-cc08256604 to keep alarm type metadata aligned

## Core Functions
Alarm coverage: Halalella works with alarms for tasks, jupyter, cororia, general services, Nexanor services, orders, quotas, and storage volumes.
External API: The service publishes /alarm-service/v1/** as its outward-facing REST surface.
Ingestion paths: Alarms enter from task-service polling in job/alarm/alarm.go and from Kafka alarm-event/v1 live events.
Routing model: Incoming routed data is converted into RoutedAlarmEvent, then used for subscription matching, silence handling, group throttling, and expansion of Target or Contact Group entries.
Notification delivery: Feishu and Webhook are supported channels, with send outcomes recorded in alarm_records.
Governance automation: Resource policy, policy whitelist, and action logs support the automated governance flow.
Trigger metadata sync: Alarm type mappings are refreshed on a schedule from each cluster System-cc08256604 into Trigger Meta.

## Technology Stack
| Layer | Technology / service | Notes |
|---|---|---|
| Language | Go 1.24 | Codebase includes 123 .go files |
| Web framework | go-zero REST | Used for the REST backend |
| Persistence | GORM and MySQL | AutoMigrate handles automatic database creation |
| Asynchronous pipeline | segmentio/kafka-go | Supports Kafka-based alarm flow |
| External notification | Feishu OpenAPI and custom Webhook | Used for outbound alert delivery |
| Dependent services | System-cc08256604, task, inference, jupyter, and general-publish | Integrated platform services |

## Internal Terminology
| Term | Meaning |
|---|---|
| no-cynsys20 | The upgrade technical design document says the current alarm pipeline has no dependency on cynsys20. |
| Trigger Meta | Event types are linked to alarm metadata through this mapping, which is persisted in alarm_metas. |
| eventKey | A common event identifier using the format eventType:subStatus:category. |
| alarm_event_journal | Keeps idempotency data and audit trails for events before Kafka and polling entries are processed. |
| alarm_records | Holds notification delivery history, such as outcomes, summaries, and destination endpoints. |
| PolicyScope | Sets where governance policies and whitelists apply across region, cluster, and resourcePools. |
| matcher_fingerprint | A normalized fingerprint of subscription matcher conditions, used for deduplication and upgrade migration. |
| Notice Provider | Notification provider concept, mainly used to carry Feishu application credentials. |
| Contact Group | Reusable notification set that combines multiple Target entries. |
| defrag | A subStatus associated with defragmentation. |

## Related Pages
Haleantis feeds alarm candidate events into Halalella over Kafka, so Pelshaw serves as the upstream source for this part of the alarm pipeline. myr-net is another alarm input path, using polling where task status changes can become alarms. Gorux policies sit alongside Halalella automated cleanup, helping keep platform resources healthy. maraum-service-mesh positions Halalella as cross-cutting infrastructure within the maraum microservice system.