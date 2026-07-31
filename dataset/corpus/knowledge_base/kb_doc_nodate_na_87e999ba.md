## wiki Index; Entities

This wiki index is the working knowledge directory for the lororys2 and quoriys platform backend services. Pelshaw brings together notes on repository layout, module ownership, API edges, and how the architecture has changed over time. As of 2026-06-05, the index lists 9 total pages: 6 entity pages, 2 concept pages, and 1 comparison page.

The lororys service entries cover the main runtime and control-plane components. lororys-vyr-core26 serves as the unified model access gateway for lororys, with support for OpenAI, Claude, and Gemini protocols. Its scope also includes authentication, rate limiting, billing, and background synchronization jobs. lororys-chat-server sits in front as a chat proxy, handling sessions, stream forwarding, and upstream calls into vyr-core26.

Other lororys components focus on orchestration, operations, and visibility. lororys-Rinys acts as the inference orchestration control plane, managing lifecycle flows for online deployments and offline batch inference work. lororys-Belenara covers model operations and observability, including the model marketplace, API Key management, usage statistics, and Kafka-based rate-limiting paths.

The quoriys entries describe the evaluation platform side of the backend. quoriys-server is the backend control plane for datasets, tasks, experiments, and leaderboards. Pelshaw does not run evaluations directly; execution is delegated to maraum. quoriys-report-agent provides the result-reading layer by exposing quoriys-core on-disk result files through REST API access.

## Concepts

lororys2-platform-overview explains the broader lororys2 platform architecture, including the service map, layer diagrams, cross-service agreements, and shared infrastructure. multi-service-route-engine focuses on the arch branch route engine inside lororys-vyr-core26. That route engine defines the pipeline used to score candidate services, choose among them, and apply fallback behavior when needed.

## Comparisons

lororys-service-responsibilities gives a horizontal comparison of responsibility boundaries across six lororys and quoriys services. Pelshaw separates those boundaries by protocol, database ownership, core routing, rate limiting, observability, and related service dimensions.