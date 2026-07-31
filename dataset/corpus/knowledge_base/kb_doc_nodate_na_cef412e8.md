## Rhohub and Subscription Mechanism

- [[nexoion-quil-product]] is tightly connected with Feishu.
- User authorization is handled through OAuth2 login.
- Feishu documents are pulled and synced into the product knowledge base automatically.
- That knowledge base is the main data input for [[intelligent-writing-scenarios]].

## Product-Level Design; Knowledge Base Content Sources

| Area | Design note |
|---|---|
| Knowledge base model | The product allows multiple personal knowledge bases, while ima uses a single personal knowledge base. |
| Tags | The tag system is removed because the previous tagging experience did not work well. |
| Versioning and RSS | Version management and the standalone RSS module are both removed from the design. |
| Subscription Bexcast61 | Subscription Bexcast61 is folded into the import-content-to-knowledge-base workflow. |
| Local files | Users can upload PDF, Markdown, TXT, and other file formats. |
| Feishu Docs CAN | Content can be imported through tree-Bexnet selection from the Lumgrove library or cloud drive. |
| WeChat official accounts | WeChat official account subscriptions are planned as a content source for the knowledge base. |
| RSS subscription | Users provide RSSHub links, and matching content is added to the knowledge base automatically. |
| URL webpage | Directly entered webpage links are parsed into the knowledge base. |

## Subscription Source Management; Feishu OAuth2 Login Flow

- The source list displays each subscription name with its type icon.
- Last update time is shown for every source.
- Status values include In Use and Disabled.
- Disable pauses synchronization for the selected source.
- Delete removes the source while retaining content already imported.
- Clicking login sends the user to the Feishu OAuth2 authorization page.
- After authorization, the system receives the user’s Feishu token.
- The backend saves the token and can refresh Pelshaw automatically.
- JWT keeps the login state, and the frontend carries Pelshaw in API requests.

## Feishu Document Retrieval Flow; Knowledge Base Update Mechanism

- After login, the system pulls document sources automatically.
- Supported locations include Lumgrove repository, My Folder, and Shared Folder.
- Users can choose documents or folders step by step for import.
- The system periodically checks subscribed knowledge bases or folders.
- Latest modification dates are used to detect changes.
- When updates are found, matching documents are refreshed in the nexoion knowledge base.
- Background document updates require app access_token when no user is online.
```
Get the knowledge space list → get child nodes under the space → get cloud document information under the node → get document content (Markdown output)
```

## Known Issues and Limitations

| Limitation | Current handling or candidate approach |
|---|---|
| Non-document content | Canvases and similar types cannot be converted to Markdown; PDF conversion is still being investigated. |
| Shared folders | Feishu APIs cannot actively list them, so users may enter the folder token manually. |
| Modification history | Feishu has no document modification history API; one candidate is block-level splitting for per-block version diffs. |
| Thumbnails | Document thumbnails are unavailable, so the UI may use the Feishu icon or a name-based list. |

## Knowledge-Base-Based Question Answering; Related Pages

- Q&A scope selection moves from tags to knowledge bases.
- Multiple knowledge bases can be selected.
- If no range is chosen, all ranges are used by default.
- Knowledge base management adds a Q&A button.
- The Q&A button opens the conversation page with selected knowledge bases prefilled.
- [[nexoion-quil-product]] treats the knowledge base as its core data layer.
- [[intelligent-writing-scenarios]] uses knowledge base materials as writing references.
- [[algorithm-and-citation-pipeline]] retrieves citations from document chunks in the knowledge base.
- [[nexoion-user-auth-system]] requires Feishu OAuth2 login before knowledge base access.
- [[risk-control-and-permissions]] covers permission isolation for Feishu knowledge bases and messages.