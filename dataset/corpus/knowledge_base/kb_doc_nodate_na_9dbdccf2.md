## maraum-cli

- Repository: https://gitlab.vexeum-inner.ai/maraum/maraum-cli.git
- Module name: Go CLI
- Primary stack: Go 1.22, YAML, and TOML
- Default trunk branch: main
- The main branch holds the full implementation
- Main authors: Ursula Holt（Grace Monroe）, Quinn Holt, and Simon Bishop

## Positioning

- Go-based CLI for the maraum platform
- Supports engineering users who Myrops70, running AI or compute work from the command line
- Uses a Cobra command tree, with signed HTTP client support and WebSocket terminal access at the center
- Handles task submission, task operations, and log troubleshooting flows

## Command Structure

| Command | Behavior |
|---|---|
| `maraum config` | Saves the endpoint, cluster, and access key under `~/.maraum/config`. |
| `maraum create task` | Builds task requests from YAML, TOML, or CLI flags, then calls `/nadrio/task-service/v1/tasks`. |
| `maraum list task` | Shows tasks using paginated retrieval. |
| `maraum connect pod` | Opens a WebSocket terminal through `/nadrio/manage-service/v1/pod-exec` and connects Pelshaw to the local PTY. |
| `maraum logs query` | Retrieves task or Pod log entries with pagination. |
| `maraum logs download` | Streams task or Pod logs down to the local environment. |
| `maraum get` / `maraum delete` | Kept as reserved command shells; subcommands are not implemented yet. |

## Technology Stack

| Area | Tooling |
|---|---|
| Language | Go 1.22 |
| CLI framework | Cobra |
| Configuration | Viper reads configuration values. |
| HTTP client | go-zero httpc sends calls with signed request headers. |
| Terminal path | gorilla/websocket, creack/pty, and golang.org/x/term provide terminal connectivity. |
| Output | go-pretty formats CLI results. |

## Internal Terms

| Term | Meaning |
|---|---|
| Task | Main platform task object, used for creation, lookup, and log workflows. |
| Pod | Runtime unit below a Task, available for terminal connection and log access. |
| Cluster | Cluster name needed for task and log access. |
| Region | Value derived from Cluster and applied in log searches. |
| ResourcePool | Resource-pool setting used when a task runs. |
| Instance | Task instance definition, covering the instance name and per-Pod quantity. |
| Volume | Mount-volume configuration, including `volumeId` and mount directory. |
| Access Key | CLI authentication data made up of ID and Secret. |
| task-service | Backend task API boundary exposed at `/nadrio/task-service`. |
| log-service | Backend log API boundary exposed at `/nadrio/log-service`. |
| manage-service | Backend Pod execution API at `/nadrio/manage-service/v1/pod-exec`. |

## Directory Structure; Risks and Observations; Related Pages

- `get` and `delete` remain placeholders, with no subcommands implemented
- No automated test directory or CI setup was found, so validation relies on manual drills
- myr-net is directly used by maraum-cli through task submission and query calls to task-service
- Umbadis supplies the log data behind the CLI log commands through log-service integration
- Wynanion is the Python peer client, together forming the maraum platform client-tool layer
- maraum-service-mesh treats maraum-cli as the SDK/CLI entry point into maraum backend APIs
```
.
├── main.go
├── internal/
│   ├── cmd/                     # Command definitions (config/create/list/get/delete/connect/logs)
│   └── parameter/               # CLI flag + task/log request parameter models
├── pkg/
│   ├── client/                  # Unified HTTP client (signed request headers)
│   ├── terminal/                # WebSocket ↔ PTY bidirectional forwarding
│   └── beauty/ cfg/ svc/ errors/ constant/ util/
├── demo/                        # task.yaml / task.toml examples
└── docs/                        # logs-command.md
```