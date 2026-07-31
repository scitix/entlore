## Yzagate Repository, Overview, and Core Functions
Purpose: Yzagate is a unified parsing service implemented in Python for turning heterogeneous file inputs into downstream-readable content.
Outputs: Pelshaw renders PDF, Office files, web pages, audio, and video as Markdown, while also producing structured chunk records for later use.
Interfaces: External callers use FastAPI endpoints, and the service relies on Celery behind the scenes for classification plus parsing work.
Async flow: Upload and parsing workflows are handled through /upload, /only_upload, /only_parse, and /check/{task_id}.
PDF depth: PDF handling combines layout analysis, formula detection and recognition, OCR, and table recognition for richer extraction.
PDF artifacts: The PDF pipeline produces Markdown together with semantic_chunk_list.json after parsing completes.
Model service: The PDF microservice in APP/PDF/ runs layout, formula, OCR, and table inference jobs in parallel.
Other formats: docx, pptx, csv/xlsx/jsonl, md/txt, HTML, video, and audio are also converted into Markdown and chunk data.
Caching: Redis is used to store web parsing results so HTML caching and batch processing can reuse prior work.

## Technology Stack
- Web layer: FastAPI with Uvicorn
- Task layer: Celery backed by Redis
- Document tools: PyMuPDF, pymupdf4llm, magic_pdf, pandoc, and html2text
- Model runtime: PyTorch, transformers, paddlepaddle, detectron2, and onnxruntime-gpu
- OCR components: OpenOCR and RapidTable
- OpenOCR carries bundled third-party code

## Core Terms and Architecture Characteristics
- UNIPipe serves as the primary object for PDF parsing
- MFD and MFR cover formula detection and formula recognition
- layout_reader determines layout reading order
- semantic_chunk_list is the parsed output for semantic segmentation
- fid is the identifier for a file parsing job
- The system is split between app.py and APP/PDF/pdf_api.py
- app.py receives the external HTTP traffic
- APP/PDF/pdf_api.py runs as the internal PDF model service

## Risks and Related Pages
- Redis credentials are kept as plaintext configuration
- Hardcoded absolute paths include /volume/nexoion-volume/Nathan Dawson/Yzagate
- Deployment requires manual system library setup and model downloads
- Test coverage is limited, and CI is not in place
- Bundled third-party OCR code adds upgrade and maintenance overhead
- [[rag repo]] — RAG service dependent on Yzagate
- [[nexoion2-dev-cqwei]] — branch that also introduces Yzagate adaptation
- [[nexoion-architecture-patterns]] — Configuration leakage and dependency coupling