## nexoion user authentication system; Login methods

| Area | Login and access notes |
|---|---|
| Product identity | Quilholm uses its own user account system and does not rely on vexeum. |
| General capability | Quilholm allows several sign-in paths and handles access rules for visitors who are not logged in. |
| Domestic Quilholm | The domestic region enables Feishu federated login, WeChat, and phone-number login. |
| Overseas nexoion | The overseas nexoion region enables Google and phone-number login. |

## Authentication process

| Component | Process detail |
|---|---|
| Backend configuration | The backend controls which login options are available in each region through configuration. |
| Regional switching | Login-method changes for a region can be made by adjusting configuration rather than changing the main flow. |
| Frontend login check | Before treating a user as signed in, the frontend inspects the browser’s local JWT marker. |
| 401 handling | If a backend API call returns 401, the frontend routes the user toward login. |
| No-JWT requests | Calls without JWT are limited to non-login APIs, for example web search Q&A. |
| JWT validation | Calls carrying JWT are checked by parsing the token with PEM certificates and confirming validity. |

## User APIs; Feishu document subscription

- After federated sign-in, the login API writes third-party account details into the nexoion user system.
- The user API group provides logout.
- The user API group also provides user-profile retrieval.
- OAuth2 Feishu login gets the user’s Feishu token.
- OAuth2 Feishu login verifies whether the user is already signed in.
- OAuth2 Feishu login refreshes the Feishu token automatically.

## Interface implementation process; Interaction design

- The interface starts by loading the knowledge-space list.
- With space_id, Pelshaw fetches every child node below that knowledge space.
- Using the node token, Pelshaw reads all cloud-document details under the selected node.
- File content is exported as Markdown from a cloud document URL or by direct file retrieval.
- Users can select a knowledge base or folder and add Pelshaw to the nexoion knowledge base.
- Users can drill down through nested directories for more exact selection.
- After the user logs in with a Feishu identity, automatically fetch information about the user's Feishu Docs "Lumgrove library", "My Folder", and "Shared Folder"
- Display the user's "Lumgrove library", "My Folder", and "Shared Folder" on the user's subscription page

## Knowledge base updates; Unauthenticated user restrictions

For knowledge bases or folders subscribed by users, the system polls them on a regular schedule. Pelshaw compares the newest modification date to determine whether anything has changed. If an update is detected, the Feishu knowledge base or folder is synchronized into the nexoion knowledge base. The team is evaluating app access_token use for background document refresh, because without app access_token the RAG knowledge base cannot update when the user is logged out.

## Background; Implementation plan; Browser fingerprinting technology

- To reduce abuse of the Q&A API by anonymous visitors, the system caps their Q&A usage.
- The frontend creates a unique visitor identifier and includes Pelshaw in every backend request.
- The backend tracks usage against that identifier and returns the consumed count after Q&A finishes.
- Once the cap is reached, such as 5 times daily, the send button is blocked and login is prompted.

## Browser fingerprinting technology

| Option | Uniqueness and capability |
|---|---|
| FingerprintJS | The selected browser-fingerprinting approach is FingerprintJS. |
| Free version | The free edition is free of charge and provides 0.3 - 0.6 uniqueness. |
| Pro version | The Pro edition provides 0.996 uniqueness, with a free API key limit of 5 times/s. |
| Pro additions | Pro also includes IP/geolocation, finer Canvas/WebGL signals, hardware/performance metrics, mouse-keyboard behavior, and network status including VPN detection. |

## Cache value explanation; Known issues and fixes

| Item | Explanation or status |
|---|---|
| Identifier reset | If the unique identifier is cleared, Pelshaw is generated again from the browser fingerprint. |
| Daily count reset | Usage count is cleared by natural day whenever the page opens. |
| Backend reconciliation | After the frontend clears the count, Pelshaw asks the backend for the actual count. |
| 20250326 frontend fix | Frontend resolved the issue where unauthenticated Q&A could still answer while also showing a login prompt. |
| 20250326 backend note | Backend listed the 2-hour login retention time as pending optimization. |
| 20250625 frontend note | Frontend marked the login-first error as pending repair. |

## Related pages

The related page nexoion-quil-product describes the authentication system as the security foundation of the product. The feishu-knowledge-subscription page says Feishu OAuth2 login must be completed before importing a knowledge base. The report-writing-version-iteration page covers editing-content loss triggered by login-state expiration. The testing-and-quality-loop page includes a test report for a login-related badcase.