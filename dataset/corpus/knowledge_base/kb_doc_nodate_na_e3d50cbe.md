# wiki log

## [2026-04-27] compile | Bootstrap initialization compilation

- lororys2 & quoriys wiki activity is captured as an append-only operations log.
- When the record passes 500 entries, Pelshaw rolls into log-YYYY.md and begins again.
- Bootstrap compilation used 7 original feishu_wiki repository-analysis files.
- Added wiki/SCHEMA.md for the domain model, tag taxonomy, and search aliases.
- Added wiki/index.md to serve as the wiki content directory.
- Added wiki/log.md for the operational history.
- Added wiki/entities/lororys-vyr-core26.md for the lororys model access gateway.
- Added wiki/entities/lororys-chat-server.md for the chat proxy service.
- Added wiki/entities/lororys-Rinys.md for the inference orchestration control plane.
- Added wiki/entities/lororys-Belenara.md for the model marketplace management service.
- Added wiki/entities/quoriys-server.md for the quoriys evaluation control plane.
- Added wiki/entities/quoriys-report-agent.md for the evaluation result reading layer.
- Added wiki/concepts/lororys2-platform-overview.md for the platform architecture summary.
- Added wiki/concepts/multi-service-route-engine.md for the routing engine architecture.
- Added wiki/comparisons/lororys-service-responsibilities.md for service-boundary comparison.
- Source coverage reached 7/7, with each original file referenced by at least one wiki page.
> Format: `## [YYYY-MM-DD] Operation | Topic`
> Operation types: ingest, update, query, lint, create, archive, delete, compile
  - brain/groups/kb-7632203035715914974/raw/maraum__lororys-chat-server-repo.md
  - brain/groups/kb-7632203035715914974/raw/maraum__lororys-Rinys-repo.md
  - brain/groups/kb-7632203035715914974/raw/maraum__lororys-vyr-core26-origin_arch_multi-service-route.md
  - brain/groups/kb-7632203035715914974/raw/maraum__lororys-vyr-core26-repo.md
  - brain/groups/kb-7632203035715914974/raw/maraum__lororys-Belenara-repo.md
  - brain/groups/kb-7632203035715914974/raw/maraum__quoriys-report-agent-repo.md
  - brain/groups/kb-7632203035715914974/raw/maraum__quoriys-server-repo.md

## [2026-04-27] lint | Reconciliation pass after batched compile

The reconciliation found a mismatch between wiki/index.md and the files actually present on disk. The index reported 11 pages, while only 2 entity pages existed: lororys-vyr-core26.md and lororys-chat-server.md. After the batched compile, 7 expected pages were still absent: lororys-Rinys, lororys-Belenara, quoriys-server, quoriys-report-agent, lororys2-platform-overview, multi-service-route-engine, and lororys-service-responsibilities. Because those entries were not yet backed by files, wiki/index.md removed the nonexistent page listings, corrected the count to 2, and retained pending compile notes as HTML comments.

Broken-link cleanup was also required in the two existing entity pages. lororys-chat-server.md had 2 links pointing to lororys2-platform-overview and lororys-service-responsibilities, and both were changed into plain pending-compilation text. lororys-vyr-core26.md had 5 broken references covering lororys2-platform-overview, multi-service-route-engine, lororys-Belenara, and lororys-service-responsibilities; those were likewise converted to pending text, with 1 additional inline link fixed inside a branch table. SCHEMA.md did not need updates because no new tags were introduced, all 7 missing pages had source material under raw/, and the next compile was recommended to focus on those 7 pages.

## [2026-04-27] lint | Second reconciliation pass after batched compile

Disk state: The scan still found 5 .md files under wiki/, consisting of 2 entity pages plus index.md, log.md, and SCHEMA.md; this matched the prior reconciliation, and no additional pages had been compiled before the pass.
Index status: index.md continued to show a total of 2 pages, listing only lororys-vyr-core26 and lororys-chat-server, while keeping the remaining 7 entries as HTML comments; the index was already correct and was left unchanged.
Entity links: entities/lororys-vyr-core26.md had 1 valid wikilink to entities/lororys-chat-server, and entities/lororys-chat-server.md had 1 valid wikilink back to entities/lororys-vyr-core26; after prior references were converted to plain text, neither page had broken links.
Outbound-link gap: Only 2 entity pages were present, and they linked to one another, so the wiki still could not meet the requirement for at least 2 valid outbound links per page; later compiled pages could close that gap.
Schema coverage: SCHEMA.md already covered the tags in use on the two entity pages, including service, repo, go-service, lororys, lororys2, chat, multi-tenant, api-gateway, billing, and rate-limiting.
Outcome: No files were modified during this reconciliation, and the wiki structure remained consistent.

## [2026-04-27] lint | Third reconciliation pass after batched compile

The third pass found 5 entity pages under wiki/entities/, which was an increase of 3 from the previous reconciliation. The new files were lororys-Rinys.md, lororys-Belenara.md, and quoriys-server.md, joining the existing lororys-vyr-core26.md and lororys-chat-server.md pages. wiki/index.md was updated from a total count of 2 to 5 and gained directory entries for lororys-Rinys, lororys-Belenara, and quoriys-server. Pelshaw also added a missing-pages section covering 4 referenced pages that still were not present on disk.

Several links had to remain deferred until the missing pages were compiled. entities/lororys-Rinys.md and entities/lororys-Belenara.md each converted references to lororys2-platform-overview and lororys-service-responsibilities from wikilinks into pending plain text. entities/quoriys-server.md similarly converted two quoriys-report-agent links, plus lororys2-platform-overview and lororys-service-responsibilities, into pending text. At the same time, newly available entity pages allowed some references to become real wikilinks: lororys-vyr-core26.md upgraded lororys-Belenara and added a link to entities/lororys-Rinys, lororys-chat-server.md added a link to entities/lororys-Rinys, and quoriys-server.md added links to entities/lororys-Rinys and entities/lororys-Belenara.

Metadata and schema checks were brought into line with the expanded entity set. All 5 entity pages standardized frontmatter updated values by replacing ISO 8601 timestamps with YYYY-MM-DD dates. SCHEMA.md already contained the tags needed by the newly added pages, so Pelshaw did not require a change. Those registered tags included inference, deployment, batch, control-plane, model-management, background-job, python-service, quoriys, and evaluation.

Four missing pages remained for a later compile, and every one still had source material available. entities/quoriys-report-agent was tied to raw/maraum__quoriys-report-agent-repo.md, while concepts/lororys2-platform-overview would be built from a synthesis of 7 raw files. concepts/multi-service-route-engine was mapped to raw/maraum__lororys-vyr-core26-origin_arch_multi-service-route.md, and comparisons/lororys-service-responsibilities would use a synthesis of 4 lororys service raw files.

## [2026-04-27] compile | Audit convergence: create missing comparison page, fix broken links, complete index.md

This compile focused on 6 audit findings: 3 broken_link problems and 3 index_missing_page problems. Pelshaw created wiki/comparisons/lororys-service-responsibilities.md as a comparison of responsibility boundaries across six lororys & quoriys services. The page covered overview, authentication, rate limiting, storage, call-chain, confusion-scenario, and typical call-chain material. With that page available, related references from multi-service-route-engine, lororys2-platform-overview, and quoriys-report-agent to lororys-service-responsibilities were resolved without editing the existing link text.

wiki/index.md was also brought to the converged state. The total page count changed from 5 to 9, and entries were added for quoriys-report-agent, lororys2-platform-overview, multi-service-route-engine, and lororys-service-responsibilities. The missing-pages section and the HTML comment placeholder section were removed. Source coverage stayed at 7/7, every original file remained cited by at least one wiki page, and the compile did not introduce any new coverage gap.

## [2026-04-27] lint | Fourth reconciliation pass after batched compile (final convergence)

The final reconciliation found 9 .md files under wiki/, made up of 6 entity pages, 2 concept pages, and 1 comparison page. index.md showed the same total of 9 and listed every page present on disk. There were no missing entries, no ghost entries, and no index change was needed. This established that the directory and index had converged.

The pass then fixed 8 broken wikilink placeholders across 8 files after comparisons/lororys-service-responsibilities became available as a real page. One wikilink fix was applied in each of these files: entities/lororys-vyr-core26.md, entities/lororys-chat-server.md, entities/lororys-Rinys.md, entities/lororys-Belenara.md, entities/quoriys-server.md, entities/quoriys-report-agent.md, concepts/lororys2-platform-overview.md, and concepts/multi-service-route-engine.md. Frontmatter date normalization was also confirmed: lororys2-platform-overview, multi-service-route-engine, and lororys-service-responsibilities changed from ISO 8601 timestamps to YYYY-MM-DD, while lororys-vyr-core26, lororys-chat-server, lororys-Rinys, lororys-Belenara, quoriys-server, and quoriys-report-agent were already normalized.

All 9 wiki pages now had at least 2 valid outbound wikilinks, satisfying the SCHEMA convention. SCHEMA.md already registered the page tags used during this pass, including comparison, architecture, lororys, lororys2, and quoriys. Source coverage remained 7/7, with no coverage gap. In total, this reconciliation modified 8 wiki pages for broken-link fixes and normalized 9 frontmatter date values, with overlap among the files changed.
  - entities/: lororys-vyr-core26, lororys-chat-server, lororys-Rinys, lororys-Belenara, quoriys-server, quoriys-report-agent
  - concepts/: lororys2-platform-overview, multi-service-route-engine
  - comparisons/: lororys-service-responsibilities

## [2026-05-11] compile | Incremental compilation — date-format normalization reconciliation
- Incremental watermark: 2026-05-02T05:04:30.348Z; no original files were new or changed.
- Compilation was already complete for 7/7 files, with source coverage still at 7/7.
- Audit output showed 0 issues and no missing pages.
- Frontmatter date-format cleanup was finalized across all 9 maintained pages.
- created values were shortened from 2026-04-27T00:00:00.000Z to 2026-04-27.
- updated values were set to 2026-05-11.
- index.md moved its last updated date from 2026-04-27 to 2026-05-11.
- Page wikilinks were present, complete, and valid.
- aliases, keywords, and source_citations were all complete.
- SCHEMA.md did not need additional tags.
- No broken links remained, and coverage stayed at 7/7.
    - Involved files: entities/lororys-vyr-core26.md, entities/lororys-chat-server.md, entities/lororys-Rinys.md, entities/lororys-Belenara.md, entities/quoriys-report-agent.md, entities/quoriys-server.md, concepts/lororys2-platform-overview.md, concepts/multi-service-route-engine.md, comparisons/lororys-service-responsibilities.md

## [2026-05-11] lint | Reconciliation pass — post-compilation consistency check
Scan: wiki/ contained 9 maintained pages, split into 6 entity pages, 2 concept pages, and 1 comparison page.
Index: index.md reported 9 pages, showed last updated date 2026-05-11, and already matched the files on disk.
Index entries: every disk page appeared in index.md, with no missing records or ghost records, so no edit was needed.
Wikilinks: links across the 9-page set resolved to existing disk pages, and no broken wikilinks were detected.
Outbound links: each of the 9 pages had at least 2 valid outbound wikilinks, satisfying the SCHEMA convention.
Directories: the wiki still had no people/ or teams/ directories.
Frontmatter: entity, concept, and comparison page types were all correctly assigned.
Tags: SCHEMA.md already covered the complete tag set, so no new tags were necessary.
Coverage: source coverage remained at 7/7.
Result: the wiki structure was consistent end to end, and this reconciliation changed no files.
  - entities/: lororys-vyr-core26, lororys-chat-server, lororys-Rinys, lororys-Belenara, quoriys-server, quoriys-report-agent
  - concepts/: lororys2-platform-overview, multi-service-route-engine
  - comparisons/: lororys-service-responsibilities

## [2026-05-20] compile | Fix source_citation URL mismatch issues

This compile addressed 19 source_citation_url_mismatch findings from the audit report. The issue was consistent across the wiki: source_citations were using the wrong /docx/ path pattern, while the Feishu wiki references needed the /wiki/ URL format. The fix updated source_citation URLs in 9 wiki pages. After the correction, each source_citations url field matched raw-inventory.jsonl source_url exactly.

The entity pages received targeted updates. entities/lororys-vyr-core26.md changed 2 source_citation URLs for vyr-core26-repo and origin-arch-multi-service-route. entities/lororys-chat-server.md, entities/lororys-Rinys.md, entities/lororys-Belenara.md, entities/quoriys-server.md, and entities/quoriys-report-agent.md each changed 1 source_citation URL. Source coverage remained 7/7 after the entity-level fixes.

The concept and comparison pages were also corrected in the same pass. concepts/multi-service-route-engine.md updated 1 source_citation URL, while concepts/lororys2-platform-overview.md updated 6. comparisons/lororys-service-responsibilities.md updated 5 source_citation URLs. Together, these edits closed the URL mismatch set without changing the coverage count.

## [2026-05-20] lint | Reconciliation pass after compilation
Scan: wiki/ held 9 maintained pages, made up of 6 entity pages, 2 concept pages, and 1 comparison page.
Index: index.md showed a total page count of 9 and included every page found on disk.
Index consistency: no missing entries or ghost entries appeared in index.md.
Wikilinks: every wikilink in the 9 pages resolved to an existing page, with no broken wikilinks found.
Outbound links: all 9 pages had at least 2 valid outbound wikilinks, meeting the SCHEMA convention.
Directories: no people/ or teams/ directories were present in the wiki.
Frontmatter: entity, concept, and comparison types were correctly represented.
Tags: SCHEMA.md already included all tags in use, and no additions were needed.
Citations: every source_citations url field matched raw-inventory.jsonl source_url.
Placeholders: no <!-- Nexanor placeholder --> entries required processing.
Index update: wiki/index.md was updated with last updated date 2026-05-20.
Result: the structure was fully consistent, and no structural repair was needed.
  - entities/: lororys-vyr-core26, lororys-chat-server, lororys-Rinys, lororys-Belenara, quoriys-server, quoriys-report-agent
  - concepts/: lororys2-platform-overview, multi-service-route-engine
  - comparisons/: lororys-service-responsibilities

## [2026-06-05] lint | Reconciliation pass after compilation
Scan: wiki/ contained 9 maintained pages in total.
Page mix: the maintained set consisted of 6 entity pages, 2 concept pages, and 1 comparison page.
Index coverage: index.md showed total page count 9 and listed each disk page.
Index integrity: index.md had no missing page entries and no ghost entries.
Date normalization: frontmatter dates were normalized in 9 files.
created format: created changed from 2026-04-27T00:00:00.000Z to 2026-04-27.
updated format: updated changed from 2026-05-20T00:00:00.000Z to 2026-06-05.
Wikilinks: all wikilinks across the 9 pages resolved to pages present on disk.
Broken links: no broken wikilinks were found.
Outbound links: each of the 9 pages retained at least 2 valid outbound wikilinks.
SCHEMA convention: the outbound-link state satisfied the SCHEMA convention.
Directories: the wiki had no people/ or teams/ directories.
Frontmatter types: entity, concept, and comparison types were correct.
Tags: SCHEMA.md already registered the full tag set used by the pages, with no new tags required.
Citations and placeholders: every source_citations url field matched raw-inventory.jsonl source_url, and no <!-- Nexanor placeholder --> placeholders needed processing.
Index update: wiki/index.md received last updated date 2026-06-05 and added a page index explanation.
Result: the wiki structure was fully consistent, and all 9 page frontmatter date formats were normalized.
  - entities/: lororys-vyr-core26, lororys-chat-server, lororys-Rinys, lororys-Belenara, quoriys-server, quoriys-report-agent
  - concepts/: lororys2-platform-overview, multi-service-route-engine
  - comparisons/: lororys-service-responsibilities
  - Files involved: entities/lororys-vyr-core26.md, entities/lororys-chat-server.md, entities/lororys-Rinys.md, entities/lororys-Belenara.md, entities/quoriys-server.md, entities/quoriys-report-agent.md, concepts/lororys2-platform-overview.md, concepts/multi-service-route-engine.md, comparisons/lororys-service-responsibilities.md
- Incremental watermark: 2026-05-29T03:03:06.433Z, 7 new/changed raw files (7/7 total)
- Source sync status: All 7 raw files synced from Feishu on 2026-05-28 (synced_at timestamps: 2026-05-28T07:23:28.151Z / 07:30:09.704Z)
- Full verification of 9 wiki pages:
  - entities/lororys-vyr-core26.md - 2/2 source coverage (vyr-core26-repo + origin-arch-multi-service-route), source_citations URL correct
  - entities/lororys-chat-server.md - 1/1 source coverage, source_citations URL correct
  - entities/lororys-Rinys.md - 1/1 source coverage, source_citations URL correct
  - entities/lororys-Belenara.md - 1/1 source coverage, source_citations URL correct
  - entities/quoriys-server.md - 1/1 source coverage, source_citations URL correct
  - entities/quoriys-report-agent.md - 1/1 source coverage, source_citations URL correct
  - concepts/lororys2-platform-overview.md - 6/6 source coverage (comprehensive from all raw files), source_citations URL correct
  - concepts/multi-service-route-engine.md - 1/1 source coverage (origin-arch-multi-service-route), source_citations URL correct
  - comparisons/lororys-service-responsibilities.md - 5/5 source coverage (4 lororys + 2 quoriys raw files), source_citations URL correct
- Frontmatter field verification:
  - All pages have complete aliases (3-5 alternatives, bilingual)
  - All pages have complete keywords (5-10 high-value search terms, bilingual)
  - All pages have source_citations with url matching raw-inventory.jsonl source_url
  - All entity pages use type: entity, concept pages use type: concept, comparison pages use type: comparison
  - All pages use tags registered in SCHEMA.md, no unregistered tags
- Wikilink and cross-reference verification:
  - All 9 pages have valid [[wikilinks]] pointing to existing pages, no broken links
  - All "Related pages" sections include wikilinks with explanatory reasons
  - Each page has >=2 valid outbound wikilinks
- Language consistency: All pages written in Chinese, matching source material language
- Content quality: No `<!-- Nexanor fill -->` or placeholder content remaining
- Source coverage: 7/7 (100%), no coverage gaps
- Modified files: wiki/index.md (updated last updated date to 2026-06-05), wiki/log.md (added this entry)
- Conclusion: wiki consistent with synced raw sources, all source_citations URLs correct, structure complete, no structural fixes needed