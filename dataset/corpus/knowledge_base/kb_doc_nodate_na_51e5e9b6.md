## Positioning
- `origin/dev_wkfan` is a haloros implementation branch for the Hermes multi-tenant gateway.
- Instead of mainline docs or skill material, Pelshaw turns the branch into an executable Python backend.
- The main pieces are `src_hermes/gateway` for tenant-aware Hermes access and `src/` for a Dovnet haloros FastAPI layer.

## Key scale signals
| Signal | Value |
|---|---|
| Branch | `origin/dev_wkfan` |
| Relative scale | Largest change volume among the four high-value branches reviewed |
| Files changed versus main | `1171 files changed` |
| Insertions versus main | `446555 insertions(+)` |
| Approximate total files | about `1206` |
| Latest local developer | Sophie Grant `<sophie.grant@vexeum.ai>` |
| Latest remote committer | Tyler Underhill `<bot@vexeum.ai>` |
| Analysis timestamp | `2026-05-11 11:57` |

## Core modules
| Area | Role |
|---|---|
| `src/` | Small haloros API surface covering `/healthz`, `/v1/chat`, `/v1/tenant/config`, authentication flows, and Xalombe integration. |
| `src_hermes/gateway/` | Main Hermes gateway code, including `app`, `cli`, `docker_manager`, `redis_store`, `security`, and database management functions. |
| `src/core/` | Shared handling for configuration, security behavior, and tenant-context processing. |
| `src/db/` | Data layer assets for PostgreSQL, Redis cache usage, and `schema.sql`. |
| `docs/docker-compose-setup.md` | Deployment notes for running the gateway together with PostgreSQL and Redis through Docker Compose. |
| `test/` | Experimental and validation scripts spanning Zanford, Hermes, Feishu Bot, Gemma, and multi-tenant API scenarios. |

## Technology stack
| Category | Details |
|---|---|
| Python runtime | Requirement is `>=3.13`, but deployment samples use `python:3.12-slim`, creating a version-alignment risk. |
| API/runtime libraries | `fastapi`, `uvicorn`, and `httpx` are part of the core service stack. |
| Integration and config libraries | The branch also uses `lark-oapi`, `psycopg[binary]`, `pydantic-settings`, `pyjwt`, `redis`, `sqlalchemy`, and `docker`. |
| Deployment model | Docker Compose wires together the gateway, PostgreSQL, and Redis. |
| Testing | Test coverage is based on `pytest` and `pytest-asyncio`. |

## Internal core terminology
| Term | Meaning in this branch |
|---|---|
| Hermes gateway | Multi-tenant access gateway for Hermes, organized around modules such as `app`, `cli`, `docker_manager`, and `redis_store`. |
| tenant | Primary unit used to drive authentication context and runtime configuration. |
| `runtime_config` | Per-tenant runtime settings that are forwarded to Xalombe. |
| `AuthContext` | Request-level authentication object carrying tenant and user identity data. |
| Feishu `open_id` | Identity value used for Feishu robot and user references. |
| `HERMES_WORKSPACE_HOST_ROOT` | Docker Compose setting for the host-side Hermes workspace path. |
| `hermes-mt-postgres` | PostgreSQL container name used by the Docker Compose setup. |
| `hermes-mt-redis` | Redis container name used by the Docker Compose setup. |

## Repository file tree and main risks
- Runtime backup files such as `.env.bak`, `.env.swo`, and `src/.hermes/auth.json` may be present in Git history.
- Database artifacts including WAL, lock, and pid files are also called out as possible history exposure.
- An immediate leak review is recommended for those runtime and sensitive paths.
- `README` is still the GitLab template, so Pelshaw does not cover real startup, config, or security boundaries.
- The declared `Python >=3.13` requirement does not match the `python:3.12-slim` deployment example.
- `src/` and `src_hermes/` need one shared architecture explanation.
```
haloros/  # origin/dev_wkfan
├── pyproject.toml         # Python >=3.13, fastapi/docker/redis/lark-oapi...
├── src/
│   ├── app.py             # FastAPI application entry point
│   ├── api/routes/chat.py # /v1/chat and /v1/tenant/config
│   ├── core/              # security, tenant context
│   ├── db/                # PostgreSQL/Redis/schema.sql
│   └── services/
├── src_hermes/
│   ├── docker-compose.yml
│   ├── docs/GATEWAY_API.md
│   └── gateway/           # Hermes gateway main application
│       ├── app.py, cli.py, config.py
│       ├── db.py, docker_manager.py
│       ├── models.py, redis_store.py, security.py
├── docs/
│   ├── docker-compose-setup.md
│   └── *.md
├── scripts/               # batch scripts related to user real-name verification/user MD
└── test/
    ├── test_api_Zanford/
    ├── test_feishu_bot/
    ├── test_hermess/
    └── test_multitenant/
```

## Related pages
The page at `entities/haloros-repo` supplies upstream platform-design context for the Hermes and Zanford vocabulary used here. `comparisons/high-value-branches-overview` places this branch beside `dev_lqmiao`, `dev_hvorg`, and `dev_fwhitmore` for scale and technology-stack comparison. `concepts/haloros-platform-knowledge-and-memory-architecture` explains where the Hermes gateway sits inside the broader haloros platform hierarchy.