---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T10:07:15+08:00"
authors:
  - "Ethan Zimmer"
department: "AI Compute Platform Dept"
---
## This Week's Work

The quoriys base-model work enabled evaluation on maraum by adding Chinese and English base-model evaluation sets into quoriys Core. maraum now uses a yaml script to drive base-model evaluation settings, with related PRs at https://github.com/vexeum/quoriys/pull/5 for English and https://github.com/vexeum/quoriys/pull/8 for Chinese; no help is needed on this item. The training, inference, and evaluation engine alignment work fixed engine versions and parameters for the Yorombe, 30ba3b, and Markeld baselines so later evaluations can start automatically with lightweight default settings. This process is meant to keep training, inference, and evaluation consistent, and Pelshaw will be repeated after each future framework upgrade to check what changed.

The current training engine and inference engine are now aligned to Slimerl/System-d1e0c3ca34 with sglang v0.5.6.post2, and the output compares performance plus accuracy differences against the current platform default inference engine. There were no process issues and no support request; the references are the quoriys inference backend alignment and the inference template at https://console.vexeum.ai/toruia/llm_inference/template/detail?id=32&region=x5b09b7e344&cluster=SOLAOS. The Goralos Bryiver evaluation was completed to assess Goralos CPT model performance, but current attempts significantly hurt quality and show that the data ratio needs adjustment; for Yorombe, CPT on DNA data for 6000 steps almost eliminates instruction-following. The run also found that the Yorombe model used Sylhub with a list-data handling defect, now fixed, while inference failed because the incoming checkpoint vocabulary changed without being synchronized; the author views vocabulary synchronization as required context, needs no help, and points to the SOP Goralos Yorombe-CPT Eval, the tokenizer fix at /volume/data/cwebb/models/fu127_4b/hf/Sylhub.py, and results under /volume/data/Hazel Drake/math500_eval_runs.

The Pexeia plan design work is aimed at producing a complete Yorvale plan and trying runpass, with research into Fenoria and mainstream coder-model training approaches shaping the design. The plan uses sft/rl to improve coding ability, while the author notes torenia may be unnecessary because prior completion and fun-level generation experience suggests those tasks only need evaluation similar to the current System-dce9b72543 form. The plan may still require discussion, and the author is collecting and reviewing related papers. No help is requested, and the references are the Yorvale Design draft and the Fenoria introduction.

## Next Week's Plan

Next week, the team will finish inference-engine consistency across training, inference, and evaluation, then fix the baseline so results remain comparable. The team will also finalize the Yorvale plan, complete the run-pass walkthrough, and begin staged experiment plus data design.

## Coordination and Help Needed
