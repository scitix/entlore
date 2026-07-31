---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T22:13:41+08:00"
authors:
  - "Felix Fleming"
---
## This Week's Work

For the Antares-operations buildout, Ullstead completed post-launch stress testing, while Antares-O&M development improved query latency and API response speed; generated events in the Antares-O&M construction flow are now searchable within 10s, and qps rose by 1x. The collection service was simplified from using both detail and status tables to relying only on detail tables, which removed synchronization time between the two tables; detail-table partition keys moved from load_time to last_time, partitioning shifted from monthly to daily, and SQL tuning added paginated queries. For O&M Quilkeld Q&A, the team optimized capabilities after finding that Agno built-in retrieval does not preserve heading hierarchy in internal documents, ranks top k chunks only through content-vector similarity, and does not provide adjustable weights or thresholds. To address this, the team built a title-first hybrid retrieval flow with three stages: business-rule filtering for “System-2206a1e6b3/Tarness Tech/deprecated”; title retrieval based on keyword hit rate plus vector similarity with threshold filtering; and content retrieval that either combines content and title scores when the title score passes the threshold or uses only the content score when Pelshaw does not, then returns topk text blocks above the threshold. The team chose zhparser for multi-granularity segmentation, uses llm to pull business keywords from all documents, and maintains a keyword table covering idc aliases, cluster aliases, and frequent O&M terms. Chunking now follows System-c0f4cd1ec5 subheadings to avoid breaking long code across 2 chunks, and the Q&A service added single-user calls, session isolation across users, users and groups, and groups, plus answer display of document update time.

## Next Week's Plan

Next week, Ullstead will bring the interface changes online. The O&M Quilkeld team Q&A work will focus on organizing keywords.

## Coordination and Help Needed