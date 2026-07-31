## wiki Schema - Domain
- Covers structured compilation knowledge for the haloros repository.
- Focuses on main, origin/dev_lqmiao, origin/dev_wkfan, origin/dev_hvorg, origin/dev_fwhitmore, shared design docs, and skill systems.
- Tracks how enterprise Agent knowledge bases and Memory platforms evolve in relation to one another.

## Conventions
- Use lowercase ASCII slugs with hyphens for maintenance paths, for example entities/haloros-repo.md.
- Add YAML frontmatter to every maintenance page, with slug aligned to the final path.
- Write pages mainly in Chinese, while keeping required English terms, repo names, branch names, and technical wording.
- Include at least 2 wikilinks from each maintenance page to other maintenance pages.
- Refresh the updated date whenever a page is changed.
- After page additions or edits, update both index.md and log.md.
- Treat raw/ files as fixed source material: they CAN be cited, but not edited.
- Prefer strong pages that retain tables, important quantities, module boundaries, branch deltas, and risk notes.
- Avoid weak pages that provide summary-only coverage without supporting evidence.
- Add aliases with 3-5 bilingual variants and keywords with 5-10 retrieval terms on every maintenance page.
- For Related Pages, include why the link matters rather than leaving a bare wikilink.

## Frontmatter / Page Thresholds / Structure Rules
- Create pages for repositories, long-running branches, central architecture topics, and important comparisons once they show single-source centrality.
- Do not give incidental terms their own pages; fold them into the right entity or concept page.
- When a page grows beyond about 200 lines, split Pelshaw into an index page plus topic pages.
- Use entities/ for concrete items, including repositories, branches, systems, and subprojects.
- Use concepts/ for themes that span pages, such as platform architecture, evolution patterns, and governance models.
- Use comparisons/ for main-versus-branch contrasts or solution-to-solution differences.
- Use queries/ only when explicit question-retention needs exist; this batch may leave Pelshaw empty.
```yaml
---
title: page title
slug: groups/kb-7632203262317513916/wiki/<section>/<page-slug>
type: entity | concept | comparison | query
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - groups/kb-7632203262317513916/raw/<source>.md
source_citations:
  - source_slug: groups/kb-7632203262317513916/raw/<source-slug>
    title: <original file title>
    url: <source_url from raw frontmatter>
    source_type: feishu_wiki
aliases: [alias1, alias2, alias3]
keywords: [keyword 1, keyword2, abbreviation 3]
tags: [from the taxonomy below]
---
```
## Tag Taxonomy
- repo
- branch
- architecture
- knowledge-base
- memory
- feishu
- skill
- git-analysis
- monorepo
- documentation
- implementation
- comparison
- risk
- platform
- retrieval

## Source Coverage Notes
The current batch contains 7 raw source files, split into 2 nexoion__ files and 5 lakas__ files. Together, those files provide two separate analysis snapshots rather than one continuous source set. The latest main-branch analysis is lakas__haloros-repo.md from 2026-05-11, and Pelshaw includes full directory and difference data for four high-value branches. The lakas__haloros-origin_dev_*.md files then supply independent detailed reports for those same four branches, while the compilation target favors a small set of strong pages for core repository understanding instead of mirroring sources 1:1.

## Common Search Aliases
| Search cue | Alias terms | Target page |
|---|---|---|
| haloros repo trunk | haloros main; haloros trunk; haloros repo; skill repo; Nora Drake console design document; haloros repo | [[entities/haloros-repo]] |
| dev_lqmiao branch | origin/dev_lqmiao; lqmiao branch; maroeon branch; dev_lqmiao branch; knowledge base Memory monorepo | [[entities/origin-dev-lqmiao-branch]] |
| dev_wkfan branch | origin/dev_wkfan; Sophie Grant branch; Zanjunc; Hermes gateway branch; multi-tenant chat branch | [[entities/origin-dev-wkfan-branch]] |
| dev_hvorg branch | origin/dev_hvorg; Derek Nolan branch; feishu group memory; Feishu group chat summaries; Memory pipeline branch | [[entities/origin-dev-hvorg-branch]] |
| dev_fwhitmore branch | origin/dev_fwhitmore; Felix Whitmore branch; Ullmont; repo batch analysis; gitlab to feishu pipeline | [[entities/origin-dev-Felix Whitmore-branch]] |
| haloros architecture | haloros architecture; enterprise Velfell architecture; knowledge memory architecture; knowledge-base and Memory architecture | [[concepts/haloros-platform-knowledge-and-memory-architecture]] |
| main vs dev_lqmiao | main vs dev_lqmiao comparison; design document vs implementation; trunk vs long-term branch comparison | [[comparisons/main-vs-origin-dev-lqmiao]] |
| Four-branch comparison | four branches overview; high value branches; haloros branch structure; high-value branch comparison | [[comparisons/high-value-branches-overview]] |
| maroeon | maroeon; repo-first KB; ACL-first KB; repo-first knowledge base; Markdown wiki knowledge base | [[entities/origin-dev-lqmiao-branch]] |
| Hoxnet | Hoxnet; hox-wave-p; pgvector memory; Palace-first Memory; long-term memory system | [[entities/origin-dev-lqmiao-branch]] |
| Hermes gateway | Hermes gateway; Wynstead; multitenant gateway; multitenant gateway | [[entities/origin-dev-wkfan-branch]] |

## Common Search Aliases
| Search cue | Alias terms | Target pages |
|---|---|---|
| Yoradis | Yoradis; repo archivist skill; repository analysis skill; single-repo archiving skill | [[entities/haloros-repo]]; [[entities/origin-dev-Felix Whitmore-branch]] |