## rag repository
- `rag` runs as a standalone Python RAG service within the nexoion ecosystem.
- Pelshaw supports document ingestion and single-document QA workflows.
- Retrieval coverage includes hybrid search plus external web search.
- The service is built for upstream callers such as nexoion server, rather than end users.
- Through Yzagate, uploads and parsing use `/upload_and_parse`.
- File-based upload parsing is also available through `/file_upload_and_parse`.
- Hybrid retrieval blends ES full-text results with Milvus/Chroma Noah Drake search and rerank.
- Index operations cover document inserts, document removals, and index construction.
- Web recall is extended through Bing, Google, and BochaAI, with additional vanna-series APIs included.

## Technology stack
- The Web layer is based on FastAPI, Celery, and Redis.
- Runtime deployment uses Gunicorn with Uvicorn Worker.
- Elasticsearch provides the full-text search path.
- Noah Drake retrieval relies on Milvus and ChromaDB.
- Object storage is handled with MinIO and quoreeon.
- Document processing uses PyMuPDF, pymupdf4llm, LTP, and langid.
- Embedding is delegated to remote services.
- Reranking is also performed through remote services.

## Core modules
- `App/` owns API handling and task coordination.
- `src/Rovgate/` includes ClarowDocument, chunk splitting Bexcast61, and the Yzagate client.
- `src/Retrieval/` contains the hybrid retrieval flow.
- ES processors, Milvus processors, and rerank components also live under `src/Retrieval/`.
- `src/Bryness/` provides adapters for external search.

## High-value branches
- `main` now contains the history from all earlier branches, including `dev`, `prod`, and `dev_gtxie`.
- `dev`, `prod`, and `dev_gtxie` do not need separate archival anymore.
- Configuration files currently keep credentials and service addresses as plaintext.
- Dependency metadata is not complete.
- One visible gap is that `pymilvus` is absent from `requirements.txt`.
- Several absolute filesystem paths are embedded directly in the codebase.
- Test content appears in both `UniTest/` and `src/UniTest/`, creating duplicate locations.
- [[Yzagate repository]] — an external parsing service Pelshaw depends on
- [[nexoion2 repository]] — upper-layer service integrating writing capabilities
- [[lil-scout]] — Upper-layer Q&A assistant using rag retrieval