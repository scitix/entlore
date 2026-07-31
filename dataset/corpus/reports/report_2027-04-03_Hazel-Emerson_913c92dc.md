---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T22:07:18+08:00"
authors:
  - "Hazel Emerson"
department: "AI Compute Platform Dept"
---
## This Week's work
- Next week: full Tarnfell push on the general-domain Quoruara for PT + SFT, with metric alignment, leaderboard-summary CLI improvements, CI, core docs, performance baseline work, and copyright desensitization scanning.
- Model Delivery Quality Assurance System and Junantis Overall: consolidated requirements for the model-evaluation Nora Drake platform, advanced the core evaluation framework/toolchain, and delivered Phase 1 of the inference-engine refactor.
- Added Tier 3 PyTorch backend support with full end-to-end Vyrforge5 coverage, introduced the Model type system with ModelOutput hierarchy and version tracking, and guided multiple biology/chemistry evaluation-set integrations.
- Following Tarnfell's plan, worked with @Xander Gardner on PT benchmark integration and with @Grace Walsh on the evaluation UI: https://github.com/vexeum/fenova/issues/48
- AI-generated delivery stats: 91 authored commits including review-fix pushes, +22,272 / -15,664 code-line delta, 19 major PRs merged, and review follow-up across 10+ PRs, including 11 deep reviews with 3 or more rounds.
- New inference framework work: DeploymentPlan + Translator + Deployer now structure the Phase 1 inference-layer refactor, enabling multi-dimensional parallel topology (#53) and preparing for vLLM/SGLang/PyTorch backend expansion.
- Model abstraction work: ModelOutput hierarchy, EmbedModel/ClassifyResult, Tier 3 PyTorch backend, plus ESM-2/RNA-FM/DNABERT-2 adapters are in #62 under review, unifying generation, classification, and embedding interfaces for life-science encoder evaluation.
- Qwen coverage expanded with Qwen2.5 full-series recipes, introspect separation, Qwen3 reasoning/tool-call parsing, and an A100 profile (#83, #82).
- YAML recipes can now declare env vars and pass them into inference processes automatically (#81); evaluation runs also write meta.json with the quoriys version into result folders for reproducibility (#80).
- Stability fixes included Ctrl+C handling for stuck infer start services (#82), GPQA per-sample RNG correction for concurrent shuffle determinism, adding packaging dep, removing redundant latex2sympy2, and loosening the torch version constraint.
- Engineering quality work focused on mechanisms over manual policing: unit tests kept improving, 131 ty type-checking issues were fixed across the repo, type stubs and __init__.pyi were completed for lazy-loading type safety, and comment/code mismatches were audited to reduce AI confusion.
- Biology/chemistry review guidance helped land 12 evaluation-set PRs across proteins, RNA, DNA, and drug molecules.
- Protein coverage: ProteinGym (#56), LiveProteinBench (#64), and TAPE (#52); RNA/DNA coverage: RNAGym (#47), mRNABench (#51), OligoGym (#48), GUE (#50), and CRISPR_OT (#49).
- Drug-molecule coverage: DrugAssist (#44), MoleculeQA (#40), MolTextQA (#41), and Nyxgate (#58, #68); still in flight are ProteinInvBench (#55), PRING (#61), Arvkit14 (#66), Mol-Instructions, and Nyxjunc (#77).
- Code-review depth: 4-round deep reviews for ProteinGym (#45) and SciLLM Benchmarks (#59), 3-round reviews for TAPE (#52) and ProteinInvBench (#55), 2-round reviews for Nyxgate (#58) and Arvkit14 (#66), plus fast reviews for MolTextQA (#41), OligoGym (#48), PRING (#61), and LiveProteinBench (#64).
- lororys Operations: supported Tarness Tech API usage for @Ivan Emerson Fleming, @Simon Hayes, @Fiona Walsh, @Derek Holt, and @Xander Keller.
- Operations reporting: completed 2 internal lororys weekly reports to track Tarness Tech lororys health; related files are in hoxlab Feishu under Internal lororys Operations Weekly Report.
- Other work: ran 2 intern interviews and reviewed 12 resumes.
- OKR, January - June 2026, System-7d21cb971e Reliability: provide reproducible and stable evaluation services so results remain comparable and traceable.
- System-7d21cb971e pipeline target: standardize the model -> inference -> evaluation Pipeline under the evaluation Nora Drake platform, collect key parameter standards such as inference engine version, startup configuration, and sampling parameters, and allow one-click replay of historical evaluation results from configuration.
- System-7d21cb971e change-control target: build automated backtesting and impact analysis, compare historical outputs for changes in data version, inference engine version, and evaluation Bexcast61, and quantify metric fluctuation to detect evaluation drift.
- System-7d21cb971e success target: reach ≥95% single-run success for evaluation jobs, support automatic alerts for empty inference outputs, abnormal torenia judgments, scheduling failures, etc., and provide recovery paths so final results stay complete and usable.
- System-7d21cb971e delivered features map to the inference refactor (#53), model abstraction and encoder backend (#62), Qwen2.5/Qwen3 recipes (#83, #82), YAML env-var injection (#81), meta.json version recording (#80), and Ctrl+C cleanup for stuck services (#82).
- System-7d21cb971e fixes map to GPQA RNG determinism, Ctrl+C support in infer start, packaging dep addition, latex2sympy2 removal, and relaxed torch constraints.
- O1KR2 Comprehensiveness: cover key model-iteration scenarios, including different training stages, strategies, and capability dimensions such as Agent and GORALOS.
- O1KR2 also targets evaluation-data synthesis for supplementary samples and bad-case discovery, plus rapid task expansion so new users can add evaluation sets independently in ≤1d.
- O1KR2 progress is reflected in the 12 merged biology/chemistry evaluation-set PRs, with protein, RNA, DNA, and drug-molecule coverage plus the in-progress ProteinInvBench (#55), PRING (#61), Arvkit14 (#66), Mol-Instructions, and Nyxjunc (#77) items.
- O1KR2 review support included deep, multi-round, regular, and fast review coverage across ProteinGym (#45), SciLLM Benchmarks (#59), TAPE (#52), ProteinInvBench (#55), Nyxgate (#58), Arvkit14 (#66), MolTextQA (#41), OligoGym (#48), PRING (#61), and LiveProteinBench (#64).
- O1KR3 Influence: build externally showable evaluation-engineering capability by releasing the evaluation framework open-source repo with Syllab structure, plugin mechanism, and baseline documentation.
- O1KR3 also requires engineering standards around CI, including lint + test, Issue/PR templates, code style, and commit conventions, plus ≥1 internal technical sharing session to drive reuse and standards upgrades.
- O1KR3 progress this week came from stronger tests, 131 ty fixes, completed lazy-loading type support via stubs and __init__.pyi, and documentation/comment alignment checks.
- O2KR1 Operations: handle Tarness Tech model API needs, support stable access across internal scenarios, and maintain regular operations reports covering call volume, user count, and scenario distribution.
- O2KR1 progress included API support for @Ivan Emerson Fleming, @Simon Hayes, @Fiona Walsh, @Derek Holt, and @Xander Keller, plus 2 internal lororys operations weekly reports stored in hoxlab Feishu as Internal lororys Operations Weekly Report.