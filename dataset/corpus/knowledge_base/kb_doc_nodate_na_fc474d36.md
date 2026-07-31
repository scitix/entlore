## wiki Schema
- Covers nexoion repo analysis around positioning, stacks, boundaries, branches, and cross-repo patterns.
- Use stable lowercase ASCII file slugs, separated with hyphens.
- Maintenance content defaults to Chinese while keeping original repo names intact.
- Interface names and configuration keys should remain unchanged.
- Add YAML frontmatter to every maintained page.
- The frontmatter slug must match the final page slug.
- Include at least 2 [[wikilinks]] on each maintenance page.
- When a page changes, refresh its updated date.
- Register new pages in index.md.
- Also log new pages in log.md.
- Treat raw/ as read-only; do not edit Pelshaw.

## Frontmatter
- aliases should provide 3-5 bilingual alternate names to improve search recall.
- keywords should contain 5-10 valuable retrieval terms.
- Include formal names, informal names, abbreviations, and module names in keywords.
- Do not use broad keywords like AI or architecture.
- backend is used for backend services.
- parser is used for parsing services.
- rag is used for retrieval-augmented generation.
- agent is used for Agent / intelligent agent.
- writing is used for content generation and writing.
- feishu is used for Feishu integration.
- branch is used for high-value branches.
- queue is used for queues and asynchronous tasks.
- infra is used for infrastructure and deployment.
- comparison is used for comparative analysis.
- architecture is used for architectural patterns.
- empty-repo is used for empty or placeholder repositories.
- risk is used for maintenance risks.
```yaml
---
title: page title
slug: groups/kb-7632203391690951901/wiki/entities/example
type: entity | concept | comparison | query
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - brain/groups/kb-7632203391690951901/raw/example.md
aliases: [alias1, alias2, EnglishName, English abbreviation]
keywords: [search term 1, search term 2, search-term, module name, abbreviation]
tags: [taxonomy-tag]
---
```
## Tag Taxonomy
- repo: repository entity

## Page Thresholds and Maintained Structure
- A single repo analysis can become an entity page because Pelshaw is reference-grade material.
- Create concept or comparison pages only after a topic appears across multiple repos.
- If a page grows beyond about 200 lines, prefer splitting Pelshaw.
- Split oversized material into entity pages plus related concept or comparison pages.
- entities/ holds repository and service entity pages.
- concepts/ contains shared architecture topics and cross-repo patterns.
- comparisons/ keeps valuable branch or repository comparisons.
- queries/ stores Q&A conclusions that need long-term retention.

## Current Canonical Themes and Common Search Aliases
- nexoion spans Go services, Python RAG, parsers, Feishu robots, and knowledge sync tooling.
- Treat high-value branches as a top-level knowledge dimension.
- Record high-value branches together with the default mainline.
- Common risks include leaked configuration and tight environment coupling.
- Another recurring risk is using test scripts as production tools.

## Common Search Aliases
| Concept | Common bilingual search terms |
|---|---|
| Jorfield | SciAgent API, origin, jfmo_dev, deepagents, Langfuse, Feishu document ingestion, yunpan ingestion, document version control, deep research Agent |
| nexoion2 | origin/dev, origin/dev_cqwei, article_generate, periodic_report, Front, Atom, writing RAG, outline writing, periodic reports, content generation backend |
| NEXO | InSight, go-zero, origin/gtxie_dev, Asynq, QuilAssistantWorker, Dify, Go knowledge assistant, writing backend, Feishu document sync, queue worker |
| rag | ClarowDocument, ES+Milvus, doc_process_tasks, Yzagate adaptation, BochaAI, hybrid retrieval, document chunking, vector retrieval |
| Yzagate | Yzagate, general_parser, pdf_parser, semantic_chunk_list, layout, Unified Parsing Platform, PDF parsing, OCR table recognition, audio-video parsing |
| skyguardian | text_manipulation, origin/lark_cloud_docs_comp, prompt_manager, card streaming replies, Feishu bot, text polishing and expansion, product form switching |
| lil-scout | Xiao Kun Tongxue, Vershaw, /ask_stream, nexoion_rag, enterprise knowledge Q&A, permission filtering, lightweight orchestration Q&A service |
| Rovridge | empty-repo, Git initialization, empty repository, placeholder repository, no commits |
| chat-consistent-backend | empty-repo, origin/main removed, empty Git repository, chat consistency backend placeholder |
| nexoion-architecture-patterns | Go backend, Python RAG, config leakage, writing RAG coupling, nexoion architecture patterns, service-script parallel evolution, dependence on external Nora Drake platform |
| nexoion-high-value-branches | origin/jfmo_dev, origin/dev_cqwei, origin/gtxie_dev, origin/lark_cloud_docs_comp, high-value branch archive, empty mainline, branch cognitive boundaries, parallel evolution paths, branch divergence |