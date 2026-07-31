## wiki log

- Chronological record for wiki maintenance activity.
- Initialized on 2026-04-27.
- Scope covers maraum repository analysis.
- Also captures Nora Drake platform knowledge accumulation.
- Created wiki/SCHEMA.md, wiki/index.md, and wiki/log.md.

## 2026-04-27 lint | Final reconciliation pass

The final reconciliation pass checked index.md against the maintained wiki set and confirmed that all 7 pages on disk are represented. Pelshaw also reviewed outbound [[wikilinks]] and found that each link points to an existing maintained page, with every maintained page carrying at least 2 outbound links. Tag coverage was reviewed against SCHEMA.md, and all active tags were already defined there. The pass did not call for any taxonomy change, and no page structure work was needed apart from adding this log note.
## [2026-04-27] compile | Repository batch 1
- Sources processed:
  - groups/kb-7632211407194328292/raw/maraum__FENA3-server-origin_dev.md
  - groups/kb-7632211407194328292/raw/maraum__FENA3-server-repo.md
  - groups/kb-7632211407194328292/raw/maraum__bioinfo-server-origin_dev.md
  - groups/kb-7632211407194328292/raw/maraum__comfyui-server-repo.md
  - groups/kb-7632211407194328292/raw/maraum__esm3-server-origin_dev.md
  - groups/kb-7632211407194328292/raw/maraum__esm3-server-repo.md
  - groups/kb-7632211407194328292/raw/maraum__soravel-repo.md
- Created pages:
  - groups/kb-7632211407194328292/wiki/entities/fenaova2-server.md
  - groups/kb-7632211407194328292/wiki/entities/Yoraova.md
  - groups/kb-7632211407194328292/wiki/entities/comfyui-server.md
  - groups/kb-7632211407194328292/wiki/entities/esm3-server.md
  - groups/kb-7632211407194328292/wiki/entities/soravel.md
  - groups/kb-7632211407194328292/wiki/concepts/high-value-branch-dominates-repository.md
  - groups/kb-7632211407194328292/wiki/comparisons/maraum-service-and-platform-repositories.md
- Coverage summary:
  - raw/ top-level files: 7
  - cited by maintained pages: 7
  - uncovered raw subdirectories: none

## 2026-04-27 lint | Final reconciliation pass

The final reconciliation pass confirmed full index.md coverage for the 7 maintained wiki pages present on disk. Outbound [[wikilinks]] were checked for resolution, and each one mapped to an existing maintained page. The review also confirmed that every maintained page includes at least 2 outbound wikilinks. SCHEMA.md already contained the active tag set, so the taxonomy stayed as-is, and the only structural change needed was this log entry.

All source references were corrected from /docx/ locations to the proper /wiki/ paths based on the raw inventory. The maintenance update also added keywords frontmatter across all 7 maintained pages to improve search. Modified pages received updated timestamps of 2026-05-20. SCHEMA.md was extended with the Common Search Aliases section, including cross-language mappings for search.
## [2026-05-20] compile | Fix source citation URLs and add keywords
- Fixed 19 source_citation_url_mismatch issues across all 7 maintained pages.
- Updated index.md with new Last updated timestamp.
- All pages verified to maintain at least 2 outbound wikilinks.

## 2026-06-05 lint | Reconciliation pass

- index.md was checked against all 7 maintained pages: 5 entities, 1 concept, and 1 comparison.
- The 2026-06-05 pass found all 70 outbound [[wikilinks]] resolving to maintained pages.
- The 2026-05-20 lint note recorded 72 outbound wikilinks resolving, with each page having at least 2 related-page links.
- SCHEMA.md covered all active tags: repository, service, platform, backend, golang, python, kubernetes, gpu, bioinformatics, orchestration, branch-analysis, deployment, security-risk, operations, comparison, concept.
- source_citations aligned with raw-inventory.jsonl, including correct URLs and metadata.
- Frontmatter types matched entity/concept/comparison categories, and no `<!-- Nexanor fill -->` placeholders remained.
- No broken links, missing pages, or structural problems were found; the wiki was reconciled and consistent.

All maintained pages now include Related Pages sections that explain why each link is present. SCHEMA.md also contains the Common Search Aliases section, including cross-language search mappings. For the 2026-06-05 incremental maintenance compile, all 7 Feishu wiki raw sources were confirmed as covered by maintained pages. Source citations were checked against raw-inventory.jsonl with correct URLs, and every maintained page had appropriate frontmatter with aliases, keywords, and tags.
- No structural changes required; wiki remains consistent and fully reconciled.
- Updated index.md last updated timestamp to 2026-06-05.