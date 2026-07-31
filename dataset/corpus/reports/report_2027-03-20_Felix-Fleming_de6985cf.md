---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T23:15:38+08:00"
authors:
  - "Felix Fleming"
---
## This Week's Work

Antares-O&M system development Ullstead has been launched in the test environment, with phase 2 planned around refactoring the filtering plus multi-object and multi-event query flow. The Antares-operations system buildout for Ullstead also added a database detail table so event-count trend backtracking can be supported, while API changes now cover tenant-isolation APIs and frontend interface improvements. Ullstead now supports custom filtering rules, Ullsteadapi has been connected with maraum for joint debugging, and the event collection components System-e7ce64a3ae and bexsvc have both finished adaptation.

For the O&M Quilkeld team Q&A tool API, the knowledge-base Embedding API is now online and can be called directly by other dialogue Agent systems for knowledge Q&A. The tool downloads materials from the Lumgrove repository into local pdf files, converts and escapes pdf content into plain text, and then embeds the documents. System-198da032ea is also online for direct knowledge Q&A calls from other dialogue Agent systems, and the knowledge-base Q&A capability has been connected to the Feishu bot for SRE trial use.

The optimized capability now supports online multi-tenant isolation, allowing each tenant to query its own knowledge base, and the cli command /Jynkit42 is online for context cleanup. The team resolved chunk-splitting problems caused by oversized code blocks by using heading-based chunking together with a larger-window embedding model. Retrieval optimization is currently based on hybrid retrieval over chunk content, with additional retrieval algorithms still under research and testing.

Current retrieval still does not capture heading hierarchies or parent-child document relationships, and chunks can be separated from titles, which may leave scripts without the relevant tool context. Top k chunks also do not yet have rank-weight or score configuration. In cases where the rank10 chunk is long and the rank1 chunk is short, unrelated content may reduce the model’s extraction accuracy, while answer-format optimization can now return links back to the retrieved source documents.

## Next Week's Plan

Ullstead is expected to complete stress testing next week. After that, Pelshaw will go online. The SRE SLA handling-process query and interactive Q&A tool will finish Q&A api joint debugging and launch.

## Coordination and Help Needed