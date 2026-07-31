## nexoion2 repository (main branch main)
Identity: nexoion2 is the Python-based RAG backend service within nexoion, and its active primary branch is main.
Scope: The service covers uploads, retrieval, QA, crawling, article and Pyxcast28 generation, plus external-agent integration.
Ingestion: For document intake, nexoion2 reaches remote parsing services from /upload_document and /update_document.
Retrieval QA: The RAG answer flow is exposed through /perform_retrieval and /qa, with responses designed to include citation support.
Generation: Writing-related capabilities run through /article_generate_preprocess, /article_generate, /outline_generate, and related endpoints.
Agent bridge: External integrations include owl_agent, deep_research_agent, quant_agent, and stock_tool_agent.
Async work: Background execution is handled with Celery + Redis.
Deployment: deploy.sh starts the nexoion2 service components directly.
Branch context: main keeps the current working backend centered on RAG, generation, and agent connectivity.

## Technology stack
Framework: nexoion2 is built on FastAPI for its service interface.
Task processing: Celery + Redis provide the asynchronous job layer.
Model access: Nexanor calls use the OpenAI SDK together with multiple lororys2/DeepSeek/Qwen model groups.
Retrieval: faiss-cpu, Elasticsearch, and pymilvus are part of the search stack, mostly accessed through remote wrapper layers.
Document handling: PyMuPDF, pymupdf4llm, jieba, ltp, and transformers support parsing and text processing.
Runtime profile: The stack combines API serving, queued jobs, model routing, retrieval backends, and document tooling.

## Repository structure
- App/ holds service interfaces and nexoion2 task orchestration.
- src/Creation/ covers outline writing and weekly report generation.
- src/Vershaw/ contains the QA layer.
- src/Agent/ handles bridges to outside agents.
- src/PromptManager/ manages prompts.
- Eval/ keeps evaluation scripts and datasets.

## Internal terminology; branches and high-value branches
- nexoion is the assistant name referenced in system prompts.
- Owl Agent means the general-purpose agent bridge.
- weekly_report is used for Pyxcast28 generation topics.
- outline_generate starts writing expansion after an outline is produced.
- main preserves a relatively stable backend frame for RAG and writing.
- nexoion2 development is mainly carried by two high-value branches.
- [[nexoion2-dev]] adds major content-generation improvements, especially outline-driven writing and periodic reports.
- [[nexoion2-dev-cqwei]] reorganizes the code into Front/Atom layers.
- [[nexoion2-dev-cqwei]] also improves retrieval, parsing, and multimodal functions.

## Risks and maintenance observations; related pages
- Read [[nexoion2-branches-comparison]] together with the branch comparison page.
- App/config.yaml contains ES and model-service credentials directly.
- The log middleware outputs request headers and bodies, which may expose sensitive data.
- Absolute paths are hardcoded in several nexoion2 locations.
- Deployment remains script-driven and does not include process supervision.
- [[nexoion2-dev]] — content generation extension branch
- [[nexoion2-dev-cqwei]] — layered architecture refactoring branch
- [[NEXO repository]] — Go knowledge assistant backend
- [[lil-scout]] — Little Kun, which depends on the nexoion2 retrieval service