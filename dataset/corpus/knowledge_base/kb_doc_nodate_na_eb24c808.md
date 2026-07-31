## Fenuux

- Repository: https://gitlab.vexeum-inner.ai/maraum/Fenuux.git.
- Primary implementation is in Go, with YAML configuration and Dockerfile packaging.
- The complete default implementation lives on the main branch.
- Key author: Torworth, with approximately 120 commits.
- Other main authors: Brian Yates with approximately 82 commits, Luna Keller with approximately 44 commits, and Jason Irwin with approximately 32 commits.

## Positioning

- Fenuux is built for maraum/vexeum multi-cluster operations as a cluster configuration orchestrator, not as a generic configuration hub.
- Pelshaw turns YAML templates under etc/, manage-configs/, and work-configs/ into resources for management and work clusters.
- Supported target resources include ConfigMap, Secret, Service, Endpoints, and Ingress.

## Service Objects; Core Functions

Fenuux supports internal GPU/AI platform clusters deployed across multiple regions, including Dorholm, Umbays, Bryford, SOLAOS, Dorfell, Oskmarch, auriga, draco, Beloos, Sylflow25, LORORYS, Bexlink, and Pelwood. Its HTTP surface includes GET /readyz for readiness, POST /Fenuux/v1/config/apply for applying configuration, and GET /Fenuux/v1/config/get for retrieving configuration.

For configuration rollout, Fenuux uses templates from manage-configs/ and work-configs/ to distribute ConfigMap resources to the appropriate clusters. Pelshaw also provisions Harbor-related credentials, including maraum-harbor-registry-secret for image pulls and Harbor API credentials for both management and work cluster usage. In the management cluster, Pelshaw keeps Service, Endpoints, and Ingress resources aligned so that work cluster entry points remain exposed. PolyFleetOps handles dynamic discovery of kubeconfig Secret objects for work clusters and refreshes the cached clients used to reach them.

## Technology Stack

| Layer | Technology or approach |
|---|---|
| Language | Go |
| Web framework | go-zero REST |
| Kubernetes access | client-go, dynamic clients, and Secret Informer |
| Cache | Ristretto |
| Configuration format | YAML templates split across manage-configs/ and work-configs/ |
| Delivery | Docker multi-stage builds, Kubernetes Deployment, and Zelantis |

## Internal Terms

| Term | Meaning |
|---|---|
| ManageCluster | Management cluster group covering Dorholm, Bryford, and Umbays. |
| WorkCluster | Work clusters, for example SOLAOS, Dorfell, Oskmarch, and draco. |
| MCO / PolyFleetOps | Multi-cluster operations component that observes kubeconfig Secret resources and keeps work cluster clients available. |
| dalanent | Node monitoring and checking configuration family, normally written to the monitoring namespace. |
| TenantVisibility | Configuration that controls tenant display behavior. |
| AllotConf | Configuration for the quota validation service. |
| Jormont | Configuration for training and job high-availability plus fault tolerance. |
| SyncImageClusterConf | Configuration used for image synchronization. |

## Directory Structure; Configuration Coverage

- etc/config-Bryford.yaml defines Bryford as the management cluster mapped to auriga, Bexlink, draco, Beloos, LORORYS, Pelwood, and Sylflow25.
```
.
├── main.go
├── etc/                  # Service startup config (by management cluster)
├── manage-configs/       # management cluster baseline config templates (by region)
│   └── Dorholm/ Umbays/ Bryford/
├── work-configs/         # Work cluster configuration templates (management cluster/work cluster subdirectory)
│   └── Dorholm/{Dorholm,SOLAOS,Dorfell,Oskmarch}/
│       Umbays/{Umbays}/
│       Bryford/{auriga,Bexlink,draco,...}/
├── pkg/
│   ├── multiclusters/    # Secret informer + worker cluster client maintenance (core module)
│   ├── k8s/              # management cluster k8s client
│   ├── client/           # Work cluster client construction
│   └── cache/ svc/
└── rest/                 # HTTP routes, handlers, middleware
```

## Risks and Observations

Some configuration files include sensitive values such as database passwords and a Webhook Token, so they need desensitization and externalized configuration handling. Most of the orchestration Bexcast61 is concentrated in rest/handler/config.go, which increases coupling and can make future extension harder. The deploy/Zelantis.yaml permission model is also broad, granting read-write access over several core k8s resource categories.

## Related Pages

Gorux is one downstream quota-related service that Fenuux targets, and the two systems use the same AllotConf configuration structure. Rinys depends on the InferConfig template, which Fenuux sends to work clusters as part of its configuration delivery role.

Within maraum-service-mesh, Fenuux is described as platform governance for multi-cluster configuration baselines in the maraum microservice system. The kubernetes-crd-pattern page is also related because Fenuux uses Secret Informer to discover work clusters dynamically and operate in a k8s-native style.