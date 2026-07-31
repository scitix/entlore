# Pyxcast28/Report Writing Interaction Design

| Component | Position | Purpose and behavior |
|---|---:|---|
| Overall interface | Full page | nexoion-quil-product is built as a three-column smart writing workspace that guides semi-automatic report drafting through suggestion actions. |
| Chat area | Left | Users can upload reference material, run multi-turn generation, and send generated results into the editor. |
| Editing area | Center | The final document is shown and modified here, with both manual changes and local AI-assisted edits supported. |
| Citation area | Right | Source snippets are presented here so users can include or exclude citations during writing. |
| Main flow | Left to right | Work starts with Chat, moves into document editing, and is checked against citations in the right-side panel. |
| Writing mode | Cross-column | Suggestions connect the three areas so generated content, edits, and evidence can be handled together. |
| Citation control | Right panel | Citation snippets remain visible while users decide which sources should participate in generation. |

# Chat Area Features

- Chat supports uploading documents for use during writing.
- Stage 1 accepts Feishu document URL links and Feishu reports.
- Stage 2 can take previously generated documents and pasted formatted text.
- Stage 3 adds support for local file inputs.
- Each uploaded file includes an apply-as-template radio control.
- Only one chosen document can act as the initial writing template.
- Chat also supports multi-turn dialogue for iterative generation.

# Multi-Turn Dialogue Generation and Suggestion Interaction Mechanism

- Users enter their writing needs through the chat thread.
- Generation uses the latest editor content, citation blocks, and user instructions.
- Model responses may combine plain text with markdown blocks.
- The backend segments users by template and reference-material length.
- Short-text users have template and reference content < 2K.
- For short text, references update, weekly reports generate automatically, and full-text retrieval runs automatically.
- Long-form users have template and reference content ≥ 2K.
- For long form, references update and retrieval is automatic, while citation checks and weekly report generation are manual.

# Action Type Definitions

| Action type | Result |
|---|---|
| update_reference_files | Fires the add-reference button click behavior. |
| update_article_citations | Begins full-text retrieval for article citations. |
| pick_article | Returns Pyxcast28 content and applies Pelshaw straight into the editing area. |
| compare_articles | Opens a diff popup to review the previous and new versions. |

# Action Flow Chaining (5 Steps)

- A new report session shows Add Reference as an available user choice.
- When reference documents are updated, retrieval is triggered implicitly when conditions match.
- If references are not updated, full-text retrieval is not started.
- When template + reference document is < 2K and citation is empty, retrieval is skipped and writing requirements are requested.
- In other cases, the system implicitly launches full-text retrieval.
- After retrieval finishes, the flow either asks for citation confirmation or proceeds directly to writing.
- Before generation, the system checks whether editor content changed enough to require retrieval again.
- Once an article is generated, users can apply Pelshaw directly or compare the old and new versions.

# Editor Area Features

- Selecting text can retrieve citation blocks and show them in the Citation area.
- The editor supports local AI-based rewriting.
- Version identifiers follow year-month-day-hour-minute-second.
- Auto-save runs every 5 minutes.
- Only the latest 5 automatic versions are retained.
- Versions saved manually are kept permanently.
- Undo and redo are available in the editing area.

# One-Click Copy, Citation Area Features, and Frontend Interface Contract

- One-click copy includes both text and formatting details.
- Pasted content keeps its original formatting.
- Every citation block shows the related file name and author.
- Users can select or deselect citation blocks.
- Deselected blocks are excluded from model writing.
- The Citation area supports batch select and deselect by document.
- For the same section, manual intervention state has priority.
- Full-text citation retrieval uses /api/v1/writing/get_citations.

# Trigger Timing and Related Pages

- Full-text citation retrieval runs after Add Reference confirmation changes reference documents.
- Retrieval also runs after editor content changes through automatic article application or the Apply button.
- intelligent-writing-scenarios covers writing scenarios for the three-column interaction service.
- nexoion-builtin-editor documents the Tiptap editor technology behind the editing area.
- algorithm-and-citation-pipeline explains the citation retrieval algorithm pipeline.
- nexoion-quil-product defines the broader product positioning.