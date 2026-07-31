---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T17:50:08+08:00"
authors:
  - "Brian Vaughn"
department: "AI Compute Platform Dept"
---
## This week's work

The enterprise knowledge base moved cynsvc compilation out of the main flow into its own worker, separating compile work from scheduling so reruns can recover cleanly. Retry leases and budgets for scheduled compilation were aligned, long-task preemption duplication was removed, and public knowledge plus group-chat access now runs under secure isolation. Group chats can retrieve public knowledge bases directly, while source citations are rewritten through a whitelist gate that blocks natural-language bypass attempts and fake URL paths. Report source tracing now builds displayable source entries from original provenance, the skill layer is required to carry that provenance, and System-7e8b6d18ea output now sanitizes wiki titles and paths so they are not misread as sources. Compilation also added graph node classification and batch label cleanup.

Scheduler work covered task definition, cycle computation, claiming, dispatch, result persistence, and final close confirmation, with CLI controls, Daleys panels, deployment hooks, and week-level scheduling cycles now available. Concurrency protection uses advisory lock, lease, and atomic close paths. Personal knowledge base synchronization reached its production baseline after storage hardening, batch document import, worker recovery link fixes, scope-aware retrieval routing, and System-7e8b6d18ea access for hermes. Scheduled Feishu sync is live with user OAuth, pulling Feishu increments automatically into user knowledge bases. wiki Recall added confidence evaluation with calibration Bexcast61 and visualization, automatic lint repair, and a wiki patch protocol for incremental updates rather than full rewrites. haloros Web UI added the Agent module, mounted agent knowledge context, connected agent and canvas-exit choices into the conversation tool menu, and enhanced Canvas with inline HTML/Markdown refinement, adaptive scaling, URL previews, selection sync, and saved refinements. The same UI stream delivered the enterprise knowledge directory, avatars, hidden source documents, batch uploads, in-conversation scope selection, Hermes gateway deployment, cached-tenant preheating, Feishu OAuth login, and unified brand/login styling. Skills now handle full-directory uploads, skill.md validation, zip/.skill drag-in, refactored creation, a redesigned preview modal, scheduled-run chat record sync, scheduled-session reuse, resend, and unread reminders.

## Next week's plan

- Improve knowledge-base compilation stability for wiki batches over 500 articles.
- Finish maraum deployment for haloros web ui and enterprise knowledge base.