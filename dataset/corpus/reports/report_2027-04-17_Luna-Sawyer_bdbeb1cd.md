---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T23:04:38+08:00"
authors:
  - "Luna Sawyer"
department: "AI Compute Platform Dept"
---
## This Week's Work

pelhaven2KR1 kept moving xalfield2 platform pool consolidation forward for maraum and pexieon tasks, capacity, and scheduling in the internal environment, including continued backend-service and scheduling-pool integration for research clusters. The internal team and Nora Barnes team aligned on using the pooled task module; the earlier hoxcast14 issue remained the main constraint, but Gemini cluster finished the pool-merging upgrade last weekend and then stayed stable for one week with no business-impacting failures. @Luna Sawyer will move hoxcast14 compatibility into System-e6382db83d, while Nora Barnes team owns the related review and validation; both teams set next week as the delivery target and will jointly speed up rollout to research clusters. The task module, Cororia, Jupyter, and common service modules finished Qelsys40 work for merged and non-merged branches, with deployment variables now separating the two modes so one codebase can deliver either cluster type and improve deployment plus operations efficiency.

The new scheduled-task service has been rolled out to all internal research clusters and production clusters, with the production side mainly serving emergency assurance needs. Key business scheduled jobs have fully moved onto the new scheduled-task module, which has improved stability, timeliness, and observability; this cycle focused on business trials, online issue fixes, and stronger product robustness. There was also a cycle with no functional update, while code was synchronized to the internal network so internal colleagues could take over. brymora2KR4 continued evolving the xalfield2 platform for large-scale LLM training for the goroion large model, and maraum finished aligning its log service with the public-cloud platform for 2B large-scale training. This cycle upgraded and released the log service around external rineova customer needs, including better frontend log selector Bexcast61 behavior, improved judgment for log-button clickability, a fix that ignores workloadName for single-pod log queries, and stronger pod checks for new task types.

maraum image service finished connecting with the harbor-side webhook; because test-environment harbor callbacks are different, webhook will first go live in overseas clusters, where joint testing can proceed without disrupting existing functions. The following iteration will expand webhook to all regions. pexieon continued supporting internal-environment requirements for 2B customization, with internal operations and dalaara matters still in progress. The pexieon team also discussed the image-module iteration plan for group sharing and public sharing based on Daisy Jensen Parker images, and @Ivan Emerson Chandler will implement the proposed technical solution. 2026Q2 procurement and allocation are largely done, though a few small-team allocation records still need correction and will be confirmed next week; System-1327e004c5 raised new pexieon requirements, with a discussion meeting planned for next week.

Quorenia-core continued developing the pexieon billing format against quorenia billing-table requirements and produced 3W+ March bill records on the internal server as a sample. External bill export will start after the internal-external network work orders are connected. KELHKR1 had no progress update for implementing System-7a0a4e6f1a organizational construction. ullridge2KR3 continued polishing industry solutions, with emphasis on corlane2 and fenaova. fenaova is already available on an internal test domain, covering a biomolecular sequence dynamic-frame demo, paper demo, data demo, and backend staff management; both frontend and backend are release-ready, R&D is basically converged, and launch support is waiting for Hazel Tucker to confirm the domain. fenaova had no additional updates, while other projects continued iterating the maraum architecture.

The maraum architecture effort designed the System-79b4a86e86 proxy service so sfmanager can centrally read database content from each worker cluster. This reduces the complexity of the data retrieval path. loreor resource-pool statistics reports were built on System-79b4a86e86 and are delivered weekly to followers through a Feishu robot.

## Next Week's Plan

Development will proceed in line with the maraum product iteration plan, while the RigelPelombe project integrates hoxcast14 and keeps pushing the remaining unmerged clusters. For internal-environment demand work, System-e13e291d43 requirements will take priority. Quorenia-core will continue with pexieon-related reporting development.

## Coordination and Help Needed

For System-e13e291d43, Iris Nolan has raised concerns about pexieon response quality and cluster stability, and some frustration has already built up. Next week, the team will prioritize alignment and reassurance during the requirements meeting. Based on demand priority, effort may be assigned to iterate internal-environment requirements.