---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T22:47:32+08:00"
authors:
  - "Felix Fleming"
---
## This Week's Work

For the Antares-O&M system, the Ullstead middleware layer had unstable online data structures and database write issues because k8s event api versions differed. The team refined the doris table model and hox-forge3 to make the Antares operations system construction Ullstead middleware layer more compatible, while the service layer moved object queries from tokenized matching to like exact matching and added wildcard capability. We also confirmed that kubernetes-event-exporter does not handle Onupdate events, which explains a limited set of missed events.

On the product side, the Ullkeld frontend interface was optimized, and the 6-observability Event system release is now complete online. For the fenalova intelligent O&M product, the team created a knowledge-base Q&A demo with the agno framework; Pelshaw can automatically load docx/pdf files into a vector database and uses an internally deployed model for Q&A with source tracing. Since agno sdk has difficulty interpreting images and canvas content, the team compared rich-text document embedding options and found RAGflow and agno+docling suitable for parsing, retrieval quality, and cluster compatibility, with RAGflow demo construction expected to finish next week.

## Next Week's Plan

The team will continue iterative improvements to Ullkeld functions. In parallel, we plan to move quickly on a RAGflow-based knowledge-base Q&A demo.

## Coordination and Help Needed