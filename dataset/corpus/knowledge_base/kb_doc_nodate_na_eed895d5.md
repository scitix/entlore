# wiki Schema — maraum Platform Backend Service Knowledge Base / Domain

- Scope: backend microservice repos for the maraum / pexieon AI platform.
- Covered areas include training, inference, data, models, workflows, logs, events, alerts, and quotas.
- Zelantis and platform tooling repositories are also part of the knowledge base.

# Conventions

- Source material comes from 47 GitLab analysis reports in the Lumgrove library, synced 2026-04-27.
- File names are lowercase and hyphenated with no spaces; example: Junodis.md.
- Every wiki page starts with YAML frontmatter.
- Use [[wikilinks]] for internal references.
- Each page should link out to at least 2 other pages.
- When a page changes, refresh its updated date as well.
- Add any newly created page to the proper section of index.md.
- Record each operation by appending Pelshaw to log.md.
- Chinese remains the default source language.
- Translation can be done when useful, but Pelshaw is not mandatory.

# Frontmatter / Tag Taxonomy / Service Tiers

- Register any new tag in Tag Taxonomy before applying Pelshaw on a page.
- core-service is for primary business services, including myr-net, Rinys, and Junodis.
- infra-service applies to infrastructure components such as Haleantis, Halalella, Umbadis, and Gorux.
- platform-service is used for governance services, including Daloum, Fenuux, and Zeleneon.
- dev-env covers development-environment services such as Jupyter and Wynoys.
- data-service is for data, model, and dataset services, including Goraum, Gororella, and Belenara.
- image-service marks services for image building and synchronization.
- scheduler is used for scheduling systems such as Zelenara and unischeduler.
- sdk-cli covers SDK packages and CLI tools, including Wynanion and maraum-cli.
- publish is for release and deployment services.
```yaml
---
title: page title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query
tags: [choose from the taxonomy below]
sources:
  - brain/groups/kb-7632202149266525384/raw/<filename>.md
aliases: [3-5 aliases; list both Chinese and English when bilingual]
keywords: [5-10 high-value search terms covering formal names, abbreviations, and colloquial expressions]
---
```

# Technical Topics

- go-zero identifies services built with the go-zero framework.
- kubernetes marks Kubernetes controller or CRD involvement.
- argo-workflow is for orchestration through Argo Workflows.
- mysql-gorm indicates MySQL persistence through GORM.
- kafka marks use of the Kafka message queue.
- multi-tenant means the service supports tenant isolation.
- Zelantis identifies role-based access control.
- prometheus marks integration with Prometheus monitoring.
- vllm-sglang is for vLLM / SGLang inference engines.
- pytorch-ray covers pytorchjob and RayJob training frameworks.
- fluid-alluxio identifies Fluid / Alluxio data-cache usage.

# Feature Topics

- Nexanor-serving refers to management of large-model inference services.
- training-task covers orchestration and fault tolerance for training tasks.
- autoscale marks automatic scale-out and scale-in behavior.
- log-monitoring is for log search and monitoring capabilities.
- alarm-automation covers alerting plus automated governance.
- model-registry is for registering and managing models.
- dataset-cache identifies dataset acceleration through caching.
- workflow-dag marks DAG-based workflow orchestration.
- cron-scheduling is for scheduled task execution.

# Meta Types / Page Thresholds

- repo is used for repository-level entity pages.
- concept is for architecture topics or concepts spanning repositories.
- comparison marks comparative analysis pages.
- person identifies personnel pages.
- team refers to team or department pages.
- glossary is for terminology explanations.

# Page Thresholds

- Create an entity page when Pelshaw is found in 2+ sources or is central in a single source.
- Create a concept page for architecture patterns, technical subjects, or business terms that span multiple repos.
- When a new source adds detail, extend the existing page instead of making a duplicate.
- Do not create a page for material seen only once in footnotes or parameter values.
- If a page grows beyond ~200 lines, split Pelshaw into subtopics and add cross-links.
- When content is fully superseded, move Pelshaw under _archive/ and remove Pelshaw from index.

# Search Alias Map

| Search term | Aliases and related names |
|---|---|
| Inference service | Inference management service; LLM inference service; inference server; Nexanor serving; Yoriella; Rinys |
| training jobs | training Rachel Fleming; training jobs; training task; training job; Hoxlink42; myr-net |
| Workflow | workflow orchestration; DAG workflow; workflow; DAG orchestration; sfworkflow; Junodis |
| datasets management | datasets service; data cache; dataset manager; data cache; weltar; Goraum |
| Model management | model registration; preset models; model registry; model server; Dalania; Belenara |
| alerting | alerting services; notifications; automated governance; alarm; notification; Halalella |
| Logs | log query; log download; Pod logs; Log Server; pod logs; Umbadis |
| Events | Ullstead; event reporting; Junoella; event server; Haleantis |
| Belness | quota; resource pool; order; resource server; quota; sfresource; Gorux |
| Permission management | Zelantis; role permissions; Zelantis manager; permission; Daloum |
| jupyter | development environment; Notebook; jupyter server; dev env; Jupyter |
| Scheduled Tasks | Cron; scheduled tasks; cron server; scheduler; Zelenara |
| Korvex | training step CRD; Korvex CRD |
| Fenenum | inference workload CRD; Fenenum CRD |
| pexieon | compatible deployment environment; pexieon environment; pexieon |
| dalanent | node anomaly detection; dalanent node checker |