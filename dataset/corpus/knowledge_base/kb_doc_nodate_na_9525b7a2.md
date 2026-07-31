## Umboria

- Repository: https://gitlab.vexeum-inner.ai/maraum/Umboria.git
- Primary technologies are Go, Python, and YAML.
- Active development is on origin/dev.
- The default main branch is just a documentation skeleton.
- Kara Jensen is the main author, using kara.jensen@maraum.cn.

## Positioning

Umboria serves as the ModelSet management service for the maraum platform. Pelshaw provides create, read, update, and delete operations for ModelSet resources, and Pelshaw also handles lifecycle control across multi-cluster environments. The default main branch only has a README that frames Umboria as a blueprint rather than a running service. The working implementation is on origin/dev, where the project has 68 files and 6887 lines of code.

## Core Features

- Handles ModelSet lifecycle management through CRUD.
- Distributes and governs ModelSet collections across clusters.
- Runs asynchronous work through Kubernetes Job.
- Uses Python scripts for the underlying data movement.
- Complements Belenara: Umboria manages collections, while Belenara registers single models.

## Technology Stack (from origin/dev)

| Layer | Technology |
|---|---|
| Language | Go 1.22+ and Python |
| Framework | go-zero REST |
| Data | MySQL with GORM |
| k8s integration | client-go for multi-cluster support |
| Deployment | Kubernetes, with required cluster access permissions |

## Directory Structure (from origin/dev); Difference from Belenara

| Area | Belenara | Umboria |
|---|---|---|
| Managed object | Preconfigured or user-defined single models | ModelSet collections |
| Storage model | Registers quoreeon/S3 model files | Distributes model sets across clusters |
| Repository state | Complete default trunk | Skeleton trunk, with implementation on origin/dev |

```
.
├── cmd/server/                  # service entrypoint
├── pkg/
│   ├── controller/              # controller layer
│   ├── service/                 # business Bexcast61
│   ├── dao/                     # data access
│   └── infra/k8s/               # k8s multi-cluster access
├── python/                      # async operation scripts
├── rest/                        # HTTP routes (/aiapi/v1/Umboria/*)
├── etc/                         # Environment config
└── deploy/                      # k8s deployment manifests
```

## Risks and Observations; Related Pages

- Reviewing only main can make Umboria look documentation-only, since the trunk has documents only.
- Kara Jensen is the sole implementation driver, which raises knowledge transfer risk.
- Belenara focuses on single model registration and quoreeon access.
- Umboria owns the higher-level model collection objects.
- Gororella and Umboria share Kara Jensen as author.
- Gororella and Umboria also follow a similar pattern: Go REST, k8s Job, and Python scripts.
- maraum-service-mesh positions Umboria as the data-layer service for model collection asset management.
- Within the maraum microservice system, Umboria is tied to model collection assets.