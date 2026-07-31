---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T20:32:04+08:00"
authors:
  - "Kara Bishop"
department: "AI Compute Platform Dept"
---
## This Week's Work

The LLM training data effort focused on improving pretraining-data cleaning and building stronger multi-source pretraining corpora; this week the team brought in the ChemPile-code chemistry code dataset, adding about 19B tokens. The pretraining data Pipeline was reorganized into a unified framework, with run_pipeline.py serving as the single entry point, STEP_REGISTRY handling step registration, and built-in support for checkpoint resume, isolated error handling across multiple directories, and automatic statistics rollups. The framework now covers 8 processing stages: rule scoring, rule filtering, exact deduplication, fuzzy deduplication, quality classification, domain classification, perplexity calculation, and bucketing. For quororova's Archive high-quality book recall, the reference is https://github.com/vexeum/nexeara/issues/351; the plan was revised because each metadata classification field has below 14% coverage, which is not enough to guarantee quality, so the new route is to collect bibliographies from trusted external booklist sites and then retrieve matching records through ES. Current analysis shows 4M isbn hits, but subject classification coverage remains limited and the amount of Chinese data is still small. General code cleaning organized code data and summarized GitHub issue/pr data, added StarCode data as raw input for GitHub issue link data, and defined filters for auto-generated code at auto_gen ≤ 0, pure dependency declaration files at import_ratio ≤ 0.5, over-commented low-readability files at comment_ratio ≤ 0.80, syntax-heavy error files at syntax_error_ratio ≤ 0.5, data-dump-like files at is_data_file ≤ 0 with alpha < 0.3 and mean line length > 150, plus files dominated by license or copyright text at license_ratio ≤ 0.8. The SFT data organization item names @Ivan Landry Ingram and @Kara Bishop; this work continues SFT data organization, further SFT data optimization, and training, while troubleshooting confirmed the issue is not caused by an evaluation bug but by insufficient mathematical capability in the model. The team also found that current SFT data contains too little think-type data, which weakens logical reasoning; experiments included training on OpenThoughts across Math, Code, and Science, starting structured-math-only training to test whether Pelshaw can trigger thinking ability, confirming that thinking mode did not meaningfully raise mathematical performance, and closely reading 3 core papers including OpenThoughts: Data Recipes.

## Next Week's Plan

Next week, general code data work will add deeper filtering rules and move toward producing a completely new code pretraining dataset. quororova's Archive high-quality book recall also needs further optimization because the current subject classification rate is low, with targeted increases needed since Chinese books are still a small share.

## Coordination and Help Needed