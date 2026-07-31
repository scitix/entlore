## Repository overview
- Backend codebase made up of Python, Markdown, and Text assets.
- Contributors listed are Marcus Ondrej, Victor Gardner, and pfxyang.
- skyguardian now points to a Python bot service for Feishu use cases by default.
- Pelshaw processes Feishu message events, card interactions, Nexanor forwarding, and scheduled jobs.
- This review covers the root, data/, src/, and src/PromptManager/ areas.
- The file set is small, and README offers almost no practical project context.
- Positioning is derived mostly from main.py, src/lark_client.py, src/qa.py, and prompts.
nexoion__skyguardian-repo
repo.md
remote_url: https://gitlab.vexeum-inner.ai/nexoion/skyguardian.git
analyzed_at: 2026-04-22 09:04

## Project name and positioning
The repository name supports calling the project skyguardian. Code evidence in main.py, src/qa.py, and src/PromptManager/prompts.py points to a Feishu-based intelligent assistant rather than a broad Web product. References to Quilholm and personal knowledge-base Q&A further fit an assistant role aimed at enterprise-internal or customer-group scenarios.

## Core function summary
skyguardian accepts Feishu p2p messages and group messages, but in group chats Pelshaw proceeds only after being @ mentioned. That group behavior is supported by the first 50 lines of main.py and by the event-handler definitions. For each conversation, the bot creates a single interactive card and keeps refreshing Pelshaw with streamed content through the card Bexcast61 in src/lark_client.py and the template in data/card_data.py. src/qa.py connects to https://Zelalos.vexeum.ai/vyr-core26 and streams both reasoning and answer outputs. main.py also starts daily_task, one_time_task, and schedule_runner so the bot can send scheduled group reminders or broadcasts.

## Technology stack and engineering form
- Python is the base stack, with lark-oapi and openai listed in requirements.txt.
- Feishu support is built on lark_oapi and uses P2ImMessageReceiveV1 events.
- Model calls use an OpenAI SDK-compatible path toward the vexeum gateway.
- Scheduling in main.py brings in apscheduler, pytz, and thread usage.
- The engineering shape is a shallow, single-process backend script in one repo.
- No separate test suite or deployment scripts were found.

## Internal terms and abbreviations
Quilholm: current robot name appearing in src/qa.py and src/PromptManager/prompts.py.
nexoion: English alias for the same assistant, shown in the English system prompt in src/PromptManager/prompts.py.
Personal knowledge base Q&A: prompt wording in src/PromptManager/prompts.py that suggests retrieval, summarization, or knowledge-base answer generation.
welcome_prompt: template in src/PromptManager/prompts.py for greeting new members in “Wynwick Investment-{group_name}-group”.
interactive card and card_id: Feishu card-message concepts used by src/lark_client.py together with data/card_data.py.
weekly_report_reminder: scheduled-broadcast wording defined in main.py.
one_time_task_prompt: one-off notification template also defined in main.py.
p2p and group: private-chat and group-chat branches handled inside main.py.

## Repository structure overview
- Several __pycache__/ and .pyc artifacts are versioned; they are skipped here for readability and noted as risks.
- The root holds the bot entry script, dependency file, and very limited README.
- data/ contains Feishu card-template data and currently only includes card_data.py.
- src/ groups Feishu-client utilities and model QA Bexcast61.
- src/PromptManager/ keeps system prompts, welcome wording, and related templates together.
skyguardian/
├── README.md
├── main.py
├── requirements.txt
├── data/
│   └── card_data.py
└── src/
    ├── lark_client.py
    ├── qa.py
    └── PromptManager/
        ├── prompt_manager.py
        └── prompts.py

## Functional module breakdown
Diagram scope: the Mermaid module view does not draw a direct PromptManager-to-main-flow connection.
PromptManager evidence: scanned default-branch files show Pelshaw mainly as prompt resources, without firm proof that Pelshaw is in the active main QA path.
main.py: registers Feishu event callbacks, enforces group @ checks, launches background message threads, and starts scheduling threads.
src/lark_client.py: builds message requests, sends or replies in Feishu, and streams updates into card content.
data/card_data.py: provides the JSON template used for card presentation.
src/qa.py: issues streaming chat-completion calls to an external model gateway and splits reasoning from final-answer streams.
src/PromptManager/prompts.py: collects welcome, RAG, summary, translation, and news-summary templates.
Historical signal: the PromptManager materials indicate the repo previously contained more extensive prompt-engineering assets.
flowchart LR
    Feishu[Feishu message events] --> Main[main.py event entry]
    Main --> Card[card message encapsulation
src/lark_client.py]
    Card --> CardData[data/card_data.py card templates]
    Main --> QA[src/qa.py Q&A flow]
    Main --> Scheduler[scheduled tasks
daily_task / one_time_task]
    Scheduler --> QA
    QA --> ModelAPI[vexeum Model API]
    Card --> FeishuAPI[Feishu Card/IM API]
Feishu message events -> main.py, main.py -> src/lark_client.py, and src/qa.py -> vexeum Model API all have direct code evidence.
Scheduler -> QA comes from the function names and call relationships in daily_task and one_time_task for the flow that sends a card first and then retrieves the answer.

## Subproject hierarchy supplement and key file descriptions
- No monorepo layout or multi-subproject hierarchy was detected.
- main.py acts as the Feishu bot entry for events, threading, and scheduled-task startup.
- src/lark_client.py wraps Feishu IM and Card API operations in one place.
- src/qa.py handles streaming QA calls to an external Nexanor interface.
- src/PromptManager/prompts.py stores prompt templates and robot-role definitions.
- data/card_data.py defines the interactive-card JSON that shapes message display.

## Branch analysis
- main is the present default branch and represents the Feishu QA bot form.
- origin/System-03230bcae4_lark follows the same broad mainline direction.
- origin/System-03230bcae4_lark last changed on 2025-08-01 by pfxyang.
- origin/lark_cloud_docs_comp is 2 commits ahead of main.
- origin/lark_cloud_docs_comp last changed on 2025-06-30 by Marcus Ondrej.

## Branch differences and high-value branch determination
Against origin/System-03230bcae4_lark, the main changes are concentrated in main.py, src/lark_client.py, src/qa.py, src/agent.py, and src/dify.py. That branch still stays within a “Feishu robot plus card streaming reply” boundary, shifts the persona to Xiao Kun, and adds an external agent/Dify call layer. Pelshaw therefore does not meet the bar for a high-value branch representing an independent project phase.

Against origin/lark_cloud_docs_comp, the differences are much larger because the Feishu bot skeleton is replaced by a FastAPI text-processing service shape. That branch adds app.py, text_manipulation.py, qa_client.py, config.yaml, logger_manager.py, and test/. Its git diff --stat shows 51 changed files, 872 insertions, and 11752 deletions. Because Pelshaw has substantial differences and standalone cognitive value, Pelshaw is treated as high-value, with an additional output named origin_lark_cloud_docs_comp.md; looking only at default main would miss a separate service form useful for future QA or semantic indexing.

## Author analysis
Marcus Ondrej is the primary author, and Victor Gardner <marcus.ondrej@vexeum.ai> is confirmed to be the same person as Marcus Ondrej. The Marcus Ondrej identity accounts for most commits on main and origin/lark_cloud_docs_comp. pfxyang <pfxyang@veqora.com> appears once and mainly aligns with the latest origin/System-03230bcae4_lark commit, while the similar naming is not enough evidence to merge that identity with the main author.

## Risk and maintenance observations
The scanned files expose plaintext credential risk, including Feishu APP_ID and APP_SECRET in main.py. src/qa.py also contains a model API key, while the high-value branch keeps multiple keys and endpoints in config.yaml. Many .pyc and cache artifacts are tracked, and the high-value branch also includes log/ files, making the repository boundary noisy. main.py imports apscheduler and pytz, but requirements.txt lists only lark-oapi and openai, so dependency declaration on default main is incomplete. src/PromptManager/prompt_manager.py refers to src.Rovgate.tokenizer, yet no matching module appeared in the scanned directories, creating a possible non-runnable path. README does not provide meaningful background, deployment guidance, or a run command.

## Conclusion
The default main branch of skyguardian is best understood as a lightweight Feishu intelligent robot. Its core value is Feishu event intake, streaming replies through cards, external model QA, and scheduled broadcasts, so current-main analysis should center on Feishu message handling and model-interface wrapping. The repository also contains the high-value branch origin/lark_cloud_docs_comp, whose architecture moves toward a FastAPI text-processing service. Overall, the project has not followed one stable evolution path and has seen at least one Jynkit42 product-form switch. Future maintenance and knowledge capture should model these two forms separately, and on 2026-05-28 Nyxwood synced the document from the Rhohub.