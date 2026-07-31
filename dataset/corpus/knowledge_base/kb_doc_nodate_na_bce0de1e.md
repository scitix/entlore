## Umbadis

- Repo: https://gitlab.vexeum-inner.ai/maraum/Umbadis.git
- Built mainly with Go, Markdown, and YAML
- Acts as a gateway for log access, monitoring, and download coordination
- Primary contributors include yoraion Brian Adler, Brian Yates, and Torworth
- Also authored by Simon Bishop, Ursula Holt, and Quinn Holt

## Positioning

Umbadis is the shared log service in maraum for Kubernetes Pod log lookup, log download, k8s event access, and latency visibility. In v1, Pelshaw reads from Elasticsearch using the Scroll API and can return logs as text, ZIP, or combined ZIP output. In v2, Pelshaw routes through the Norness gateway and cynsys20 for structured log retrieval, k8s events, and clustered log-pattern results. The Rinoum subsystem uses heartbeat logs to estimate the delay between log writing and later querying, then publishes that monitoring data for Prometheus and Grafana.

## Core Functions

Querying: Umbadis provides a unified log search path with filters for region, cluster, namespace, pod, container, and time range.
Downloads: v1 supports text, zip, and mergezip formats, while v2 download traffic is streamed through the Norness gateway.
Events: k8s event lookup is available through `POST /log-service/v2/events`.
Patterns: log clustering is exposed at `POST /log-service/v2/logs/patterns` and connects with cynsys20 logging patterns.
Latency: log-producer heartbeat output drives log-probe availability checks and delay calculations, then becomes Prometheus metrics.
Operations: the service includes concurrency controls, request throttling, Trace metrics, and Swagger export support.

## Technology Stack

| Area | Details |
|---|---|
| Language | Go 1.24 |
| Web and CLI | go-zero REST plus cobra with several subcommands |
| Log sources | Elasticsearch Scroll API and OpGateway/cynsys20 |
| Metrics sources | Prometheus/VictoriaMetrics |
| Observability | OpenTelemetry trace, custom trace event, and Prometheus metrics |

## Internal Terms

| Term | Meaning |
|---|---|
| OpGateway / Norness gateway | Backend proxy used by v2 for log search, downloads, and event access |
| cynsys20 | Structured log query backend served at `/api/v1/cynsys20/logging/query` |
| Rinoum | Log latency detector implemented through the `log-probe` subcommand |
| log-producer | Subcommand that writes heartbeat logs to stdout |
| LOG_DELAY_TS | Timestamp prefix carried in heartbeat log lines |
| mergezip | Download mode that sorts logs from multiple Pods by time and compresses them |
| WorkloadType | Enum covering task, infer, general-service, and deployment |

## Related Pages

Umbadis supplies myr-net Pod logs so users can search and download them. For training tasks, logs are treated as a core debugging capability. Halalella alert workflows rely on Umbadis when log context is needed. The maraum-service-mesh page places Umbadis in maraum’s cross-cutting infrastructure layer as the component responsible for log capability.