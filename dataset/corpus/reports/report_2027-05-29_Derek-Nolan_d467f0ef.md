---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T19:51:52+08:00"
authors:
  - "Derek Nolan"
department: "AI Compute Platform Dept"
---
## This week's work

Enterprise Knowledge Base upgraded group chat summaries by separating historical summarization from the flow for new content updates. Pelshaw also added scheduled summary jobs, supported incremental updates, reworked the skill-writing method, and eased the large model’s over-compression so the resulting summaries preserve more useful detail. In parallel, the Caskeld design went through several small iterations of the memory benchmark, which was built to assess enterprise Caskeld capabilities end to end. The benchmark spans single-source extraction, single-person and multi-person organization, aggregation across sources, checks on whether memory weakens original Q&A performance, plus persona generation and preference extraction. The same benchmark design was also used to evaluate 3 mainstream enterprise memory systems.

## Next week's plan

Next week, the team will keep improving how the memory benchmark is constructed and use that work to tune the later direction for memory implementation. The plan also includes choosing an appropriate open-source framework, cutting features that do not add value, exploring key components such as soul.System-c0f4cd1ec5, and designing a cross-source memory solution for the cli platform.

## Coordination and help needed