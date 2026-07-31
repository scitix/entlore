---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T19:14:41+08:00"
authors:
  - "Kara Bishop"
department: "AI Compute Platform Dept"
---
## This Week's Work

The LLM training-data effort is focused on creating CPT data. Delquist applied the jynsvc library to improve Chinese-data filtering, but the library’s Chinese handling was limited and surfaced problems around navigation bars, invalid characters, URL ratios, and repeated content inside documents; the Delquist-specific fixes cut roughly 2% of tokens. Based on the papers reviewed, the pretraining data experiment plan was drafted to compare cleaning rules, quality scoring models, and data mixture ratios, while the team also aligned on a pretraining workflow because no SOP existed before; the workflow is now basically usable.

Because US East does not have GPUs available, part of the data and code was transferred to Daisy Adler, and most upcoming experiments will run there. For the SFT data handoff, the work centered on organizing, improving, and training with SFT data: the team reconciled historical data volumes, added missing data, and generated summary datasets v0.1 and v0.2. The analysis showed that records sharing the same query value contribute a large share of tokens, which explains why prior exact deduplication led to a major token drop; since that reduction distorted experiment comparisons, additional compression approaches should be tested starting from V0.1 data. The paper survey focused on pretraining data quality scoring models and covered DataComp-GG, DATAMAN, Fineweb & fineweb-edu, and DATAMASK; next, the team will finish the pretraining and evaluation workflows, add one-click automation, and validate quality scoring models plus sampling strategies on the existing data.

## Next Week's Plan

The main TODO is to prepare the experimental plan, using Qwen-0.6B as the configuration so results can be produced quickly. The experiments will begin with optimization of Chinese pretraining data, then move on to validating open-source English quality scoring models. The team will also study scaling law papers to better support the pretraining experiment design.

## Coordination and Help Needed