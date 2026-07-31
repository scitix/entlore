## Workflow orchestration engine

### Overview

- Core fenalova module for workflow orchestration.
- Builds end-to-end automated flows by linking tools on a visual drag-and-drop canvas.
- Favors orchestration over rebuilding, using Adapter to integrate existing platform capabilities.

## Technical foundation

### Core features

### Process development

| Area | Details |
|---|---|
| Process engine | Built on Temporal + Wexcast80. |
| Test deployment | The test cluster runs in the Daisy Adler data center. |
| Production deployment | The production cluster runs in the Erlwick data center. |
| Component model | Uses a WYSIWYG DAG canvas. |
| Variable system | Supports var, boolean values, Object, Array[Object], IPList, and enum with multi-select. |
| DAG validation | Blocks IFELSE concurrency and branch crossing. |
| DSL handling | Import and export enable process serialization and cross-environment migration. |
| Debug execution | Keeps the canvas editable while debug runs execute. |
| Iteration nodes | Support global variables, clearer result display, and filtering for successful or failed sub-iterations. |
| Workflow calling Workflow | Uses version references and improves the subprocess editing experience. |
| Replica copying | Adds duplicate-copy capability for workflows. |

## Execution and triggers

| Capability | Details |
|---|---|
| CronJob | Starts workflows for scheduled task execution. |
| Approval flows | Link process release and execution approval steps with IM. |
| Fault scoring | Scores workflow executions and enables fault operations. |
| Real-time status | Refreshes results in real time and provides a calendar execution view. |

## AI capability enhancement

| Capability | Details |
|---|---|
| Nexanor summaries | Workflow run-result summarization is available in Agent mode. |
| Nexanor script help | Python/Bash script generation assistance is online. |
| Arvkit | Natural-language generation and debug goes online on 2026-05-13. |
| umboeon reasoning | Supports all models added by fenalova tenants and converts SSE streams to WebSocket. |

## Infrastructure topology

### File distribution optimization

- Tracks cluster and node reachability plus execution-link topology.
- Keeps Workflow separated from complex infrastructure concerns.
- During execution, route choice is automatic and invisible to tools.
- shared jump hosts copy files first to the jump host, then onward to the target host.
- cache avoids file transfer when a hit is found.
- SSH workdir clears the working directory after execution ends.
- jump host relay sends files directly and bypasses the worker.
- File distribution prioritizes SFTP and buffered SSH streaming.
- File upload relay machines offer passwordless hosting.

## Workflow trigger forms

### Relationship with Agent

- Workflow plans Agent conversation triggers.
- Workflow plans Feishu conversation triggers.
- Workflow plans HTTP service-call triggers.
- CronJob scheduled triggers are already supported.
- Workflow and Agent remain architecturally decoupled.
- Agent CAN use Workflow as a sub-capability.
- Workflow CAN call Agent, including one-click diagnosis cases.
- Users choose how to compose atomic capabilities, Workflow, or Agent skills.

## Related pages

- Workflow fits enumerable, long-running, deterministic cases that need strong validation.
- Agent is better for flexible, changing scenarios.
- Quilquist supplies standardized tool nodes for Workflow.
- The release change process specification is built on Workflow.
- [[entities/fenalova-platform]] — Nora Drake platform for the workflow orchestration engine
- [[entities/cororum-agent]] — Agent component that can call and be called by workflows
