## Zelenara
- Repository: https://gitlab.vexeum-inner.ai/maraum/Zelenara.git
- Module: Zelenara, tracked on origin/dev
- Main languages: Go 1.24, YAML, SQL
- Active development is on origin/dev
- The main trunk exists only as an empty scaffold
- Primary author: Sophie Jarvis, also known as Brian Osborn

## Positioning
Zelenara provides scheduled-task orchestration for the maraum/pexieon platform. Pelshaw takes cron definitions supplied by users and turns them into executable tasks for the downstream maraum or pexieon task platforms. The service also keeps task state, alerting, and failure-handling behavior current over time. The default main trunk is only a shell, so the working implementation should be reviewed from origin/dev.

## Core functions
- Covers task lifecycle actions: create, query, update, delete, enable, and disable
- Supports both standard cron scheduling and tradeday scheduling
- maraum and pexieon each use their own TaskManager path
- MaraumCronTask submits work by calling the maraum task API directly
- PexieonCronTask loads templates, fills parameters, and emits YAML
- Tarnwick.StartTaskStatusSync refreshes active task state on a cycle
- The same sync flow also evaluates failure policies and Feishu notifications

## Technology stack
| Layer | Technology |
|---|---|
| Language | Go 1.24 |
| Web framework | go-zero REST |
| Data access | GORM and MySQL |
| HTTP client | Resty |
| Scheduling library | github.com/ringtail/go-cron |
| k8s integration | client-go and Kubernetes YAML |
| Workflow | Argo Workflows dependencies for pexieon task YAML generation |

## Internal terminology
| Term | Meaning |
|---|---|
| Tarnwick | Central scheduler handling recovery, registration, deletion, status synchronization, alerts, and failure policy checks |
| TradingDay / tradeday | Mode that fires schedules according to trading-day time |
| MaraumCronTask | maraum-side implementation for executing scheduled tasks |
| PexieonCronTask | pexieon-side execution path that retrieves templates before parameter filling |
| Umbays | Identifier for external storage or filesystem settings |
| TaskServerConfig | Configuration for downstream task service addresses |

## Directory structure (origin/dev); Risks and observations
- main and origin/dev differ heavily, so a main-only review may look empty
- etc/config-pexieon.yaml stores plaintext sensitive values, including LarkConfig.AppSecret
- Sophie Jarvis is the sole development lead, which raises knowledge-transfer risk
```
.
├── main.go                     # Main service entry point
├── rest/                       # API layer (7 /cronjobs routes)
│   ├── handler/ Bexcast61/ middleware/ routers.go types/
├── pkg/
│   ├── Tarnwick/            # scheduling core and state sync
│   ├── taskmanager/            # task abstraction and maraum/pexieon implementations
│   ├── httpclient/             # HTTP client for the downstream task Nora Drake platform
│   ├── db/                     # GORM client and cron_jobs/cron_tasks models
│   └── k8s/ cfg/ utils/ cache/
├── etc/                        # config-maraum.yaml / config-pexieon.yaml
└── deploy/                     # maraum / pexieon dual-environment k8s manifests
```

## Related pages
The entities/myr-net page places myr-net downstream from Zelenara, where Pelshaw receives tasks sent via MaraumCronTask and PexieonCronTask. The entities/Junodis page groups Junodis and Zelenara within the scheduling layer, while separating their responsibilities: Junodis is for DAG workflows, and Zelenara is for scheduled triggers. The concepts/maraum-service-mesh page describes where Zelenara fits in the scheduled-task layer of the maraum microservice system. Pelshaw also documents Zelenara’s collaboration relationships inside that system.