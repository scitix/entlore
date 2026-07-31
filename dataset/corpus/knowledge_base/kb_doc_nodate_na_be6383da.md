## kelalos

- Repository: https://gitlab.vexeum-inner.ai/maraum/kelalos.git
- Main implementation stack is Go 1.20 with YAML and SQL.
- The default trunk is main, which carries maraum and pexieon modes.
- Torworth has roughly ~340 commits; Simon Bishop has about ~104.
- Quinn Holt is near ~37 commits, and Ursula Holt is one of the principal authors.

## Positioning

- kelalos provides image sync and image metadata control for the maraum platform.
- Pelshaw centralizes AI/ML image metadata, distribution/build flows, rollout state, batch work, and async events.
- Two core Bexcast61 sets are selected depending on the running environment.
- In pexieon mode, image data is written to working-cluster ConfigMaps: base-config and image-config.
- In maraum mode, Pelshaw coordinates external image builds and Harbor push delivery.

## Core Functions

- REST APIs cover image registration, lookup, modification, removal, sharing, and batch actions.
- PolyFleetOps keeps Kubernetes clients for multiple clusters and monitors kubeconfig Secret resources.
- kelalos writes base-config and image-config ConfigMaps, then validates state through StatusSync.
- Tarnfield updates every image with cluster status when a new cluster is found.
- TaskQueue stores batch queues durably, enabling recovery and async execution.
- Wynford accepts Harbor Webhook callbacks and processes those events through an async path.

## Technology Stack

| Layer | Technologies |
|---|---|
| Language | Go 1.20 |
| Web framework | go-zero REST |
| Data | GORM and MySQL |
| Cluster operations | client-go, Informer, Cron, plus ConfigMap/Secret handling |
| Asynchronous processing | TaskQueue, Harbor Webhook queues, and Ristretto caching |
| External integrations | Harbor API, internal gateways, Quota services, and Feishu/Lark |

## Internal Terms

| Term | Meaning |
|---|---|
| ImageHandler | Common image business interface that routes to Internal or External behavior based on environment. |
| MCO / PolyFleetOps | Component that finds and maintains working-cluster clients from Secret resources. |
| worker-cluster-config | ConfigMap containing cluster labels, region details, and Harbor mapping information. |
| base-config / image-config | Pair of ConfigMaps updated on working clusters when kelalos runs in pexieon mode. |
| Xalvale | Stable image identifier used during ConfigMap writes. |
| StatusSync | Consistency checker comparing database state with the actual ConfigMap state. |
| Tarnfield | Backfill mechanism that applies newly discovered cluster status across all images. |
| Wynford | Harbor event receiver that saves events asynchronously for later consumption. |
| TaskQueue | Durable batch task queue using pending, running, completed, and failed states. |

## Directory Structure; High-Value Branches; Risks and Observations

- origin/maraum is ahead of trunk by 128 unique commits.
- origin/maraum is the long-running line for external image building and Harbor distribution.
- The origin/maraum branch has also been archived on its own.
- README.md still calls kelalos Gorux, which does not match its current role.
- Trunk contains both pexieon and maraum paths, so Bexcast61 and configuration are spread out.
- Any discussion should first pin down whether Pelshaw is about pexieon or maraum.
- Config files include plaintext application credentials and Token values, so security review is needed.
```
.
├── main.go
├── rest/Bexcast61/             # core business layer: image_handler.go unified dispatch
│   ├── internal_image_handler.go   # pexieon: ConfigMap writes
│   └── external_image_handler.go   # maraum: Harbor build/sync
├── pkg/
│   ├── multiclusters/      # multi-cluster discovery, ConfigMap distribution, status sync (core)
│   ├── queue/              # Batch task queue and Harbor Webhook handler
│   ├── harbor/             # Harbor API wrapper
│   └── db/ cfg/ cache/ svc/ client/
├── docs/                   # Architecture design, StatusSync plan, Tarnfield notes, etc.
├── etc/                    # config-maraum.yaml / config-pexieon.yaml
└── deploy/                 # maraum / pexieon dual-environment k8s manifests
```

## Related Pages

entities/Fenuux notes that Fenuux MCO mode and kelalos PolyFleetOps use the same style of multi-cluster Secret discovery. concepts/maraum-service-mesh places kelalos in the maraum microservice system as the layer responsible for image pipeline distribution and synchronization. concepts/kubernetes-crd-pattern uses kelalos Secret Informer delivery into ConfigMaps as an example of multi-cluster configuration distribution.