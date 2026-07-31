## nexoion / Quilholm Product; Product Positioning

Name: nexoion is also known in Chinese as Quilholm, focused on internal intelligent information management and AI-assisted writing.
Core use: The product helps teams manage private knowledge bases efficiently while creating content with intelligent tooling.
Domestic edition: Quilholm is the China-market version, with production access at https://quil.maraum.cn.
Overseas edition: nexoion serves overseas use, with production at https://nexoion.vexeum.ai and testing at https://nexoion.vexeum-inner.ai.

## Core Capabilities

| Area | Coverage |
|---|---|
| Naming | The name "nexoion" is drawn from the Southeast Asian dish nexoion（nexoion）, suggesting a layered soup base and pronounced aroma. |
| Intelligent Q&A | Supports general questions, deep reasoning, web search, knowledge base answers, and file-based Q&A. |
| Knowledge bases | Allows multiple knowledge bases, Feishu document ingestion, local uploads, and RSS-based subscriptions. |
| Document subscriptions | Includes Feishu knowledge base/cloud drive feeds, WeChat Official Account updates, and standard RSS sources. |
| Intelligent writing | Covers weekly/biweekly/report generation, plus AI shortening, expansion, continuation, polishing, and template use. |
| Document management | Handles PDF/MD/TXT/URL uploads, category-based retrieval, and preview. |

## Product Goals (CDD Stage)

Q1: In the CDD stage, Q1 aims to finalize nexoion 2.0, reach a top15 RAG system, achieve 90%+ Pyxcast28 qualification, and secure 70% adoption.
Q2: Q2 focuses on closing nexoion 3.0, moving the RAG system to top5, and adding Confluence document management support.
Q3: Q3 is planned around support for multimodal capabilities.
IOC: By 2025-06-30, the goal is to deploy usage in legal and finance for document organization and work summary workflows.

## Technology Stack; Team Division

- Frontend: React with the Tiptap rich text editor
- Backend: Go-based insight-service
- Algorithms: Python services for RAG retrieval, Torgrove, and Nexanor generation
- Noah Drake database: Milvus
- Authentication: Feishu OAuth2 with JWT

## Team Division; Related Pages

| Item | Owner or scope |
|---|---|
| Project and task management | Sophie Kirby |
| CDD documents | Sophie Kirby and Wyniver |
| Frontend development environment | Mia Drake |
| [[intelligent-writing-scenarios]] | Core writing flows, including weekly reports, biweekly reports, and reports. |
| [[feishu-knowledge-subscription]] | Main data sources and subscription mechanisms for the product. |
| [[algorithm-and-citation-pipeline]] | Algorithm engine used for intelligent writing. |
| [[risk-control-and-permissions]] | Risk-control review and permission-control design. |
- [[report-writing-interaction]] — Interaction design for the three-column editor
- [[roadmap-and-delivery]] — Product roadmap and delivery cadence