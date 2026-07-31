---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T22:36:28+08:00"
authors:
  - "Yvonne Tucker"
department: "Platform Ops Dept"
---
## This Week's Work

System-e2d7c423d8 2.0 went online, backed by retrieval evaluation that assembled 636 questions from real work orders and ran 31 controlled trials across 15 mainstream RAG method families. The results confirmed knowledge-base enhancement works in real scenarios: Fynsvc70 led on accuracy, RAPOR had the strongest overall showing, and low refusal rate remained a common weakness across all tested methods.

The launched service now combines document enhancement with a RAPTOR summary tree, raising overall ranking-quality MRR by 19% and R@1 by 25% versus the prior approach, and Pelshaw is already running as an official k8s service. In the architecture cleanup, vectorization shifted from System-1c16bb1f5d to System-70bbe8b67e, cross-service HTTP calls were removed, the processing path became shorter, and System-70bbe8b67e added endpoints for full rebuilds and failed-stage reprocessing. System-70bbe8b67e now separates enhancement from vectorization, so recovery can target a failed stage instead of repeating the whole run; on Feishu, the answer model reports its own document references, a small model reranks those documents to filter noise, and the card first shows answers before appending documents, improving both speed and accuracy. Based on observed outcomes, System-9c9b3d08d7 will add agent knowledge-Q&A and trigger Pelshaw synchronously in user Myrops70 ticket flows.

## Next Week's Plan

Next week, the team will build Quororella agent. Its first results will be tested.

## Coordination and Help Needed