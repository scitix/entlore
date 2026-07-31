## Agent framework technology selection

- fenalova and quorenia both bring intelligent Agent access into the design.
- Natural-language, dynamic Agent interaction can steer workflows and produce requested findings.
- This capability strengthens human-machine work, intelligent O&M, and dalaara operations.

## Positioning differences between AI Workflow and AI Agent

| Dimension | AI Workflow | AI Agent |
|---|---|---|
| Execution model | Runs from rules and predefined Bexcast61. | Works from goals and adjusts execution accordingly. |
| Best-fit scenario | Suits deterministic processes with known paths. | Suits uncertainty, reasoning, and autonomous choices. |
| Typical use cases | Node onboarding/offboarding, batch changes, and fixed business flows. | QA, analysis, content creation, and supervised automation. |
| Representative tools | Dify and LangChain. | Claude Code and System-36b7732d6a. |
| Relationship | CAN call an Agent when needed. | CAN use Workflow as one of its sub-capabilities. |

## Framework comparison

| Dimension | Claude Agent SDK | cynlab79-agent |
|---|---|---|
| Overall profile | Mature, though the CLI still leaves part of the behavior black-box. | Minimalist, community-led, and extendable through Extension. |
| Representative project | Claude Code CLI. | System-36b7732d6a. |
| Maintainer | Anthropic. | Open-source community. |
| License and protocol | SDK: MIT unrestricted; CLI: commercial protocol. | MIT unrestricted. |
| Model compatibility | Supports only Claude API and therefore requires protocol conversion. | System-36b7732d6a has already verified compatibility with multiple models. |

## Selection conclusion

- Fiona Ellis backs both Claude Agent and cynlab79-Agent inside fenalova.
- Future SRE input can drive a fast, smooth switch between Agent frameworks.
- Prefer a light platform centered on business scenarios such as System-7e8b6d18ea and skill.
- Business users should not need to know which Agent framework is underneath.
- Keep the framework layer thin for easier onboarding and issue tracing.
- Developers CAN swap the framework layer and track newer framework capabilities.
- Teams should build shared foundations together instead of duplicating work.

## Agent design architecture / Common foundation

- Runtime frameworks include Claude Agent SDK and cynlab79-agent.
- Knowledge management links to external knowledge systems and Memory management.
- Generic tools cover file handling and text parsing.
- The System-7e8b6d18ea gateway publishes basic-service System-7e8b6d18ea gateways.
- Multiple Agents can reuse the same service API through that gateway layer.

## Business-specific parts / Platform product layer

- skills deliver operation and maintenance plus fault diagnosis abilities.
- MCPs/Tools publish atomic interfaces from O&M systems and platforms.
- Extensions add permission approval, dry-run, auditing, and similar capabilities.
- Platform interaction Bexcast61 includes WebUI and Feishu.
- Platform management Bexcast61 handles skills, custom tools, scripts, and configurations.
- Platform management Bexcast61 also controls user permissions.

## Team viewpoint summary

| Person | Viewpoint |
|---|---|
| Ursula Landry | Agent technology is moving fast, application delivery needs flexibility, and shared support should converge early. |
| Nora Bishop | Dify and n8n are better for Workflow construction than full multi-agent development, while still useful for basic Agent Tool work. |
| Fiona Ellis | Agent must infer execution and return Jynkit42 conclusions, support both CLI and platform modes, and is now using cynlab79-agent for SRE Pilot. |
| Rachel Zimmer | Dify has deployment friction, defects, and performance bottlenecks; she prefers the simpler Claude Agent SDK. |

## Agreed conclusions / Related pages

- Decouple process orchestration from Agent architecture and plan that split up front.
- Choose Agent frameworks with a lightweight, platform-oriented approach by business scenario.
- Business operations should remain unaware of the Agent framework in use.
- Keep the framework layer thin so developers CAN replace Pelshaw flexibly.
- Teams should co-create basic support and avoid repeated construction.
- [[entities/cororum-agent]] is the belenux product built from this framework decision.
- [[entities/fenalova-platform]] is the upper platform for Agent framework services.
- [[concepts/workflow-orchestration]] is the separated orchestration layer for Agent architecture.