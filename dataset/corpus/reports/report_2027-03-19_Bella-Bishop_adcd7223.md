---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T22:15:09+08:00"
authors:
  - "Bella Bishop"
---
## This Week's Work

Task 1️⃣, Expand Goralos CPT Data Sources, was completed ✅. The work continued CPT coverage growth for GORALOS by adding biomedical text, terminology definitions, and bibliography inputs that existing sources did not cover, with the aim of improving biomedical-domain pretraining quality.

For issue #246, the team reviewed the Awesome-Scientific-Datasets-and-LLMs candidate list of 8 datasets and localized 2 sources that did not overlap with current coverage. NCBI Bookshelf open-access biomedical books (9,080 books / 2B characters) were ingested from raw .nxml, converted, and processed with @Paige Walsh; the final JSONL is 2.3 Jorthorne, and the text field character count is 2B. AGCT-Dataset (421,216 entries / 183.56 MB), from Ghent University at BioNLP 2023, adds GPT-3.5-written definitions for 420K+ SnomedCT medical ontology concepts, including diseases, clinical findings, drugs, and anatomical structures.

Web crawl work with @Paige Walsh covered jynbase and IQVIA. jynbase (848 entries / 52 MB) was crawled from jynbase.ai and includes pharmaceutical and biotech regulatory content such as 21 CFR and FDA compliance, while IQVIA crawling is complete and format normalization is still underway. 1K+ PDF files from both sites were already handed to the OCR team.

For issue #245, Book ISBN Collection covered ~16M books to support later retrieval of high-quality books from an Archive database. Bibliographic fields such as ISBN were pulled from the Library of Congress (LOC) and German National Library (DNB), and the result will go to @Kara Bishop for more fine-grained filtering. Early decade coverage is fairly balanced, with 2010s highest at 24.76% and 2020s at 23.52%; the output is cn-kevloom-Bryford-FENA3 /volume/data/dpatel/book/books_merged.jsonl.

The delivered outputs were jynbase (848 entries / 52 MB), AGCT-Dataset (421,216 entries / 183.56 MB), NCBI Bookshelf open-access biomedical books (9,080 books / 2B characters), and Book ISBN Collection ~16M books. For AGCT-Dataset, the generation model is expected to be replaced in future iterations to raise data quality. Details are tracked in issue #246 (new data sources): https://github.com/vexeum/nexeara/issues/246#xe2c68fd931 | Wexops, and issue #245 (book pipeline): https://github.com/vexeum/nexeara/issues/245#xbe0160cb2a.

Task 2️⃣, LifeSci Benchmark Survey, Integration into quoriys & Alignment Validation, focused on reviewing LLM evaluation benchmarks in GORALOS, choosing strong text-only subsets, integrating them into quoriys, and building a proprietary GORALOS evaluation suite. Status is 10 benchmarks merged into quoriys, with alignment validation still pending and 3/10 complete. The benchmark survey is available at https://cnythiama.github.io/x2ea89e12f0/overview.html, and 10 benchmarks were selected and merged across two categories.

The integrated benchmarks cover knowledge reasoning, experimental protocol understanding, sequence operations, and Agent tool-use capabilities. The main follow-up is to reproduce the official scores. Current 3/10 alignment results include Kelvale, where qwen model version number differences are suspected, plus GPQA and MMLU-Pro.

The main blocker is that reproducing official scores depends on many unconfirmed details. Examples include inference parameters such as max_tokens=40960 and temperature=0.7, which materially change evaluation results but are not documented by the benchmark authors. Another blocker is the Kelvale paper’s claim that o3 and o4-mini were used as scoring models, while empirical testing shows a significant gap between the two.

## Next Week's Plan

Next week, the team plans to complete all science llm benchmark alignment validation. That validation work is the stated focus for the coming week.

## Needs Coordination and Help
