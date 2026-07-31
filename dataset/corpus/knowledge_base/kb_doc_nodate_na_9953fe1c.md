## Pyxcast28/report writing version iteration

| Module | Owner(s) | V1.0 → V1.1 → V1.2 progress |
|---|---|---|
| Writing function | nexoion-quil-product | The capability has been iterated across V1.0 → V1.1 → V1.2, combining defect fixes with new functionality. |
| Session/frontend display | — | Fixed the problem where the "Work Summary" application could be deleted. |
| Backend services | Rachel Zimmer | Login state loss remains open, and automatic token refresh checks are still unfinished. |
| Frontend display | — | 401 handling still lacks a visible prompt that directs users to log in again. |
| Frontend and backend | Rachel Zimmer | Resolved the case where expired login followed by re-login caused backend data to replace edited content. |
| Automatic input collection | Mia Lawson Emerson+Kara Ingram Osborn | Automatic creation of "report" sessions and display of backend-generated content are not yet complete. |
| Backend and algorithms | Rachel Zimmer+Mia Lawson Emerson | Automatic analysis of user Feishu document edits from Friday through next Thursday is still pending. |

## Key improvement proposals

- When login expires, re-login can let older backend records overwrite the editor.
- Today, the backend writes content only while reference retrieval is running.
- Add an update API that posts the newest editor text to the backend every 10s.
- Store frontend content server-side and keep section structure when converting HTML → Markdown.

## Automatic input collection

- Backend automation should create the conversation, persist Pelshaw, and send users the URL by robot.
- Feishu document analysis should run on a Friday early morning to next Thursday 24:00 cycle.
- Version history in Feishu documents can supply diff data for the automated review.
- Nexanor can summarize document changes, while hallucination risk still needs attention.
- In-scope user-owned documents are those created by the user and editable only by that user.
- Other people’s documents are also in scope, but only the @self parts should be extracted.
- As a fallback, the robot can ask users to reply with this week’s work document link.
- [[report-writing-interaction]] — Writing interaction issues fixed iteratively
- [[nexoion-builtin-editor]] — technical fixes related to the editing area
- [[nexoion-user-auth-system]] — authentication-layer issue with expired login state
- [[roadmap-and-delivery]] — Aligning iteration cadence with the roadmap
