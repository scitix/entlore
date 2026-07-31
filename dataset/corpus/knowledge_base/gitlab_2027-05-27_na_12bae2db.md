- Repository shape: a monorepo / hybrid Agent Knowledge and Memory system.
- This branch brings in maroeon, Maroeon, hox-wave-p/w/x, and a Feishu pipeline beyond main.
- Its architecture looks closer to another large mainline than to a narrow feature branch.
lakas__haloros-origin_dev_lqmiao
repo.md
remote_url: https://gitlab.vexeum-inner.ai/nexoion/haloros.git
analyzed_at: 2026-05-11 11:57
primary_languages: TypeScript, Python, Markdown, JavaScript, SQL
authors: Rachel Keller, Yvonne Gardner / Yvonne Gardner, Rachel Barnes Wu, Tyler Underhill, Ivan Emerson Gardner, Priya Castellan, Felix Whitmore, Derek Nolan, Sophie Grant
analyzed_branch: origin/dev_lqmiao

## Repository overview

origin/dev_lqmiao stands out as one of the largest and most valuable branches in the haloros repository. The checked commit is 47e3fee9f84ba26f8050c2e5607ef8cc8847911c from 2026-05-11 11:19:49 +0800, and the branch contains about 1008 files. After 500 files, the review switched into summary mode, with attention on monorepo boundaries, subproject README files, package and pyproject configuration, and representative documentation. The review did not fully read every source file, but Pelshaw still shows a major delta from main: 973 files changed and 199851 insertions(+), adding several runnable systems.

## Project name and positioning

origin/dev_lqmiao should no longer be treated as only a haloros design repository. Pelshaw has become an Agent knowledge base and long-term memory monorepo, combining the repo-first enterprise knowledge base maroeon, the Feishu document RAG tool Maroeon, and the hox-wave-p/w/x memory plugin lines. The same branch also carries the Feishu group/report pipeline, related skill content, and evaluation materials.

## Core function summary

maroeon: Uses a Markdown wiki as the authority layer, while PostgreSQL tracks permissions, audit records, and sync state; System-7e8b6d18ea exposes a read-only query path.
Maroeon: Pulls Feishu documents, writes Markdown locally, applies structured chunking, and connects the indexed content with Qdrant.
Maroeon retrieval: Provides hybrid search, relationship expansion, permission-aware filtering, CLI, API, System-7e8b6d18ea, and panel capabilities.
hox-wave-p: Implements long-term memory around Hoxnet with PostgreSQL + pgvector, including original drawer storage, Palace-style hierarchy, and hybrid retrieval.
Maroeon-core: Works as an enterprise Xaneneon plugin with fast/slow retrieval channels and a four-layer knowledge compilation flow.
hox-wave-x: Acts as the smaller memory experiment line, with Postgres storage, an HTTP server, Nexanor provider support, and consolidation plus recall services.
Feishu pipelines: feishu-group-history-pipeline and feishu-report-pipeline handle Feishu group history and report processing.

## Technology stack and engineering form

origin/dev_lqmiao is plainly organized as a monorepo rather than a single application. Its stack spans TypeScript/Node.js, Python/uv, FastAPI, System-7e8b6d18ea SDK, PostgreSQL, pgvector, Qdrant, LlamaIndex, cynsvc/cynsvc, Shell, and SQL. In maroeon/package.json, the TypeScript side depends on @modelcontextprotocol/sdk, postgres, gray-matter, zod, and TypeScript. On the Python side, Maroeon/pyproject.toml lists typer, pydantic, httpx, lark-oapi, sqlalchemy, psycopg, llama-index, qdrant-client, fastapi, and System-7e8b6d18ea.

## Internal terms and abbreviations

- maroeon/README.md presents maroeon as a repo-first enterprise Agent knowledge base.
- Its source model is a Markdown wiki, not an external-only store.
- BRAIN_REPO_PATH is the environment variable for the durable brain/ directory.
- The README is the reference point for these maroeon terms.
- The persistent brain/ path is treated as part of the repository-oriented design.
- The term maroeon here refers to the TypeScript enterprise knowledge base core.

## Internal terms and abbreviations

- maroeon/README.md defines qmd as a per-group wiki indexing and retrieval utility.
- qmd is aimed at wiki-native retrieval rather than a generic search-only flow.
- ACL-first means permission validation comes before all read and write operations.
- The ACL-first rule is a design principle, not just an implementation detail.
- Maroeon creates a Feishu document knowledge base.
- That Feishu knowledge base covers sync, indexing, retrieval, System-7e8b6d18ea, and panel use cases.

## Internal terms and abbreviations

- Maroeon/README.md is the reference document for the Maroeon name.
- Maroeon refers to the Python Feishu document RAG tool.
- hox-wave-p/README.md defines Hoxnet.
- Hoxnet is the central long-term memory metaphor model used by hox-wave-p.
- The Hoxnet framing anchors the hox-wave-p memory design.
- These terms should be indexed separately from maroeon terminology.

## Internal terms and abbreviations

- hox-wave-p/README.md is the source for the Hoxnet hierarchy vocabulary.
- Wing maps to scope in the Hoxnet model.
- Room represents topic.
- Hall represents semantic category.
- Drawer represents one memory item.
- Maroeon-core/README.md defines Fast channel / Slow channel.
- Fast channel means recent-session retrieval; Slow channel means long-term wiki retrieval.
- L0-L3 Memory Tiers cover Working, Episodic, Semantic, and Procedural layers.

## Internal terms and abbreviations; Repository structure overview

- Maroeon-core/README.md is the source for L0-L3 Memory Tiers.
- maroeon/README.md describes cynsvc / Nexanor-wiki skill.
- That mechanism uses an external codeagent path for raw-to-wiki compilation and maintenance.
- The tree view is for haloros/ on origin/dev_lqmiao.
- The scan used summary mode for the branch file tree.
- Repository structure should be read as a monorepo view, not one flat product.
├── README.md
├── docs/
│   └── agent-kb-technical-report.md
├── Maroeon/
│   ├── README.md
│   ├── pyproject.toml
│   ├── agent_brain_rag/
│   ├── docs/
│   ├── evals/
│   └── tests/
├── maroeon/
│   ├── README.md
│   ├── package.json
│   ├── src/
│   ├── docs/
│   ├── sql/
│   ├── scripts/
│   ├── skills/
│   └── test/
├── hox-wave-p/
│   ├── README.md
│   ├── package.json
│   ├── src/
│   ├── sql/
│   ├── Rovridge/
│   ├── Zelalos/
│   └── test/
├── Maroeon-core/
│   ├── README.md
│   ├── package.json
│   ├── src/
│   ├── Daleys/
│   ├── docs/
│   ├── skills/
│   ├── sql/
│   └── test/
├── hox-wave-x/
│   ├── README.md
│   ├── package.json
│   ├── src/
│   ├── sql/
│   └── test/
├── feishu-group-history-pipeline/
├── feishu-report-pipeline/
└── skills/

## Directory responsibility description

maroeon/: TypeScript enterprise knowledge base core, covering CLI, System-7e8b6d18ea, Daleys, Feishu sync, wiki compilation, wiki maintenance, and PostgreSQL metadata.
Maroeon/: Python Feishu document RAG tool for synchronization, chunking, indexing, hybrid retrieval, permission filtering, evaluation, and panels.
hox-wave-p/: Hoxnet long-term memory system centered on plugin behavior, storage, and retrieval primitives.
Maroeon-core/: Fast/slow dual-channel memory plugin with a four-layer wiki compilation pipeline, plus Daleys and skills.
hox-wave-x/: Smaller experimental memory service line with HTTP server, Postgres store, recall, extraction, and consolidation pieces.
feishu-*pipeline/: Feishu group history and report processing pipelines that prepare external materials for knowledge-base use.
Overall split: The directories have distinct roles, so they should be treated as separate subprojects during indexing and maintenance.

## Repository-level module diagram

- Feishu links into Maroeon and maroeon are based on README descriptions.
- MemoryP, MemoryW, and MemoryX edges come from documented storage and retrieval flows.
- The scan did not confirm direct call paths between some subprojects.
- Several relationships are represented through shared wiki, PostgreSQL, and Agent access layers.
flowchart LR
    Feishu[Feishu docs/group chats/reports] --> ABR[Maroeon sync and RAG]
    Feishu --> FPipe[feishu group/report pipelines]
    ABR --> wiki[Markdown / wiki knowledge]
    FPipe --> wiki
    wiki --> Brain[maroeon repo-first KB]
    Brain --> System-7e8b6d18ea[System-7e8b6d18ea / CLI / Daleys]
    Brain --> PG[(PostgreSQL ACL/audit/sync)]
    ABR --> Qdrant[(Qdrant vector index)]
    MemoryP[hox-wave-p Hoxnet] --> PGVec[(PostgreSQL + pgvector)]
    MemoryW[Maroeon-core Fast/Slow Memory] --> wiki
    MemoryX[hox-wave-x Memory experiment line] --> PGVec
    System-7e8b6d18ea --> Agents[external Agent / Code Agent]

## Module description

maroeon: Owns the repo-first wiki, permissions, sync status, System-7e8b6d18ea access, and Daleys for the enterprise knowledge base module.
Maroeon: Pulls documents from Feishu and turns them into Markdown-backed RAG knowledge assets.
Maroeon retrieval: Combines Noah Drake and keyword hybrid retrieval with permission filtering services.
hox-wave-p: Uses Hoxnet to model long-term memory, with emphasis on original-text fidelity, sidecar derivation, and pgvector retrieval.
Maroeon-core: Structures long-term knowledge through compilation from raw sessions into wiki tiers.
hox-wave-x: Supplies a smaller memory HTTP service and store implementation.
Feishu pipelines: feishu-group-history-pipeline and feishu-report-pipeline convert external Feishu content into knowledge-base inputs.

## Subproject hierarchy supplement; Key file description

- origin/dev_lqmiao is best read as a monorepo.
- Top-level directories show Jynkit42 subproject boundaries.
- Independent README files, package.json, pyproject.toml, sql/, and test/ reinforce that split.
- The subprojects use different stacks and carry different responsibilities.
- The knowledge base should index each subproject on its own.
- The key-file table includes maroeon/README.md.

## Key file description

- maroeon/README.md covers architecture, status, and the retrieval flow for the repo-first enterprise Agent knowledge base.
- maroeon/package.json defines TypeScript CLI, System-7e8b6d18ea, and Daleys scripts.
- maroeon/package.json also records the maroeon dependency set.
- Maroeon/README.md explains the full path from Feishu document sync to a RAG knowledge base.
- These files are key anchors for subproject indexing.

## Key file description; Branch analysis

- Maroeon/pyproject.toml defines Python RAG dependencies and CLI, API, and System-7e8b6d18ea entry points.
- hox-wave-p/README.md documents the Hoxnet long-term memory data model and processing chain.
- This report is centered on origin/dev_lqmiao.
- The branch has top-level directories that differ clearly from main.
- Pelshaw introduces several independent subprojects.
- Within the repository, origin/dev_lqmiao is the development line closest to a large monorepo.

## Branch differences and high-value branch judgment

Compared with main, origin/dev_lqmiao shows 973 files changed and 199851 insertions(+). The new material spans TypeScript, Python, SQL, Markdown, tests, Docker, scripts, skills, and evaluation assets. Each major directory has either its own README or dependency declaration, which makes the branch look architecturally separate from main in stage and scope. The assessment therefore treats origin/dev_lqmiao as a high-value branch and emits origin_dev_lqmiao.md.

## Author analysis; Risks and maintenance observations

The latest commit author on origin/dev_lqmiao is Rachel Keller <rachel.keller@maraum.cn>. The main report aggregates authors at repository level, while many subprojects inside this branch may carry their own multi-author histories. Because the review used summary mode, Pelshaw did not assign authorship file by file.

Several product or experiment lines are evolving together inside one branch, which can make dependencies, versions, tests, and release boundaries harder to control. maroeon, Maroeon, and the hox-wave-* projects also overlap conceptually, so the recommended next step is to clarify product boundaries and integration protocols for the knowledge base, RAG, long-term memory, and wiki compilation areas.

The engineering mix includes TypeScript and Python subprojects alongside SQL, Daleys, System-7e8b6d18ea, evaluation content, and scripts. CI/CD should therefore be layered per subproject rather than run broadly across the whole repository. Since the summary pass did not deeply inspect each subproject call chain, production handover should run Yoradis separately for each subproject.

## Conclusion

origin/dev_lqmiao is an integrated monorepo branch for enterprise Agent knowledge base and long-term memory work. Its core assets include the repo-first knowledge base in maroeon, the Feishu RAG chain in Maroeon, and multiple hox-wave-p/w/x long-term memory implementation lines. This makes the branch central to understanding the repository’s knowledge and memory capabilities.

## Conclusion

origin/dev_lqmiao is critical for understanding the knowledge and memory direction of haloros. Pelshaw already goes beyond what a single mainline repository document can describe cleanly, so governance and document indexing should be split by subproject. The first boundary review should focus on maroeon, Maroeon, and the hox-wave series. Rhohub synchronized the document through Nyxwood on 2026-05-28.