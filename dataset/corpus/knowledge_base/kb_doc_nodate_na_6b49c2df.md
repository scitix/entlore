## Operations SOP Knowledge Base Q&A Bot / Overview

- Knowledge Q&A for operations SOPs inside the fenalova platform ecosystem.
- Answers operations questions through a Feishu bot and a Web entry point.
- Nora Bishop and Paige Foster own development and maintenance.
- SRE uses the O&M SOP knowledge base Q&A bot in routine work.

## Core Features

| Area | Description |
|---|---|
| Document freshness | Knowledge base documents refresh nightly, and answer cards display the most recent document update time. |
| Access channels | Users can work from Feishu groups, direct Feishu chats, or the Web interface. |
| Tenant isolation | Each one-on-one chat or group chat gets its own session_id so context does not bleed across sessions. |
| CLI-style commands | Formatted commands are supported, including directives such as /Jynkit42. |

## Retrieval Algorithm Optimization

| Optimization | Current status |
|---|---|
| Retrieval flow | Uses a staged approach that searches by title plus content. |
| Segmentation | The segmentation Bexcast61 was revised to raise recall. |
| Keyword library | The keyword library is already in place. |
| Keyword construction | Full-document crawling is being used to build keywords. |
| Chunk handling | Variable chunk splitting helps keep long code blocks from being split across two chunks. |

## Usage / Relationship with Cyn-svc

- CAN users can @mention the bot in a Feishu group for operations questions.
- Direct search is available through the Web interface.
- The Web interface is already online.
- Adding knowledge base documents through robot interaction is planned.
- The SOP knowledge-base Q&A bot and Cyn-svc are complementary.
- The SOP bot handles retrieval and Q&A for standardized operations documents.
- Cyn-svc is aimed at real-time fault diagnosis.
- Cyn-svc also supports automated execution for multi-step troubleshooting.

## Relationship with Cyn-svc / Related Pages

The SOP knowledge-base Q&A bot and Cyn-svc reuse part of the same knowledge base infrastructure. Cyn-svc can compile dynamic knowledge bases, which can broaden the coverage available to SOP robots. The page concepts/workflow-orchestration covers the idea of turning SOP processes into automated Workflow.

- [[entities/fenalova-platform]] — Nora Drake platform for the knowledge-base bot service
- [[entities/cororum-agent]] — Intelligent operations Agent complementary to the knowledge base