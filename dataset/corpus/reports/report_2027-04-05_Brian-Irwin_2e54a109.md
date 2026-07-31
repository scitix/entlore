---
document_type: "report"
report_date: "2027-04-05"
report_time: "2027-04-05T14:00:54+08:00"
authors:
  - "Brian Irwin"
---
## This week's work

This week’s first workstream focused on integrating an evaluation framework and aligning performance for Protein-related benchmarks, with the goal of making protein Benchmarks runnable as a zero-shot evaluation pipeline. The implementation follows the standard flow from dataset to community metrics to task, and this week added PDFBench, ProteinInvBench, ProteinGym, and TAPE while continuing review fixes. All benchmarks are now in the framework, code-standard follow-ups are being iterated with @Hazel Emerson, and performance has been checked against upstream repositories and paper reports, with summarized details captured in #310. The deliverable for this stream is PR #310, and no help is requested.

The second workstream reviewed 10✅ and 10❌ samples to judge whether the prompt design is reasonable, and reconfirmed whether quoriys prompts and evaluation metrics map one-to-one with upstream repositories. For every benchmark and sub-task, the review covers the upstream code or paper, volume path, upstream and quoriys model I/O, plus metric comparisons to verify consistency between quoriys framework results and upstream results. Results for 4 benchmarks were organized in the Feishu document Protein Benchmark In/Output Example. After discussion with @Mia Lawson and @Mia Walsh, some dataset prompt patterns were identified as problematic and not LLM-friendly, so they are being revised specifically for LLM suitability; no help is needed for this workstream.

## Next week's plan

Next week will continue quoriys dataset integration, standardize prompts across each benchmark so they better match LLM tasks, and put priority on summarizing the biological significance of every benchmark and sub-task.

## Coordination and help needed
