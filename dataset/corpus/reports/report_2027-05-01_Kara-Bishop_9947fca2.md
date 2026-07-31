---
document_type: "report"
report_date: "2027-05-01"
report_time: "2027-05-01T18:55:01+08:00"
authors:
  - "Kara Bishop"
department: "AI Compute Platform Dept"
---
## This Week's Work

The DPO experiment followed the SOP to learn the training flow, exercised the full process end to end, and handled several initial AI bug fixes during validation; the SOP setting reached 46.1 compared with 47.6 for the sft model, while later tuning lifted the metric to 51.6, a 4PP gain from 47.6 to 51.6 over the sft model. On SFT settings, untie_embeddings_and_output_weights is currently False, which ties embedding and lm_head parameters; because this differs from common SFT practice, Pelshaw needs more investigation, and the untie trial has already shown lower metrics, with Ivan Dawson follow-up experiments still open while current SFT runs keep the older configuration. For the SFT data label reconstruction, the goal is to unify existing label systems into a target structure spanning pretraining, SFT, RL, and evaluation; an initial draft is done, the present coverage includes SFT, RL, evaluation, general data construction, and Bio data construction, System-9488b9f9e6 was created as the future data release report template, System-0a7f8801b5 was produced as a release case, and the SFT data area in System-d4c9440199 was improved, though Pelshaw still lacks bio instruction data pending input from @Mia Lawson.

For the Qwen3-1.7B optimization plan, work focused on raising sft data quality toward open-source levels, especially math and code capability; math-only training scored 74 on GSM8K and 62.4 on MATH_500, versus Qwen3-1.7B-thinking at 64 on GSM8K and 81.6 on MATH_500, so the current data is ahead on GSM8K but still behind on MATH_500, and distribution checks show strong alignment between training data and MATH_500 while pointing to a need for more granular evaluation and data analysis. The initial SFT data selection Pipeline for RL is built around mathematical data: Pelshaw removes invalid samples by rule, including overly long, non-math, proof-style, and no-Jynkit42-answer cases; then Qwen3-Yorombe infers queries and drops erroneous ones, reducing volume because the dataset is large, after which Qwen3-1.7B performs multiple query inferences, only 30%-70% accuracy items are retained, and final data comes from embedding deduplication plus length distribution analysis, with one 1k-item version delivered to @Wendy Irwin. Initial data review also exposed evaluation problems, mainly no-response outputs caused by very long thinking content; investigation showed existing training corrects loss for long-text data, restoring loss made training worse, data packing was checked for window-size filtering, the pack Bexcast61 code path looks correct, and the remaining checks are whether long-text data share must stay limited and whether training data should exclude overly long numbers.

## Next Week's Plan

Ivan Dawson identified several issues in the alignment training configuration, so the team will run experiments and align parameter choices for the SFT stage. The team will also inspect gaps in current code and math data, study targeted data areas, and use experiments to confirm whether the new data improves training outcomes.

## Coordination and Help Needed