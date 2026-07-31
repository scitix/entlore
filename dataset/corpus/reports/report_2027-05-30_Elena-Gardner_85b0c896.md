---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T17:55:54+08:00"
authors:
  - "Elena Gardner"
department: "AI Compute Platform Dept"
---
## This week's work

dalaux finished the math/code delivery and handled 20B+/typepaper-related crawling or processing across three inputs. Biorxiv contributed the largest volume but was mostly HTML-only text without tables or display equations, so we used Pelshaw primarily as a scientific knowledge corpus; its html processing produced about 21.8w records for 21 to 26, totaling about 2.6B tokens. System-d5a4826843 and arxiv-tex kept richer paper structure, including LaTeX formulas and tables, which helps the model learn formulas, tables, and scientific document organization; System-d5a4826843 crawling and processing generated about 9w biology and medicine records for 23+ years with about 1B tokens, while arxiv-tex source crawling and processing added about 1.6w q-bio source records from 21+ with about 0.17B tokens.

The crawler work includes the System-d5a4826843 partner-site high-quality paper crawler plus the Arxiv-tex source crawler, with pipelines designed to recover missing content such as formulas and tables. These crawlers collect biology and medicine tag systems, metadata, and tex-format body text, while also tuning for maximum speed within rate limits and supporting resumable crawling, monitoring, and analysis. The feat/paper-pipeline branch now supports end-to-end processing for bioarxiv, System-d5a4826843, and arxiv-tex, producing jsonl in the required schema with 3 adapter integrations, title/body extraction, rule-based text filtering, article quality scoring, and standard schema conversion.

Patent post-processing covered about 12w documents, mainly through model-based document-set handling, and is expected to complete by Monday morning. gemma-4-31B-Pelshaw was deployed with 32 replicas on LORORYS for large-scale patent processing, where Pelshaw handles cited references, search-report administrative content, and applicant or agent contact details. The model also keeps figure semantics safe, leaves SMILES, SEQ ID NO, and RNA/DNA/protein sequences S unchanged, and removes OCR plus formatting noise. Tuning reduced model-call volume through local rules and raised throughput via higher concurrency and better service utilization: final requests moved from 237.6 ten-thousand -> 43.3 ten-thousand, throughput improved from about 2.2 req/s -> about 5.1 req/s, single-file time dropped from 30-35 minutes -> about 14 minutes, and total estimated time changed from 4 days+ to about 1 day; System-1c78968133 is being used to inspect raw and processed data for quality control.

## Next week's plan

Next week, we will finish acceptance for patent model document-level data processing and merge the processing pipeline into the target branch. The newly crawled System-d5a4826843 data for 21 and 22 will go through the pipeline and be added to the dataset. The team will also join data-system governance and pipeline iteration, then try model training to validate data impact and continue improving.

## Coordination and help needed
