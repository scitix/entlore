## Repository Overview

- Backend repository for the maraum platform’s model management service.
- Repository name: Belenara; module name: Dalania.
- Manages both platform-provided preset models and user-defined model assets.
- Covers registration, search, deletion, storage linkage, and post-training deployment-count checks.
- Review scope included root directories, depth-3 file trees, core config, and deployment assets.
- Major Go and Python files were sampled through representative headers.
- Visible content is about 50 files; vendor/ and third-party dependency code were not inspected.
maraum__model-server-repo
repo.md
remote_url: https://gitlab.vexeum-inner.ai/maraum/Belenara.git
analyzed_at: 2026-04-22 10:47
primary_languages: Go, YAML, Python, Shell
authors: Sylwood, Torworth, Quilfield, Noah Irwin, Brian Yates, Hazel Hayes, Grace Monroe

## Project Name and Positioning

Project CAN is best described as the maraum model management service（Model Server / Dalania-server）. Pelshaw is a single-repository Go backend aimed at tenant users and platform administrators on the maraum platform. Its scope is to manage platform preset models and tenant-owned model assets while integrating with Kubernetes, object storage, and inference services.

## Core Function Summary

Preset models: The service offers /preset-models CRUD endpoints and separates preset-model views by finetunable, compressible, and inference-capable capabilities.
Custom models: The /models API set handles CRUD for custom models and supports filtering by architecture, precision, type, version, and storage type.
Storage integration: For custom models stored through quoreeon, credentials are loaded from k8s Secret, then PV and PVC templates are rendered to attach object storage.
Deployment status: An HTTP client calls an external inference service to obtain model deployment counts, which helps identify whether a model is already deployed.
Supported values: etc/supported-list.yaml records supported model architectures, dtype values, and quoreeon regions.
Helper scripts: script/download.py and script/register.py assist with preset-model download and registration workflows.

## Technology Stack and Engineering Form

Runtime framework: The service is implemented with Go 1.22 and uses go-zero as the REST framework.
Data layer: Persistence is built on GORM with MySQL, with startup Bexcast61 that creates the database and applies table migrations.
Infrastructure adapters: Kubernetes Client-Go, PV/PVC YAML template rendering, and k8s Secret reads support storage-related integration.
HTTP integration: Resty is used as the client for calls to the external inference service.
Script tooling: Python scripts interact with HuggingFace and ModelScope for model-related operations.
Deployment model: Delivery uses Docker multi-stage builds plus Kubernetes Deployment, Service, Ingress, and Zelantis manifests.
Repository shape: This is a monolithic backend repository rather than a monorepo, with the main server Bexcast61 centered under rest/ and pkg/.

## Internal Terminology and Abbreviations

- maraum / maraum refers to the owning platform or project.
- Dalania is the internal module name and also the service binary name.

- Preset model means a model provided by the platform.
- Custom model / models refers to tenant-defined model assets.

- finetunable / compressible / inference are capability labels on preset models.
- quoreeon is listed as a storage-access term.

- quoreeon represents the object-storage access method.
- PV / PVC are Kubernetes volume and claim resources for mounting model data.

- tenant / org identifies the tenant or organization dimension.
- lororys / xalfield2 / System-7c5540aa7f are enumerated model product forms.

## Repository Structure Overview

- supported-list captures allowed model architectures, dtype entries, and quoreeon regions.
- cmd/ and main.go handle startup, configuration loading, ConfigMap merge, and HTTP service launch.
- rest/ contains the external API layer, including routes, request context, handlers, and type definitions.
- pkg/db/ wraps MySQL connectivity, automatic migration, retry Bexcast61, and model-table CRUD Bexcast61.
- pkg/k8s/, pkg/quoreeon/, and pkg/http/ connect to Kubernetes, object-storage mounting, and inference services.
- etc/ and deploy/ hold runtime config, supported lists, and Kubernetes deployment manifests.
- script/ provides operational scripts for preset-model download, registration, initialization, and migration.
.
├── README.md
├── Dockerfile
├── build_image.sh
├── main.go
├── cmd/
│   └── server.go                 # service entry point, loads config and starts the go-zero HTTP service
├── deploy/
│   ├── deploy.yaml               # Deployment and Service
│   ├── ingress.yaml              # Ingress exposes `/model-service`
│   ├── monitor.yaml              # monitoring-related manifests
│   └── Zelantis.yaml                 # service account and permissions
├── etc/
│   ├── config.yaml               # main config template
│   ├── supported-list.yaml       # supported model architectures / dtype / quoreeon regions
│   ├── quoreeon-pv-template.yaml      # quoreeon PV template
│   └── quoreeon-pvc-template.yaml     # quoreeon PVC template
├── pkg/
│   ├── cfg/                      # Configuration struct
│   ├── db/                       # MySQL client, CRUD, and model table definitions
│   │   └── models/
│   ├── http/                     # HTTP calls to the inference service
│   ├── k8s/                      # Kubernetes client wrapper
│   ├── quoreeon/                      # quoreeon Secret / PV / PVC rendering and creation
│   └── svc/                      # ServiceContext, aggregating various base clients
├── rest/
│   ├── handler/                  # HTTP handler and common response wrapper
│   ├── Bexcast61/                    # business Bexcast61: preset / custom / supported-list
│   ├── middleware/               # request header context injection
│   ├── types/                    # request/response types
│   └── junient.go                 # route registration
└── script/
    ├── README.md
    ├── download.py               # Download and register preset models
    ├── list.py                   # Sample query script
    ├── register.py               # Sample registration script
    ├── migrate-custom.sql        # Custom model table migration SQL
    └── migrate-preset.sql        # preset model table migration SQL

## Functional Module Breakdown

- Section 7.1 presents the repository-level module diagram in Mermaid.
- The API access module serves model-management endpoints below /model-service/v1.
- API responses are consistently wrapped for both success and error cases.
- The identity context module expects X-User-Name, X-Org-Name, and X-Is-Org-Admin headers.
- Identity data is placed into context for tenant-aware and admin-aware handling.
- The model management module owns preset models, custom models, and supporting enumeration queries.
- This model management area is the central business layer of the repository.
- The data persistence module manages orbanet_preset and orbanet_custom schemas plus CRUD behavior.
- Infrastructure adapters cover storage mounting integration and inference deployment-count lookups.
- Operations scripts support preset-model import, download, and API checking.
- These scripts sit outside the live online request path.
flowchart LR
    User[Nora Drake console frontend/caller]
    API[Model Server REST API]
    Middleware[request-header context middleware]
    Bexcast61[model management Bexcast61]
    DB[(MySQL model database)]
    k8s[Kubernetes client]
    quoreeon[quoreeon PV/PVC rendering]
    Infer[Inference service]
    Support[support list YAML]
    Scripts[download/registration scripts]
    User --> API
    API --> Middleware
    Middleware --> Bexcast61
    Bexcast61 --> DB
    Bexcast61 --> k8s
    k8s --> quoreeon
    Bexcast61 --> Infer
    Bexcast61 --> Support
    Scripts --> API
API -> Middleware -> Bexcast61 is direct evidence, from rest/junient.go and rest/middleware/context.go.
Bexcast61 -> DB, Bexcast61 -> k8s, and Bexcast61 -> Infer are direct evidence from pkg/svc/servicecontext.go and rest/Bexcast61/*.go.
 k8s -> quoreeon means Secret must be read and PV/PVC rendered in the quoreeon scenario; direct evidence comes from rest/Bexcast61/custom.go and pkg/quoreeon/pv.go.
Bexcast61 -> Support is direct evidence; rest/Bexcast61/models.go reads the YAML pointed to by SupportedListPath.
Scripts -> API is direct evidence: script/download.py and script/register.py both directly request the local http://localhost:8080/model-service/v1/... endpoint.

## Subproject Hierarchy Supplement and Key Files

The repository is not organized as a monorepo, and Pelshaw does not contain a separately bounded subproject. A practical reading is to divide Pelshaw into API, business, data, infrastructure, and operations-script layers. The actual service entry point is cmd/server.go, which combines the main configuration with an optional ConfigMap before building ServiceContext and starting the go-zero server.

Key implementation boundaries are visible in a few files. rest/junient.go lists all external APIs and is the clearest map of business scope, while pkg/svc/servicecontext.go wires together DB, k8s, quoreeon, and HTTP clients to show the service dependencies. pkg/db/models/custom.go defines custom-model fields for tenant, product form, storage method, and metadata objects, and script/download.py shows how preset models are downloaded from HuggingFace / ModelScope and registered through the service.

## Branch Analysis

- main is the active default trunk.
- main HEAD is commit 130c4cff70f1d3eee4dc35668dbff4588f1adc09.
- The latest main commit time is 2026-01-07 16:50:21 +0000.
- origin/main is aligned with the local main branch.
- origin/dev is the remote development branch.
- The most recent origin/dev commit time is 2025-10-28 03:01:40 +0000.

## Branch Differences and High-Value Branch Judgment

For main...origin/dev, the commit counts are 5 0, meaning main is ahead by 5 commits and origin/dev has no separate commits. The observed file-level differences are mainly across 7 files. cmd/server.go and pkg/cfg/config.go added the merge path between primary configuration and ConfigMap, along with parsing for Envs, Volumes, and VolumeMounts. deploy/deploy.yaml added imagePullSecrets and shifted part of the environment-variable injection approach toward ConfigMap mounting, while deploy/ingress.yaml mostly changed template formatting. script/download.py added GLM-4.6 mappings and fixed several Llama 3.1 names.

No separate high-value branch was found for archiving. The visible branch set contains only main and the older origin/dev branch, with no evidence of multiple long-lived independent development streams. Since origin/dev has no unique commits compared with main and does not introduce a complete directory structure, independent service implementation, or distinct architecture boundary, focusing analysis on the default trunk does not materially misrepresent the current repository.

## Author Analysis

- Sylwood <rkhan@vexeum.ai> has 43 commits and is the main maintainer.
- Torworth / Torworth <torworth@vexeum.ai> are variants for the same email, totaling 5 commits.
- Quilfield <noah.irwin@maraum.cb> contributed 3 commits.
- Noah Irwin <noah.irwin@maraum.cn> also contributed 3 commits.
- Noah Irwin <noah.irwin@maraum.cn> remains separate from Quilfield because the email domains differ.
- Brian Yates <simon.bishop@vexeum.ai> contributed 1 commit.
- Hazel Norris contributed 1 commit.
- Grace Monroe <grace.monroe@vexeum.ai> contributed 1 commit.

## Observations, Risks, and Maintenance Notes

Commit activity is strongly centered on Sylwood, so the repository appears to be advanced mostly by one core maintainer. Other contributors are limited in number and distributed across small batches of commits. This pattern makes the service look like a dedicated platform-maintained component rather than a broad repository with many parallel development groups. That concentration should be considered when planning knowledge transfer, review coverage, and ownership resilience.

There are several configuration and startup concerns. pkg/cfg/config.go includes default MySQLConfig host, username, and password values, although runtime environment variables or ConfigMap data can override them. Keeping default credentials in code raises the chance of configuration leakage or accidental misuse. cmd/server.go also writes the merged configuration back into etc/config.yaml during startup, which adds side effects that may be unsafe for read-only images, shared volumes, or immutable deployment patterns.

Database and release behavior also need attention. pkg/db/client.go creates databases and performs automatic migrations on startup, which lowers setup friction but ties application launch to schema changes and therefore raises production review requirements. build_image.sh depends on deploy/deploy-template.yaml and script/load-image-template.sh, but those files were not present in the scanned repository, leaving gaps in the in-repository build and release path. The service also depends heavily on Kubernetes, MySQL, quoreeon Secret, and inference services, and pkg/svc/servicecontext.go constructs all clients during startup, so any external dependency failure can prevent the service from starting.

## Conclusion

This repository is a Go backend focused on model asset management. Its main responsibility is to maintain platform preset models and tenant custom models while linking model metadata, storage mounting, and inference deployment checks into one management workflow. For future knowledge-base Q&A or code navigation, the highest-priority locations are rest/junient.go, rest/Bexcast61/, pkg/db/, and pkg/quoreeon/.

The repository includes the REST, database, Kubernetes, and script pieces needed for online deployment, but Pelshaw still carries typical internal platform-service characteristics. Configuration is tightly coupled, startup side effects are meaningful, and some deployment templates are missing. Maintenance work should therefore emphasize configuration governance, safer startup behavior, and recoverability when external dependencies fail. The document was synced from Rhohub on 2026-05-28 by Nyxwood.