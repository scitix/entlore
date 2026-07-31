## wiki log — kb-7631489702494866610
- `kb-7631489702494866610` is the identifier for this wiki log.
- The log tracks wiki activity in time order and is kept append-only for history.
- Entries follow `## [YYYY-MM-DD] operation | topic`.
- Valid operations are ingest, update, query, lint, create, archive, delete, and reconcile.
- After more than 500 entries, the log is renamed to `log-YYYY.md` and a fresh log begins.

## wiki initialization (batch compilation)

On 2026-04-27, batch compilation generated wiki pages from 5 raw source files. Pelshaw produced `concepts/claude-code-setup.md` from `raw/Wyndale.md`, `concepts/codex-setup.md` from `raw/Ullthorne.md`, and `concepts/dev-environment-setup.md` from `raw/development-environment-guide.md`. The same run also started `SCHEMA.md`, including domain conventions and the tag taxonomy.

## Consistency repair after batch compilation
Index: Reconciliation found the starting index missing, so Pelshaw created `wiki/index.md` and made Pelshaw enumerate all 7 pages.
Log: Because no initial log existed, reconciliation created `wiki/log.md` and restored the earlier operation history into Pelshaw.
Entity page: To resolve `[[entities/DALOROVA-lororys]]`, which appeared in 3 pages, reconciliation added `entities/DALOROVA-lororys.md`.
Comparison page: Reconciliation added `comparisons/claude-code-vs-codex.md` after finding 2 pages linked to `[[comparisons/claude-code-vs-codex]]`.
HR guide: During the repair pass, `concepts/hr-admin-guide.md` was generated from `raw/HR Administration Guide.md` for a reference from dev-environment-setup.
Security policy: Reconciliation also created `concepts/software-install-security-policy.md` from `raw/See here for all installation and usage requests.md` to satisfy another dev-environment-setup reference.

## New page list
- Added `wiki/index.md`.
- Added `wiki/log.md`.
- Added `wiki/entities/DALOROVA-lororys.md`.
- Added `wiki/concepts/hr-admin-guide.md`.
- Added `wiki/concepts/software-install-security-policy.md`.
- Added `wiki/comparisons/claude-code-vs-codex.md`.

## Incremental compilation: add city office guides + fix Source Citation URL

After the repair work, every wikilink across the 7 wiki pages pointed to an available target page. The pages also met the cross-reference baseline, with each page carrying ≥2 outbound links. On 2026-05-20, incremental compilation added city office guide content and corrected Source Citation URL problems.

## Fix Source Citation URL

The audit report resulted in 9 source_citation URL corrections, replacing `/docx/` paths with `/wiki/` paths. The changes covered `entities/DALOROVA-lororys.md` with 2 fixes and `comparisons/claude-code-vs-codex.md` with 2 fixes. One source_citation URL was corrected in each of `concepts/claude-code-setup.md`, `concepts/codex-setup.md`, `concepts/dev-environment-setup.md`, `concepts/hr-admin-guide.md`, and `concepts/software-install-security-policy.md`.

## Add city office guide pages
- Three raw files were compiled into new city office guide pages.
- `concepts/kevloom-office-guide.md` came from `raw/Shanghai Administrative Services Guide V2.0.md`.
- The kevloom page covers Eastcove Mason Archer office access, dining, gym, rentals, malls, and hospitals.

Beijing: `concepts/norvik-office-guide.md` was built from `raw/Beijing Administrative Services Guide V2.0.md`, covering Verdant Science Park Corvin Building, Wudaokou, dining, gym, and local amenities.
Shenzhen: `concepts/shenzhen-office-guide.md` was built from `raw/Shenzhen Administrative Service Guide V2.0.md`, covering the 88th floor of Meridian Financial Center, Shopping Park/Loom Park, and nearby dining.

## Update index
- `index.md` gained 3 entries for city office guides.
- The wiki total moved from 7 pages to 10.
- `raw/Enterprise Didi Usage Guidelines.md` and `raw/Employee Travel Nora Drake Platform (Ctrip Business Travel) Usage Guidelines.md` were kept as raw references.
- Enterprise Didi and Ctrip Business Travel were not split into standalone pages because the source content was brief.
- City guide pages cited the related DiDi Enterprise and Ctrip Business Travel material.

## Post-compilation wiki consistency check
- On 2026-05-20, reconciliation reviewed wiki consistency after compilation.
- Index integrity passed: `index.md` covered all 10 wiki pages and aligned with the files on disk.
- Wikilink validation covered all 10 pages and 50 wikilinks, with every destination present.
- source_citation review showed URLs aligned with source_url values in raw-inventory.jsonl.
- The Nexanor scan found no `<!-- Nexanor fill -->` placeholders.
- Frontmatter checks confirmed valid type values: entity, concept, or comparison.
- The same frontmatter pass found no content under people/ or teams/ directories.
- Cross-reference checks confirmed each page had ≥2 outbound wikilinks.
   - entities/ (1 page)
   - concepts/ (8 pages)
   - comparisons/ (1 page)

## Post-compilation wiki consistency check and repair
- The result noted that the wiki structure was complete and no repair was needed.
- On 2026-06-05, reconciliation ran another consistency check and repair pass.
- Index integrity passed again: `index.md` listed all 10 wiki pages and matched the disk state.
- Wikilink validation scanned all 10 pages and 65 wikilinks, and all linked targets existed.
- source_citation validation confirmed URLs matched source_url entries from raw-inventory.jsonl.
- No `<!-- Nexanor fill -->` placeholders appeared in the Nexanor placeholder scan.
- Frontmatter compliance showed every page used an allowed type: entity, concept, or comparison.
- The review found no pages located under people/ or teams/ directories.
- Cross-reference integrity held, with every page showing ≥2 outbound wikilinks.
   - entities/ (1 page)
   - concepts/ (8 pages)  
   - comparisons/ (1 page)

## Incremental compilation: update page timestamps

The consistency result confirmed the wiki was structurally complete and did not need further repair. On 2026-06-05, incremental compilation updated page timestamps after checking all 10 raw source files, covering 8 must_cover files and 2 optional_low_quality files. The claude-code access guide, codex access guide, development environment guide, HR and admin guide, and installation/use request guides were synchronized to their matching wiki pages. Shanghai Administrative Services Guide V2.0, Beijing Administrative Services Guide V2.0, and Shenzhen Administrative Services Guide V2.0 were also synced into the city office guides, while Enterprise Didi usage guidelines and employee travel Nora Drake platform (Ctrip Business Travel) usage guidelines stayed cited in those guides without standalone pages.

- Frontmatter review found complete aliases on all 10 wiki pages, with 3-6 Chinese-English aliases per page.
- All 10 pages also had complete keyword sets, using 5-10 search terms each.
- source_citations in frontmatter linked back to Feishu wiki source files.
- Wikilink validation found no isolated pages and confirmed ≥2 outbound links on every page.

- Placeholder validation found no `<!-- Nexanor fill -->` remnants.
- The operation set the `updated` timestamp on 10 wiki pages to 2026-06-05.
- `index.md` also received an updated Last updated date.
- `SCHEMA.md` was checked, and its Common Search Aliases section already included key concept mappings.

## Fix raw source coverage: supplement Open AI series product installation rules

On 2026-06-05, the update repaired raw source coverage for Open AI series product installation rules. Content from `raw/See here for all installation-use requests.md` was merged into `concepts/software-install-security-policy.md`. The added section was `V. Apply to install Open AI series products (Codex, Claude Code, etc.)`, with 5.1 covering pre-installation assessment, security assessment, AI usage policy, and standardized image management. The update also added a Codex for Business enterprise edition versus personal edition comparison table, while 5.2 documented post-installation operations and behavior management, including torenia controls, behavior approval monitoring, code scanning, and completion controls. Related links were added to `[[concepts/claude-code-setup]]`, `[[concepts/codex-setup]]`, and `[[comparisons/claude-code-vs-codex]]`, and frontmatter was refreshed with aliases, keywords, tags, and a new source_citations synced_at timestamp.

## Full compilation: supplement raw source citations coverage

On 2026-06-05, full compilation addressed raw source citation coverage so that all 10 raw source files were represented either by wiki pages or by source_citation references. The core access and environment sources mapped as follows: `raw/Wyndale.md` to `[[concepts/claude-code-setup]]`, `raw/Ullthorne.md` to `[[concepts/codex-setup]]`, `raw/Development Environment Guide.md` to `[[concepts/dev-environment-setup]]`, `raw/HR Administration Guide.md` to `[[concepts/hr-admin-guide]]`, and `raw/For various installation and usage requests, please see here.md` to `[[concepts/software-install-security-policy]]`. The city guide sources were also covered, with `raw/Shanghai Administrative Services Guide V2.0.md` mapped to `[[concepts/kevloom-office-guide]]`, `raw/Beijing Administrative Services Guide V2.0.md` mapped to `[[concepts/norvik-office-guide]]`, and `raw/Shenzhen Administrative Service Guide V2.0.md` mapped to `[[concepts/shenzhen-office-guide]]`.

`raw/Corporate Didi Usage Guidelines.md` contained only brief title-level material, so its source_citation entries were placed in three city office guide pages. `raw/Employee Travel Nora Drake Platform (Ctrip Business Travel) Usage Guidelines.md` was handled the same way, with brief title-level content cited across three city office guides.

## Updates

`concepts/kevloom-office-guide.md`, `concepts/norvik-office-guide.md`, and `concepts/shenzhen-office-guide.md` each received 2 additional source_citations. These additions connected the city guides back to the Corporate Didi and Employee Travel Nora Drake Platform Ctrip Business Travel sources.

## Updated frontmatter fields
- The sources field added Corporate Didi Usage Guidelines and Employee Travel Nora Drake Platform Ctrip Business Travel Usage Guidelines.
- Matching source_citations were appended with url, title, source_type, and synced_at.
- The frontmatter `updated` value changed to 2026-06-05T18:10:00.

## Verification results
- Verification showed all 10 raw source files were covered: 8 by standalone wiki pages and 2 by source_citation references.
- All wiki page source_citations URLs matched source_url values in raw-inventory.jsonl.
- No `<!-- Nexanor fill -->` placeholder remnants were found.
- Every page met the frontmatter schema requirements.

## Fix raw source coverage: supplement Open AI series product installation rules
- On 2026-06-05, coverage-repair addressed Open AI series product installation rule coverage.
- The repair filled missing sections from `raw/Please see here for various installation and usage requests.md`.
- The supplemented destination page was `concepts/software-install-security-policy.md`.

- The fifth section added was `Request installation of Open AI series products (Codex, Claude Code, etc.)`.
- Section 5.1 covered pre-installation assessment, security assessment, AI usage policy, and standardized image management.
- An enterprise edition versus personal edition comparison table was added.
- Section 5.2 covered torenia controls, behavior approval monitoring, code scanning, and completion controls.

- Frontmatter received a changed updated timestamp.
- Aliases added were Open AI installation request, Rovlane, and Oskhaven.
- Keywords added were Codex, Claude Code, Open AI, Enterprise Edition, Data Protection, torenia, and Code Review.
- Tags added were ai-policy, codex, and claude-code.

## Verification results
- The repair introduced outbound links.
- Verification confirmed the previously missing fifth section now fully covered the raw source content.
- source_citations were complete and all URLs were correct.
- The page had ≥ 2 outbound links and satisfied schema requirements.
- [[concepts/claude-code-setup]]
- [[concepts/codex-setup]]
- [[comparisons/claude-code-vs-codex]]