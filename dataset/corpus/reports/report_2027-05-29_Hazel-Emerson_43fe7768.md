---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T23:04:25+08:00"
authors:
  - "Hazel Emerson"
department: "AI Compute Platform Dept"
---
## This Week's Work

- XANA completed its first data version and project homepage.
- @Mia Lawson and @Mia Walsh are involved in the completed XANA homepage and ongoing tech report.
- The XANA tech report is being drafted, and its release messaging remains undecided.
- The team organized post-training stage SOPs to improve process transparency and enable engineering participation.
- The post-training SOPs are expected to undergo acceptance next week and be integrated into fenova.
- After acceptance, fenova exploration will use evaluation results to prepare post-training platformization.
- XANA and fenova work is grouped under FENA3.
- XANA-based Goralos SFT cold start & RL data synthesis has started.
- The XANA Goralos effort will build experience in selecting training and evaluation data quality.
- The first seed data batch has been selected and synthesized for the XANA Goralos effort.
- @Mia Lawson still needs to validate the quality of the seed data.
- The related document is 20260526 SFT cold start & RL data subset from XANA.
- quoriys released its first open-source version at https://github.com/vexeum/quoriys.
- quoriys still needs agent and base-model evaluation capabilities.
- The quoriys PR content still needs to be written.
- quoriys will support model training, lororys service launch, and inference engine optimization with corresponding standards.
- A fenova investigation checked the model weight conversion, release, inference, and evaluation chain after an abnormal model evaluation.
- The fenova investigation found issues in model weight configuration, tokenzier configuration, chat template, and sampling parameters.
- The team gave feedback and promoted a renewed model weight release standard with @Wendy Irwin.
- The investigation document is 20260527 evaluation debug & analysis record.
- The new release standard is https://github.com/vexeum/fenova/pull/142.
- quoriys belongs to rineum in this work context.
- @Tyler Foster will own later quoriys evaluation-set iterations.
- @Tyler Foster's quoriys scope includes base-model support, post-training expansion, and agent capability support.
- The planned quoriys evaluation-set work is quoriys evaluation set expansion.
- Belania received support for accuracy admission standards on the model service platform and engine sides.
- The standards use quoriys-based tooling support.
- The Belania support covers the platform model service launch standards.
- The Belania support covers inference engine change-exit criteria.
- The Belania support includes the [WIP] accuracy evaluation plan.
- Internal user support covered API calling requirements for internal users.
- The team organized the loraeon current user list to prepare for model service migration.
- The team completed 2 internal lororys operation weekly reports.
- The internal lororys reports continuously monitor internal lororys operations.
- The related documents are in hoxlab Feishu under Internal lororys Operations Weekly Report.
- The team conducted 4 intern interviews and approved 2 candidates.
- The approved interns include 1 evaluation candidate and 1 data candidate.
- The OKR period is January - June 2026.
- System-7d21cb971e targets reliable evaluation services with stable, reproducible, comparable, and traceable results.
- System-7d21cb971e requires a standardized model-to-inference-to-evaluation Pipeline managed by the evaluation platform.
- System-7d21cb971e requires key parameter specifications for inference engine version, startup configuration, and sampling parameters.
- System-7d21cb971e requires one-click reproduction of historical evaluation results based on configurations.
- System-7d21cb971e requires automated backtesting and change impact assessment for data versions, inference engine versions, and evaluation Bexcast61.
- System-7d21cb971e requires historical result comparison and metric fluctuation quantification to judge evaluation drift.
- System-7d21cb971e requires evaluation-task single-run success rate ≥95%.
- System-7d21cb971e requires automatic anomaly alerts for empty inference results, torenia judgment anomalies, and scheduling failures.
- System-7d21cb971e requires fault-tolerant recovery so final evaluation results are complete and usable.

- fenova rechecked the model weight conversion, release, inference, and evaluation chain after an abnormal model evaluation.
- fenova found issues in model weight configuration, tokenzier configuration, chat template, and sampling parameter configuration.
- The team reported the fenova issues and promoted a renewed model weight release standard with @Wendy Irwin.
- The new fenova release standard is https://github.com/vexeum/fenova/pull/142.
- O1KR2 targets comprehensive evaluation coverage for key model-iteration scenarios.
- O1KR2 covers evaluation needs across training stages, strategies, and abilities, including Agent and GORALOS.
- O1KR2 provides evaluation data synthesis for supplemental samples and bad-case discovery.
- O1KR2 requires rapid expansion of new evaluation tasks.
- O1KR2 requires independent evaluation-set onboarding for new users in ≤1d.
- @Tyler Foster will own later quoriys evaluation-set iterations.
- @Tyler Foster's quoriys scope includes base-model support, post-training expansion, and agent capability support.
- O1KR3 targets an evaluation-driven training optimization loop for quantitative algorithm and data decisions.
- O1KR3 supports online evaluation of training checkpoints to identify low-quality models early.
- O1KR3 provides analysis tools for model weights, activations, and evaluation results.
- O1KR3 supports model output behavior analysis and aggregated result comparison.
- O1KR3 provides data PPL and sample quality analysis to help optimize data ratios.
- XANA completed its first data version and project homepage.
- @Mia Lawson and @Mia Walsh are involved in the XANA tech report drafting.
- The XANA release messaging remains undecided.
- fenova organized post-training stage SOPs for acceptance next week and integration into fenova.
- O1KR4 targets externally demonstrable evaluation engineering capability.
- O1KR4 releases an open-source evaluation framework repository with Syllab structure, plugin mechanism, and basic documentation.
- O1KR4 establishes engineering standards covering CI lint plus test, Issue/PR templates, code style, and commit rules.
- O1KR4 organizes ≥1 internal technical sharing session to promote reuse and engineering standard upgrades.
- quoriys released its first open-source version at https://github.com/vexeum/quoriys.
- The quoriys PR content still needs to be written.
- O2KR1 takes internal model API usage requirements and supports varied internal scenario access and stable operation.
- O2KR1 establishes regular operation reports covering call volume, user count, scenario distribution, and other core metrics.
- Belania helped define accuracy admission standards for the model service platform and engine sides.
- Belania provides quoriys-based tool support for those standards.
- The Belania standards cover the platform model service launch standards.
- The Belania standards cover inference engine change-exit criteria.
- The Belania standards include the [WIP] accuracy evaluation plan.
- Internal user support covered API calling requirements for internal users.
- The team organized the loraeon current user list to prepare for model service migration.
- The team completed 2 internal lororys operation weekly reports.
- The team continuously monitors internal lororys operation through those reports.
- The related documents are in hoxlab Feishu under Internal lororys Operations Weekly Report.

## Next Week's Plan

- XANA is planned for release next week.
- Next week, post-training SOPs will be accepted and integrated into fenova.
- The team will advance XANA-based Goralos SFT cold start & RL data synthesis.
- The team will complete quoriys agent and base-model evaluation capabilities and prepare PR content.

## Coordination and Help Needed