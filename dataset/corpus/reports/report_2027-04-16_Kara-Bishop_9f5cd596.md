---
document_type: "report"
report_date: "2027-04-16"
report_time: "2027-04-16T19:51:35+08:00"
authors:
  - "Kara Bishop"
department: "AI Compute Platform Dept"
---
## This Week's Work

quororova combined open-source sources with an es index to deliver 70w strong English book entries, with categories assigned through rules; Pelshaw also crawled 11w highly rated Douban Chinese book entries and retained 7w after es-based retrieval. For the Qwen3-1.7B SFT optimization plan, the focus is raising the current SFT dataset quality toward open-source standards, and the team also supplied one baseline model for RL training. The analysis tooling now reviews dataset scale, turn counts, query and response lengths, think ratio, think-tag ratio, language mix, and PPL, while the labeling setup follows the earlier taxonomy and adds a practical annotation flow. Diversity checks cover exact, fuzzy, and semantic duplicate detection across queries, query-response pairs, and complete conversations; basic quality review also checks formatting, think-tag rules, tool_call existence, repeated answers, and responses that are too short. Semantic vectors are being clustered so that issue patterns inside clusters can be reviewed and used to judge diversity distribution. The team also completed an early pass on olmo3 data, where format-related quality problems were found and will need manual review plus filtering later. Math and code samples showed light duplication, which is currently considered within a normal range and not the highest-priority follow-up. Evaluation review also surfaced many examples where thinking sections were too long and caused the final response to be missing.

## Next Week's Plan

Next week, the team will look into why repeated outputs are appearing and will restore loss to test the effect, since current training applies loss correction for long-text data. The team will also verify whether packing is properly excluding samples that go beyond the window limit. One hypothesis is that the share of long-text samples is too high, or that individual samples are simply too long, and this still needs confirmation. Another detail to check is that tokenizer_conifg is set to 1M while the real window is 32K, though the impact is uncertain and expected to be small. For RL coldstart delivery, the first optimization target will be math data. Current SFT math content is difficult, with Qwen3-1.7B accuracy only at 2%-3%, so the team will test lowering the difficulty level.

## Coordination and Help Needed