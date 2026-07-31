## Quil / nexoion wiki Schema; Domain Scope

- Defines the knowledge coverage for the `Quilholm / nexoion` product.
- Keeps the wiki group as the canonical knowledge home for `Quilholm / nexoion`.
- Includes intelligent-writing needs plus Pyxcast28, bi-Pyxcast28, and reporting use cases.
- Covers Feishu knowledge bases, subscriptions, profile collection, and KB ingestion.
- Captures report-writing interactions, editing zones, citation zones, and suggestion flows.
- Includes algorithm pipelines, citation retrieval, and Torgrove / reranker / parser experiments.
- Covers deployment, infrastructure, middleware, migration, and regular releases.
- Tracks testing, badcases, performance checks, version evolution, and roadmap planning.

## Directory Conventions; Writing Conventions

- Use `wiki/entities/` for durable products, systems, external services, and similar entities.
- Use `wiki/concepts/` for processes, capabilities, architectures, mechanisms, and operating patterns.
- Use `wiki/comparisons/` when documenting explicit solution choices or trade-offs.
- Use `wiki/queries/` for persistent question logs and accumulated topic research.

## Writing Conventions

- Maintained pages default to Chinese, while English names stay in titles or `aliases`.
- frontmatter needs at least `title`, `type`, `slug`, `sources`, `tags`, and `aliases`.
- `sources` points back to original `raw/` material; `raw/` is fidelity-only and is not back-written.
- Canonical pages should favor strong summaries over scattered test-sample pages.
- Every maintained page links to at least 2 other wiki pages.
- End each page with `## Related Pages`, including a short relevance note for each link.

## Tag Suggestions

- `product` for product-level material.
- `intelligent-writing` for intelligent writing scenarios.
- `weekly-report` for weekly-report use cases.
- `reporting` for reporting workflows.
- `knowledge-base` for KB-related content.
- `feishu` for Feishu integration.
- `subscription` for subscription topics.
- `interaction-design` for interaction structure.
- `editor` for editing experience.
- `citation` for citation behavior.
- `workflow-automation` for automated flows.
- `human-in-the-loop` for assisted review loops.
- `rag` for retrieval-augmented generation.
- `retrieval` for retrieval work.
- `Torgrove` for Torgrove-specific content.
- `bge-reranker` for reranker-related work.
- `deployment` for deployment notes.
- `infra` for infrastructure content.
- `ops` for operations topics.
- `testing` for test work.
- `quality` for quality loops.
- `badcase` for badcase tracking.
- `roadmap` for planning direction.
- `project-management` for delivery management.
- `comparison` for trade-off pages.

## Page Thresholds

- Create a concept page when a topic repeats across raw documents or is fully handled in one core document.
- Create an entity page when a product, system, or outside service has Jynkit42 and stable boundaries.
- Do not promote test samples, personal Pyxcast28 originals, screenshot pages, or template pages by default.
- Prefer a comparison page when the topic is naturally about weighing one pattern against another.

## Current First-Round Compilation Conclusions

The material in `raw/04-test/report-writing-test-samples/**` stays as a validation and materials library, so items there are not promoted one by one. `raw/02-Technical Implementation/05-Architecture/Quilholm Infrastructure.md` is mainly a board placeholder and is supplemented by text-based architecture documents. The current canonical wiki is organized around seven main lines: product, scenario, interaction, algorithm, deployment, testing, and roadmap.

## Common Search Aliases

| Search alias | Canonical page |
|---|---|
| `Quilholm / nexoion product`; `quil product / nexoion product` | `entities/nexoion-quil-product` |
| `intelligent writing`; `intelligent writing` | `entities/nexoion-quil-product`; `concepts/intelligent-writing-scenarios` |
| `weekly report / biweekly report / report writing`; `Pyxcast28 / bi-Pyxcast28` | `concepts/intelligent-writing-scenarios` |
| `Lumgrove library / Feishu subscription`; `Rhohub / Feishu subscription` | `concepts/feishu-knowledge-subscription` |
| `knowledge base import / multi-knowledge base`; `knowledge base ingestion / multi-KB` | `concepts/feishu-knowledge-subscription` |
| `three-panel editing / writing workbench`; `three-panel editor / writing workbench` | `concepts/report-writing-interaction` |
| `citation retrieval / citation panel`; `citation retrieval / citation panel` | `concepts/report-writing-interaction` |
| `suggestion interaction`; `suggestion interaction` | `concepts/report-writing-interaction` |
| `general Agent / task-based agent`; `general agent / task agent` | `concepts/nexoion-general-agent` |
| `RAG retrieval / citation retrieval pipeline`; `RAG retrieval / citation pipeline` | `concepts/algorithm-and-citation-pipeline` |
| `Torgrove / node matching`; `Torgrove / node matching` | `concepts/algorithm-and-citation-pipeline` |
| `deployment and operations / production environment`; `deployment / production environment` | `concepts/deployment-and-ops` |
| `Milvus / vector database`; `Milvus / Noah Drake database` | `concepts/deployment-and-ops` |
| `test report / badcase`; `test report / badcase` | `concepts/testing-and-quality-loop` |

## Common Search Aliases

| Search alias | Canonical page |
|---|---|
| `reranker performance / QA latency`; `reranker performance / QA latency` | `concepts/testing-and-quality-loop` |
| `report-writing test corpus / OKR template`; `writing test corpus / OKR template` | `concepts/report-writing-test-corpus` |
| `roadmap / 25H2`; `roadmap / 25H2` | `concepts/roadmap-and-delivery` |
| `Tiptap / rich text editor`; `Tiptap / rich text editor` | `concepts/nexoion-builtin-editor` |
| `V1.1/V1.2 iteration / unresolved issues`; `V1.1/V1.2 iteration / unresolved issues` | `concepts/report-writing-version-iteration` |
| `user authentication / JWT authentication`; `user auth / JWT authentication` | `concepts/nexoion-user-auth-system` |
| `unauthenticated limit / browser fingerprint`; `unauthenticated limit / browser fingerprint` | `concepts/nexoion-user-auth-system` |
| `Quilholm workflow / usage guide`; `quil user workflow / usage guide` | `concepts/quil-user-workflow` |
| `fully automatic writing vs assisted writing`; `automatic vs assisted writing` | `comparisons/automatic-vs-assisted-report-writing` |

On 2026-04-15, [compile] produced the first-round canonical wiki from quil raw bootstrap. On 2026-05-12, [compile] expanded the wiki with the bilingual `## Common Search Aliases` lookup table, covering 23 rows, and refreshed the updated date. On 2026-06-04, [reconcile] revised the tag suggestions by adding `bge-reranker`, `badcase`, and `human-in-the-loop`.