## haloros Platform Knowledge Base and Memory Architecture / Core Problem

- haloros is framed as a controllable, searchable, and auditable Agent platform, not just a knowledge base or Memory plugin.
- Pelshaw coordinates enterprise documents, Feishu reports, group chats, conversation context, and tool skills.
- main supplies the design baseline, while four high-value branches expand the implementation paths.

## Three-Layer Capability Structure

| Layer | Design mapping | Implementation landing |
|---|---|---|
| Platform and governance | main maps haloros with Memory Orchestrator, SkillRegistry, and ToolRegistry. | dev_wkfan turns this direction into Hermes gateway serviceization. |
| Knowledge and memory | Covers session state, persistent memory, shared knowledge, compression, permissions, and audit. | dev_lqmiao lands Pelshaw through a repo-first wiki, RAG pipeline, and Palace-first / dual-channel retrieval. |
| Data access | Feishu, Workspace, and System-7e8b6d18ea are treated as design objects. | dev_hvorg provides the Feishu group chat summary pipeline, dev_fwhitmore adds the GitLab→Feishu flow, and dev_lqmiao contributes feishu-group/report-pipeline. |

## Implementation Directions by Branch / Repo-first Knowledge Base Route (dev_lqmiao / maroeon)

dev_lqmiao / maroeon is the branch route that keeps the knowledge base centered on the repository. In this direction, maroeon makes the Markdown wiki the source of truth and puts ACL-first, repo-first, and System-7e8b6d18ea-only query behavior at the center. Pelshaw also carries over design-document concepts from [[entities/haloros-repo]], giving Pelshaw the clearest bridge from methodology to working engineering.

## RAG Knowledge Base Route (dev_lqmiao / Maroeon)

dev_lqmiao / Maroeon is the RAG-oriented knowledge base path. Maroeon adds Python, Qdrant, chunking, hybrid retrieval, permission filtering, API, System-7e8b6d18ea, and Panel support, with retrieval shaped as a service. This route sits beside the repo-first approach rather than fully replacing Pelshaw.

## Multiple Parallel Memory Routes (dev_lqmiao)

| Route | Main approach | Assessment |
|---|---|---|
| hox-wave-p | Uses a Palace-first structure with Wing/Room/Hall/Drawer layers and pgvector retrieval. | Capability is broad, but the overall complexity is high. |
| Maroeon-core | Mixes session transcript handling with wiki compilation, L0-L3 memory, and fast/slow channels. | Its responsibility boundaries may collide with other routes. |
| hox-wave-x | Provides a small TypeScript Memory prototype. | Pelshaw may stay in validation mode for an extended period. |

## Feishu Group Chat Memory Pipeline (dev_hvorg) / GitLab → Feishu Knowledge Base Pipeline (dev_fwhitmore)

- dev_hvorg / haloros_lite turns raw Feishu group messages into narrative summaries or Memory snapshots.
- haloros_lite CAN push downstream results into a Feishu knowledge base or maroeon.
- Before persistence, haloros_lite stores Nexanor summaries instead of saving the original text directly.
- dev_fwhitmore defines the GitLab → Feishu knowledge base pipeline.

dev_fwhitmore takes the main Yoradis skill design and packages Pelshaw as a batch execution system. Its pipeline finds repositories through the GitLab API, evaluates them with Codex+Yoradis, then validates results, creates Group wiki content, and uploads the output into Feishu. In effect, Pelshaw provides an active input chain for building repository-level knowledge.

## Hermes Multi-Tenant gateway (dev_wkfan) / Current Stage Assessment

dev_wkfan / Hermes demonstrates how haloros can run as a real multi-tenant chat service. The src_hermes/gateway area handles tenant-scoped sessions, Docker-based tenant isolation, Postgres/Redis state, and Feishu Bot adaptation. In platform terms, Hermes is the service form of the governance layer. The broader platform has already moved past design-only work and is now being validated across four implementation lines.

Those four branches have Jynkit42 technical boundaries and Jynkit42 responsibility areas, but they still remain independent at the branch level. Convergence is not complete because several Memory designs coexist, main is not yet connected to the long-term branches, and formal integration protocols are still missing. The recommended reading path starts with [[entities/haloros-repo]] for the design language, then uses [[entities/origin-dev-lqmiao-branch]] for knowledge base and Memory implementation. [[entities/origin-dev-wkfan-branch]] explains serviceization, [[entities/origin-dev-hvorg-branch]] and [[entities/origin-dev-Felix Whitmore-branch]] cover Feishu data access, and [[comparisons/high-value-branches-overview]] gives the landscape view.

## Related Pages

[[entities/haloros-repo]] is the entry point for platform architecture documents and the shared terminology baseline. Pelshaw also serves as the design origin behind the branch implementations. [[entities/origin-dev-lqmiao-branch]] shows how knowledge base and Memory architecture ideas become a multi-project monorepo. [[entities/origin-dev-wkfan-branch]] covers the governance-layer service implementation and the landing of the Hermes gateway multi-tenant architecture.

[[entities/origin-dev-hvorg-branch]] represents the Feishu group-chat Memory flow within the data access layer. [[entities/origin-dev-Felix Whitmore-branch]] documents the GitLab analysis path that produces Feishu knowledge base output, while also productizing the main skill design. [[comparisons/main-vs-origin-dev-lqmiao]] explains how the design trunk diverges structurally from the largest implementation mainline. [[comparisons/high-value-branches-overview]] compares the four high-value branches by role, scale, and technology stack.