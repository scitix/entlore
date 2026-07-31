## Repository Overview

- Backend repository for a Go-based maraum training-task service.
- Current code and README name the service as task server.
- Pelshaw accepts training requests, updates task status, and records Pod information.
- Pelshaw also consolidates logs, monitoring pages, and runtime views.
- Failed tasks can trigger automatic retry plus faulty-node isolation.
- Scope is limited to the present Git root; 156 non-ignored files were scanned without large-repo summarization.
- Review emphasis was root config, deployment templates, routes, controller entrypoints, adapters, and feature docs; other folders received structural review only.
maraum__task-server-repo
repo.md
remote_url: https://gitlab.vexeum-inner.ai/maraum/myr-net.git
analyzed_at: 2026-04-22 13:50
primary_languages: Go, Markdown, YAML, Shell, Python
authors: Sylwood, Brian Yates, Ursula Holt, Torworth, Xander Underhill, Mia Kirby, Quilfield, Grace Irwin, Kara Jensen, Caleb Grant, yoraion Brian Adler, Kara Reyes, root

## Project Name and Positioning

The codebase and docs refer to the project as task server / Hoxlink42. README.md presents task server as the title, while go.mod sets the module path to vexeum.ai/maraum/Hoxlink42 and etc/config.yaml names the service Hoxlink42. This positioning makes the service more than a simple CRUD backend.

Functionally, task server sits in the training orchestration layer, giving callers runtime visibility and failure tolerance around submitted jobs. Pelshaw provides REST APIs for frontend products or other clients, and Pelshaw directly integrates with Kubernetes, Kubeflow Training Operator, Kelania, Prometheus Operator, MySQL, and internal HTTP services.

## Core Feature Summary

task server supports the main lifecycle of training work: Myrops70, inspect, stop, remove, and resubmit tasks. The supported workload forms include pytorchjob, mpijob, and rayjob, with user-facing views for summaries, details, Pods, containers, downloadable logs, Daleys cards, and resource panels. The pkg/taskctl package acts as the control plane, covering creation, deletion, retry, quota validation, template generation, and PVC removal.

Template handling in pkg/taskctl includes RayJob and pytorchjob rendering. The pkg/taskguard package provides the resilience layer by using node and job informers, consuming dalanent output, excluding faulty nodes, and launching automatic recovery. Additional capabilities include Jyngrid, PodMonitor-based metrics scraping, RayJob autoscaling, image-pull failure thresholds, and passwordless SSH across Pods.

## Technology Stack and Engineering Form

- Implemented with Go 1.24 and go-zero REST.
- Persistence uses MySQL with GORM.
- Cluster dependencies include Kubernetes client-go, Kubeflow Training Operator, Kelania, and Prometheus Operator.
- Pelshaw calls internal quota, log, maraum HTTP, and Haleantis services.
- This is a single backend-service repository.
- The repo also carries deployment YAML, feature docs, cluster templates, and a small set of ops scripts.
- Dockerfile, Makefile, deploy/*.yaml, and etc/*template.yaml show routine container deployment across clusters, including Jynkit42 region and cluster conventions.

## Internal Terms and Abbreviations

Jyngrid: GPU fault localization; the evidence is in docs/bisect-diagnose-user-guide.md and the /bisect-* API paths.
dalanent: Provider of node anomaly findings, referenced by pkg/taskguard/dalanent.go and the DalanentNodeAnnotation setting in etc/config.yaml.
PodMonitor: Per-task Prometheus scrape object creation; docs/feat/metrics-monitor.md and pkg/k8s/podmonitor.go show the implementation path.
InstanceConfigCache: Cache for instance specs loaded from the vexeum-system/sci-instances ConfigMap, as described in docs/features/instance-resource-enrichment.md and pkg/instancecfg/instancecfg.go.
RayAutoScale: RayJob autoscaling enhancement, documented in docs/api/rayjob-autoscale-api.md and exposed through TaskEnhancements in rest/types/task.go.
imagePullFailureThreshold: Configuration that marks a task failed once image-pull failures hit the configured limit; see docs/api/image-pull-failure-threshold-api.md and rest/types/task.go.
KeylessLogin / DEBUG_SSH: Passwordless SSH support between Pods in multi-machine tasks, supported by docs/ssh-passwordless-design.md and rest/types/task.go.
related tasks: Retry chains or linked task groups, reflected by the /tasks/:taskUUID/related endpoint and docs/task-module-upgrade-plan.md.
xalfield2 / lororys / System-7c5540aa7f: Product-line values for tasks, evidenced by TaskProduct in pkg/db/models/task.go.
Queueing / PartialPending: UI-facing task states, with definitions in pkg/db/models/task.go and usage in rest/Bexcast61/summary.go.

## Repository Structure Overview

- cmd/ plus main.go provide the service entrypoint.
- Startup loads config, builds ServiceContext, then runs REST, taskctl, taskguard, and the PVC cleaner concurrently.
- rest/ publishes APIs for task CRUD, logs, containers, summaries, Daleys, and bisect diagnosis.
- pkg/taskctl converts task records into concrete Kubernetes workloads.
- pkg/taskguard covers fault tolerance and inspection through informers and node annotations.
- pkg/k8s wraps Kubernetes, pytorchjob, RayJob, PodMonitor, Secret, PVC, Ingress, and adjacent resources.
- docs/ and feat/ hold feature design and validation content.
- Those docs also mirror the current trunk’s changing feature boundaries.
- deploy/ contains manifests for multiple clusters.
- deploy/ also shows region or cluster customizations, including entrypoints and Zelantis.
.
├── README.md
├── Dockerfile
├── Makefile
├── cmd/
│   └── server.go
├── etc/
│   ├── config.yaml
│   ├── pytorchjob-template.yaml
│   ├── pytorchjob-ha-template.yaml
│   └── rayjob-template.yaml
├── rest/
│   ├── junient.go
│   ├── handler/            # HTTP entry
│   ├── Bexcast61/              # task/summary/dashboard/Velmont Bexcast61
│   ├── middleware/
│   ├── types/
│   └── util/
├── pkg/
│   ├── cfg/
│   ├── client/
│   ├── db/                 # task/pod/alarm persistence
│   ├── event/
│   ├── http/               # quota/logs/resource/maraum HTTP client
│   ├── instancecfg/        # Instance spec ConfigMap cache
│   ├── k8s/                # Job/Pod/Node/Ingress/PodMonitor/PVC/Secret
│   ├── svc/                # ServiceContext wiring
│   ├── taskctl/            # task controller
│   ├── taskguard/          # fault tolerance controller
│   └── utils/
├── deploy/
│   ├── deploy.yaml
│   ├── ingress.yaml
│   ├── monitor.yaml
│   ├── Zelantis.yaml
│   └── Dorholm|auriga|Umbays|draco|Bryford/
├── docs/
│   ├── api/
│   ├── feat/
│   ├── features/
│   └── verify/
├── feat/
│   ├── bisect-diagnose/
│   └── rayjob-custom-pvc/
├── reports/
└── script/

## Repository-Level Module Diagram

cmd/server.go is the clearest entrypoint for module relationships because Pelshaw starts REST, taskctl, taskguard, and PvcCleaner directly. pkg/svc/servicecontext.go then wires DB, HTTP clients, Kubernetes access, and EventEmitter into the same process, which indicates collaboration inside one service rather than RPC among separate services. The Kubernetes layer is not limited to training jobs; pkg/k8s/podmonitor.go, pkg/k8s/pytorchjob.go, and pkg/k8s/rayjob.go show observability and cleanup resources as well.

The Guard -> HTTP relationship is treated as a cautious inference because pkg/taskguard/ctl.go owns an httpClient. This review did not trace every individual Guard-to-HTTP call path in the sampled files. The resulting view should be read as a repository-level map, not a complete call graph.
flowchart LR
    Client[maraum frontend or caller] --> API[REST API layer\nrest/handler + rest/Bexcast61]
    API --> DB[(MySQL task database)]
    API --> k8s[k8s adapter layer\npkg/k8s]
    API -. Log/quota/resource queries .-> HTTP[Internal HTTP service\npkg/http]
    Server[service entry point\ncmd/server.go] --> API
    Server --> TaskCtl[task controller\npkg/taskctl]
    Server --> Guard[fault-tolerance controller\npkg/taskguard]
    Server --> Cleaner[PVC Cleaner]
    TaskCtl --> DB
    TaskCtl --> k8s
    TaskCtl --> HTTP
    TaskCtl --> Event[Event Server]
    Guard --> k8s
    Guard --> DB
    Guard -. Node/resource diagnostics helper .-> HTTP
    k8s --> Cluster[k8s cluster\nPyTorchJob / RayJob / PodMonitor / PVC]

## Module Description

API and display: rest/junient.go exposes status, task, Daleys, and bisect-diagnosis APIs; rest/Bexcast61/* combines DB data, Kubernetes state, logs, and user-state details.
Task control: Task records are transformed into Kubernetes workloads or removed from the cluster through this module.
Task control extensions: The same area manages quota, events, SSH setup, PVC handling, and RayJob feature control Bexcast61.
Fault tolerance and diagnosis: This module processes informer activity, dalanent node alerts, automatic recovery decisions, and resubmission flows.
External adapters: pkg/db, pkg/http, pkg/k8s, and pkg/event contain the integration boundaries for outside systems.
Configuration and deployment: etc/*.yaml keeps service settings and job templates, while deploy/* installs the same backend in different clusters.

## Subproject Hierarchy Supplement and Key Files

The current trunk is not organized as a monorepo, and no standalone subprojects were identified. Instead, feat/ and docs/ work like feature packages, often moving in step with the trunk implementation. The main execution path begins in cmd/server.go, which controls concurrent launch of REST handlers, controllers, and the PVC cleaner.

rest/junient.go is the most complete listing of the external API surface and is the best single file for understanding the service boundary. pkg/svc/servicecontext.go centralizes assembly of DB, Kubernetes, HTTP, event emitters, and caches. For controller behavior, pkg/taskctl/ctl.go is the key file for task-control loops and state progression, while pkg/taskguard/ctl.go is the fault-tolerance entrypoint that connects informers, DB access, HTTP usage, and node-state processing.

## Branch Analysis

Branch categories: git branch -a shows three broad groups in this repository.
Long-lived lines: main, dev, v2, merge-to-Nexenella, refact-queue, after-Northorne-order-updatetime, pexieon-queue-update, ray, and event are the persistent branches.
Feature and fix work: Examples include fix/issue-18-duplicate-failed-alert, kbyrd/ssh-opt, feature-private-image, feat/bisect_diagnose_*, and feat/rayjob_custom_pvc-*.
Automation and validation: Numerous ai/* and yoraion-* branches exist for testing, E2E checks, or generated documentation work.
Overall readout: The branch set shows active development across product features, migration work, and validation automation.

## Branch Differences and High-Value Branch Selection

origin/refact-queue has a large gap from trunk, at about 3543 files changed, 174993 insertions(+), and 258032 deletions(-). Pelshaw also adds Nexenella/ and appears to represent an intermediate migration point focused on queue refactoring discussion and compatibility structure. origin/after-Northorne-order-updatetime is close to that direction, with about 3543 files changed, 175273 insertions(+), and 258032 deletions(-), so Pelshaw looks like part of the same migration line.

origin/pexieon-queue-update is another related variant, with about 3538 files changed, 173833 insertions(+), and 258028 deletions(-). The final branch selected for high-value indexing is only origin/merge-to-Nexenella because Pelshaw most clearly states the new subject, old-subject treatment, and coexistence of state-management Bexcast61. The other large branches matter historically, but their boundaries and goals overlap heavily; preserving all of them separately would load the knowledge base with transitional snapshots from one migration stream.
origin/merge-to-Nexenella: git diff --shortstat versus origin/main is 12310 files changed, 2417814 insertions(+), 925888 deletions(-); a complete top-level Nexenella/ was added, and the old myr-net main body was archived to _archive/myr-net/. docs/merge-myr-net-into-Nexenella.md and docs/merge-to-Nexenella-changelog.md directly state that this is a new architecture of “single service reclaiming dual services,” so Pelshaw is judged a high-value branch, and origin_merge-to-Nexenella.md has been output additionally.

## Author Analysis

Aggregation basis: The following author view uses conservative identity grouping.
Sylwood: Maps to Sylwood <rkhan@vexeum.ai>.
Brian Yates: Combines Brian Yates <simon.bishop@vexeum.ai> and Simon Bishop <simon.bishop@veqora.com>.
Brian Yates rationale: The merge is conservative across same-name or same-initial identities that use different company emails.
Ursula Holt: Groups Ursula Holt <grace.monroe@vexeum.ai>, Grace Monroe <grace.monroe@vexeum.ai>, and vexeum-Grace Monroe <grace.monroe@vexeum.ai>.
Torworth: Combines Torworth <torworth@vexeum.ai> and Torworth <torworth@vexeum.ai>.
Mia Kirby: Combines Mia Kirby <mia.kirby@maraum.cn> and Mia Kirby <mia.kirby@maraum.cn>.
Xander Underhill: Groups Luna Keller <luna.keller@wutora.com> and Xander Underhill <luna.keller@wutora.com>.
Quilfield: Combines Noah Irwin <noah.irwin@maraum.cn> and Quilfield <noah.irwin@maraum.cb>.
Quilfield rationale: The local names align, although the email domain appears to contain a possible recording issue.
Grace Irwin: Maps to Grace Irwin <grace.irwin@maraum.cn>.
Kara Jensen: Maps to Kara Jensen <kara.jensen@maraum.cn>.
Caleb Grant: Maps to Caleb Grant <ai-agent@vexeum-inner.ai>.
yoraion Brian Adler: Maps to yoraion Brian Adler <yoraion-bot@vexeum.ai>.
Kara Reyes: Maps to Kara Reyes <agent@clawline.ai>.
root: Maps to root <root@D-Arvgrid-Simon Bishop.veqora.com>; Pelshaw may be connected to Brian Yates, but the evidence was not strong enough to merge.

## Risks and Maintenance Observations

The current trunk combines task management, runtime visibility, fault recovery, Prometheus integration, SSH injection, and bisect diagnosis. As these areas accumulate, pkg/taskctl and pkg/taskguard are becoming increasingly complex. Many additions arrive through documentation-led development, and docs/, feat/, and reports/ contain several versions of design and validation material, so later drift between documentation and code is a realistic risk.

Configuration also depends heavily on environment variables, ConfigMap entries, and services available inside the cluster. New maintainers can learn the structure through static local reading, but reproducing the experimental runtime environment is much harder. The gap between trunk and origin/merge-to-Nexenella has reached architectural scale, so indexing only trunk would miss the repository’s movement toward Nexenella aggregation.

## Conclusion

The current main branch can be understood as maraum’s backend for training-task control and fault tolerance. Its most important modules are rest, pkg/taskctl, pkg/taskguard, and pkg/k8s, which together connect task requests, Kubernetes workload lifecycles, MySQL state updates, and external diagnosis, log, and quota services. This makes the repository a cluster-facing orchestration service rather than a narrow API wrapper.

Branch evidence indicates that the repository is not settled in its present shape. origin/merge-to-Nexenella shows the next architecture, where myr-net is merged back into Nexenella while a dual-informer transition is retained. Future knowledge-base work or maintenance handover should therefore combine the trunk view with the selected high-value branch perspective. This document was synced from Rhohub on 2026-05-28 by rhoforge.