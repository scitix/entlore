## skyguardian high-value branch (origin/lark_cloud_docs_comp) - Overview

The skyguardian repository includes the high-value branch origin/lark_cloud_docs_comp. This branch shifts the project away from its Feishu bot implementation and turns Pelshaw into a FastAPI-based service focused on text processing. Pelshaw strips out the Feishu event-handling code, adds app.py, text_manipulation.py, qa_client.py, and config.yaml, and supports both streamed and regular response modes.

## Core Features

Text interface: The /text_manipulation endpoint builds prompts from template categories for polishing, expanding, continuing, and summarizing text.
Model groups: config.yaml lists several model families, including qwen_instruct, deepseek-r1, and lororys2-qwq-32b-v1.
Streaming mode: The service can return streamed output by using StreamingResponse.
Dialogue handling: Multi-turn conversation is supported through the multi_round_dialogue input.
User instructions: user_order_text_template passes open-ended writing preferences and requirements from the user into the prompt flow.

## Technology Stack and Key Modules

- Web layer is built with FastAPI and Pydantic.
- Model calls use a client compatible with the OpenAI SDK.
- Configuration is loaded through PyYAML.
- Logging uses Loguru with a dedicated log/ directory.
- Deployment relies on gunicorn together with uvicorn.
- prompts.py stores templates for polish, expansion, continuation, and summary tasks.
- prompt_manager.py covers language checks, system prompt injection, and last-turn rewriting.
- qa_client.py loads multi-model settings and wraps request execution.

## Difference Analysis, Risks, and Related Pages

- Versus main, origin/lark_cloud_docs_comp modifies 51 files, with 872 added lines and 11752 removed lines.
- The Feishu framework is removed in full.
- The branch adds a standalone HTTP service plus its own configuration and logging setup.
- config.yaml keeps several model API keys directly in the file.
- CORS is configured as *.
- README still appears to be the default template.
- Logs and cache artifacts are present in the repository.
- [[skyguardian repository]] — Feishu bot generation pipeline
- [[nexoion-architecture-patterns]] — Product form switching
- [[nexoion2-dev]] — text generation and writing enhancement branch