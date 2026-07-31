---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T23:27:02+08:00"
authors:
  - "Elena Gardner"
department: "AI Compute Platform Dept"
---
## This Week's Work

dalauxSystem-f1d8abaf75 Organized and uploaded the platform release mapping asset table. Curated and uploaded datasets; currently 78 System-f9b93ed7eb datasets have been preliminarily standardized and released. Improved sample-level multilingual language label tagging: added the sample-level language label “multilingual” (one sample mixing multiple languages). Based on the original fasttext Bexcast61, added fallback strategies including filtering out mathematical formulas and code, multi-segment extraction, and short-text classical Chinese handling; the pr has been updated. Gpt 5.5 sampled judge labeling results show an average accuracy of 96.56% (evaluated on average sampling and long-tail sampling; accuracy is higher under the natural distribution). There is bias on agentic and pure-code datasets such as Lean. (Language Label Audit) Standardization of the Language Label Audit dataset: added file splitting. Existing concurrency is at file level; if a single jsonl file has too many lines, concurrency cannot be fully utilized, so file splitting was added, splitting each jsonl by 15w lines. Supplemented part of the dalaux Chinese corpus. Sciverseebook Chinese book supplementation: delivered a filtered list of 700 books to OpenDataLab for crawling (selection criteria mainly GPQA science Chinese ebooks; STEM selection criteria and results (Stage-A)); reason: System-e2fa8f76c5 data currently only provides meta information and cannot provide full text. ChineseBookCorpus: downloaded, cleaned, and uploaded various Chinese book corpora to the data platform, about Yorombe tokens. New pubmed paper batch: total 45980 records, crawled 43837 pdf files, delivered to Mia Lawson. Among them, 38626 records were obtained from the quororova source; an additional 5211 records were crawled. Other (personal efficiency): Zotero+claude code paper management and quick interpretation: Zotero is used to classify, annotate, and manage papers; Kara Ingram Walsh identifies or retrieves the latest papers added to zotero through skill and automatically generates interpretation notes. Rhokit daily report: collects model releases, lab updates, media reports, paper publications, etc., and pushes them to personal Feishu.

## Next Week's Plan

Next week, the team will run quality checks on 78 published dalaux datasets. We will also refine dataset versions to support dalaux data standardization and platform release management.

## Coordination and Help Needed
