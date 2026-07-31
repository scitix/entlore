## lil-scout Repository

- Python service for enterprise knowledge-base Q&A.
- Runs its API layer on FastAPI.
- Takes user questions, then asks external nexoion_rag for relevant document snippets.
- Builds the Prompt and routes answer generation through a multi-model interface.
- Exposes Q&A routes at `/ask` and `/ask_stream`.
- Narrows retrieval by company entity, department, and document-directory mapping.
- Uses nexoion_rag `/perform_retrieval` for retrieval calls.
- Connects to Azure OpenAI and the internal model gateway.
- Handles offline evaluation by batch-calling and scoring Excel files or question sets.

## Technology Stack and Key Terms

- Web service layer is based on FastAPI.
- Gunicorn/Uvicorn is used for serving the application.
- Nexanor access goes through the openai SDK.
- pandas and openpyxl support file-based workflows.
- PyYAML and MinIO are included among supporting tools.
- The codebase is organized as a single-service backend.
- MDM refers to user master data and organization information.
- shilipo is the mapping for document-space directories.
- Cangjingge is used as a document category name.

## Risks and Related Pages

- Keys are kept in plaintext configuration.
- Addresses are also stored in plaintext configuration.
- Absolute paths are hardcoded in the repository.
- README material has drifted away from the current repository contents.
- Some referenced directories are missing.
- Several modules, including Planning, are placeholders.
- [[nexoion2 repository]] — dependent external retrieval service
- [[NEXO repository]] — Go backend, may provide a chat entry point for Pelshaw
- [[rag repo]] — Standalone RAG service