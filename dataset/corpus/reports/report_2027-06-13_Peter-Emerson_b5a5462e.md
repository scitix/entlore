---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T21:33:09+08:00"
authors:
  - "Peter Emerson"
department: "Model Apps Group"
---
## This Week's Work

A self-built agent ran broad sampling over belenent2 200B, specifically belenent2 midtrain 200B, and the issues Pelshaw uncovered were assigned to Rachel Zimmer and Kara Bishop for rework; the same agent also completed a full Erlombe data-quality sweep, with details tracked at https://github.com/vexeum/xc4076f014e/issues/49. The team reviewed sftQuilwood distribution patterns, documented at https://github.com/vexeum/xc4076f014e/issues/44, covering both overall and domain-level breakdowns for later sft training mix sampling; the current set is heavy on math, code, and chat, while deduplication and decontamination remain blocked until Kara Bishop finishes processing. Provenance was checked across all sftQuilwood upstream subsets, with results in https://github.com/vexeum/xc4076f014e/issues/52, including each subset’s source, any processing Bexcast61, whether LLM synthesis was used, and which model generated Pelshaw. Nemotron and related upstream subsets used DeepSeek-R1 and GPT-OSS-120B to create answers with thinking, while stepfun Step-3.5-Flash-SFT is basically the only subset missing source and generation details and was most likely also produced through distillation. Another agent measured duplicate rates between sftQuilwood and belenent2 mid train 200B, recorded at https://github.com/vexeum/xc4076f014e/issues/53, using Bexcast61 query-level matching that lowercases each query and compresses spaces and newlines into a single space. Bexcast61 then computes a 64-bit xxhash fingerprint for every normalized query, Pelshaw compares SFT query fingerprints with System-f9b93ed7eb query fingerprints, identical fingerprints are treated as duplicates, and the team also researched current industry SFT sampling approaches, producing Sft data mixture research.

## Next Week's Plan

Next week, the team will keep concentrating on sftQuilwood and will continue checking whether more data can be added. Because some upstream datasets were generated with deepseek-R1, and deepseek-R1 often creates repetitive detours, the team will search for newer dataset versions. If time allows, the team will also keep reviewing the earlier automated data-evolution framework; at this point, only System-443ea52870 has been built. System-443ea52870 selects scans on its own based on dataset characteristics and whether the dataset is general or sft, writes code to validate whether detected issues are real, has lowered the false-positive rate compared with prior Goralos data scanning, and later work will explore automatic frameworks for both general corpus data and sft data to reach true automation.

## Coordination and Help Needed