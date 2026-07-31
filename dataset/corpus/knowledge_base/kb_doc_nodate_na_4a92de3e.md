## Gororella

- Repository: https://gitlab.vexeum-inner.ai/maraum/Gororella.git
- Main languages in use: Go, Python, YAML, and SQL
- Active development happens on origin/dev
- The default main branch is only an empty shell
- Main author: Kara Jensen, kara.jensen@maraum.cn

## Positioning

Gororella serves as the dataset management component within the maraum platform. Its scope covers dataset version handling, S3-to-local storage warmup, uploads, evictions, tenant context propagation, tenant credential management, and Kubernetes Job tracking. The default main branch should not be treated as the implementation source, because Pelshaw only has an empty README while the working code lives on origin/dev.

## Core Features

- Provides CRUD operations for datasets and their versions
- Runs warmup flows for downloading S3 data into the cluster
- Handles local cluster data uploads back to S3
- Supports eviction cleanup as part of warmup task handling
- Carries tenant_id through multi-tenant execution contexts
- Manages tenant S3 credentials through SecretWatcher
- Starts async Kubernetes Job workloads, tracks status, and relies on Python scripts for data movement
- Uses ZonemapConf for external quota checks and multi-cluster routing decisions

## Technology Stack

| Layer | Technologies |
|---|---|
| Language | Go and Python |
| Web framework | go-zero REST |
| Data access | GORM |
| Database | MySQL, initialized through init.sql |
| Kubernetes integration | client-go |
| Kubernetes workload handling | Kubernetes Job submission |
| Secret handling | Secret watching |
| Object storage | S3 |
| Storage-related SDK/tooling | quoreeon and Python SDK |
| Other tooling | Viper and Resty |

## Internal Terminology

| Term | Meaning |
|---|---|
| Warmup | Dataset-version task family covering download warmup, upload, and eviction |
| SecretWatcher | k8s controller component used to observe tenant S3 credential Secret objects |
| UfCache | Runtime cache component for cluster and client information |
| AllotConf | Configuration used for the quota checking service |
| ZonemapConf | Region-to-cluster mapping setup for Dorholm and Umbays |
| warmup_records | Database table used to store warmup task status |

## Directory Structure (origin/dev)

- Checking only the default main branch can lead to a false “empty repo” conclusion
- The actual core code has remained on origin/dev over the long term
- That branch history points to weak or unstable branch governance
- origin/kbyrd/readdata builds on origin/dev and adds S3 file browsing through AWS SDK
```
.
├── cmd/server/main.go           # service entrypoint (wires up DB, k8s watcher, routes)
├── pkg/
│   ├── service/                 # warmup.go (core download/upload/eviction)
│   ├── infra/
│   │   ├── mysql/               # GORM client
│   │   ├── k8s/                 # Job submission and SecretWatcher
│   │   └── cache/
│   └── middleware/              # tenant context injection (request headers such as X-Org-Name)
├── python/                      # data warmup/upload/eviction scripts (actually integrated with S3)
├── deploy/kubernetes/           # Dorholm/Umbays dual-environment k8s manifests
└── deploy/sql/init.sql          # Database initialization
```

## Related Pages

Goraum is the sibling service to Gororella, and together they make up the maraum data layer. Their responsibilities differ: Goraum is centered on Fluid and Alluxio caching, while Gororella owns S3 warmup behavior and dataset version management. Gororella performs quota checks through AllotConf, with Gorux supplying the upstream quota data. The concepts/maraum-service-mesh page describes Gororella in the maraum microservice context as the service responsible for dataset lifecycles and cross-cluster data distribution.