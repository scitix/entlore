---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T19:51:30+08:00"
authors:
  - "Iris Otis"
department: "AI Compute Platform Dept"
---
## This Week's Work

Over the last two weeks, the team connected Claude Code to multiple common open-source models, refreshed the related docs, and finished Codex support for GPT Codex as well as those model options. We also kept improving Claude closed-source model capabilities while aligning open-source integrations to the Anthropic protocol, supporting the OpenAI Responses API, and bringing GPT Codex online on lororys. GPT Codex was integrated with Codex and documented in detail; Codex primarily offers stable access through Responses API, while open-source models still need adaptation because tool calls and output formats are not fully consistent. To bridge that gap, the team used protocol conversion plus external System-7e8b6d18ea server tools, reused Codex’s unified scheduling and tool execution paths, and lowered the future cost and change scope for adding or replacing open-source models; for Claude closed-source services, we also improved retry handling, simplified command execution, strengthened log persistence, and reviewed path latency after users reported slowness, with the data showing a need for faster and more stable model agents.

## Next Week's Plan

In the next biweekly cycle, the team will focus on stronger adaptation for mainstream model protocols, with Gemini protocol support and user documentation improvements as key items. We will continue monitoring feedback from released closed-source models and make fast optimizations where issues appear. Once procurement is complete or an agent vendor is selected, the team will move quickly on supplier replacement to improve the user experience. After protocol support and alignment are ready, we will connect System-36b7732d6a and evaluate the feasibility and risk of using Claude subscriptions instead of API access based on cost and availability.

## Coordination and Help Needed

No coordination is needed at this stage. No additional help is being requested.