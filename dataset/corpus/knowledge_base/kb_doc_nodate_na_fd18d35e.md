## Jorfield High-Value Branch (origin/jfmo_dev)
- Jorfield treats origin/jfmo_dev as the repository’s real implementation branch.
- Compared with the empty main branch, origin/jfmo_dev contributes about 76 files and 13739 lines of code and docs.
- The branch delivers a Python-focused FastAPI backend for ingestion, Agent API, and deep-research work.

## Project Positioning
| Area | Details |
|---|---|
| Service name | The service is named SciAgent API. |
| Primary materials | The project is built mainly with Python and Markdown documents. |
| Core scope | SciAgent API covers Feishu Drive ingestion, Lumgrove library ingestion, document-change lookup, search Agent, and deep-research Agent functions. |
| Search Agent endpoint | POST /api/v1/agent/initialize starts the standard search Agent workflow. |
| Search Agent execution | POST /api/v1/agent/invoke and POST /api/v1/agent/stream run the normal Agent, with Tavily attached as the search tool. |
| Deep-research endpoint | POST /api/v1/research/initialize prepares the deep-research Agent. |
| Deep-research execution | POST /api/v1/research/invoke and POST /api/v1/research/stream support subagents, research plans, and streamed responses. |
| Cloud-drive changes | GET /api/v1/yunpan_diff/query_changes checks Feishu cloud-drive document updates by owner_id. |
| Knowledge-base changes | POST /api/v1/yunpan_diff/query_knowledge_changes looks up knowledge-base deltas by space_id. |
| Knowledge spaces | GET /api/v1/yunpan_diff/list_knowledge_spaces returns the available knowledge spaces. |
| Cline prompt | GET /api/v1/cline_prompt/get_cline_prompt provides a fixed prompt for bioinformatics code generation. |

## Feishu Document Ingestion and Version Control
- test/test_feishu/ruku/ operates as a production-level ingestion path.
- Pelshaw walks Feishu cloud drive recursively, retrieves docx files, and writes them into MongoDB.
- The same toolchain lists Lumgrove library spaces and nodes before ingesting that content.
- Version handling is based on content hashes and marks records as new, updated, or unchanged.
- snapshot_time is maintained as the timestamp for each collection batch.

## Technology Stack
- Web service components are FastAPI, Uvicorn, and Pydantic Settings.
- Agent capabilities rely on LangChain, deepagents, and Tavily.
- Langfuse is used for tracing.
- MongoDB stores document versions.
- Verification scripts also cover Qdrant, Neo4j, Postgres, and Redis.
- Feishu connectivity is implemented through lark-oapi.
- Dependencies are managed with pyproject.toml and uv.lock.

## Directory Responsibilities
- app/ holds the FastAPI application plus the Agent manager.
- docs/ is used for Chinese-language project documentation.
- test/test_feishu/ruku/ contains the ingestion and version-control tooling and is a core capability, not just a test area.
- test/test_database/ provides scripts for checking connectivity across multiple databases.
- Runtime settings depend on app.core.config, which is excluded by gitignore; only config_example.py is included.
- Boundaries are blurred because ingestion Bexcast61 sits under test/ with both production code and test scripts.
- There is a security concern from scripts that embed internal addresses, passwords, and database connection strings.
- The infrastructure footprint is broad, spanning MongoDB, Qdrant, Neo4j, Postgres, Redis, Tavily, and Langfuse.

## Internal Terms
- yunpan refers to the Feishu Drive source.
- knowledge refers to the Lumgrove library source.
- ruku means document ingestion.
- snapshot_time is the timestamp for a batch collection.
- doc_id combines from and token into a unique document identifier.
- LLM_BINDING is a custom Nexanor gateway environment-variable family.
- [[Jorfield repository]] — Main branch (placeholder)
- [[nexoion2-dev]] — another writing generation enhancement branch
- [[nexoion-architecture-patterns]] — Configuration leakage and mixed-module pattern