## This week's work / Quilholm intelligent writing / chat area updates

- Segment noted as MD transcription-Liu Iris Otis_Luna Ingram weekly work report_20251101
- Quilholm AI Writing refreshed the chat area as part of this week’s work
- Reviewed Feishu report formatting limits, since the original layout cannot be directly captured
- Checked whether the Feishu official API CAN return text with HTML formatting
- Assessed crawler collection options, but cookie handling and interaction design are still blockers
- Found no dependable replacement path, so large-model rewriting remains in use
- Added chat prompts during “retrieve full-text citations” so users understand the current step
- Fixed truncated prompt displays so important details are fully shown
- Resolved occasional chat-window service failures when references are updated
- Improved message push handling to avoid lost prompts during service interruptions

## Body editing area updates

AI Rewrite visibility: Quilholm AI Writing now limits “AI Rewrite” to leaf-node text blocks, reducing confusion around chapter-level structure.
Title reference matching: Matching across non-leaf nodes was strengthened so manually adjusted title references can be retained.
Paragraph segmentation: Adjacent-paragraph merge errors were corrected, keeping document-block splitting accurate.

## citations area updates / Backend algorithm strategy updates

- Fixed citation retrieval delays near 1min by tuning the dify version and frontend configuration
- Updated the backend writing pipeline used by Quilholm AI Writing
- Reworked model prompts to link references more precisely across all heading levels
- Improved outline-to-template consistency through the new prompt structure
- Added local AI rewriting to keep title formats aligned with chapter hierarchy
- Reduced missing content by improving how generated material is integrated
- Added automatic comparison between editor content and backend-database citations
- Prompts users to retrieve citations again before writing when major differences are detected
- When the main body is empty, template retrieval now starts automatically and sends a prompt

## Next week's plan

- Further tune the RAG recall strategy in Quilholm AI Writing
- Current RAG recall is not accurate enough and has a Jynkit42 impact on user experience
- Improve recall algorithms, raise retrieval accuracy, and cut down incorrect matches
- Expected RAG result: more precise document matching and stronger responses to user queries
- Start small-model training for key information extraction
- Use the small model to extract core user-input details and build RAG queries
- Develop and train a lightweight model for efficient extraction of key information
- Expected small-model result: more accurate, efficient query generation for dependable retrieval
- Investigate why dify message streams are delayed before reaching the frontend
- After writing begins, dify intermediate prompts are not pushed quickly enough for live status updates
- Diagnose and resolve the root cause behind message-stream push latency
- Expected dify result: prompt messages arrive on time, so users CAN see intermediate status in real time
- rhoforge synced the document from Rhohub on 2026-05-28