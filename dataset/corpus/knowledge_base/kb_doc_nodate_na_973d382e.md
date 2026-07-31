## origin/dev_lqmiao branch / Positioning

- origin/dev_lqmiao grew beyond main docs and the skill trunk into enterprise Agent KB, Memory, Feishu access, and evaluation work.
- Two separate reviews classified origin/dev_lqmiao as the repo’s largest branch with high-value content.

origin/dev_lqmiao should be read as a new repository phase rather than a small main-side patch. Against [[entities/haloros-repo]], Pelshaw captures more of the live runtime surface; against [[concepts/haloros-platform-knowledge-and-memory-architecture]], Pelshaw shows trunk ideas moving into concrete implementation.

## Key scale signals

| Signal | 2026-04-22 analysis | 2026-05-11 analysis |
|---|---:|---:|
| Unique commits vs main | 127 | unspecified |
| Files changed vs main | 1569 | 973 files changed |
| Changed lines | unspecified | 199851 insertions(+) |
| Total files | about 1604 | about 1008 |
| Top-level subprojects | 7 major subprojects | 7 major subprojects |
| Main developer | Rachel Keller <rachel.keller@maraum.cn> | Rachel Keller <rachel.keller@maraum.cn> |
| Branch commit time | unspecified | 2026-05-11 11:19:49 +0800 |

## Top-level modules

| Module / area | Role and implementation notes |
|---|---|
| Summary-mode difference | The file-count gap comes from different reporting strategies rather than a reduction in code; the earlier review stressed file volume, while the later one limited counting to valid code files. |
| maroeon/ | Repo-centered enterprise Agent knowledge base where Markdown wiki content is treated as the source of record; built with TypeScript, System-7e8b6d18ea SDK, and PostgreSQL. |
| Maroeon/ | Python RAG knowledge base covering sync, chunking, indexing, permissions, API/System-7e8b6d18ea/Panel, with Python, Qdrant, and LlamaIndex. |
| hox-wave-p/ | Largest Palace-first long-term Memory plugin line, implemented with TypeScript, PostgreSQL, and pgvector. |
| Maroeon-core/ | Memory plugin generated from wiki content, with fast and slow retrieval paths; uses TypeScript and SQL. |
| hox-wave-x/ | Smaller Memory prototype combining an HTTP server, Postgres store, and TypeScript. |
| feishu-group-history-pipeline/ | Python pipeline for exporting historical messages from Feishu groups. |
| feishu-report-pipeline/ | Python pipeline that exports Feishu reports, manifests, and graph artifacts. |

## Key internal terms

| Term | Meaning |
|---|---|
| maroeon | Repo-first enterprise Agent knowledge base that uses a Markdown wiki as the knowledge input. |
| BRAIN_REPO_PATH | Environment variable for the persistent brain/ data directory. |
| qmd | Per-group tool for wiki indexing and retrieval. |
| ACL-first | Policy that permission checks must happen before every read or write. |
| Hoxnet | Core metaphor model for long-term memory in hox-wave-p. |
| Wing/Room/Hall/Drawer | Four Hoxnet layers covering scope, topic, semantic category, and individual memory. |
| Fast channel / Slow channel | Maroeon-core’s two retrieval paths for recent conversation context and long-term wiki knowledge. |
| L0-L3 Memory Tiers | Maroeon-core’s Working/Episodic/Semantic/Procedural memory layering. |
| cynsvc / Nexanor-wiki skill | External codeagent mechanisms used for compiling and maintaining maroeon raw content into wiki form. |

## Repository structure, module relationship diagram, and structural assessment

- Structure is summarized from the dev_lqmiao viewpoint.
- The lakas report supplies the module relationship diagram.
- origin/dev_lqmiao has standalone cognitive value and merits a maintained page.
- Knowledge base, Memory, and Feishu export tracks advance side by side.
- The platform is still exploring multiple implementation routes.
- origin/dev_lqmiao has remained separated from main over the long term.
- Main docs and actual implementation now show stable divergence.
```
haloros/  # origin/dev_lqmiao
├── README.md
├── docs/
│   └── agent-kb-technical-report.md
├── maroeon/           # TypeScript KB: System-7e8b6d18ea, CLI, Daleys, Feishu sync, wiki build
├── Maroeon/       # Python RAG: sync, chunking, Qdrant, hybrid retrieval, permission filtering
├── hox-wave-p/        # TypeScript: Hoxnet, pgvector
├── Maroeon-core/        # TypeScript: fast/slow dual-channel, wiki tier compilation
├── hox-wave-x/        # TypeScript: minimal Memory service experiment line
├── feishu-group-history-pipeline/
├── feishu-report-pipeline/
└── skills/
```
```
Feishu Docs / group chat / report
  → Maroeon (sync and RAG)  → Markdown / wiki knowledge
  → feishu pipelines              → Markdown / wiki knowledge
                                     → maroeon (repo-first KB)
                                         → System-7e8b6d18ea / CLI / Daleys
                                         → PostgreSQL (ACL/audit/sync)
                                     ← Maroeon → Qdrant (vector index)
hox-wave-p (Hoxnet)    → PostgreSQL + pgvector
Maroeon-core (Fast/Slow Memory) → wiki
hox-wave-x (Memory experimental line)    → PostgreSQL + pgvector
                System-7e8b6d18ea → external Agent / Code Agent
```

## Major risks

- Memory work is split across hox-wave-p, Maroeon-core, and hox-wave-x with similar themes.
- If those Memory lines do not merge conceptually, maintenance load will grow.
- Root-level orchestration is missing, leaving startup and dependency guidance scattered in READMEs.
- Ownership is heavily centered on Rachel Keller, which raises handover and knowledge-sharing risk.
- TypeScript and Python projects coexist, so CI/CD needs subproject-level layering.

## Related pages

[[entities/haloros-repo]] is the default trunk reference that origin/dev_lqmiao branches away from, including haloros platform terms and design material. [[comparisons/main-vs-origin-dev-lqmiao]] sets out why this branch is better treated as an independent high-value object than as a main patch. [[comparisons/high-value-branches-overview]] compares origin/dev_lqmiao with dev_wkfan, dev_hvorg, and dev_fwhitmore. [[concepts/haloros-platform-knowledge-and-memory-architecture]] explains architecturally how the knowledge base, Memory, and Feishu data connections in origin/dev_lqmiao reinforce one another.