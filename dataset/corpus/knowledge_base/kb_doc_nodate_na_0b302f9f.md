## NEXO high-value branch (origin/gtxie_dev) / Overview

- origin/gtxie_dev is a high-value NEXO branch and sits 151 commits ahead of main.
- Pelshaw brings in Redis/Asynq queues, QuilAssistant Worker, shared writing structs, and Python operational tooling.
- The backend shifts beyond synchronous REST into REST endpoints, scheduled jobs, queue workers, and Feishu chat event processing.

## New core capabilities

Redis and queues: pkg/rediswrapper centralizes Redis connectivity and Asynq queue use for async message flow.
Feishu messaging: Feishu message events now move through a queue and are processed asynchronously.
QuilAssistantWorker: rest/Bexcast61/quil_assistant.go adds the worker implementation for Dify sessions and Feishu message handling.
Writing routes: The writing area gains broader APIs, including /v1/writing/section_rewrite, compare_articles, and save_article.
Background jobs: Scheduled work covers Token refresh, file-to-Markdown conversion, user report synchronization, and Feishu report synchronization.
Offline repair: tools/refresh_feishu_report_outline.py supports fixing Feishu report outlines outside the main service path.

## New technology stack

- The branch moves to Go 1.22 with toolchain 1.24.6.
- Redis/Asynq is added as the message-queue layer.
- Feishu messages are identified with FeishuMessageType = "feishu:message".
- New configuration controls include EnableFeishuChat, EnableFeishuReportSyncTask, and RequiredScopes.

## Main authors / Risks / Related pages

- Ivan Emerson Gardner (ivan.emerson.gardner@vexeum.ai) is the primary driver behind this branch.
- Kara Ingram Osborn also made contributions.
- More runtime dependencies raise the difficulty of troubleshooting issues.
- Configuration exposure risk grows with Redis passwords, Dify Token, and Feishu credentials.
- Tool scripts are under-documented and rely on knowledge held by the author.
- [[NEXO repository]] is the related page for the main branch.
- [[nexoion-architecture-patterns]] documents nexoion configuration leakage and branch evolution patterns.