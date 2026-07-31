# Dataset schema

Three files. All content is synthetic and English.

## `corpus/` — 2,341 markdown documents
Organized by genre subdirectory: `reports/` (weekly reports, with YAML frontmatter:
`document_type`, `report_date`, `report_time`, `authors`, `department`), `knowledge_base/`
(KB pages, markdown with `##` headings), `faults/` (incident tickets). `corpus/manifest.json`
lists every document (`id`, `path`, `genre`, `chars`, `sha256`).

## `questions.json` — 907 questions
A JSON array of `{"id": "s7so-l1-0001", "question": "..."}`. The `id` encodes the tier
(`-l1-`/`-l2-`/`-l3-` = L1/L2/L3). This is all a system under test sees.

Example:
```json
{"id": "s7so-l1-0001", "question": "I'm following up on the PEXI incident from Apr 19, 2027. Who does the record list as responders?"}
```

## `golden_packets.jsonl` — 907 gold packets (one JSON object per line)
Used by the scorer. Key fields:

| Field | Meaning |
|---|---|
| `id` | matches `questions.json` |
| `operator` | question type (63 total) |
| `s7_track` | tier: `L1` / `L2` / `L3` |
| `answer_status` | `answerable` or `unanswerable` (18 verified-unanswerable) |
| `expected_answer_type` | `entity`, `entity_set`, `short_answer`, `count`, `comparison`, `structured` |
| `scoring_mode` | how the answer is scored (`fact_match`, set coverage, ...) |
| `question_text` | the question (same as `questions.json`) |
| `gold_answer` / `canonical_answer` | the correct answer |
| `required_facts[]` | facts the answer must cover: `{fact_id, fact_preview, points, required_evidence}` |
| `required_evidence[]` | precise evidence pointers, `document_id#p<N>` (paragraph N of that corpus doc) |
| `evidence_policy` | which documents are canonical / supporting for grounded scoring |
| `set_scoring` | for set-valued answers: the `required_items` used for precision/recall/F1 |
| `_provenance.canonical_span_text` | the exact answer-bearing span in the evidence |

Example `required_facts[0]`:
```json
{"fact_id": "s7so-l1-0001:f0", "fact_preview": "Lumfell Dawson; Kara Ingram Otis; Leon Yates",
 "points": 1, "required_evidence": ["kb_doc_2027-06-04_na_b50d28a9#p1", "kb_doc_2027-06-04_na_b50d28a9#p5"]}
```

JSON Schemas for these structures live in `../specs/schema/`.

## Version

Dataset version 2026-07-30. `gold_answer_optional` (present on 12 questions): answers that earn credit if given but cost nothing if omitted — requires scorer support, currently ignored by the bundled scorer.
