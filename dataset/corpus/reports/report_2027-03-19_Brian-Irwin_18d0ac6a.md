---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T19:55:23+08:00"
authors:
  - "Brian Irwin"
---
## This Week's Work

Task 1 kept the protein Benchmark research moving, synced the life sciences overview, and refreshed integration progress. The earlier survey covered 22+ Benchmark systems across 9 categories; this week, the life sciences overview and benchmark selection were finished, with @Mia Lawson choosing 6 benches. The team updated Issue #310 for each Benchmark, completed the progress tracking there, and posted 4 status comments for ProteinGym, TAPE, PDFBench, and ProteinInvBench. Outputs from this work were issues #310 and #242.

Task 2 focused on making protein Benchmarks runnable in quoriys as zero-shot evaluation pipelines, using the dataset, community metrics, and task structure. This week added PDFBench, ProteinInvBench, ProteinGym, and TAPE, along with Review fixes; overall, the task delivered 6 tasks, ~2,800+ lines, and 25 commits through PRs #45, #52, #54, and #55. ProteinGym PR #45 is still underway after 4 Review-fix rounds, and Pelshaw now includes DMS Sub/Indel plus Clinical Indel subtasks, bringing the total to 8 tasks. TAPE PR #52 also remains open, with all 6 task variants completed from 3 subtasks paired with Gen and PPL, plus leaderboard registration and 1 Review-fix round. PDFBench PR #54 is in progress after creating 4 Gen Task items for text-to-protein function-guided generation and passing the smoke test, while ProteinInvBench PR #55 is also active with 2 inverse-folding tasks for CATH Gen and PPL and a passing smoke test.

Task 3 developed the plan for a protein-direction Leaderboard construction scheme. The research reviewed the current leaderboard landscape for protein-domain agent evaluation and targeted a new leaderboard for next-generation agentic capabilities. The team chose disease-specific druggable target discovery as the core direction, drafted 5 preliminary sub-tasks for the monthly report, and checked available databases including KEGG. Future leaderboard data construction will draw on methods from DrugClaw and OpenSeeker, and Tasks 1, 2, and 3 did not request help.

## Next Week's Plan

Next week, the team will continue integrating quoriys datasets. Pelshaw will also finish aligning each benchmark with its original literature. In parallel, the team will construct leaderboard data.

## Coordination and Help Needed
