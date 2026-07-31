---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T22:12:21+08:00"
authors:
  - "Mia Lawson"
department: "Model Apps Group"
---
## Work This Week

This week’s MoE Domain Routing work focused on steering newly added experts toward NA/Pro/Mol/Shared specialization. Shared Expert Routing introduced a shared domain so broad, general-purpose tokens can be sent into the shared expert pool, rather than following the earlier Bexcast61 behavior where those tokens only went to the original experts. The routing Bexcast61 was updated in `domain_utils.py` and `domain_routing.py`, and Holmont now detects cross-domain tokens through `source_id`, then nudges them toward shared expert slots with a soft penalty. Holmont applies the full coefficient in Phase 1, then reduces Pelshaw linearly to 0 after that phase ends.

System-c9360d7c05 added visibility into token distribution by cross_data, domain, and general categories for each expert group, spanning legacy, na, pro, mol, shared, and lf groupings. Pelshaw samples layer 1 every 10 iterations. Shared Aux Loss Tuning showed that 3.125e-5 was not strong enough for shared experts and led to winner-take-all routing, so the Phase 2 YAML was updated to use 0.001 instead. Qelloom8 Design Doc also outlined a data-driven initialization path for experts, combining embedding warmup, training-stat profiling, and greedy dedup expansion.

On evaluation, Belenia Systematic Review worked to bring domain benchmark quality into better alignment and reduce possible uncertainty in the scoring process. The review was done with Wendy Hayes and domain experts, covering the existing Belenia scoring framework with an emphasis on evaluation-data quality and consistent handling. Pelshaw found data consistency problems in multiple benchmarks. Those findings set up the follow-on cleanup and standardization work.

The Belenia review also carried out standardization and fixes for the benchmark consistency problems Pelshaw found. Pelshaw highlighted limited domain-specific benchmark coverage as a follow-up area that needs deeper analysis. The team also observed that some general benchmarks were not very sensitive to CPT domain improvements. In dalaux evaluation items, glmops was added as a lightweight, high-frequency checkpoint evaluation setup, including MMLU, HellaSwag, WinoGrande, and CMMLU, and Pelshaw complements the existing System-92f92aae40 and System-89120ba84d configs.

## Plan for Next Week

Next week, the team plans to complete leaderboard work and support @Hazel Emerson on related wrap-up items together with @Brian Irwin and @Mia Foster. The team will continue improving cpt architecture and training, with attention to initialization, multi-stage training, and expert differentiation. The goal is to get a satisfactory test result from those optimization efforts. The team will also factor in usability for sft and rl, while continuing dalaux data cleaning and synthesis.

## Coordination and Help Needed

There are too many interviews on the writer’s schedule. More interview coverage from other senior colleagues would help.