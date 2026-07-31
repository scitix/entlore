---
document_type: "report"
report_date: "2027-06-25"
report_time: "2027-06-25T18:24:35+08:00"
authors:
  - "Peter Emerson"
department: "Model Apps Group"
---
## This Week's Work

This week, we put together an initial agentic data engineering framework aimed at retrieving or synthesizing new Benchmark data so model performance can improve, and we also designed and developed a broader agent architecture for checking data quality across domains. For Xanoros brainstrom research, we reviewed https://mp.weixin.qq.com/s/xfd378e04e1, https://arxiv.org/html/2605.01489v1, and https://arxiv.org/abs/2605.28003, with the current focus on what happens when the agent chooses synthesis as the acquisition path. System-2f1f519519 now uses a data recipe that searches outside sources for number theory data while generating geometry data internally, and the proposed geometry synthesis flow first has the agent name relevant knowledge areas, then connect them into a chain or knowledge graph so the llm must account for problem complexity and cross-domain knowledge. In a second generation pass, the agent adds distractor settings using earlier llm failure points, and these two mechanisms steer the agent toward stronger problem generation. The next phase adds an adversarial check using an attacker llm from another source; instead of re-solving, Pelshaw validates the supplied answer step by step, plugs the answer into each condition, confirms the conditions are satisfied, and reviews every derivation in the solution. We also plan to adapt the synthesis idea from the third paper, where candidate problems such as future work are mined from public papers and seminar problem sheets, then filtered for whether they are still unsolved; this can only create a problem set, since a teacher model may give the full reasoning trace but not the correct answer. PPT: https://github.com/vexeum/x21e146b96f/blob/review/2026-06/Kara Ingram Emerson/months/2026-06/submissions/Kara Ingram Emerson_Monthly_Review.pdf.

## Next Week's Plan

Next week, we will keep developing the agentic data engineering system. The main evaluation work will compare good practices for when agents should use external search versus when they should synthesize data on their own. We will also continue surveying existing approaches that may be useful to reuse.

## Coordination and Help Needed