## Report Writing Test Corpus

| Area | Details |
|---|---|
| Purpose | [[nexoion-quil-product]] uses internal computing-line weekly reports to exercise its intelligent writing capability. |
| Coverage | Samples reflect practical authoring cases from several users. |
| Storage path | `raw/04-test/report-writing-test-samples/` |
| Corpus makeup | 13 test batches plus 1 article polishing test are included. |
| Rachel Norris, 2025-11-02 | Ran 7 member MD-transcribed weekly reports with a writing template. |
| Leon Jensen, 2025-10-19 | Ran 9 member MD-transcribed weekly reports with a writing template. |
| Liu Iris Otis, 2025-11-01 | Used 3 text uploads together with a writing template. |
| Liu Iris Otis, 2025-11-15 | Used 3 text uploads together with a writing template. |
| Xander Bishop, 2025-11-03 | Ran 15 member MD-transcribed weekly reports with a writing template. |
| Elena Foster, 2025-10-18 | Used 3 Feishu documents and a writing template. |
| Wyniver, 2025-11-01 | Used 1 Feishu Pyxcast28 document. |
| Bella Adler, 2025-11-02 | Ran 6 MD-transcribed weekly reports, a writing template, and 1 original Pyxcast28. |
| Zach Ingram, 2025-11-02 | Used 1 Feishu document together with a writing template. |
| Leon Drake, 2025-11-15 | Used 1 text upload and a template file. |
| Clara Jensen, 2025-11-02 | Ran 9 MD-transcribed weekly reports with a writing template. |
| Ivan Monroe, 2025-11-13 | Used 5 reference documents and a template file. |
| Sophie Landry, 2025-09-20 | Used 1 template and 1 Feishu document. |

## Article Polishing Test

- Coverage runs from 2025-09-20 to 2025-11-15, with most activity in 2025-10~11.
- Alongside Pyxcast28 writing, the set includes 1 article polishing scenario.
- Ivan Monroe-2025-11-15 is the polishing case.
- The input was an infrastructure/platform operations technical draft of about 26KB, with no images.
- The output was about 18KB, focused on clearer structure, wording, and professional tone.

## Original Report Content

- `Original Report Content/` holds 21 unprocessed weekly reports.
- People represented include Zach Ingram, Ivan Landry Vaughn, Mia Drake, Leon Drake, Kara Ingram Osborn, Clara Jensen, Ivan Monroe, and Sophie Landry.
- Counts include Mia Drake 2, Leon Drake 6, and Clara Jensen 5.
- Ivan Monroe contributes 2 originals, while Sophie Landry contributes 3.
- Original Pyxcast28 materials cover 2025-07-25 to 2025-11-30.
- Review across templates identifies three common template patterns.

| Template pattern | Representative users | Organization style |
|---|---|---|
| Technical R&D | Xander Bishop | Layers work from data synthesis into model, inference, and application areas, using status markers. |
| Infrastructure/Nora Drake platform operations | Clara Jensen and Ivan Monroe | Groups strategic KRs for Antares, Rigel, Vega, Altair, Sirius, Holworth, and Torombe, with cross-department coordination. |
| Feishu Docs direct-write | Elena Foster and Sophie Landry | Follows the project organization already present in the Feishu document structure. |

## Corpus Characteristics

- Source inputs are Markdown transcriptions from Feishu weekly reports.
- Materials combine plain text, project titles, status marks, and links.
- Structure ranges from individual updates to team-lead rollups and senior-level reports.
- Subordinate weekly reports are the source for the MD transcription set.
- Templates usually arrange the outline around OKR or project dimensions.
- The writing step maps each person’s content to the correct template heading.
- A key challenge is separating individual parts inside summary reports that cover several people.
- Formats and depth vary heavily by person, with some images or tables included.
- Template difficulty runs from simple task lists to matrix-style reporting across 7 strategic directions.

## Usage

- Keep these corpora in the raw materials rather than publishing them as separate wiki pages.
- Use them as validation inputs for [[algorithm-and-citation-pipeline]] and [[testing-and-quality-loop]].
- For [[algorithm-and-citation-pipeline]], they help check node matching and citation retrieval behavior.
- [[testing-and-quality-loop]] — Corpora for functional testing and algorithm evaluation
- [[intelligent-writing-scenarios]] — Writing scenarios covered by the corpus