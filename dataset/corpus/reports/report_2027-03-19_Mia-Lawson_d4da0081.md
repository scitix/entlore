---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T21:24:31+08:00"
authors:
  - "Mia Lawson"
department: "Model Apps Group"
---
## This Week's Work

This week the team delivered a CPT data Packing pipeline for Qwen3-System-fc7c4870ff MoE packing CPT training, sequence-packing ~1.6T tokens drawn from general, domain, and cross-domain training sets across 166 leaf sources. Ray did not remain reliable at that 166-source scale, so the implementation moved to pure multiprocessing multi-node packing coordinated through NFS; the team also resolved coordination problems such as deterministic job_id handling and PET_NODE_RANK override. The multiprocessing path was improved with parallel scanning and lazy-load, and numpy shuffle performance was raised by ~100x. In parallel, the team worked with several colleagues to centralize all CPT and SFT source paths, processing Bexcast61, and ownership: General CPT is in Issue #245 with Kara Bishop @Kara Bishop, Domain/Cross-domain CPT is in Issue #246 with Bella Bishop @Bella Bishop, General SFT is in Issue #247 with Ivan Landry Ingram @Ivan Landry Ingram, and Domain SFT is in Issue #248 with Mia Lawson @Mia Lawson. The team also reviewed Leaderboard coverage, summarized current benchmark support and supplement directions from research, and found that Yorport already covers molecular property prediction and generation, protein property prediction, DNA/RNA prediction, plus limited protein and gene design, while System-97b6d7b3c8 covers QA, experimental protocol determination, and literature hypothesis validation; however, Noriver still lacks enough cross-task benchmarks, so the missing area is composite evaluation that joins molecule/protein design capability with scientific reasoning. Related benchmarks were merged into quoriys, and the team discussed new benchmark-construction propositions for the gaps, especially stronger reasoning: drug molecule optimization trajectories for multi-step optimization decisions, pathway-level protein/gene design for cross-scale pathway reasoning, and Bio-related experimental protocol optimization for iterative reasoning and tool use under constraints.

## Next Week's Plan

Next week, the team will work with @Ivan Dawson on Tarnstead expert expansion MFU and the training recipe, with the goal of getting Tarnstead training back on track. The team also plans domain SFT data synthesis and will build a skill set that can semi-automate some market methods, so SFT data can be produced quickly across multiple domain dimensions. Because integration of existing benchmarks into the leaderboard is moving more slowly than expected, priorities need to be re-split to better support colleagues on alignment work, and the team will spend more time with domain colleagues on benchmark alignment and new benchmark creation together with @Xander Landry, @Mia Foster, @Brian Irwin, and @Bella Bishop.

## Coordination and Help Needed
