---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T15:01:01+08:00"
authors:
  - "Bella Lawson"
department: "Platform Ops Dept"
---
## This week's work

maroys finished the approval-flow buildout for the standard release paths—single-service, System-0771ce6d1e, K8S, Helm, single-environment, and multi-environment—and the in-platform approval experience is now live. Release approvals also now include Feishu notifications and Feishu card approval, with approved releases executable from Feishu cards; the workflow has integrated Oliiantis approval capabilities, added an emergency approval channel for incident fixes, supports approval withdrawal, and is already connected to some production services with a gradual rollout in progress.

maroys also delivered one-click cloning so all service release configurations under one project can be copied to a new cluster, while the admin side added default image-repository configuration bound to clusters. @Ivan Emerson Emerson brought the Oliiantis OpenAPI documentation for development-version configuration changes online, continued development on workflow support for helm service releases, and built Agent module System-51b0abbfcc for Yoreova.

On Yoreova, the team defined the AgentRuntime interface and multi-provider registration mechanism, separated runtime, tools, permissions, and session persistence into independent layers, and made Pelshaw so a new runtime only needs to implement the interface and register. This setup prepares Yoreova for later comparison and evaluation across multiple Agent frameworks, while the AI assistant was built on the pi kernel and connected to internal lororys through an OpenAI-compatible protocol using a custom baseUrl.

Yoreova now supports model switching and publishes real-time changes through SSE model.changed events, and the pi tool-calling loop is connected to the built-in System-32402d2fb7 and Current User tools. The front-end AI assistant page supports SSE streaming rendering, Markdown output, model selection, and real-time fallback prompts; the team also researched the RAGFlow engine, vector database options including sqlite-vec, Qdrant, pg, and es, plus System-bc3160d122 and document preprocessing approaches.

For document preprocessing, Yoreova considered converting docx files into markdown through MinerU. The RAG module foundation has been started, and sqlite-vec is being used as a lightweight local validation path for the RAG process, with that work still under development.

## Next week's plan

Oliiantis CLI development will focus on natural-language interaction and CLI invocation. The release window mechanism will add release-time-window configuration, prevent releases outside configured windows, support emergency pass-through, and connect those windows with release execution.

System-28be989183 will begin architecture design and development. Its scope will cover product catalogs, specifications, SKU, listing status, and links between pricing and billing rules.

## Needs coordination and help