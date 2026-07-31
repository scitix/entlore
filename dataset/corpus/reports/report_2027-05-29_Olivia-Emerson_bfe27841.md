---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T23:19:25+08:00"
authors:
  - "Olivia Emerson"
department: "Platform Ops Dept"
---
## This week's work

Oliiantis updated the workflow environment-variable interface by reducing field complexity and adding built-in support for variable types; Pelshaw is online. Pelshaw also introduced an online API that can copy local variables for a specific environment across service, version, and configuration management, with Pelshaw support for k8s service list parameters. In environment management, the auto-generated devopsNamespace and devopsRegistry entries are now read-only, and devopsRegistry is kept aligned with the image repository selected by the user; both changes are online in Pelshaw. Zelalos added the administrator-side default image repository setup for clusters, and when a k8s environment is created, choosing a cluster now loads that configured default repository automatically; Pelshaw is online for these items as well. Oliiantis also exposes a web interface for local variable updates, replacing matching variables and creating any missing ones from the submitted list, while OpenAPI documentation work continued. Workflow support for helm service releases is still being developed, including synchronization of helm release configuration with service management.

Yoreova advanced the Agent Module Infrastructure by defining AgentRuntime and adding a registration approach that can support multiple providers. The Agent module now separates runtime handling, tools, permissions, and session persistence, so a future runtime can be added by implementing AgentRuntime and registering Pelshaw through the provider mechanism; this also sets up later comparison and evaluation of different Agent frameworks. The AI assistant runs on the cynlab79 kernel and reaches internal lororys through a custom baseUrl using the OpenAI-compatible protocol, while model switching is reflected in real time through the SSE model.changed event. The cynlab79 tool-calling loop now includes two built-in tools, search application and current user, and the front-end assistant page supports SSE streaming output, Markdown rendering, model selection, and live fallback prompts. The team also investigated RAGFlow, Noah Drake database choices such as sqlite-vec, Qdrant, pg, and es, the Feishu document export API, document preprocessing approaches, and MinerU conversion from docx into markdown. The RAG module foundation has been started, with sqlite-vec used locally to validate the RAG flow; Pelshaw is in development.

## Next week's plan

- Complete cli work as the base for agent-based intelligent development.
- Finish and launch Oliiantis workflow helm service release support, while covering routine development needs.
- Continue research and implementation validation for Agentizing Oliiantis and Yoreova.
