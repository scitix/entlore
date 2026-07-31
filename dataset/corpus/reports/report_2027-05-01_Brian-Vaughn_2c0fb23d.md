---
document_type: "report"
report_date: "2027-05-01"
report_time: "2027-05-01T11:02:58+08:00"
authors:
  - "Brian Vaughn"
department: "AI Compute Platform Dept"
---
## This Week's Work

This week, we finished the enterprise Agent knowledge base wiki-mode implementation and upgraded the System-7e8b6d18ea service plus Hermes multi-Agent integration from stdio to Streamable HTTP System-7e8b6d18ea service, with health probes, structured logging, and operations endpoints added. The gateway now requires X-maroeon-User-Id to take precedence over permission.userId, moving identity injection out of the Agents; Hermes multi Agents can stay resident while reusing one shared service. Feishu Report synchronization is now connected with organization-level permission diffusion: sync-feishu-report was introduced as a biweekly window sync path, raw data is stored by period, and cynsvc turns Raw data into wiki pages for people, teams, and periods. Report access no longer depends on the knowledge base member list, instead projecting open_id as viewer and extending visibility through departments; same-department people pages remain visible only at the current department layer and no longer spread through the graph, avoiding cross-department exposure through collaboration links.

We also completed the Dovflow migration, Docker deployment, and real-scenario integration work: the maroeon compile/enrich flow moved to Dovflow, the batch compilation route was removed, gate tightening now prunes outdated wiki pages automatically, maroeon was containerized and placed on a virtual machine, and Hermes now supports end-to-end retrieval against the live Feishu knowledge base and Report data. For the Agent cross-session memory System-32a5d7f7fb effort, we iterated the solution and built System-85bab75206 from the ground up around a 4-layer Wiki model centered on wiki documents, where the promotion pipeline carries L0 raw session data into L1 episodic, L2 semantic, and L3 procedural layers. Retrieval is now divided into fast and slow paths: the fast side uses recent N sessions with a recency boost, while the slow side uses wiki RRF multi-route Qelsys40; compilation runs through plan, torenia, and apply stages, with torenia relying on cynsvc and the System-00f1b6ccd5 skill. LLM tokens are consumed only during compilation, while retrieval remains fully keyword-based; Hermes integration and the System-7e8b6d18ea query path are complete, Dormarch and the content sanitizer are done, the host agent records session lifecycle and turns only via hooks, and memory lookup is limited to System-7e8b6d18ea APIs including search, get_page, get_session, and status. We separated write and read paths to reduce prompt-injection coupling during hooks, completed production hardening, made the debugging panel usable, added advisory lock and retry for safe serial compilation, improved the wiki linter and graph expansion, enabled user-scoped multi-tenant storage with dashboard switching, rebuilt Dashboard UI/UX v2, brought Overview, Sessions, Wiki, Maintenance, and Health to daily usable quality, completed the Dovflow abstraction with CLI and SDK switching for the compile pipeline, and built a vexeum new-employee onboarding skill on maroeon.

The onboarding skill runs through welcome, profile completion, concurrent wiki retrieval, and rolling onboarding context package maintenance, while keeping only very stable facts hardcoded. All other knowledge goes through maroeon System-7e8b6d18ea, making the skill an enterprise POC scenario for maroeon; the Feishu bot also now replies with emoji while waiting.

## Next Week's Plan

Next week, the Agent wiki knowledge base will add raw file reference capability. The Agent cross-session memory module will continue with further optimization and iteration.

## Needs Coordination and Help