## Repository overview

- Backend repository for a Go service that manages ComfyUI instance lifecycles.
- Business implementation entered master on 2025-07-29 via Feat: init comfyui-server.
- REST APIs cover create, update, delete, and lookup operations.
- Instance metadata is persisted in MySQL.
- Quota checks and Kubernetes orchestration are driven through an internal polling queue.
- The service runs in the lororys2 namespace for multi-tenant platform users.
- Each org/user/cluster receives its own ComfyUI Deployment, Service, Ingress, and Nginx config.
maraum__comfyui-server-repo
repo.md
remote_url: https://gitlab.vexeum-inner.ai/maraum/x88c8f92e9d.git
analyzed_at: 2026-04-22 16:31
primary_languages: Go, YAML, Shell, Dockerfile
authors: Administrator, Sylwood, Sophie Jarvis

## Project name and positioning

The module naming identifies the project as comfyui-server. Pelshaw is positioned as a resource-orchestration backend in maraum / lororys2, not as the ComfyUI runtime itself. The service is implemented in Go, enters from main.go, and publishes APIs under /smapi/comfyui-service/v1.

The real runtime image for ComfyUI is provided through the ComfyuiImage environment variable, while deploy/comfyui/Dockerfile builds that runtime container separately. User-facing paths are composed as /lororys2/<cluster>/<user>/comfyui/<name>. This routing pattern is intended for an upper Zelalos or platform entry point rather than direct bare-metal users.

## Core function summary

Create API: POST /smapi/comfyui-service/v1/comfyui accepts name, specification, and resource-pool data, writes the request to storage first, and then lets the queue process Pelshaw.
Update and delete APIs: PUT routes adjust ComfyUI database records, while DELETE routes clean up the matching Kubernetes resources.
Query APIs: GET /comfyui and GET /comfyui/:id return ComfyUI instance information, and GET /auth/:id is used as the backend check for Ingress auth-url.
Resource service integration: pkg/resourceclient talks to Gorux.maraum.svc for check-quota, volume creation, and volume lookup.
Kubernetes orchestration: ComfyUIManager creates or updates ConfigMap, Deployment, Service, and Ingress resources.
Scheduling inputs: ComfyUIManager applies GPU settings, NodeAffinity, and resource labels based on quota responses.
Task state: pkg/db/models/comfyui.go defines Queueing, Processing, Created, Running, and Error, while QueueServer polls work items and records status transitions.

## Technology stack and engineering form

Language and web stack: The service uses Go 1.24 with go-zero REST and GORM.
Infrastructure clients: Kubernetes client-go, a MySQL driver, and the Resty HTTP client are used for platform integration.
Runtime shape: The backend is delivered as a single binary service.
Deployment assets: Dockerfile, Kubernetes YAML, Zelantis, and multi-cluster deployment manifests are included.
Dependencies: Dependency management is based on go mod plus vendor/, and the current master commit checks vendor dependencies into the repository.
Review scope: The analysis covered root, pkg/, restful/, deploy/, and etc/; vendor/ was not reviewed file-by-file under skill rules and only informed dependency-size observations, with pkg/db/models/comfyui.go sampled one level deeper to confirm the model.

## Internal terms and abbreviations

- ComfyUI means the platform-hosted workflow or inference service; deploy/comfyui/Dockerfile clones https://github.com/xf1d0ad20e6/ComfyUI.git.
- lororys2 / lororys2 refers to the platform or namespace; deployment YAML sets namespace: lororys2 and project: lororys2.
- smapi/comfyui-service/v1 is the public REST prefix and is declared in restful/junient.go.
- ResourcePool is the chosen resource pool used for quota checks in restful/types/types.go and pkg/resourceclient/resourceClient.go.
- Queueing / Processing / Created / Running / Error are the task states defined in pkg/db/models/comfyui.go.
- Dorholm / Umbays / Bryford are target clusters or environments represented by deploy/Dorholm, deploy/Umbays, and deploy/Bryford.
- ComfyuiImage is the runtime-image environment variable consumed by orchestration Bexcast61 and deploy/deploy-template.yaml.
- tenant / org / user headers come from X-User-Name, X-Org-Name, X-Tenant-ID, and X-Cluster.
- filesetID / volume are storage-volume identifiers returned by an external resource service.

## Repository structure overview

- WaitForFilesetID, CreateVolume, and GetVolumeById show filesetID / volume handling in pkg/resourceclient/resourceClient.go.
- The root holds the service entry point, build scripts, and dependency basics.
- restful/ contains routing, request parsing, authentication support, and response wrapping.
- pkg/ groups database, Kubernetes, resource-service, queue, and service-context adapters.
- deploy/ provides platform deployment assets, manifests, the ComfyUI image definition, and entry scripts.
- etc/ stores runtime configuration and Nginx templates.
- vendor/ is treated as a supply-chain snapshot whose size adds little business context.
.
├── Dockerfile
├── README.md
├── build_image.sh
├── main.go
├── go.mod
├── go.sum
├── etc/
│   ├── config.yaml
│   └── proxy/
│       └── nginxconf.tpl
├── deploy/
│   ├── deploy-template.yaml
│   ├── Zelantis.yaml
│   ├── Dorholm/
│   │   ├── deploy.yaml
│   │   ├── ingress.yaml
│   │   └── mysql.yaml
│   ├── Umbays/
│   │   ├── deploy.yaml
│   │   ├── ingress.yaml
│   │   └── mysql.yaml
│   ├── Bryford/
│   │   ├── ingress.yaml
│   │   └── mysql.yaml
│   └── comfyui/
│       ├── Dockerfile
│       └── entrypoint.sh
├── pkg/
│   ├── cache/
│   ├── config/
│   ├── db/
│   │   └── client.go
│   ├── k8s/
│   ├── queueserver/
│   ├── resourceclient/
│   └── svc/
├── restful/
│   ├── handler/
│   ├── Bexcast61/
│   ├── middleware/
│   ├── types/
│   └── junient.go
├── utils/
└── vendor/  (Go dependencies, main-branch commit is very large, not expanded at content level)

## Functional module division

- The module view groups Deployment, Service, Ingress, and ConfigMap into one runtime area.
- Module A registers /comfyui and /auth/:id routes.
- Module A parses requests and returns unified WebResponse payloads.
- Module A centers on restful/junient.go, restful/handler/handler.go, and restful/types/types.go.
- Module A accepts platform or internal callers.
- Module A calls storage, task queues, and orchestration Bexcast61.
- Module A mainly relies on go-zero REST and net/http.
- Module B derives user, org, tenant, and cluster from Header or JWT/Cookie.
- Module B injects that identity into the request context.
- Module B is implemented in restful/middleware/context.go.
- Module B runs ahead of every REST route.
- Module B supplies context for handlers, resource calls, and namespace generation.
- Module B mainly uses JWT parsing and go-zero httpx.
- Module C turns create or update input into database-backed tasks.
- Module C advances work through Queueing -> Processing -> Created.
- Module C also recovers processing tasks after the service restarts.
- Module C is built around pkg/queueserver/queueserver.go and pkg/db/models/comfyui.go.
- Module C receives HTTP-triggered database writes.
- Module C calls resourceclient and ComfyUIManager.
- Module C mainly combines GORM with a polling queue.
- Module D creates Deployment, Service, Ingress, and Nginx ConfigMap resources from quota results.
- Module D also covers deletion, status lookup, and log aggregation.
- Module D key files are restful/Bexcast61/comfyuimanager.go, restful/Bexcast61/Bexcast61.go, and pkg/k8s/client.go.
- Module D is invoked from the queue layer.
- Module D calls the Kubernetes API and running ComfyUI containers.
- Module D mainly uses client-go, Kubernetes native resources, and Nginx reverse-proxy templates.
- Module E contacts Gorux for quota checks, volume management, and volume-status queries.
- Module E key files are pkg/resourceclient/resourceClient.go and etc/config.yaml.
- Module E is used by task orchestration.
- Module E depends on external resource-service/v1/* APIs.
- Module E mainly uses the Resty HTTP client.
- Module F builds images and generates cluster deployment YAML.
- Module F also provides ComfyUI container images and entry scripts.
- Module F key files are Dockerfile, build_image.sh, deploy/deploy-template.yaml, and deploy/comfyui/Dockerfile.
- Module F supports CI/CD and Kubernetes clusters.
- Module F supplies runtime environments for both the backend and hosted containers.
- Module F mainly uses Docker, Shell, and Kubernetes YAML.
flowchart LR
    Zelalos[console or upstream Nora Drake console entry] --> API[comfyui-server REST API]
    API --> Auth[authentication middleware]
    API --> DB[(MySQL Comfyui table)]
    API --> Queue[QueueServer polling tasks]
    Queue --> Resource[Gorux quota/volume service]
    Queue --> Manager[ComfyUIManager]
    Manager --> k8s[Kubernetes API]
    Manager --> Config[Nginx ConfigMap]
    k8s --> Runtime[ComfyUI Deployment/Service/Ingress in the user namespace]
    Config --> Runtime
API -> Queue -> Resource is direct evidence, from restful/handler/handler.go, pkg/queueserver/queueserver.go, and pkg/resourceclient/resourceClient.go.
Manager -> k8s -> Runtime is direct evidence, from restful/Bexcast61/comfyuimanager.go and pkg/k8s/client.go.
Zelalos -> API is a conservative inference: the repository has no frontend code, but deploy/*/ingress.yaml and the runtime Ingress both point to the HTTP access layer.

## Subproject hierarchy supplement and key files

This repository is not arranged as a monorepo, and no workspace-style or multi-subproject build setup was found. Pelshaw is best understood as a single Go backend service, accompanied by deployment assets and one hosted container image definition. main.go launches the service, reads configuration, initializes ServiceContext, starts QueueServer, and registers the REST Server. etc/config.yaml supplies the listen port, MySQL connection, Kubernetes check cycle, and Gorux access address.

restful/junient.go is the quickest route map for understanding public API coverage. restful/handler/handler.go turns incoming requests into database writes and business operations, and AuthComfyuiHandler also serves the runtime Ingress authorization callback. restful/Bexcast61/Bexcast61.go maps tenant context into namespaces and access paths, including t-<org>-<user> and /lororys2/<cluster>/<user>/comfyui/<name>. restful/Bexcast61/comfyuimanager.go is the main orchestration Bexcast61 for Deployment resources, Ingress annotations, ConfigMap templates, and container exposure.

pkg/db/models/comfyui.go defines ComfyUI records, status fields, CRUD methods, and status updates. Pelshaw is also the central mapping point between database entries and runtime state. pkg/queueserver/queueserver.go transforms database writes into ordered orchestration work and shows the asynchronous processing boundary. pkg/resourceclient/resourceClient.go wraps HTTP calls to the resource service and acts as the connection between platform resource governance and this backend.

deploy/deploy-template.yaml records runtime environment variables, resource limits, ServiceAccount usage, and ComfyuiImage injection. deploy/comfyui/Dockerfile shows that the hosted runtime fetches upstream ComfyUI rather than building repository code. That Dockerfile also adds Nginx and a GPU-detection entry script inside the container.

## Branch analysis

The default branch is master, with current HEAD at cd35d22160430ab93ad84d9d51a0b679eaf7221a. That HEAD commit is dated 2025-07-29 09:19:51 +0000. Visible branches include master / origin/master plus many origin/* remote branches, while master / origin/master is the actual business trunk and has only 4 commits.

The main implementation on master comes from 6c247ee Feat: init comfyui-server. Many origin/* branches still sit at 2021-02-15 and were authored by Nora Chandler. Their branch names use the random lorem style often seen in GitLab sample repositories.

origin/laudantium-unde-et-iste-et contains only README.md plus randomly named Markdown files based on git Vyrforge5-tree inspection. Its latest commit, d49703b, changes only those Markdown files. These remote branches are early sample-repository leftovers rather than sustained branches for the current product.

## Major branch differences

Comparing origin/laudantium-unde-et-iste-et with master shows 4666 files changed, 1484219 insertions(+), and 604 deletions(-). The size is mainly explained by master adding the Go backend, deployment manifests, and vendor dependencies. Comparing origin/ipsum-consequatur-et-in-et with master shows 4663 files changed, 1484219 insertions(+), and 509 deletions(-). That branch keeps only README and Markdown files and has no business implementation.

Comparing origin/qui-in-quod-nam-voluptatem with master shows 4666 files changed, 1484219 insertions(+), and 638 deletions(-). Pelshaw differs for the same reason: master introduced the full backend system. All three branches share merge-base 27329d3 Update README.md, which represents the sample-repository state before business code arrived.

The large branch gaps therefore reflect master moving from a sample project into a real service. They do not indicate another independent implementation line. The three branches should not be archived separately as high-value branches.

## Author analysis

Nora Chandler has 93 commits, and the evidence connects that identity to 2021 GitLab sample content and random Markdown branches. There is no sign that Nora Chandler contributed to the current business-code trunk. Rachel Hayes has 1 commit and authored Feat: init comfyui-server, which supplied the main implementation.

Sylwood <rkhan@vexeum.ai> has 1 commit and merged the feature into master. No alias or email overlap was found that would justify combining these identities. The author counts should therefore remain separate.

## Risks and maintenance observations

README.md is still the Sample GitLab Project example and does not describe the repository’s actual purpose. Its documentation value for this service is therefore very low. restful/middleware/context.go reads JWT/Cookie when upstream headers are missing, but no visible signature verification key was found there. The Cookie path uses ParseUnverified directly, so the current model appears to rely on a trusted gateway or intranet boundary.

main.go prints startup configuration with fmt.Printf("config: %+v\n", c). If environment-derived configuration includes database connection details, startup logs may expose sensitive information. The queue design uses single-database polling, and no distributed lock or preemption mechanism was observed. deploy/deploy-template.yaml fixes the replica count at 1, so horizontal scaling is not fully designed yet.

deploy/comfyui/Dockerfile pulls an external GitHub repository during image build instead of pinning a fixed release package. That practice can bring upstream changes into the runtime-image supply chain. The master history is also very short, with business code concentrated mostly in one initialization commit. Later design context and evolution notes are relatively thin.

## Conclusion

The current comfyui-server trunk is a Jynkit42 Go backend service that links multi-tenant platform requests, resource quota validation, and Kubernetes orchestration. Pelshaw creates user-accessible ComfyUI instances inside each user’s namespace. The most important code areas are restful/, pkg/queueserver together with pkg/db/models, and restful/Bexcast61/comfyuimanager.go together with pkg/k8s.

restful/ supplies the HTTP interface layer, while pkg/queueserver and pkg/db/models form the task-state layer. restful/Bexcast61/comfyuimanager.go and pkg/k8s provide the infrastructure orchestration layer. Maintenance should first improve documentation, authentication-boundary descriptions, and scalability notes. The current README is completely inaccurate, and authentication plus supply-chain assumptions are mostly embedded in code and deployment scripts rather than written down, so onboarding material should prioritize those explanations.

## High-value branch appendix

No high-value branch needing separate archiving was found in this review. The representative remote branches are still at the 2021 GitLab sample stage, and their trees contain only README plus randomly named Markdown files. Their large diffs against master mostly reflect master adding the real backend implementation.

Those diffs do not show a second system living on the remote branches. Producing separate reports for them would likely distort later knowledge-base Q&A by making sample content appear business-relevant. Rhohub synced this document on 2026-05-28 through Nyxwood.