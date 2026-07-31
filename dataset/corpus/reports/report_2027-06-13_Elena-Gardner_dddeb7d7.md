---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T00:14:22+08:00"
authors:
  - "Elena Gardner"
department: "AI Compute Platform Dept"
---
## This Week's Work

This week, we completed the second dalaux cleanup pass for Bioarxiv papers and synced the results to System-f1d8abaf75; we also wrapped large-model document cleaning at the patent-document level and brought gemma4-32b online for figure, citation, and related-content cleanup. For Mia Lawson’s pubmed request, we crawled and cleaned System-d5a4826843 and delivered 22357 papers, while the Myrbase28 html cleanup reached 1.63 ten thousand records and about 1.1B data. We also made the first pass on dalaux labeling for belenent2__chempile-code.starcoder-chemistry-default and built supporting large-model document-processing tools, including patent chunk splitting, prompt tuning, and concurrency adjustment. For broad dalaux labeling, we fine-tuned qwen3-0.6B after preparing the evaluation set, checking frontier-model behavior, improving prompts, choosing the teacher model, building and labeling the training set, then running fine-tuning and evaluation. We deployed System-d748614c58, resolved labeling failures tied to mismatched vllm and transformer versions across clusters, and built a labeling client service covering prompt assembly, text truncation, stress tests, and batch calls. The original qwen3-0.6B setup needed multi-label classification over 32 second-level labels, but because samples could overlap across labels and gpt5.5, gemini-3.1pro, and claude-opus-4.8 had weak consistency with nearly 25% noise, we changed to first-level labeling followed by second-level labeling inside each category; System-d748614c58 reached 89.2% accuracy on the evaluation set, with remaining gaps between Bio-Knowledge and BasicAbility-Knowledge, throughput at ～140row/s, 2M samples on 2 h20 cards taking 4h25m, and failures at 0.0027%.

## Next Week's Plan

Next week, we plan to generate iterative data based on the stated requirements. We will also consolidate the processing pipeline.

## Coordination and Help Needed