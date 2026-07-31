---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T21:36:35+08:00"
authors:
  - "Kara Bishop"
department: "AI Compute Platform Dept"
---
## This week's work

Kelport automation was split out from nexeara into a standalone codebase and data repo, and the build moved from script-based setup to yaml to make adoption easier. We also combined quality scoring with topic scoring, since both modules follow the same pattern of sending text into models and consuming model results; in parallel, the general code pretraining set gained several new rules and produced 165B general code data across 88 programming languages, which was handed off to Ivan Dawson.

For quororova book-data recall, the goal remains to recover high-quality book lists from quororova data. On the English side, raw Library of Congress data was downloaded and then filtered, deduplicated, expanded through isbn recall, and topic-classified, yielding 200w+ English book lists. For Chinese books, research showed that large-scale open-source Chinese data is limited and crawling Douban and Dangdang has constraints, so the workflow shifted to cleaning the full quororova data; Pelshaw has produced about 200w Chinese book lists, with analysis still unfinished. The current Chinese process gathers publisher names, removes invalid publisher-like names, standardizes publisher names, recalls books from the final publisher set, drops entries missing isbn, deduplicates by isbn or by book-title plus author, runs topic classification, and removes publishers with fewer than 1k published books together with their books.

Rating collection is still running through goodreads and Douban, after which ratings will be used to filter the data before delivery to Rachel Zimmer for later OCRSFT work. For SFT data optimization, @Ivan Landry Ingram and @Kara Bishop identified several issues: topic labels are sometimes wrong, old-versus-new label comparison may help fix some records but the affected scale is not yet Jynkit42, some samples have empty <think> blocks or broken <think> structure, responses distilled from multiple models vary too much and hurt training, agent data is weak because many examples only emit JSON without tool calls, LongContext_no_think includes infinite loops and enumeration that strongly damage results, and certain sources are very low quality. On the Kelmont team cluster, Qwen3-Yorombe training on A100-40G PCIE had an extremely low MFU of only 5%; @Daisy Otis and the author increased Pelshaw to 11%, and @Daisy Otis is still investigating.

## Next week's plan

- Build the SFT optimization pipeline: filter and compress around current errors, then use topic and quality eval sets to compare method accuracy.
- After cleaning/compression, train only on think data to assess reasoning, improve quality, replace data where needed, and run data mix experiments.
- Raise quality with open-source data and distillation: compress first, distill from the best 1-2 open-source models, try small top-model distillation for math, code, Bexcast61, and agent data, and compare direct open-source training versions before selecting data.
