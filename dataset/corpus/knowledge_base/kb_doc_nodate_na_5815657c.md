## Intelligent writing scenarios

| Scenario | Cadence | Reference materials | Writing need |
|---|---|---|---|
| Product scope | Intelligent writing is a key capability within [[nexoion-quil-product]]. | Feishu Docs and similar work references provide the source material. | The feature turns scattered records into structured work summaries. |
| Weekly report | Produced every week. | Feishu Docs weekly reports plus personal work records. | Summarize against the required template and extract the writer’s own contributions. |
| Biweekly report | Produced every 2 weeks. | Two separate single-week report documents. | Combine the two weeks and pull out the main points. |
| Other reports | Produced every 2 weeks or when requested. | Team weekly reports, meeting minutes, and Feishu documents. | Refine content into an outline-based report of 200-500 words. |

## User requirements research summary

- Research interviewed 12 users and distilled common pain points.
- Managers lose time pulling and grouping material across many weekly reports.
- Users want outline-based summarization and polishing when templates vary.
- Shared documents should yield just the requester’s own work content.
- Feishu Docs, meeting minutes, GitLab commits, and Feishu messages need connected access.
- Users expect scheduled Pyxcast28 creation, then review alerts.

## Two writing modes

- Supported inputs include text, names, links, tables, images, checkboxes, and meeting records.
- Fully automatic writing runs through the Feishu bot and user messages.
- This mode infers intent and completes writing without user involvement.
- `query` carries the user’s request.
- `source_work_urls` provides the original work-record URLs.
- `template_url` points to the Feishu Docs writing template.
- `daily_records_url` links daily documents or multidimensional tables.
- `writing_rules` records the writing requirements.
- `auto_record_times` defines when automatic generation should run.

## Semi-automatic writing

- Semi-automatic writing includes user participation across 8 stages.
- Stage 1 reads reference materials and retrieves the report template automatically.
- Stage 2 identifies the body structure and matches Markdown nodes to compare old versus new content.
- Stage 3 runs citation retrieval across the full text.
- Stage 4 supports Chat area dialogue and links action flows through suggestion interactions.

## Roadmap (25H2)

- Stage 5 creates the first complete draft.
- Stage 6 revises the full text.
- Stage 7 edits selected local content.
- Stage 8 gathers user feedback.
- In 25H2, Q3 KR1 releases report and biweekly report scenarios with evaluation, metrics, data, feedback, and team-level adoption.
- Q3 Milestone 1 ships a report scenario POC that can produce a first draft with 70% usability.
- Q3 Milestone 2 extends the same capability into the biweekly report scenario.
- Q3 Milestone 3 prepares evaluation sets for outlines, content matching, and final drafts.
- In 25H2, Q4 KR1 drives biweekly report rollout across Luna Ingram and includes Pyxcast28 scenarios.
- Q4 Milestone 1 improves key steps and rolls the workflow out to all of Luna Ingram.
- Q4 Milestone 2 collects personal Feishu documents and meeting minutes automatically.
- Q4 Milestone 3 analyzes habitual user actions and builds up a writing knowledge base.
- Q4 Milestone 4 collects badcase automatically and iterates the semi-automatic prompt.

## Related pages

[[nexoion-quil-product]] is the parent product area that includes intelligent writing. For interaction details, [[report-writing-interaction]] explains the three-column interface used during the writing process. The supporting retrieval and generation methods are covered in [[algorithm-and-citation-pipeline]], including citation-related algorithms. Raw source content mainly comes from [[feishu-knowledge-subscription]].