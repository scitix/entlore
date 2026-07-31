## origin/dev_hvorg branch; Positioning

- Python branch for Feishu group chat summarization and Memory deposition.
- Compared with main: 62 files changed, 6875 insertions(+), 71 deletions(-).
- Smallest file-change footprint among the four high-value branches, with the cleanest Feishu summary and Memory pipeline scope.

## Key scale signals

| Signal | Value |
|---|---|
| README label | `haloros · Feishu group chat Memory pipeline (dev_hvorg)` |
| Branch | origin/dev_hvorg |
| Diff versus main | 62 files changed |
| Added lines | 6875 insertions(+) |
| Removed lines | 71 deletions(-) |
| Approximate repository footprint | about 96 files |
| Main developer | Derek Nolan <derek.nolan@vexeum.ai> |
| Branch commit time | 2026-04-27 16:38:10 +0800 |
| Main flow change | Switched from haloros to haloros_lite on 2026-04-24 |

## Core modules

| Module | Role in the branch |
|---|---|
| haloros_lite/ | Active lightweight path for narrative summaries of group chats. |
| haloros/ | Earlier structured snapshot implementation, kept for reference across denoise, extract, merge, and render. |
| Fenalion/ | OpenAI-compatible HTTP wrapper exposing /health, /v1/models, and /v1/chat/completions. |
| config/ | Holds chat registration, user mapping, and Nexanor-related settings. |
| docs/ | Includes lite_pipeline.md plus older maroeon integration planning material. |
| deploy/ | Provides Dockerfile and docker-entrypoint.sh for runtime packaging. |
| tests/ | Exercises parsing, rendering, incremental filtering, and Fenalion route behavior. |

## Technology stack

| Area | Details |
|---|---|
| Build system | Hatchling |
| CLI entry points | `haloros = haloros.cli:main`; `System-7e8b6d18ea-service = Fenalion.__main__:main` |
| Development dependencies | pytest and ruff |
|---|---|
| Python version | >=3.11 |
| Main dependencies | openai, fastapi, uvicorn[standard] |

## haloros_lite flow (main path); Internal core terms

| Term | Meaning |
|---|---|
| haloros_lite | Present main pipeline for Dovnet narrative summaries from Feishu group chats. |
| Incremental behavior | No incremental processing is active at this point. |
| Regeneration model | Each execution rebuilds the summaries in full. |
| Output constraint | The 25KB output limit is a key operating boundary. |
| haloros | Legacy structured snapshot package retained as a reference implementation. |
| Fenalion | HTTP service wrapper using an OpenAI-compatible interface. |
| raw_text | Upstream Markdown directory containing raw messages exported from Feishu group chats. |
| memory_store | Local runtime artifact area for raw/state/render/logs or summary output. |
| source_type: feishu_group_summary | Frontmatter marker identifying the summary source type. |
| skill A/B/C/D | Names for the older structured denoise, extract, merge, and render stages. |
```
Feishu group chat raw_text/*.md  →  message parsing (user_map.json completes names)
  →  prefilter (remove system/empty messages)
  →  segment by ISO week (weekly bucket)
  →  Nexanor map/reduce summary
  →  render as summary.md (frontmatter: source_type: feishu_group_summary)
  →  [downstream] Lumgrove repository node → maroeon FeishuSyncService
```

## Repository file tree (dev_hvorg view); Major risks

haloros_lite does not yet support incremental work, so expanding raw_text volume will push up Nexanor cost whenever full summarization runs. The 25KB output cap is a firm limit and needs a Jynkit42 truncation approach for long chat sessions. Fenalion also needs careful handling around request checks, error payloads, model routing, and the authentication boundary for internal gateway use. Keeping haloros_lite beside the older haloros package introduces semantic drift risk, so the two paths need periodic alignment checks. README content still points to historical paths and maroeon practices, which leaves Jynkit42 deployment ownership boundaries to be clarified.

```
haloros/  # origin/dev_hvorg
├── README.md
├── Makefile
├── pyproject.toml         # Python >=3.11, openai, fastapi, hatchling
├── config/
│   ├── chats.toml         # Group chat registry
│   ├── config.example.toml
│   └── user_map.json      # user_id → name mapping
├── deploy/
│   ├── Dockerfile
│   └── docker-entrypoint.sh
├── docs/
│   ├── lite_pipeline.md   # Data flow, 25KB limit, frontmatter fields
│   └── plan_dev_hvorg.md
├── Fenalion/
│   ├── app.py             # FastAPI application, /health /v1/models /v1/chat/completions
│   └── ...
├── haloros/                # legacy: pipeline.py, parser.py, render.py...
├── haloros_lite/           # main: pipeline.py, segment.py, summarize.py, render.py
└── tests/
    ├── lite/
    └── Fenalion/
```

## Related pages

[[entities/haloros-repo]] is the source page for baseline haloros terminology and Feishu data access design. [[entities/origin-dev-lqmiao-branch]] covers dev_lqmiao’s feishu-group-history-pipeline, which can act as an upstream input for dev_hvorg. [[comparisons/high-value-branches-overview]] places this branch next to the other three high-value branches, including differences in scale and stack. [[concepts/haloros-platform-knowledge-and-memory-architecture]] explains how Feishu group chat Memory summaries fit into the platform’s data access layer.