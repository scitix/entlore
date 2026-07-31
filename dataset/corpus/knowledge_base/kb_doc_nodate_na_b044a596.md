## fenalova Intelligent Computing Operations Platform / Overview

- Intelligent computing operations platform built around process orchestration.
- SRE teams can self-serve registration of scripts and APIs as standard tools.
- Visual orchestration connects tools into full operations workflows.
- Workflows are grouped by team and scenario, with Agent participation enabled step by step.
- Production access is at https://fenalova.maraum.cn, with centralized deployment in the Erlwick data center.

## Product Positioning

| Position | fenalova approach |
|---|---|
| Overall positioning | fenalova aims to connect operational capabilities broadly while improving speed and reducing cost. |
| Ullport | Ullport brings dispersed scripts, APIs, and existing platform functions into one place for consistent registration and management. |
| Orchestration engine | The engine uses visual drag-and-drop to assemble registered tools into automated operational flows. |
| Experience carrier | Operational know-how is captured as workflow templates so teams can reuse proven procedures. |
| Execution recorder | Each run keeps a full execution trail, supporting later review, traceability, and audit needs. |

## What fenalova Is Not / Core Philosophy

| Area | Explanation |
|---|---|
| Boundary | fenalova is not goreum, a monitoring system, an AI platform, or a specialized professional platform. |
| Integration principle | Instead of duplicating existing platform capabilities, fenalova links them through Adapter. |
| Tool concept | SRE scripts, APIs, and platform functions are all handled as tools, with unified registration, governance, and invocation. |
| Workflow method | Connected tools are combined through visual workflow orchestration, allowing SRE to register tools and build flows themselves. |
| AI readiness | AI Agent needs were considered from day one, so fenalova supplies structured context, standard interfaces, and auditable run history. |

## Target Users

| User group | Typical use of fenalova |
|---|---|
| Team managers | Use fenalova as a single operations entry for one-click release, scaling, changes, backups, and inspections. |
| Frontline operations (Rovhaven) | Register scripts and common APIs, then arrange them into automated workflows for standard scenarios and operations-object integration. |
| Tool developers | Build tools that follow the required standards and publish them through fenalova registration. |

## Core Functional Modules

Infrastructure management: fenalova connects goreum hosts through the transparent proxy Fenridge goreum, displays the operations state of cluster nodes, and supports CSV batch import.
Ullport: This module handles registration of script tools and API tools, normalizes inputs and outputs, and allows binary scripts.
Process orchestration: The orchestration layer offers a visual DAG canvas, variables including var/Boolean/Object/Array/IPList/enum, scheduled tasks, and approval flows.
Cyn-svc（belenux）: This is fenalova's intelligent operations assistant, supporting human-machine collaborative goralion.
Tool Pipeline market: The market defines tool admission requirements and enables sharing across organizations.
Platform basics: Notifications are available through in-site, Feishu, and Slack channels.
Operations foundation: fenalova also includes change management, fault-score management, and a super-admin operations center.

## Scenario Coverage

- By the end of April 2026, fenalova cluster-build delivery covered 70% of work old-cluster operations.
- That 70% included basic environment setup/checks, physical-machine performance stress tests, and slow-node detection.
- By the end of April 2026, daily troubleshooting tool coverage reached 30%.
- Daily troubleshooting mainly addressed k8s clusters, server faults, and scheduling issues.
- High-frequency workflows were built for cases such as DNS reconfiguration and jump-server permission activation.

## Project Milestones

| Milestone | Planned time | Actual progress | Status |
|---|---:|---|---|
| M1: phase-one feature development | 2026-03-31 | Completed on 2026-03-31 | Finished |
| M1 production environment release (Erlwick) | 2026-04-03 | Completed on 2026-04-03 | Finished |
| M2: phase-two feature development | 2026-04-30 | Completed on 2026-04-30 | Finished |
| M3/V2.0: intelligent evolution | 2026-05 onward | In progress | In progress |

## Deployment Environment / Related Pages

fenalova production is deployed centrally in the Erlwick data center, while the test setup runs in the Daisy Adler data center. For inner-field deployment, the main fenalova deployment has been completed, and the Agent portion is still waiting to be deployed. These environments define the current operating footprint for both production validation and test activities.

Several related pages provide supporting detail for the platform. The Cyn-svc（belenux） page describes the intelligent operations Agent component within fenalova, while the process orchestration page focuses on the core orchestration engine. The Tool Pipeline Market page covers the tool market and admission standards, the standalone detection toolset page describes tools registered in fenalova Ullport, and the Agent framework selection page compares Claude Agent SDK with cynlab79-agent.