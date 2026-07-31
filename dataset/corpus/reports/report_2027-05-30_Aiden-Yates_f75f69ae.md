---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T22:59:37+08:00"
authors:
  - "Aiden Yates"
department: "Model Apps Group"
---
## This Week's Work

This week’s implementation moved from research into building and refining the QA data generation pipeline on PrimeKG. Subgraph extraction was changed from open-ended BFS to a meta-path-driven approach, with dozens of clinically relevant patterns defined in advance, such as disease→gene→drug and drug→target→pathway. Each step now checks node categories and relation categories, so the resulting subgraphs are cleaner than the earlier random-neighborhood outputs.

The updated subgraph.py and pipeline.py can select meta-paths by name, length, and semantic label, and they also remove non-direct causal relation edges. The pipeline now completes an end-to-end run and produces data with reasonable structure. However, quality is still only moderate because a single LLM call is responsible for both question creation and reasoning-chain generation without an added validation step, leaving question quality and reasoning depth at an average level.

## Next Week's Plan

Next week’s focus is to improve pipeline quality rather than just structure. The first optimization direction is an agent-style adversarial loop that separates generation, critique, and revision to make the questions and reasoning chains more reliable. The second direction is to connect paper retrieval so graph edges can be enriched with literature-backed evidence and mechanism descriptions.

## Coordination and Help Needed