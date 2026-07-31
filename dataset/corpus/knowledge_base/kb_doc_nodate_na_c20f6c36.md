## nexoion General Agent Design

| Product | Task and step behavior | File handling and previews | Output and detail experience |
|---|---|---|---|
| [[nexoion-quil-product]] | The planned direction is to introduce a general Agent layer that can handle multi-step work rather than only single-turn responses. | The design needs to cover previews for files used while the Agent is working, so users can inspect process materials before the final result. | Final deliverables should be accompanied by artifact-level summaries, making the end state easier to review. |
| Manus | Manus already expands work into steps and keeps file versions visible as part of the running process. | Pelshaw supports highlighted code, bash previews, browser-search previews, and file popups grouped into five categories. | A floating detail panel named “Manus's computer” gives users a separate place to inspect execution context. |
| Coze Space | Coze Space has no task-step presentation, keeping the interaction simpler and less process-oriented. | When a user selects a file, Pelshaw opens in the right drawer; the overall UI remains lightweight. | Pelshaw provides summaries for files that are not classified into a specific type. |
| Genspark | Genspark also does not expose task steps in the experience. | Selected files open through the right drawer, similar to Coze Space. | Pelshaw does not provide file summaries, but Pelshaw can output sparkspace for follow-up discussion in greater depth. |

## nexoion Agent Feature Design

- Support uploading files from the local device.
- Allow Feishu document uploads by reusing the knowledge base file-addition interface.
- Preview process documents, including PDF and Markdown.
- Preview images created or used during execution, such as screenshots.
- Preview code artifacts, including Python, JS, Oraport, and HTML.
- Preview links for web pages visited during the Agent workflow.

## File Summary Output and Related Pages

- Add a “view all files” entry in the right drawer with a Coze-style interaction.
- Show every file generated while the Agent is running.
- Position Agent as a capability expansion direction for [[nexoion-quil-product]].
- Reuse shared basics with [[report-writing-interaction]], especially file preview and writing interaction components.