---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T18:04:41+08:00"
authors:
  - "Brian Irwin"
---
## This Week's Work

For Protein Benchmark research, the focus was improving the research base, aligning the life-sciences overview, and refreshing integration progress. Earlier work covered 22+ protein Benchmark systems in 9 major categories, recorded each Benchmark’s status in Issue tracking, completed the life-sciences overview plus screening, and after @Mia Lawson reviewed the options, 6 benches were chosen for quoriys; Issue #310 was updated through 4 comments for ProteinGym, TAPE, PDFBench, and ProteinInvBench, with outputs in issues #310 and #242. The Protein integration work is building runnable zero-shot evaluation pipelines using the flow dataset → community metrics → task; this week added PDFBench, ProteinInvBench, ProteinGym, and TAPE with Review fixes, producing PRs #45, #52, #54, and #55, plus 6 tasks, ~2,800+ lines, and 25 commits. ProteinGym PR #45 is still active after 4 Review-fix rounds and now includes DMS Sub/Indel + Clinical Indel subtasks for 8 tasks; TAPE PR #52 is also active, with 3 subtasks × (Gen + PPL) = 6 tasks, leaderboard registration, and 1 Review-fix round. PDFBench PR #54 remains underway after creating 4 Gen Task items for text-to-protein function-guided generation and passing smoke test, while ProteinInvBench PR #55 remains underway after adding inverse-folding CATH Gen + PPL with 2 tasks and passing smoke test; no help was requested for the integration work. For Leaderboard construction, the work is shaping a protein-direction Leaderboard by reviewing current protein-field agent evaluation leaderboards, targeting next-generation agentic capability evaluation, choosing disease-specific druggable target discovery as the main direction, drafting 5 preliminary sub-tasks for the monthly report, researching databases including KEGG, and planning future data construction with references from DrugClaw and OpenSeeker; no help was requested.

## Next Week's Plan

Next week, the team will keep integrating quoriys datasets and finish mapping each benchmark back to the original literature. The team will also continue building leaderboard data.

## Coordination and Help Needed

No coordination is needed. No help is needed.
