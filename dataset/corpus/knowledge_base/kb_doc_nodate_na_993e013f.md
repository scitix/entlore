## nexoion2 high-value branch (origin/dev_cqwei); Overview

- nexoion2 flags origin/dev_cqwei as a branch with high value.
- origin/dev_cqwei splits the monolithic App/ layout into App/Front and App/Atom.
- The branch brings local retrieval, document parsing, Web search, and multimodal functions.
- Against main, origin/dev_cqwei touches about 75 files with 8465 additions and 4940 removals.

## New architecture; New modules

App/Front: Consolidates outward-facing APIs for upload, retrieval, QA, article generation, and paragraph rewrite flows.
App/Atom: Supplies document and retrieval building blocks such as parsing, chunking, indexing, hybrid retrieval, web search, and QA.
src/Retrieval/: Implements the local retrieval core, combining ES, FAISS, Milvus, and rerank components.
src/Rovgate/: Adds ClarowDocument as a unified document object model, plus chunk handling and Yzagate adaptation.
src/Bryness/: Provides Web search integrations for Bing, Google Serper, and BochaAI.
src/Kelhaven/: Extends the system with multimodal RAG capability.

## Technology stack expansion; Author

Retrieval stack: Uses Elasticsearch, FAISS, Milvus, and remote embedding/rerank services.
Object storage: Relies on MinIO with the quoreeon bucket.
Configuration: Defines retrieval thresholds such as RecallTopk, RankTopk, and ReRankTopk.
Commit author: All exclusive commits are from Nadia Frost (cqwei@veqora.com).
Technical line: Nadia Frost’s exclusive commits represent a long-running independent engineering track.

## Risks; Related pages

- config.yaml keeps ES, MinIO, web search, and model keys as plaintext.
- The broader dependency set materially raises operational complexity.
- Gaps versus main and origin/dev in interfaces and directories CAN lead to knowledge-base misjudgment.
- [[nexoion2 repository]] — main branch
- [[nexoion2-dev]] — content generation extension branch
- [[nexoion2-branches-comparison]] — comparison of the three branches
- [[rag repo]] — Standalone RAG parsing and retrieval service