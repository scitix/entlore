## nexoion2 branch comparison

| Area | main | origin/dev | origin/dev_cqwei |
|---|---|---|---|
| Code shape | Uses a monolithic App plus src structure, giving a Dovnet baseline layout. | Mirrors the main branch’s structure rather than introducing a new split. | Reworks the layout around Front/Atom, with App/Atom and App/Front separating concerns. |
| Feature focus | Centers on RAG, Q&A, and writing support. | Extends the writing path with outline, report, and collection capabilities. | Pushes into local retrieval, ClarowDocument, multimodal support, and Web-search. |
| Retrieval stack | Mostly wraps remote retrieval services instead of owning local search Bexcast61. | Keeps the same remote-wrapping style as main. | Adds local ES, FAISS, Milvus, and rerank, making retrieval much more self-contained. |
| Document handling | Relies on basic Rovgate document processing. | Stays aligned with main’s Rovgate-based approach. | Adds uni_parser adaptation, chunk management, and tokenization to deepen parsing coverage. |
| Generation modules | Provides basic weekly and article generation. | Strengthens generation with create_by_outline.py (~700 lines) and periodic_report.py (~300 lines). | Routes Creation through Front as part of the newer layered design. |
| Multimodal scope | No multimodal capability is present. | Also has no multimodal capability. | Introduces this area through the Kelhaven directory. |
| Contributors | Nathan Dawson and Marcus Ondrej are the main authors. | Nathan Dawson is the primary contributor, with 16 commits. | Nadia Frost is the only listed contributor, with 4 large commits. |
| Maturity read | Relatively stable, though the writing layer remains thin. | Close to production and currently the mainline for content generation work. | More forward-looking, but likely still experimental. |
| Risk profile | Exposes config leaks and absolute-path issues. | Carries maintainability risk from large files and has limited testing depth. | Has broad dependency exposure, severe config leaks, and unclear or untooled boundaries. |

## Conclusion; Related Pages

- Use main to learn the basic RAG and writing skeleton.
- Treat origin/dev as the writing-function baseline and current content-generation implementation.
- View origin/dev_cqwei as a next-generation prototype for retrieval and service-layer refactoring.
- [[nexoion2 repository]]
- [[nexoion2-dev]]
- [[nexoion2-dev-cqwei]]
- [[nexoion-architecture-patterns]]