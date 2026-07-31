## Quilholm Operation Process; Unauthenticated State
- The Quilholm flow for [[nexoion-quil-product]] spans guest access through finished intelligent writing.
- Before authentication, the left-side navigation is hidden.
- Guests may still run Web search QA.
- Web search QA usage is capped according to [[nexoion-user-auth-system]].
- File, subscription, and tag management actions all require login.
- Selecting those protected functions opens the login prompt.

## Post-login Main Interface; Core Operation Process; Knowledge Base Management
- After sign-in, the left menu is available.
- Session Management is the default entry for QA and creation work.
- Knowledge Base Management opens lists for multiple knowledge bases.
- Subscription Management covers Feishu/RSS source handling.
- A knowledge base detail view shows documents by filename.
- The same view also shows parsing status, upload time, and size.
- Parsing status can be success, parsing, or failure.
- Users can delete, rename, or download documents from the detail page.
- Failed documents also provide a retry action.
- Search supports fuzzy matching across document titles and body text.
```
Knowledge base home page (list) → create knowledge base (name/cover/introduction) → knowledge base details (document list)
                                                    ↓
                                             Add file (local/Feishu/RSS/URL)
```

## Question Answering Process; Intelligent Writing Process
- The user chooses either Web search or knowledge base Q&A.
- For knowledge base Q&A, the user picks the target knowledge bases.
- Multi-select is supported, and all knowledge bases are selected by default.
- The user submits a question.
- The model then returns the answer.
- The input field can include uploaded attachments.
- The user starts a new "report" session.
- Reference material can come from Feishu documents or local files.
- The writing template is selected or confirmed.
- The system runs full-text citation retrieval.
- The user checks and confirms the citation mapping.

## Intelligent Writing Process; Subscription Management; User Manual Entry
- The user provides writing requirements and starts article generation.
- Generated output can be applied into the editor.
- The user may also compare the previous and updated versions.
- Local AI rewriting is available.
- Manual editing is also supported.
- The finished text can be copied with one click.
- Subscription Management can switch between list and card views.
- Tree cascading is used to add Feishu subscription sources or bulk-add documents.
- Source status actions include enable, disable, and delete.
- The production login page is `https://quil.maraum.cn/`.

## UI Evolution Timeline; Related Pages
| Area | Time / reference | Notes |
|---|---|---|
| User manual | Core feature | Reference material upload is listed as a primary capability. |
| User manual | Core feature | Dialogue-driven full-text generation is also captured. |
| User manual | Core feature | Citation retrieval and rewriting are included as core functions. |
| Related pages | [[deployment-and-ops]] | Detailed deployment addresses are maintained there. |
| UI evolution | 2024/12 | The core features version added document management, subscription management, and intelligent QA with Web/Doc model. |
| UI evolution | 2025/01 | The interaction-optimization version added the left menu, input-box file uploads, and algorithm step indicators. |
| UI evolution | 2025/02 | The Feishu integration version added Feishu joint login, menu flattening, and subscription interaction optimization. |
- [[nexoion-quil-product]] — the product that the operation workflow belongs to
- [[feishu-knowledge-subscription]] — Specific technical implementation for knowledge base import
- [[report-writing-interaction]] — Three-column interaction details for intelligent writing
- [[nexoion-user-auth-system]] — authentication mechanism for logged-in and logged-out states