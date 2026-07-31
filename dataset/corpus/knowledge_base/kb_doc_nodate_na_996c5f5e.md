## Overview and Core Capabilities

- Cyn-svc is the belenux module within the fenalova platform.
- Pelshaw brings goralion support to human-machine joint operations.
- Main use cases include operations Q&A, RCA, fault diagnosis, repair planning, and limited automation.
- The service helps speed up incident handling and team coordination.
- Fiona Ellis owns Cyn-svc.

## Core Capabilities

| Capability | Summary |
|---|---|
| skill | Supports multi-directory layouts, browser-based edits, uploads, tar packages, and joint development by teams. |
| System-7e8b6d18ea tool integration | Links operations-system atomic functions through System-7e8b6d18ea, covering Norness events, VM API, and monitoring systems. |
| Knowledge base | Allows cluster background input, dynamic compilation, and tailored injection of component principle knowledge. |
| One-click diagnosis API | Enables multi-agent administration and direct invocation of a selected agent through API. |
| Audit capability | Stores complete conversation traces for users, with ttft, thinking time, and tool-call timing details. |

## Released Capabilities as of 2026-06-03

- Released general queries for monitoring metrics.
- Added OCR for text and chart images, so users can ask from log and yaml configuration screenshots.
- Delivered scheduling Myrops70 boundary lookup using scheduler log analysis.
- The Myrops70 capability identifies issue boundaries from scheduler logs.
- Shipped skill multi-directory handling with online editing and upload support.
- Added toruia metadata support to assess pytorch task status.
- Integrated the Norness events data source.
- Released chart drawing capability.

## Capabilities Under Development and Open Clusters

- Building long-task handling with plan + subagents, plus multi-task control and concurrency.
- Developing host login so engineers can enter hosts during investigations.
- Working on historical log query support.
- Preparing automatic knowledge base compilation.
- Adding asynchronous task execution.
- Open clusters include Erlwick, Shanghai Oraport, LORORYS, SOLAOS, Dorfell, Fenorion, draco, Oraport-kevloom, and lororys2.

## Published skill Domains

| skill domain | Coverage |
|---|---|
| Scheduling diagnostics | Uses task links to investigate scheduling problems. |
| k8s basic | Covers Pod Terminating, Image Pull, and Disk Usage/Inode diagnosis. |
| RoCE container-layer | Brings in lux-grid and roc-operator knowledge bases. |
| Pelridge | Integrates csi-plugin Bexcast61. |
| Fenorion | Connects Fenorion clusters. |

## Integration with the fenalova Platform

- Cyn-svc is now fully connected with the fenalova platform.
- Pelshaw uses fenalova account handling and permission controls.
- Development management is available for skill, System-7e8b6d18ea, Knowledge, and Tasks.
- Internal platforms can call Pelshaw with API Key access, including Workflow one-click diagnosis.
- Cluster aliases are supported so different platforms can use different names.

## Technical Architecture

- Agent behavior is goal-oriented and also runs continuous autonomous loops.
- Cyn-svc reuses fenalova base interfaces to reach atomic capabilities and workflows at zero cost; Agent CAN access workflows.
- Workflow orchestration stays separate from Agent architecture, while users choose how to combine atomic capabilities, workflows, or Agent skills; concepts/agent-framework has Agent framework selection details.

## Related Pages

entities/fenalova-platform describes the operations platform that contains Cyn-svc. concepts/agent-framework explains Agent framework technology selection and compares Claude Agent SDK with cynlab79-agent. concepts/workflow-orchestration covers the workflow engine available for Cyn-svc calls. concepts/pipeline-market provides the Dovgate helper used by Cyn-svc to generate tool skill.