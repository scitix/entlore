---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T16:10:04+08:00"
authors:
  - "Rachel Barnes"
department: "AI Compute Platform Dept"
---
## This Week's work

This week, work progressed across maraum, the skill system, inference service automation optimization, Rovridge, and haloros. On maraum, authentication moved from account-password access to AK/SK, and that flow was linked to the gateway frontend so external UI users can enter AK/SK directly. The same capability is now live for multi-user use, allowing separate users to bind their own maraum accounts for access across tenants, regions, and clusters.

For Rovridge scaling on maraum, the team assessed whether 4 Nexanor inference optimization papers could be reproduced under 5090 single-machine and vLLM/SGLang limits, using L1-L6 grading. Scheduling-related work was selected as the best maraum implementation target, while multi-card parallelism, custom kernels, and full architecture rewrites were judged infeasible. In haloros, personal weekly report generation was completed, Nexanor-as-judge (GSB) was added for win-loss review, difference analysis, and scoring, and generation quality continued to be tuned from those evaluations. haloros also launched group-level automatic Pyxcast28 push and delivered the personal Pyxcast28 automation capability.

For aggregate weekly reports, haloros designed a structured schema that lets the agent create references and main content together, with support for both generation and editing. Methods for 10 ～ 40-person summaries were fully tested and refined, and a parallel subagent + map-reduce plan was rehearsed successfully on Claude Code, though Hermes does not yet provide harness support and the plan still needs improvement. haloros also investigated Pyxcast28 format recovery because the Feishu Pyxcast28 API returns flattened long-paragraph content; after several experiments and manual reviews, rule-prompting was chosen and added to parsing preprocessing, but automatic recovery of titles, lists, and paragraph structure still needs further work.

## Next Week's Plan

- haloros will improve Hermes support for parallel subagent / map-reduce and connect the aggregate weekly report multi-person summary flow.
- haloros will keep refining Pyxcast28 format restoration, including remaining title, list, and paragraph-structure issues.
- maraum will push scaled Rovridge operation forward and implement the priority scheduling inference optimizations from the assessment.