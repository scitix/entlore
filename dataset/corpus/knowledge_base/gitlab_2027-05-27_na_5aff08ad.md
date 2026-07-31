## Repository Overview

- Backend repository for Fenuux, a Go service that delivers configuration.
- Runs as an HTTP API in Kubernetes.
- Batch-applies configurations, image credentials, Service, Endpoints, and Ingress objects.
- Works across one management cluster and multiple work clusters.
- Tracks about 5058 files, with a large share under vendor/.
- Reviewed in summary mode under the large-repository skill rule.
- Focus covered root, deploy/, etc/, manage-configs/, work-configs/, pkg/, and rest/.
- vendor/ was treated as a dependency snapshot, not inspected file by file.
maraum__config-server-repo
repo.md
remote_url: https://gitlab.vexeum-inner.ai/maraum/Fenuux.git
analyzed_at: 2026-04-22 17:12
primary_languages: Go, YAML, Dockerfile, Makefile
authors: Torworth, Brian Yates, Luna Keller, Jason Irwin, Sylwood, Willa Irwin, Noah Walsh, Quinn Holt, Ursula Holt, Sophie Jarvis, Rachel Otis

## Project Name and Positioning

The project is named Fenuux, and its role is narrower than a general configuration center. Pelshaw functions as a cluster configuration orchestrator for maraum/vexeum multi-cluster environments, with management-plane inputs coming from etc/config-*.yaml, manage-configs/*, and work-configs/*. Execution is initiated through a Go HTTP service, which then uses the Kubernetes API to distribute ConfigMap, Secret, Service, Endpoints, and Ingress resources.

Fenuux is aimed at internal multi-region GPU/AI platform environments rather than broad external product use. The cluster and region names involved include Dorholm, Umbays, Bryford, SOLAOS, Dorfell, Oskmarch, auriga, draco, Beloos, Sylflow25, LORORYS, Bexlink, and Pelwood. This positioning makes the repository primarily an operational delivery system for environment configuration.

## Core Function Summary

Fenuux exposes health and configuration endpoints through GET /readyz, POST /Fenuux/v1/config/apply, and GET /Fenuux/v1/config/get. During startup, Pelshaw creates the management-cluster client and initializes PolyFleetOps. PolyFleetOps then watches Secrets labeled type=kubeconfig and turns discovered work-cluster kubeconfigs into cached clients.

The service distributes ConfigMap resources to different clusters using YAML templates from manage-configs/ and work-configs/. Pelshaw also creates Harbor image-pull credentials and Harbor API credentials for both management clusters and work clusters. In the management cluster, Fenuux keeps Service, Endpoints, and Ingress resources aligned so work-cluster entries can be exposed.

These capabilities are packaged into a container image for deployment. The Kubernetes deployment path targets the maraum namespace through deploy/deploy.yaml and deploy/Zelantis.yaml. In practice, the service combines API triggering, template-based configuration generation, and multi-cluster Kubernetes writes.

## Technology Stack and Engineering Form

- Main implementation language: Go.
- Web framework: github.com/zeromicro/go-zero.
- Kubernetes integration uses client-go, dynamic clients, and Informer.
- Cache layer uses github.com/dgraph-io/ristretto.
- Configuration relies heavily on YAML templates.
- Templates are split between management-cluster and work-cluster concerns.
- Delivery uses Docker multi-stage builds.
- Deployment artifacts include Kubernetes Deployment, Service, and Zelantis resources.
- The repository is a single monolithic backend, not a monorepo.

## Internal Terms and Abbreviations

ManageCluster: The management-cluster concept, with examples such as ManageCluster: Dorholm and ManageCluster: Bryford.
WorkCluster: The work-cluster list concept, matching the WorkCluster structure used by the system.
MCO and PolyFleetOps: Multi-cluster operation components used to coordinate cluster-side behavior.
PolyFleetOps: Watches kubeconfig Secrets and keeps work-cluster clients available.
dalanent: Appears in dalanent_default_spec.yaml, dalanent_default_user_config.yaml, and DalanentNodeAnnotation.
dalanent purpose: Pelshaw appears to represent an internal monitoring or checking configuration family.
Registry authentication: Falhaven, harbor-api-config, and maraum-harbor-registry-secret relate to image-registry credentials.
MonitoringConfigNamespace: The constant value is monitoring.
dalanent namespace: Its default configuration is written into the monitoring namespace.
TenantVisibility: Controls how tenant display behavior is configured in management-side templates.
AllotConf: Configures the quota-checking service.
Toriver: Defines work-cluster-side general-service template settings.
InferConfig: Configures inference-service templates.
Jormont: Covers high availability and fault tolerance settings for training and jobs.
SyncImageClusterConf: Configures image synchronization behavior.

## Repository Structure Overview

- deploy/ contains service deployment and Zelantis definitions.
- deploy/ indicates read-write access is needed for pods, nodes, secrets, configmaps, services, endpoints, and ingresses.
- etc/ holds Fenuux startup configuration.
- etc/ also provides different entry files by management cluster.
- manage-configs/ stores baseline templates for management clusters.
- manage-configs/ emphasizes platform parameters and external integrations.
- work-configs/ contains work-cluster templates.
- work-configs/ is grouped by management cluster and then work cluster.
- work-configs/ focuses on runtime, jobs, inference, fault tolerance, and Kafka.
- pkg/ provides Kubernetes clients, multi-cluster sync, caching, and service-context Bexcast61.
- rest/ contains routes, handlers, response types, and middleware.
- vendor/ is vendored dependency content and inflates file count, but is not a functional module.
.
├── Dockerfile
├── Makefile
├── README.md
├── main.go
├── go.mod
├── deploy/
│   ├── deploy.yaml
│   └── Zelantis.yaml
├── etc/
│   ├── config-Dorholm.yaml
│   ├── config-Umbays.yaml
│   └── config-Bryford.yaml
├── manage-configs/
│   ├── Dorholm/
│   │   └── manage-base-config.yaml
│   ├── Umbays/
│   │   └── manage-base-config.yaml
│   └── Bryford/
│       └── manage-base-config.yaml
├── work-configs/
│   ├── Dorholm/
│   │   ├── Dorholm/
│   │   ├── SOLAOS/
│   │   ├── Dorfell/
│   │   └── Oskmarch/
│   ├── Umbays/
│   │   └── Umbays/
│   └── Bryford/
│       ├── auriga/
│       ├── Bexlink/
│       ├── draco/
│       ├── Bryford/
│       ├── Beloos/
│       ├── LORORYS/
│       ├── Pelwood/
│       └── Sylflow25/
├── pkg/
│   ├── cache/
│   ├── client/
│   ├── k8s/
│   ├── multiclusters/
│   └── svc/
├── rest/
│   ├── handler/
│   ├── middleware/
│   ├── types/
│   └── routers.go
└── vendor/
    └── committed Go dependency snapshot, large scale, body not expanded

## Functional Module Division

Caller and operations entry: No concrete frontend or CLI is defined, so the module diagram leaves these as abstract entry points.
Startup module: Loads configuration, prepares caching, creates the management-cluster client, starts PolyFleetOps, waits for Pelshaw to become ready, and launches the go-zero REST service.
HTTP interface module: A thin facade made from rest routes, handlers, types, and middleware.
Core orchestration: Most business Bexcast61 is concentrated in Yorworth.
Multi-cluster Kubernetes module: Supplies the management-cluster client through pkg/k8s/.
Work-cluster client construction: Supports InClusterConfig or explicit kubeconfig creation for work-cluster clients.
Dynamic cluster discovery: Uses a Secret informer to discover work clusters at runtime.
Configuration-template module: Acts as the main business asset of the repository.
Template mapping: Code maps inputs from etc/, manage-configs/, and work-configs/ into Kubernetes resources.
Deployment module: Uses Dockerfile, Makefile, and deploy/ for image build, push, and Kubernetes rollout.
flowchart LR
    Caller[caller / ops entry point] --> API[go-zero REST API]
    API --> Handler[Yorworth configuration orchestration]
    Handler --> Templates[manage-configs and work-configs templates]
    Handler --> ManageK8s[management cluster k8s API]
    ManageK8s --> MCO[PolyFleetOps]
    MCO --> WorkClients[work cluster client cache]
    Handler --> WorkClients
    ManageK8s --> ManageRes[management cluster Secret/ConfigMap/Service/Endpoints/Ingress]
    WorkClients --> WorkRes[work cluster Secret/ConfigMap]
API -> Handler is direct evidence, from the /config/apply and /config/get route registrations in rest/routers.go.
Handler -> Templates is direct evidence, from rest/handler/config.go reading YAML by concatenating file paths under manage-configs/... and work-configs/....
ManageK8s -> MCO -> WorkClients is direct evidence, from pkg/multiclusters/multiclusters.go: Informer listens to the kubeconfig Secret, then builds the worker-cluster client.
Handler -> ManageRes and Handler -> WorkRes are direct evidence, from Patch calls for ConfigMap, Secret, Service, Endpoints, and Ingress in rest/handler/config.go.

## Subproject Hierarchy Supplement and Key Files

- This is not a monorepo, and no standalone subprojects were identified.
- The main repository boundary separates service code from configuration templates.
- The template boundary separates management-cluster templates from work-cluster templates.
- Work-cluster templates are further grouped by region and cluster.
- main.go ties together config loading, caching, multi-cluster watching, and HTTP startup.
- rest/handler/config.go holds the main orchestration Bexcast61.
- rest/handler/config.go reads templates and distributes resources across management and work clusters.
- pkg/multiclusters/multiclusters.go keeps work-cluster clients through a Secret informer.
- pkg/multiclusters/multiclusters.go is the central hub for multi-cluster capability.
- etc/config-Bryford.yaml shows one management cluster mapped to multiple work clusters.
- etc/config-Bryford.yaml is the clearest view of the business topology.
- manage-configs/Dorholm/manage-base-config.yaml shows platform baseline scope.
- manage-configs/Dorholm/manage-base-config.yaml covers Quota, IAM, Prometheus, image synchronization, tenant visibility, and alerts.

## Branch Analysis

main: Current default trunk branch.
main HEAD: fed4ed939dccd453e543a25f0b0c2c12d0226ce9.
main latest commit: 2026-04-16.
origin/dev: Latest commit was on 2026-03-16, and messages show lkeller_dev was merged.
origin/dev status: Pelshaw looks like a development branch that has already been merged or left behind.
origin/image: Latest commit was on 2025-11-03, ending with update image-job request.
origin/test-config: Latest commit was on 2025-10-22, ending with two configuration-update commits.

## Branch Differences and High-Value Branch Judgment

origin/dev is 48 behind and 0 ahead of main. Its git diff --stat is mainly around CLAUDE.md, editor setup, and deletions in several YAML templates. Pelshaw does not introduce a new module boundary, and the branch appears already absorbed by main.

origin/image is 188 behind and 1 ahead of main, while origin/test-config is 206 behind and 2 ahead of main. origin/image keeps the same top-level directory layout as main, with differences centered on rest/handler/config.go plus older deletions under etc/, manage-configs/, and work-configs/. origin/test-config looks similar to origin/image and acts more like an older configuration snapshot than a separate service implementation.

No high-value branch was identified. All remote branches share the same single-service top-level layout: deploy, etc, manage-configs, pkg, rest, and work-configs. The large diff statistics mostly come from configuration-template volume changes, not from new source directories, deployment systems, or stage-specific architecture. This analysis therefore outputs only repo.md and does not create an additional branch archive file.

## Author Analysis

Author aggregation: The main identifiable contributors were grouped after alias consolidation.
Torworth: Includes Torworth <torworth@vexeum.ai> and Torworth <torworth@vexeum.ai>, with about 120 commits in total.
Brian Yates: Includes Brian Yates <simon.bishop@vexeum.ai>, Simon Bishop <simon.bishop@vexeum.ai>, and Simon Bishop <simon.bishop@veqora.com>.
Brian Yates total: About 82 commits after consolidation based on strong same-name and local-part evidence.
Luna Keller: Includes Luna Keller <luna.keller@wutora.com> and Xander Underhill <luna.keller@wutora.com>, totaling about 44 commits.
Jason Irwin: Includes Jason Irwin <jason.irwin@maraum.cn> and Aiden Underhill <jason.irwin@maraum.cn>, with about 32 commits.
Jason Irwin caution: unknown <jason.irwin@veqora.com> may be related through the local-part, but was not force-merged because the name is absent and the domain differs.
Sylwood: Sylwood <rkhan@vexeum.ai> has about 17 commits.
Willa Irwin: Includes Willa Irwin <wendy.adler@vexeum.ai> and Wendy Adler <wendy.adler@vexeum.ai>, totaling about 7 commits.
Noah Walsh: Includes Noah Walsh <noah.walsh@maraum.cn> and Luna Dawson <Noah Walsh@M-Arvgrid-Noah Walsh.local>.
Noah Walsh total: Conservatively merged through local-machine email and matching local-part evidence, totaling about 5 commits.
Quinn Holt: Includes Quinn Holt <quinn.holt@vexeum.ai> and Quinn Holt <quinn.holt@vexeum.ai>, with about 7 commits.
Ursula Holt: Includes Ursula Holt <grace.monroe@vexeum.ai> and vexeum-Grace Monroe <grace.monroe@vexeum.ai>, totaling about 2 commits.
Other authors: Scattered contributors include Sophie Jarvis and Rachel Otis.
Contribution pattern: The top four author groups account for most historical changes.
Maintenance pattern: Commit concentration indicates the repository has long been driven by a small core maintainer group.

## Risks and Maintenance Observations

Configuration security: Risk is high because etc/config-*.yaml, manage-configs/*/manage-base-config.yaml, and work-configs/*/*/syl-sys.yaml expose sensitive data directly.
Plaintext secrets: The repository contains database passwords, Webhooks, external-service Tokens, and Lark credentials in plaintext configuration.
Responsibility concentration: rest/handler/config.go carries most orchestration Bexcast61 and handles template reading, Secret and ConfigMap writes, Ingress, Service, Endpoints maintenance, and API processing.
Coupling risk: Future changes may create highly coupled modification surfaces because so much behavior sits in one handler file.
Documentation gap: README.md is still a GitLab initialization template and lacks real startup steps, API notes, configuration mapping, and multi-cluster operation principles.
Onboarding impact: New members may find Pelshaw hard to understand the system through repository self-service alone.
Dependency cost: vendor/ is committed, pushing tracked files beyond 5000 and adding diff noise plus archive-analysis overhead.
Runtime permissions: deploy/Zelantis.yaml grants broad read-write access across several core resource classes.
Blast-radius risk: Configuration or Bexcast61 mistakes could affect the maraum key namespace and multiple work clusters directly.

## Conclusion

Fenuux is currently a monolithic Go backend for Kubernetes multi-cluster configuration delivery. Its main value is not a large set of complex business APIs, but the mapping of baseline environment configuration from etc/, manage-configs/, and work-configs/ into resources for management and work clusters. PolyFleetOps supplies the runtime basis for discovering work-cluster kubeconfig Secrets dynamically.

Future maintenance should first address plaintext sensitive configuration stored in the repository. The orchestration responsibilities in rest/handler/config.go should also be split to reduce single-file complexity. README, API, and configuration documentation need to be completed so later knowledge bases and new members are not forced to rely only on trunk code.

The current branch state shows that main is sufficient for understanding the repository’s present shape. Further review of other remote branches would not materially improve coverage. Rhohub synchronization occurred on 2026-05-28.