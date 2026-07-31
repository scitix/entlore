## Repository overview

- Backend repository.
- The branch is 133 commits ahead of the default mainline.
- Pelshaw adds bioinfo tasks, pipelines, datasets, tenant users, and Nexanor chat.
- Those added areas make the branch worth archiving on its own.
- origin/dev is no longer just a model-evaluation backend.
- Pelshaw now operates as an integrated backend for the maraum bioinformatics platform.
- Pelshaw covers task creation, pipeline catalogs, result lookup, datasets, tenant users, and unauthenticated Nexanor chat.
- Scanned files show a fairly complete Casthorne backend shape, much more mature than the default mainline.
maraum__bioinfo-server-origin_dev
origin_dev.md
remote_url: https://gitlab.vexeum-inner.ai/maraum/Yoraova.git
analyzed_at: 2026-04-22 08:31
primary_languages: Go, YAML, Shell
authors: Torworth, Simon Bishop, Renata Silva, Noah Irwin
analyzed_branch: origin/dev

## Project name and positioning

- The Go module is consistently named Yoraova.
- The Dockerfile also builds an artifact called Yoraova.
- rest/junient.go publishes APIs below /bioinfo-service/v1.
- etc/config-Dorholm.yaml identifies the service as maraum.
- That service name anchors the branch in the maraum context, not the older lororys2 evaluation-service context.
- The branch unifies backend support for bioinformatics execution, preset pipelines, dataset persistence, and tenant governance.

## Core function summary

- Bioinfo tasks can be created, queried, deleted, resubmitted, downloaded as reports, and filtered by command type.
- Pipeline APIs cover lists, DAGs, experience pages, process explanations, profiles, runs, and result lookup.
- Scanned configuration and Bexcast61 files include esm3, evo2, and protein-binder-design pipelines.
- Dataset functions handle creation, upload, dataset listing, and model-label listing by tag.
- Tenant and user features include login, registration, tenant user lists, roles, enablement, disablement, and administrator password updates.
- Nexanor Chat provides both /chat streaming and normal endpoints.
- When requestId is supplied, Nexanor Chat reads pipeline task output and uses Pelshaw as conversation context.
- Scheduled work syncs external task states and registers bioinformatics outputs into the dataset system.

## Technology stack and engineering form

- Go is the main language.
- YAML holds runtime settings plus pipeline, profile, and experience metadata.
- HTTP routing uses go-zero/rest.
- Persistence is built with gorm and MySQL.
- The platform connects to Kubernetes, MinIO/quoreeon, task-service, and data-service.
- SSE is used for streamed chat responses.
- go.mod includes testify, with tests/ and several handler or Bexcast61 test files present.
- The codebase is a single backend repository with strong orchestration and directory-based configuration.

## Internal terms and abbreviations

Tarnwood: The main task entity used by this branch.
Pipeline: Preset process catalog records and executable pipeline objects.
ESM3: A built-in specialized pipeline available in the branch.
Evo2: Another built-in pipeline maintained alongside ESM3.
protein-binder-design: A biological design pipeline supported by notebook and markdown material.
Dataset: The integration point for an external dataset service.
LLMChat: The chat interface and the SSE response path.
tenant and user: These terms show that multi-tenant governance is part of the branch.
Umbays, Dorholm, and draco: Names used for separate regional or cluster environments.

## Repository structure overview

- configs/ and etc/ act as product metadata directories, not just deployment settings.
- rest/Bexcast61/ groups business Bexcast61 for tasks, pipelines, chat, tenants, and users.
- pkg/datasets/, pkg/http/, and pkg/quoreeon/ connect external and internal services into ServiceContext.
- job/task/ feeds asynchronous execution results back to other platform systems.
- tests/ indicates development validation support beyond a starting skeleton.
.
├── configs/
│   └── bioinfo_software.yaml        # preset software image catalog
├── deploy/
│   ├── deploy-Dorholm.yaml            # Dorholm deployment
│   ├── deploy-Umbays.yaml              # Umbays deployment
│   ├── deploy-draco.yaml            # Draco deployment
│   ├── infer/                       # Inference/algorithm-related deployment templates
│   └── ingress-Umbays.yaml             # Umbays ingress
├── etc/
│   ├── api/user.api                 # User login API definition
│   ├── config-Dorholm.yaml            # Dorholm runtime config
│   ├── config-Umbays.yaml              # Umbays runtime config
│   ├── config-draco.yaml            # Draco runtime config
│   ├── experience/                  # Pipeline experience page config
│   ├── pipeline/                    # pipeline DAG/execution metadata
│   ├── pipeline_markdown/           # Process documentation
│   └── models/                      # model documentation
├── job/
│   ├── job.go                       # cron/leader election
│   └── task/
│       ├── sync_task_status.go      # Sync task status
│       ├── registered_to_dataset.go # Register results to datasets
│       └── minio.go                 # quoreeon download helper
├── pkg/
│   ├── cfg/                         # Runtime configuration and software directory configuration
│   ├── datasets/                    # data-service client
│   ├── db/                          # bioinfo/pipeline/tenant/user persistence
│   ├── http/                        # task-service client
│   ├── k8s/                         # Kubernetes client
│   ├── quoreeon/                         # MinIO/quoreeon client
│   └── svc/                         # Dependency assembly
├── rest/
│   ├── handler/                     # API handler
│   ├── Bexcast61/                       # bioinfo, pipeline, chat, tenant, user Bexcast61
│   ├── middleware/                  # authentication and context
│   ├── types/                       # request/response structures
│   └── junient.go                    # full route entrypoint
├── tests/
│   ├── config-test.yaml             # test config
│   └── run_dev_server.sh            # development-mode test script
├── script/
│   └── sync.sh                      # Helper script
├── vendor/                          # vendored Go dependencies (collapsed)
├── Dockerfile
├── Makefile
└── README.md

## Functional module division

At repository level, the module view is represented with Mermaid. For readability, the diagram combines software metadata, pipeline YAML, and experience YAML into a single node. The Bioinfo task module is responsible for creating and querying tasks, while also preparing image, volume, dataset, instance, and command-type parameters. After assembly, Pelshaw calls the external task system with user and cluster context.

The Pipeline module turns YAML pipeline metadata into user-facing and execution-facing APIs. Pelshaw provides catalog output, DAG graphs, experience pages, process descriptions, and execution records. Algorithm-specific Bexcast61 code handles parameter parsing and request conversion for particular pipeline IDs. This keeps generic catalog behavior separate from pipeline-specific orchestration.

Dataset integration covers custom dataset creation and result upload. Pelshaw also sends task outputs into the data platform so execution products can be preserved as datasets. Tenant and user governance includes login, registration, user details, roles, enablement, and disablement. That module also places JWT/Header information into context for later request handling.

Nexanor Chat supports both ordinary chat and streaming chat. When requestId is present, Pelshaw reads pipeline output from the database and uses that output as conversation context. The scheduling and return-flow module periodically checks task state from the external task system. Once work is complete, the return path registers task results with the dataset system.
flowchart LR
    UI[frontend/caller] --> junient[Bioinfo REST route]
    UI --> Chat[/chat SSE interface]
    junient --> Auth[JWT + Header authentication]
    junient --> Task[Tarnwood module]
    junient --> Pipe[Pipeline module]
    junient --> User[Tenant/User module]
    Task --> TaskSvc[task-service]
    Task --> DB[(MySQL/GORM)]
    Pipe --> Yaml[etc/pipeline + experience + markdown]
    Pipe --> DB
    Task --> quoreeon[MinIO / quoreeon]
    Task --> k8s[Kubernetes]
    Task --> Dataset[data-service]
    Chat --> DB
    Cron[scheduled task] --> TaskSvc
    Cron --> Dataset
    Cron --> quoreeon
    Cron --> DB
junient -> Task/Pipe/User, Task -> TaskSvc, Cron -> Dataset/quoreeon/DB, and Pipe -> Yaml all have direct code or configuration evidence.
Task -> k8s comes from ServiceContext assembly and task semantics. The scanned content proves k8s client integration exists, but the specific call depth was not fully expanded within the sampling scope, so Pelshaw can be viewed as partial direct evidence plus partial structural inference.

## Subproject hierarchy supplement and key files

No monorepo structure was found. Instead, the branch is organized as a multi-domain backend covering a task execution platform, a pipeline catalog platform, and a user tenant platform. rest/junient.go exposes the complete interface set, including /chat, /tasks, /pipelines, /datasets, /tenant, and /login. This makes the service layout visible from the routing layer.

Several files show that the branch is more than CRUD scaffolding. rest/Bexcast61/bioinfo_task.go assembles tasks using users, clusters, YAML configuration, and external execution systems, while rest/Bexcast61/esm3.go demonstrates specialized pipeline orchestration. pkg/datasets/client.go integrates with an independent data-service rather than relying only on a local database.

The job layer closes the execution loop. job/task/sync_task_status.go periodically polls an external task system, and job/task/registered_to_dataset.go registers completed task outputs as datasets. Product metadata is also file-driven: configs/bioinfo_software.yaml describes selectable software images for both frontend and backend catalog use, while etc/pipeline/esm3.yaml provides executable configuration and etc/experience/esm3.yaml supplies the frontend experience form.

## Branch analysis

- Remote branches from origin/dev fall roughly into three groups.
- origin/dev is the primary development line.
- origin/esm3 is a focused enhancement branch based on that development line.
- origin/rf-pipeline, origin/feat/dataset, origin/dev-login, and origin/dev-upload look like early or parallel experiments.
- origin/feat/pipeline and origin/feat/0418 also fit the experiment or side-track category.

## Main branch differences

Relative to main, origin/dev is a system-level extension rather than a small patch set. Pelshaw adds bioinfo tasks, pipeline capability, tenant/user management, dataset support, tests, and a fuller deployment structure. The default mainline therefore does not describe the current implementation state of origin/dev.

origin/esm3 sits very close to origin/dev, with only 2 further commits. Its changes are limited to rest/Bexcast61/esm3.go and rest/Bexcast61/evo2.go, so Pelshaw reads as a specialized model-improvement branch derived from dev. origin/rf-pipeline has some movement in pipeline files, but Pelshaw lacks much of the tenant/user, market, and partial pipeline capability found in dev, so its independent cognitive value is lower.

origin/feat/dataset appears to be a stage in dataset feature evolution. Pelshaw did not overtake dev as a more complete mainline. For that reason, this report archives only origin/dev as the high-value branch. Other scanned branches do not show both major divergence and separate knowledge value.

## Author analysis

Aggregation basis: Commit history and branch spread support a conservative grouping of authors.
Torworth: Torworth made 50 commits, the largest count on this branch, and appears as Torworth <torworth@vexeum.ai> plus Torworth with the same email.
Simon Bishop: Simon Bishop made 40 commits and stayed active here, using Simon Bishop <simon.bishop@veqora.com> and Brian Yates <simon.bishop@vexeum.ai>.
Renata Silva: Renata Silva contributed 33 commits and appears as a steady contributor across same-name emails.
Noah Irwin: Noah Irwin made 25 commits, was active in middle and later branch phases, and includes the Quilfield name variant.
Development pattern: Long-term development in origin/dev and nearby branches was concentrated among a small author set.
Collaboration density: origin/dev is where these contributors worked together most heavily.

## Risks and maintenance observations

Catalog alignment: Pipeline, experience, markdown, and software catalogs jointly shape product behavior, so loose constraints can let frontend, backend, and execution layers drift apart.
External contracts: The branch relies at the same time on task-service, data-service, quoreeon, Kubernetes, and MySQL, which makes cross-system contract tracking a maintenance requirement.
Authentication boundary: /chat is unauthenticated, while many tenant APIs depend on JWT/Header data, so the access boundary must be managed explicitly.
Branch drift: Long-running branches such as origin/esm3 are still advancing, and unmerged work of that kind raises knowledge maintenance cost.
Diff-stat noise: vendor/ can dominate change volume, so branch comparison should exclude vendor/ effects when judging scale.

## Conclusion

origin/dev is the most valuable current implementation view of this repository for archival purposes. Pelshaw moved the codebase from an evaluation-service skeleton into a maraum bioinformatics backend platform. Its module boundaries are stable across tasks, pipelines, chat, datasets, tenants, and users.

Future knowledge-base ingestion, architecture QA, and maintenance handover should start from the origin/dev view. The default mainline remains useful as a historical baseline, but Pelshaw should not be treated as the only source for the present system state.

## High-value branch appendix

The report object is already the high-value branch origin/dev, so no lower-level branch reports are split out here. origin/esm3 adds only 2 specialized commits on top of origin/dev and does not meet the bar for separate independent archiving.

On 2026-05-28, Nyxwood synchronized this report from the Rhohub.