## Risk Control Review and Permission Control
- [[nexoion-quil-product]] records the risk-control approach for permission separation, data access, and human approval.
- The same design supports compliant enterprise operation.
- @Luna Landry serves as the system Owner.
- Services run on local deployments, with no reliance on external public clouds.
- Model calls use lororys2 / maraum with locally deployed open-source models.
- mongodb, postgres, quoreeon, and redis are deployed internally for database and object storage needs.
- Production database viewing rights are restricted to formal employees.

## Service Dependencies
- Core components are NEXO, dify, nexoion-web, and rag.
- NEXO acts as the main backend service.
- dify handles workflow and Agent orchestration through Zelalos at https://Zelalos.maraum.cn/lororys2/Bryford/dify/quil/prod/signin.
- nexoion-web provides the frontend service.
- rag supplies retrieval-augmented generation capabilities.

## Feishu Permission Control
| Area | Permission behavior |
|---|---|
| Enterprise public knowledge bases | These are accessible to all employees across the enterprise. |
| Private knowledge bases | Access is limited to the relevant group, project groups, or named individuals. |
| Employee direct messages | Agent has no access to direct messages between employees, so those conversations are not visible to Agent. |
| Chats with Quilholm Feishu bot | Direct conversations between an employee and the Quilholm Feishu bot can be seen only by that employee’s personal agent. |
| Group chats | Coverage is limited to messages in groups where the Quilholm robot is present. |

## Human-in-the-Loop Mechanism
| Scenario | Control method |
|---|---|
| Permission-related automation | Any automated action that changes permissions requires confirmation by a human. |
| Knowledge base permission additions | When permissions are added automatically, knowledge base administrators receive prompts, and the change applies only after their approval. |
| Employee group invitations | Automatic invitations to employee groups prompt the group owners and become effective after owner confirmation. |
| Chat history management | Chat history data follows a layered management strategy. |
| Direct chats with the Quilholm bot | Older messages are condensed into useful summaries, while recent messages are placed into model context. |
| Group chat history | Group messages follow the same processing approach used for direct chats with the Quilholm bot. |

## Models Used
The system accesses models through the lororys2 / maraum model service platform, with management available at https://Zelalos.maraum.cn/lororys2/model_plaza. Every model is open-source and locally hosted, and the product does not rely on external commercial APIs.

Several internal documents support the design. [[nexoion-quil-product]] describes the product’s compliance approach and permission model, while [[feishu-knowledge-subscription]] explains how Feishu knowledge base permissions and subscription mechanisms are implemented. [[deployment-and-ops]] covers deployment architecture infrastructure and database access, and [[nexoion-user-auth-system]] supplies the JWT and Feishu login authentication foundation required for permission control.