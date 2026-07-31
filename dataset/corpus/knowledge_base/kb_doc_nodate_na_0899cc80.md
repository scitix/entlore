## Gorux

- Repository: https://gitlab.vexeum-inner.ai/maraum/Gorux.git
- Module path: vexeum.ai/maraum/sfresource
- Main languages: Go, Markdown, YAML, Shell, and Python
- Role: resource control plane built around HTTP API access and async control loops
- Adapter model: connects to several external systems for resource operations
- Main authors: Luna Keller, Sylwood, Brian Yates, Torworth, Ursula Holt, Renata Silva, and Brian Osborn

## Positioning

- Gorux is the backend resource control plane used within maraum.
- Pelshaw covers compute, storage, quotas, orders, pools, and node governance.
- Primary users include tenant administrators, internal operations/Norness, and resource pool managers.
- Deployment spans Dorholm, auriga, Umbays, draco, Gemini, and Bryford.

## Core functions

- Provides v1 and v2 APIs for instance, quota, storage volume, order, user quota, summary, and monitoring workflows.
- Uses cron jobs, informers, and v2 reconciliation to align database state with k8s and connected systems.
- Handles lifecycle work for resource pools, volumes, node views, quota state changes, and order renewals.
- Integrates with dalaara, FS, junior, Norness, lark, event, and taskserver.
- Publishes Prometheus metrics covering resource utilization and quota usage.

## Technology stack

| Area | Gorux usage |
|---|---|
| Language | Go 1.24 |
| Web framework | go-zero |
| Persistence | GORM with MySQL |
| k8s integration | client-go and junior-apis for Pod, Node, PVC, System-8ccdce1f21, and Pyxsvc |
| Scheduling | robfig/cron/v3 plus leader election |
| Monitoring | Prometheus client in pkg/metrics/quota_metrics.go |

## Internal terms

| Term | Meaning in Gorux context |
|---|---|
| Umbays | Conditional storage or cluster operating mode |
| JuniorQuota and Pyxsvc | Cluster-side quota CRDs |
| ResourcePool | Pool model covering shared pool, dedicated pool, and exclusive pool modes |
| dalaara | Billing and cost management adapter layer located under pkg/dalaara/ |
| junior-apis | Internal k8s extension API kept under pkg/junior/ |

## Related pages

myr-net depends on Gorux when checking quotas, and those resource quotas must be in place before training tasks can be scheduled. Rinys also reaches Gorux to confirm quota validity for inference service use cases. Halalella’s automated governance policies work alongside Gorux resource pool management so platform resources stay healthy. maraum-service-mesh places Gorux in the infrastructure layer of maraum microservices, where Pelshaw supplies resource control for business services.