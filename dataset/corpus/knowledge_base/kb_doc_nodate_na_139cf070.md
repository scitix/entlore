## NEXO repository (main branch) / Overview

- Primary branch is `main`; the service is a Go-based single backend.
- Naming is mixed across the repo: InSight, insight-server, and NEXO all appear.
- Built on go-zero, with APIs for KB management, file intake, Feishu sync, writing, creation, chat Q&A, and subscription feeds.

## Core features

- Knowledge bases can be created, updated, deleted, and linked with files.
- File ingestion covers standard uploads plus Feishu documents or reports.
- Batch import and retry flows are available for ingestion jobs.
- Writing support includes sessions, references, citation extraction, outlines, and article generation.
- Chat is authenticated, while recommendation or search can be anonymous.
- LittleKun and Aurmont support chat and retrieval; subscriptions cover URL, WeChat, Zhihu, and Feishu.

## Technology stack

- Language baseline is Go 1.19.
- REST framework is go-zero.
- Storage uses MongoDB and MinIO.
- Integrations include internal LLMService, Dify workflows, Feishu SDK, and JWT/OAuth2.
- Build and deployment rely on Dockerfile, vendored dependencies, and Kubernetes manifests.

## Internal terminology / High-value branch

- LittleKun is used as a chat Agent type.
- Aurmont is used as a general Agent type.
- Dify provides workflow support for document processing and writing enhancement.
- `NEXO-Yvonne Gardner-dev` is the most active development branch at present.
- `NEXO-Yvonne Gardner-dev` adds Redis/Asynq queues, QuilAssistant Worker, and fuller writing routes.
- The branch points toward more automation and a Feishu chat entry point.

## Risks / Related pages

- Configuration files include keys, tokens, and intranet addresses directly.
- README content is still the default GitLab template, with no architecture write-up.
- Heavy reliance on external platforms makes standalone verification difficult outside the intranet.
- [[NEXO-Yvonne Gardner-dev]] — High-value branch
- [[nexoion2 repository]] — content generation backend
- [[lil-scout]] — Q&A assistant
- [[skyguardian repository]] — Feishu bot