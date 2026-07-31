---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T23:59:41+08:00"
authors:
  - "Hazel Emerson"
department: "AI Compute Platform Dept"
---
## This Week's work

This week centered on XANA (fenaova2) and QUORIYS, with quoriys now technically prepared for its initial open-source release while PR-facing product docs are in progress to explain full agent coverage and differentiation. quoriys finished the agent-evaluation architecture plus adapter-mode design for faster onboarding of new evaluation sets, and that same agent-evaluation and adapter work is still being actively developed toward completion. XANA finished small sample-set runs for the planned open-source and closed-source full models, and the outcomes aligned with expectations; the detailed conclusions are tracked in XANA Samples Results. The production XANA build is being connected into quoriys for Vyrforge5 SFT/RL evaluations, while @Grace Walsh continues improving the research version and has largely removed the known data defects. Next steps for the research path are larger data scaling, trend checks, and backfill work, although overall delivery is running a little behind plan because the data volume was too high and, after discussion with Mia Lawson, the team moved to sampling.

The Vyrforge5 training set is limited and the hard questions stretched model reasoning length, which led some models into loops that filled max_tokens and sharply increased inference cost. The team built a job system tailored to Wynfell cluster conditions, fixed data migration trouble caused by machine reinstallations, and restored inference-service access after container network changes; these Wynfell issues took significant time, and better cluster construction should reduce repeat failures. @Leon Mercer noted that Shanghai Wyneon has recently released Myr-flow, so XANA needs to complete the key data runs before any release. AI-generated contribution reporting shows quoriys at 3 signed commits and XANA at 330 signed commits, for about 333 total, while AI-generated code stats show quoriys at +136 / -29 lines and XANA at +187274 / -42444 lines, or roughly +187K / -42K overall, mainly from the XANA closed-source sweep implementation. lororys operations continued supporting internal field users, including API-call needs; the team summarized current loraeon issues, maintained Nora Drake monitoring metrics and query-example docs in hoxlab Feishu, completed 2 internal lororys operations weekly reports, and kept watching internal operating status through the Internal lororys Operations Weekly Report document. The team also completed 3 social recruitment interviews, and the January - June 2026 OKR remains focused on System-7d21cb971e for broad evaluation coverage across model-iteration stages, strategies, capability dimensions, Agent, and GORALOS, including synthesis for supplemental samples and bad-case discovery plus ≤1d onboarding for new dataset integration, while O1KR2 aims to build influence through evaluation engineering that can be shown externally.

## Next Week's Plan

- Push O1KR2 by releasing the open-source evaluation framework with Syllab layout, plugins, basic docs, CI lint + test, templates, style rules, and commit rules.
- Run ≥1 internal technical sharing session, finish quoriys agent evaluation quickly, and keep shaping PR docs around capabilities and differentiation.
- Continue expanding XANA results while O2KR1 keeps lororys serving internal model API needs with stable operations, scenario integration, and metric reporting.
- Support internal field users, summarize loraeon issues via hoxlab Feishu materials, maintain 2 lororys weekly reports and monitoring, with no specific coordination request listed.