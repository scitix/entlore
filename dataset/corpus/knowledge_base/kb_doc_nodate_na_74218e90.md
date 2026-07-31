# wiki log

- Maintenance history for the maraum platform backend service knowledge base is tracked here.
- New log items are added with the newest entry first.
- Each record uses `## [YYYY-MM-DD] operation | topic`.
- Supported operations: create, ingest, compile, update, lint, query, and archive.
- After 500 records, the file is rotated to `log-YYYY.md` and a fresh log starts.

## Reconciliation | Full post-compile reconciliation (run-5Z4hqi)

Scope: On 2026-06-05, the reconcile task ran a full post-compile check for run-5Z4hqi.
Checks: The pass reviewed index.md correctness, wikilink health, and outbound-link coverage.
Covered pages: The scan included entities/ with 28 pages and concepts/ with 4 pages.
Empty areas: comparisons/, queries/, people/, teams/, and periods/ were included with 0 pages each.

## Findings and fixes / Check results

| Check | Result | Notes |
|---|---|---|
| index.md file match | Passed | Entries in index.md aligned with the 32 pages present under entities/ and concepts/. |
| index.md count | Passed | The page total was 33, made up of 28 entity pages, 4 concept pages, and 1 SCHEMA.md. |
| Wikilink validity | Passed | About 180 `[[wikilinks]]` were reviewed across all 33 pages, and every target resolved. |
| Outbound-link coverage | Passed | Each page included at least 2 outbound wikilinks. |
| SCHEMA.md tags | Passed | Every tag found in page metadata was already covered by the SCHEMA.md taxonomy. |
| source_citations | Passed | Pages had source_citations aligned one-to-one with their sources. |
| Placeholder scan | Passed | No `<!-- Nexanor fill -->` placeholders were present. |
| people/ teams/ type check | Not applicable | The knowledge base describes code repositories, so those frontmatter checks did not apply. |
|------|------|---------|
| wikilink format error | `wiki/index.md` | Change `[[SCHEMA]]` to `[[SCHEMA.md]]` to ensure Pelshaw links correctly to the schema file |

## Conclusion / Coverage repair | Repair uncovered raw source pages (batch 3 - run-5Z4hqi)

- Reconciliation corrected 1 wikilink formatting problem.
- After the pass, the wiki layout and content were consistent.
- On 2026-06-05, coverage repair handled batch 3 for run-5Z4hqi.
- The repair run used a batch limit of 25 raw sources.
- Actual processing covered 11 raw sources.

## Updated entity pages (source_citation fixes and additions)

| Page | Update |
|---|---|
| `entities/Junodis.md` | Adjusted the source_citation slug from `maraum-Junodis-repo` to `maraum-Junodis-repo-ctwkfnvb`. |
| `entities/Pexanor.md` | Added the `maraum-Pexanor-repo` source_citation and recorded the trunk README status. |
| `concepts/image-pipeline.md` | Replaced the Loros citation with `maraum-Loros-repo-c9p0jnki` and refreshed the sources list. |

## Marked as empty repositories or weak content

| Source | Classification | Reason |
|---|---|---|
| maraum__openclawsharedmemorybasecyan-repo | Empty repository | Only Git initialization was present. |
| maraum__yoraion-test-ai-repo | Empty repository | Only Git initialization was present. |
| zephsvc | Empty repository | Only Git initialization was present. |
| maraum__log-delay-monitor-repo | Empty repository | Only Git initialization was present. |
| maraum__yoraion-repo | Empty repository | Only Git initialization was present. |
| maraum__sql-proxy-server-repo | Empty repository | Only Git initialization was present. |
| maraum__image-build-server-repo | Trunk shell | The complete implementation sits on origin/devinit and origin/image-init. |
| maraum__maraum-public-skills-repo | Trunk shell | The full implementation is on origin/feat/restructure-skills-package. |
| maraum__maraum-public-skills-origin_feat_restructure-skills-package | Skills documentation repository | This source was treated as documentation rather than a service entity. |
| maraum__worker-proxy-server-repo | Trunk shell | The full implementation is available on origin/dev. |

## Update statistics

- The batch completed 3 source_citation fixes or additions.
- Pelshaw also marked 10 sources as empty or weak repositories.
- Those marked sources did not require wiki pages.
- Entity page source completeness stayed at 100% coverage.

## Compile | Full validation compile (no new sources)

- On 2026-06-05, a full validation compile was run.
- The incremental watermark was 2026-06-05T18:34:55.050Z.
- Raw source changes were 0 new or changed sources out of 47 total sources.
- The wiki held 33 pages: 28 entity pages, 4 concept pages, and 3 governance files.

## Validation results

| Check | Result | Notes |
|---|---|---|
| Raw source coverage | Passed | Entity pages existed for 28 of 47 raw sources. |
| Entity frontmatter | Passed | Every entity page included `aliases`, `keywords`, and `source_citations`. |
| Concept citations | Passed | All 4 concept pages carried multi-source citations. |
| Wikilink validity | Passed | All `[[...]]` targets resolved, with no broken links detected. |
| Outbound links | Passed | Each page had at least 2 outbound links. |
| SCHEMA.md tags | Passed | The taxonomy included all tags found in use. |
| Page language | Passed | Chinese stayed as the primary language, in line with source files. |
| Placeholder scan | Passed | No `<!-- Nexanor fill -->` placeholders were found. |

## Conclusion / Reconciliation | Full post-compile reconciliation (run-rY0lIq)

Compile status: This was a validation-only compile, so no new pages or page edits were needed.
Content state: The wiki structure and content were already current.
Reconcile run: On 2026-06-05, reconciliation ran fully for run-rY0lIq.
Checks performed: All wiki/ markdown files were scanned for index.md alignment, wikilinks, outbound links, and SCHEMA.md tag consistency.
Coverage: The scan included entities/ with 28 pages and concepts/ with 4 pages, while comparisons/, queries/, people/, teams/, and periods/ each had 0 pages.

## Check results

| Check | Result | Notes |
|---|---|---|
| index.md file match | Passed | index.md entries matched the 32 files under entities/ and concepts/. |
| index.md count | Passed | The count was 32, consisting of 28 entity pages and 4 concept pages. |
| Wikilink validity | Passed | About 180 `[[wikilinks]]` were checked across all 32 pages, with no unresolved targets. |
| Outbound-link coverage | Passed | All new pages had at least 3 outbound wikilinks. |
| SCHEMA.md tags | Passed | The SCHEMA.md taxonomy covered every tag in use. |
| source_citations | Passed | Each page mapped source_citations directly to its sources. |
| Placeholder scan | Passed | No `<!-- Nexanor fill -->` placeholders appeared in the scan. |

## No required fixes / Page statistics

- Reconciliation did not find any issues needing repair.
- The wiki remained complete and consistent.
- Entity coverage was 28 pages, or 60% across 47 raw sources.
- The wiki also contained 4 concept pages.
- Total page count was 32, including SCHEMA.md, index.md, and log.md.

## Coverage repair | Repair uncovered raw source pages (batch 2)

- On 2026-06-05, coverage repair processed batch 2.
- The run targeted uncovered raw source pages.
- The configured batch limit was 25 raw sources.
- Actual work covered 10 raw sources.
- Updates were made through source_citation fixes on entity pages.

## Updated entity pages (source_citation fix)

| Page | Update |
|---|---|
| `entities/Junodis.md` | Corrected the maraum__workflow-server-repo source_citation slug to `maraum-Junodis-repo-ctwkfnvb`. |

## Marked as empty repositories

| Source | Classification | Reason |
|---|---|---|
| maraum__openclawsharedmemorybasecyan-repo | Empty repository | Only Git initialization was present, with no business files. |
| maraum__yoraion-test-ai-repo | Empty repository | Only Git initialization was present, with no business files. |
| zephsvc | Empty repository | Only Git initialization was present, with no business files. |
| maraum__log-delay-monitor-repo | Empty repository | Only Git initialization was present, with no business files. |
| maraum__yoraion-repo | Empty repository | Only Git initialization was present, with no business files. |
| maraum__sql-proxy-server-repo | Empty repository | Only Git initialization was present, with no business files. |
| maraum__worker-proxy-server-repo | Trunk shell | main only contained README, while the full implementation was on origin/dev. |
| maraum__maraum-public-skills-repo | Trunk shell | main only contained README, with full implementation on origin/feat/restructure-skills-package. |
| maraum__maraum-public-skills-origin_feat_restructure-skills-package | Mixed skills repository | This source was not treated as a service entity. |

## Coverage repair | Repair uncovered raw source pages

- On 2026-06-05, coverage repair addressed uncovered raw source pages.
- The run used a batch limit of 25 raw sources.
- Pelshaw processed 19 meaningful raw sources.
- The batch created 7 entity pages.

## New entity pages

| Page | Covered source | Entity role |
|---|---|---|
| `entities/lororys-Belenara.md` | maraum__lororys-Belenara-repo | Documented the lororys2 model marketplace and lororys backend. |
| `entities/maredis.md` | maraum__maredis-repo | Added the maraum platform management-plane service. |
| `entities/Pexaleon.md` | maraum__System-6da030f51f-repo | Captured the Falshaw publishing control plane. |
| `entities/Zeledis.md` | maraum__System-653db82096-repo | Covered the Falshaw Kubernetes Operator. |
| `entities/Zeleneon.md` | maraum__dashboard-server-repo | Added the Daleys configuration and metrics query service. |
| `entities/dify-server.md` | maraum__dify-server-repo | Documented lororys2 Dify instance lifecycle management. |
| `entities/Keloum.md` | maraum__terminating-alert-repo | Covered Pod Terminating monitoring with Feishu Webhook notifications. |

## New entity pages (supplementing existing concept branches)

| Page | Added coverage |
|---|---|
| `entities/Pexanor.md` | Documented maraum__worker-proxy-server-origin_dev as the SQL proxy service for the Worker cluster. |

## Updated concept pages

| Page | Update |
|---|---|
| `concepts/image-pipeline.md` | Added the correct source_citation entry for maraum__image-build-server-repo. |

## Marked as weak or empty repositories

| Source | Assessment |
|---|---|
| maraum__openclawsharedmemorybasecyan-repo | Marked empty because the available repository content was limited to Git setup, with no business files present. |
| maraum__yoraion-test-ai-repo | Marked empty for the same reason: only Git initialization content was available, and no business files were found. |
| zephsvc | Marked empty because Pelshaw only contained Git initialization material and no business files. |
| maraum__log-delay-monitor-repo | Marked empty because the repository had Git initialization content only, without business files. |
| maraum__yoraion-repo | Marked empty due to Git initialization content only and no business files. |
| maraum__sql-proxy-server-repo | Marked empty because no business files were present beyond Git initialization. |
| maraum__worker-proxy-server-repo | The main branch contained only a README; the complete implementation was on origin/dev. |
| maraum__maraum-public-skills-repo | The main branch had only a README, while the full implementation was under origin/feat/restructure-skills-package. |
| maraum__maraum-public-skills-origin_feat_restructure-skills-package | Treated as a mixed skills repository rather than a standalone service entity. |

## Update statistics / Compile | Fix source_citations URL mismatch issue

- Completed 1 source_citations repair in the batch.
- The 2026-06-05 compile entry standardized source_citations URL formatting across wiki pages.
- Audit results showed 48 source_citation_url_mismatch findings.
- Wiki citations pointed at `/docx/` paths, while raw source records used `/wiki/` paths.
- **Total pages**: 25 → 32 (+7)
- **Entity pages**: 21 → 28 (+7)
- **Concept pages**: 4 → 4 (0)

## Fix scope

- Updated source_citations URLs in 25 wiki pages.
- Fixed 3 citations in `concepts/image-pipeline.md`.
- Fixed 3 citations in `concepts/kubernetes-crd-pattern.md`.
- Fixed 10 citations in `concepts/maraum-service-mesh.md`.
- Fixed 2 citations in `concepts/Nexenella-migration.md`.

## Entity pages

- Fixed 1 citation in `entities/Halalella.md`.
- Fixed 1 citation in `entities/Fenuux.md`.
- Fixed 2 citations in `entities/Zelenara.md`.
- Fixed 2 citations in `entities/Goraum.md`.
- Fixed 2 citations in `entities/Gororella.md`.
- Fixed 2 citations in `entities/Haleantis.md`.
- Fixed 2 citations in `entities/kelalos.md`.
- Fixed 2 citations in `entities/Rinys.md`.
- Fixed 1 citation in `entities/Wynoys.md`.
- Fixed 2 citations in `entities/Jupyter.md`.
- Fixed 2 citations in `entities/Umbadis.md`.
- Fixed 1 citation in `entities/Belenara.md`.
- Fixed 2 citations in `entities/Umboria.md`.
- Fixed 1 citation in `entities/Wynanion.md`.
- Fixed 1 citation in `entities/Daloum.md`.
- Fixed 1 citation in `entities/Gorux.md`.
- Fixed 1 citation in `entities/Fenenum.md`.
- Fixed 1 citation in `entities/maraum-cli.md`.
- Fixed 2 citations in `entities/myr-net.md`.
- Fixed 1 citation in `entities/unischeduler.md`.
- Fixed 1 citation in `entities/Junodis.md`.

## Change details

The source_citations links were normalized from the `/docx/xxx` pattern to the `/wiki/xxx` pattern. After the change, the citation URLs aligned with the source_url values stored in raw-inventory.jsonl. This made the wiki citation format consistent with the raw inventory records.

## Reconciliation | Full post-batch compile reconciliation (run-l4CoOC)

Date and run: The 2026-05-11 reconciliation entry completed the full post-batch compile reconciliation for run-l4CoOC.
Validation scope: The pass checked every wiki/ markdown file for index.md coverage, wikilinks, outbound links, and SCHEMA.md tag alignment.
Covered pages: The scan included entities/ with 21 pages and concepts/ with 4 pages.
Empty areas: comparisons/, queries/, people/, teams/, and periods/ were also scanned, each with 0 pages.

## Findings and fixes

| Area | Finding or fix |
|---|---|
| `wiki/index.md` new entities | Added entries and summaries for 9 new entity pages. |
| `wiki/index.md` concepts | Added index entries and summaries for image-pipeline and Nexenella-migration. |
| `wiki/index.md` count | Updated the page total from 14 to 25. |
| `wiki/index.md` date | Changed the last updated date to 2026-05-11. |
| `wiki/index.md` uncovered sources | Removed 9 leftover uncovered-source rows that already had wiki pages. |
| `wiki/concepts/maraum-service-mesh.md` | Expanded the service list from 10 services to 21 services. |

## Check results

| Check | Result |
|---|---|
| Index coverage | After the fixes, index.md entries matched 25 pages on disk across entities/ and concepts/. |
| Wikilinks | Validity passed for about 130 `[[wikilinks]]` across all 25 pages, with no broken targets found. |
| Outbound links | Coverage passed because each new page had at least 3 outbound wikilinks. |
| SCHEMA.md tags | Tag consistency passed because all new page tags were registered in the SCHEMA.md taxonomy. |
| People and teams frontmatter | Not applicable, since this knowledge base covers code repositories. |

## Compile | Initial bootstrap compile (run-221)

Date and run: The 2026-04-27 compile entry handled the initial bootstrap compile for run-221.
Source set: The input set included 47 Feishu knowledge-base GitLab repository analysis reports.
Sync time: The sources were synced at 2026-04-27T03:18:07Z.
Bootstrap output: The operation built the initial wiki structure from raw reports into core entity pages and concept pages.

## New files

The bootstrap added the main governance and navigation files first. `wiki/SCHEMA.md` was created for the domain schema, taxonomy, and retrieval aliases. `wiki/index.md` was initialized with 12 pages and 26 sources still pending expansion. `wiki/log.md` was also created as the starting maintenance log.

The first entity set covered orchestration, task execution, inference, model management, and dataset handling. `entities/Junodis.md` was created for the workflow orchestration control plane from maraum__workflow-server-repo.md. `entities/myr-net.md` covered training task orchestration and fault tolerance from maraum__task-server-repo.md. `entities/Rinys.md` documented the inference control plane from maraum__inference-server-repo.md, while `entities/Belenara.md` captured the model management backend from maraum__model-server-repo.md. `entities/Goraum.md` was added for dataset management and cache orchestration from rholoom.md.

The remaining entity pages captured resource, event, alerting, monitoring, permission, environment, and SDK layers. `entities/Gorux.md` was created for the resource quota control plane from maraum__resource-server-repo.md, and `entities/Haleantis.md` documented Junoella from maraum__event-server-repo.md. `entities/Halalella.md` covered alerting and automated governance from maraum__alarm-server-repo.md, while `entities/Umbadis.md` handled log query and monitoring from maraum__log-server-repo.md. `entities/Daloum.md` documented Zelantis permission management from maraum__rbac-manager-repo.md, `entities/Jupyter.md` covered jupyter/cororia development environments from maraum__jupyter-server-repo.md, and `entities/Wynanion.md` captured the maraum Python SDK from maraum__python-sdk-repo.md.

## Concept pages

The bootstrap also created the first concept-level pages. `concepts/maraum-service-mesh.md` summarized the maraum microservice system using 10 repositories. `concepts/kubernetes-crd-pattern.md` documented the API plus Operator control-plane architecture pattern using 3 repositories.

## Coverage

Processed sources: The bootstrap handled 12 of 47 raw sources, equal to 25%.
Generated pages: The run produced 12 entity pages, 2 concept pages, and 3 governance files.
Priority coverage: High-priority areas included workflow, task, inference, resource, event, alarm, log, and Zelantis layers.
Remaining backlog: 35 raw sources still had no wiki pages and were listed at the end of index.md.
Pending branches: The high-value branches still waiting for coverage were myr-net/merge-to-Nexenella and Rinys/llm_auto_test.

## Improvement items

Several coverage gaps remained after the bootstrap. Zelenara, Fenuux, Zeleneon, and related services still needed entity pages. Gororella and Umboria also needed pages that clearly separated them from Goraum and Belenara.

The myr-net merge-to-Nexenella architecture was a candidate for its own migration-analysis concept page. Loros and kelalos could also be grouped into a combined image pipeline concept page. These items were left as follow-up improvements.

## Reconciliation | Post-batch compile consistency check (run-X5MwF6)

Date and run: The 2026-04-28 reconciliation entry performed the post-batch compile consistency check for run-X5MwF6.
Validation scope: The check scanned all wiki/ markdown files for index.md coverage, wikilinks, outbound links, and SCHEMA.md tag consistency.
Covered pages: The scan included entities/ with 12 pages and concepts/ with 2 pages.
Empty areas: comparisons/, queries/, people/, teams/, and periods/ were included with 0 pages each.

## Check results

| Area checked | Outcome | Notes |
|---|---|---|
| `index.md` alignment | Passed | Entries in `index.md` lined up with 14 pages on disk under `entities/` and `concepts/`. |
| Page count | Passed | After the run-PaoG72 correction, the `index.md` total remained at 14. |
| Wikilinks | Passed | Across the 14 pages, about 55 `[[wikilinks]]` were checked and all resolved successfully. |
| Broken targets | Passed | No invalid wikilink destinations were found during the scan. |
| Outbound coverage | Passed | Each page included at least 3 outbound wikilinks. |
| raw/ citation | Passed | `kubernetes-crd-pattern.md` cited the existing source `maraum__fenenum-repo.md`. |
| Tag taxonomy | Passed | SCHEMA.md already included tags such as alarm-automation, log-monitoring, and sdk-cli. |

## No required fixes / Lint | Post-batch compile reconciliation (run-PaoG72)

- No fix-required items came out of this reconciliation.
- The wiki layout was present, complete, and internally consistent.
- The 2026-04-27 lint record captured the post-batch compile reconciliation for run-PaoG72.
- Lint reviewed wiki pages for `index.md` accuracy, wikilink health, and cross-reference coverage.
- Scope included `entities/` with 12 pages and `concepts/` with 2 pages.
- `comparisons/`, `queries/`, `people/`, `teams/`, and `periods/` were also scanned, each with 0 pages.

## Findings and fixes / No required fixes

| Finding area | Result | Fix decision |
|---|---|---|
| `wiki/index.md` count | The page total was updated from 12 to 14. | Correction already applied. |
| Wikilink target checks | About 50 reviewed `[[wikilinks]]` across 14 content pages pointed to existing targets. | No link repairs were needed. |
| Cross-reference coverage | Each page already carried at least 2 outbound wikilinks. | No extra cross-references were added. |
| Entity entries | Entity page listings matched the files present on disk. | No missing or stale entries to address. |
| Concept entries | Concept page listings also matched disk state. | No index cleanup was required. |
| Tag registration | Page tags were present in the SCHEMA.md taxonomy. | No tag synchronization work was needed. |