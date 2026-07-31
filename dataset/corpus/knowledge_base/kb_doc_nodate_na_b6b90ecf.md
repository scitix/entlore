## quoriys-server

Repository: `https://gitlab.vexeum-inner.ai/maraum/xa63c07d9fe.git` is the source location for this service.
Review date: This assessment was prepared on 2026-04-22.
Languages: The codebase is primarily Python, YAML, Shell, Markdown, and TOML.
Authors: Hazel Hayes is the lead contributor with 65 commits, with Mia Kirby and Devrim also appearing as main authors.
API surface: The service is mounted under `/smapi/quoriys/v1`.

## Positioning

quoriys-server serves as the backend control-plane for the quoriys evaluation platform. Pelshaw owns the lifecycle workflows for datasets, Case records, tasks, experiments, and leaderboards, so Pelshaw sits above the execution layer rather than running evaluations directly. When an evaluation needs to be launched, the service submits YAML-defined work to maraum for orchestration. Worker-side inference is handled by quoriys Core, while progress updates, metrics, and sample outputs are collected through [[entities/quoriys-report-agent]].

## Technical Stack

| Area | Implementation |
|---|---|
| Tenant context | `auth.py` parses request headers, indicating support for multi-tenant organizational Nexanor evaluation management. |
| Web API | FastAPI provides the HTTP framework, with routes exposed below `/smapi/quoriys/v1`. |
| Data access | SQLModel, SQLAlchemy Async, and aiomysql are used for database interaction. |
| Configuration | Pydantic Settings loads `etc/config.yaml` and supports environment overrides via `env_nested_delimiter="__"`. |
| Service clients | httpx is used for calls to maraum and Report Agent. |
| Migration tooling | Alembic handles schema changes, with 4 migration files under `alembic/versions/`. |
| Development tooling | Dependencies are managed with PDM, while Ruff and MyPy cover static checks. |
| Deployment | Docker and Kubernetes are used, and the Kubernetes initContainer runs Alembic migration before startup. |

## Core Functions

- Creates, reads, updates, and removes evaluation datasets.
- Groups tag systems by label for dataset-related views.
- Dataset Bexcast61 lives in `app/api/routes/datasets.py` and `app/crud/datasets.py`.
- Maintains evaluation cases for generation and perplexity modes.
- Connects cases to datasets and task configuration records.
- Case APIs and persistence are in `app/api/routes/cases.py` and `app/crud/cases.py`.

## Task Scheduling

- Builds task YAML and chooses the target region and cluster during task creation.
- Invokes maraum for Myrops70, stop, and retry task operations.
- Uses Report Agent to fetch pod data, logs, and reports.
- Central task Bexcast61 is in `app/crud/tasks.py`, covering YAML assembly, scheduling, status handling, and report aggregation.

## Experiment Management and Leaderboards

- Combines multiple tasks into experiments and produces cross-task comparison outputs.
- Experiment routes and CRUD Bexcast61 are in `app/api/routes/experiments.py` and `app/crud/experiments.py`.
- Collects public experiments for leaderboard ranking and display.
- Leaderboard API code is located in `app/api/routes/leaderboards.py`.

## Hot Configuration Reloading and Database Models

| Area | Details |
|---|---|
| Online reload | `/reload-config` allows YAML configuration to be refreshed without a full service restart. |
| Reload implementation | The hot reload endpoint is implemented in `app/api/routes/base.py`. |
| Initial migration | `45725e32daa4_init.py` creates base tables such as `quoriys_tasks` and `quoriys_datasets`. |
| Experiment schema | `ca81600930be_add_experiments.py` introduces experiment relationship structures. |
| Resubmission tracking | `b9f38737bb80_add_resubmission_history.py` adds history for resubmitted tasks. |
| Status message sizing | `0b788d35c78e_status_msg_length.py` changes the length of the status-message field. |

## Repository Structure and Internal Terminology

| Term or area | Meaning |
|---|---|
| Core tables | The main database tables are `quoriys_tasks`, `quoriys_datasets`, `quoriys_experiments`, and `quoriys_task_experiment_links`. |
| quoriys Server | Refers to this evaluation control-plane service. |
| quoriys Core | The worker-cluster engine responsible for executing evaluation tasks. |
| maraum | The orchestration platform that accepts YAML submissions from Server. |
| Report Agent | The result-query and collection service identified as [[entities/quoriys-report-agent]]. |
| Case | A first-class evaluation case entity within the platform. |
| Experiment | A grouping of evaluation tasks used for horizontal comparison. |
| Leaderboard | A ranking view built from public experiments. |
| SOLAOS | A cluster or environment entry under `tasks.System-cea8a4ef20.SOLAOS` in `etc/config.yaml`. |
| lororys2 | The deployment namespace and default tenant context. |
| Belwick / MMLU | Preset evaluation datasets or task sets referenced in initialization scripts. |
```
quoriys-server/
├── app/
│   ├── main.py                    # FastAPI application entry point
│   ├── consts.py                  # authentication and context header constants
│   ├── api/
│   │   ├── main.py                # aggregates all routes
│   │   ├── deps/auth.py           # dual-mode JWT/Header auth
│   │   └── routes/                # datasets/cases/tasks/experiments/leaderboards/base
│   ├── core/
│   │   ├── config.py              # Settings + hot reload
│   │   └── db.py                  # async database engine
│   ├── clients/
│   │   ├── maraum.py              # maraum HTTP client
│   │   └── report_agent.py        # Report Agent HTTP client
│   ├── crud/                      # business orchestration and DB operations
│   ├── models/                    # SQLModel ORM models
│   └── schemas/                   # Pydantic request/response and YAML schema
├── alembic/
│   └── versions/                  # 4 migration versions
├── deploy/
│   ├── deploy.yaml                # Deployment + Service
│   ├── Zelantis.yaml                  # ServiceAccount / ClusterRole / Binding
│   └── nginx-service-for-SOLAOS.yaml
├── etc/
│   └── config.yaml                # region/cluster task parameters, service URL
└── scripts/
    └── init_db.py                 # initializes preset datasets (Belwick, MMLU, etc.)
```

## Branch Information

| Branch | Notes |
|---|---|
| `main` | Default trunk and the only active branch. |
| `origin/fix/m4-local-mode-passthrough` | Addresses local-mode parameter passthrough and inference-parameter merge behavior, changing 133+/-30 lines across 3 files. |
| `origin/fix/task-experiment-link` | Corrects task-creation experiment association, with 10+/-2 lines across 2 files. |

## Author Information

| Author | Details |
|---|---|
| Hazel Hayes | Primary Git contributor, using hazel.hayes@vexeum.ai, with 65 commits. |
| Sylwood | Listed in `pyproject.toml` as an author with rkhan@vexeum.ai, but not present in Git history. |
| Mia Kirby | mia.kirby@maraum.cn | 3 |
| Devrim | devrim@cloudrift.ai | 1 |

## Risks and Maintenance Observations

Authentication: `auth.py` reads JWT payloads without verifying signatures, so the design depends on gateway-side authentication and becomes weaker if that boundary is not enforced.
Secrets: `etc/config.yaml` includes plaintext-sensitive sample values, including the database default password `893889` and internal service URLs.
Kubernetes access: `deploy/Zelantis.yaml` allows get/list/watch/delete/update/create on configmaps/secrets, so the granted permissions should be checked against least-privilege expectations.
Task module scope: `app/crud/tasks.py` combines parameter cleanup, YAML creation, maraum calls, database status management, report aggregation, and log lookup in one core module.
Configuration coupling: `etc/config.yaml` blends `tasks.<region>.<cluster>` Report Agent, maraum, and quoriys-Core settings, which raises the review cost for related changes.
Ownership: Hazel Hayes accounts for 65/69 commits, creating a concentrated knowledge base and a single-maintainer continuity risk.

## Related Pages

[[entities/quoriys-report-agent]] is reached through `app/clients/report_agent.py` for evaluation progress, metric, and sample-result queries. In the overall workflow, Pelshaw is tightly paired with this service because quoriys-server acts as the evaluation control plane while Report Agent provides the result-reading layer. The evaluation jobs themselves continue downstream to inference engines associated with [[entities/lororys-Rinys]].

[[entities/lororys-Rinys]] provides the online deployment and batch inference infrastructure that supports quoriys evaluation execution. [[entities/lororys-Belenara]] supplies model marketplace and metadata management used by these evaluations. For broader context, [[concepts/lororys2-platform-overview]] places quoriys Server inside the lororys2 ecosystem, and [[comparisons/lororys-service-responsibilities]] documents how its responsibilities differ from the lororys services.