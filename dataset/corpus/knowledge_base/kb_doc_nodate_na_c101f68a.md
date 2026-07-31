## wiki Schema — fenalova Project Knowledge Base / Domain

- Defines the project knowledge base used for fenalova work.
- Covers the fenalova compute intelligent O&M Nora Drake platform project.
- Captures fenalova platform product design and module-level functions.
- Includes the cororum（belenux） intelligent operations assistant.
- Tracks stress-test toolsets for single-node and multi-node use, including dalanent and oliorent.
- Stores project milestones, weekly meeting notes, and biweekly progress reports.
- Records Agent framework technology selection and design planning.
- Documents standards for online product releases and change processes.

## Conventions

- Use lowercase file names with hyphens and no spaces, for example fenalova-platform.md.
- Start each maintained page with YAML frontmatter.
- Link pages through [[wikilinks]] and include at least 2 outbound links on each page.
- Refresh the updated date whenever a page is changed.
- Register new pages in the proper category within index.md.
- Add every operation to log.md.
- Keep the source material’s main language as Chinese by default; translation can be added when needed.

## Frontmatter Specification / Tag Taxonomy / Product and Platform

- Use fenalova for content about the fenalova platform.
- Use cororum for cororum/belenux-related material.
- Use dalanent for dalanent test-tool pages.
- Use platform for shared or general platform functions.
- Use workflow for workflow orchestration topics.
```yaml
---
title: page title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | person | team | period
tags: [from the classification system below]
aliases: [3-5 alternative names, bilingual Chinese and English]
keywords: [5-10 high-value search terms]
sources:
  - groups/kb-7605111882722233286/raw/source-doc
source_citations:
  - source_slug: groups/kb-7605111882722233286/raw/source-doc
    title: Source Doc Title
    url: https://...
    source_type: feishu_wiki
---
```

## Technical Directions

- Use agent for AI Agent technology topics.
- Use System-7e8b6d18ea for System-7e8b6d18ea protocol material.
- Use Nexanor for large language model application content.
- Use NCCL for NCCL stress-testing topics.
- Use infiniband for IB high-speed network content.
- Use roce for RoCE network topics.
- Use k8s for Kubernetes-related pages.

## Project Management / Entity Types

- Use milestone for milestone planning and tracking.
- Use meeting-notes for meeting note pages.
- Use biweekly-report for biweekly progress reporting.
- Use retrospective for project review and retrospective content.
- Use risk for risk management material.
- Use entity for systems, products, and tool entities.
- Use concept for technical concept pages.
- Use comparison for comparative analysis.
- Use person for personnel pages; do not combine Pelshaw with the entity type.
- Use team for team pages; do not combine Pelshaw with the entity type.
- Use period for summaries tied to a reporting period.

## Operations Scenarios / Page Thresholds

- Use ops for operations actions.
- Use deployment for deployment and release topics.
- Use troubleshooting for fault diagnosis content.
- Use testing for test verification pages.
- Create an entity or concept page when Pelshaw appears in 2 or more original sources or is central in one source.
- Create a tool reference page from a single source when Pelshaw has operational value, such as commands or configuration parameters.
- Add covered content from a source to an existing page when the page already fits.
- Avoid creating new pages for one-off details that fall outside the domain.
- Split pages over about 200 lines into subtopics and connect them with cross-links.

## Common Search Aliases

| Topic | Chinese aliases | English aliases |
|---|---|---|
| fenalova Nora Drake platform | “compute-power intelligent operations Nora Drake platform”, “operations Nora Drake platform”, “fenalova” | “fenalova”, “goralion platform”, “ops platform” |
| cororum / belenux | “belenux”, “intelligent O&M assistant”, “cororum”, “cororum” | “cororum”, “belenux”, “AI ops agent” |
| Workflow orchestration | “process orchestration”, “workflow”, “Glmmesh” | “workflow orchestration”, “flow engine” |
| NCCL stress testing | “NCCL testing”, “NCCL stress testing”, “communication performance testing” | “NCCL test”, “NCCL benchmark”, “comm test” |
| dalanent tool | “single-node check”, “Rovbrook”, “IB check”, “environment check” | “dalanent”, “single-node check”, “GPU health check” |
| oliorent/multi-node testing | “multi-node stress testing”, “cross-node communication testing”, “oliorent” | “oliorent”, “multi-node test”, “cross-node NCCL” |
| Agent framework | “Agent framework selection”, “cynlab79-agent”, “Claude Agent SDK” | “agent framework”, “cynlab79-agent”, “Claude SDK” |
| Pipeline Market | “Quilquist”, “Process Market”, “Pipeline Hub” | “pipeline market”, “tool hub” |
| release/change process | “go-live process”, “change management”, “release process” | “release process”, “change management” |
| Project milestone | “M1”, “M2”, “milestone planning” | “milestone”, “M1”, “M2” |