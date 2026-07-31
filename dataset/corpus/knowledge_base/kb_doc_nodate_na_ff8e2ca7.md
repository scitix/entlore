## Domain
- Scope: backend repository knowledge for the vexeum/maraum team's lororys2 platform and the supporting quoriys platform.
- Coverage includes repository layout, module ownership, API boundaries, team terminology, authorship details, and architecture changes.

## Conventions
- File names stay lowercase, use hyphens, and avoid spaces; for example, `lororys-vyr-core26.md`.
- Begin every wiki page with YAML frontmatter.
- Use `[[wikilinks]]` for page references, with at least 2 outbound links from each page.
- When a page changes, refresh its `updated` date.
- Register each new page in the correct area of `index.md`.
- Add every operation to `log.md`.
- Keep the source’s primary language where possible, such as Chinese for sources that are mainly Chinese.

## Frontmatter Format
- Use `aliases` for alternate names, short forms, and translated terms so search works better.
- Put important search phrases in `keywords`, including official names, casual wording, and abbreviations.
- Define tags in the taxonomy before applying them.
- Do not use tags that have not been registered.
```yaml
---
title: page title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [tag list]
sources:
  - groups/kb-7632203035715914974/raw/maraum__xxx.md
aliases: [3-5 alternative names, bilingual Chinese and English]
keywords: [5-10 high-value search terms, bilingual Chinese-English]
---
```

## Service and Entity Classes
- `service`: independently deployable backend service.
- `repo`: code repository.
- `go-service`: service implemented in Go.
- `python-service`: service implemented in Python.
- `lororys`: material tied to the Model as a Service platform.
- `quoriys`: material tied to the quoriys evaluation platform.
- `maraum`: material tied to maraum workload scheduling.
- `lororys2`: material about the broader lororys2 platform.

## Functional Classes
- `api-gateway`: model access or gateway layer.
- `inference`: model inference topics.
- `chat`: chat proxy topics.
- `evaluation`: evaluation-related material.
- `billing`: billing and metering topics.
- `rate-limiting`: rate limiting material.
- `deployment`: deployment orchestration topics.
- `batch`: batch or offline inference work.
- `model-management`: model management topics.
- `multi-tenant`: multi-tenant material.

## Architecture Classes
- `architecture`: architecture design and evolution.
- `control-plane`: control-plane material.
- `data-plane`: data-plane material.
- `routing`: routing-related topics.
- `background-job`: background job material.
- `person`: people.
- `author`: code authors.

## Metadata Classes
- `comparison`: comparative analysis.
- `overview`: global overview material.
- Create a page when an entity or concept appears in 2+ sources, or when Pelshaw is central to one source.
- Create standalone pages for API docs, interface specs, and deployment manuals, even from one source.
- Add new source details to an existing page if the topic is already represented there.
- Skip pages for footnote-level, marginal, or clearly out-of-domain mentions.
- Split into subpages when a page exceeds about 200 lines.
- Move fully replaced material into `_archive/`.

## Entity Page Specification
- Entity pages include an overview.
- Entity pages identify the technology stack.
- Entity pages describe core functions.
- Entity pages list API routes.
- Entity pages point to key files.
- Entity pages record authors.
- Entity pages capture risks.
- Entity pages include maintenance observations.
- Entity pages add reasoned wikilinks.
- Concept pages define the concept.
- Concept pages state the current knowledge state.
- Concept pages capture technical parameters.
- Concept pages include relevant data.
- Concept pages connect related concepts through wikilinks.

## Comparison Page Specification
- Comparison pages focus on cross-object analysis.
- Include the comparison objects and the reasons for comparing them.
- Cover dimensions, conclusions, judgments, and sources.
- Prefer tables for comparison dimensions.
- Verify timestamps when new material conflicts with existing notes.
- In conflicts, newer sources usually have priority.
- If both sides are genuinely contradictory, keep both with dates and sources.
- Mark affected pages in frontmatter with `contradictions: [page-name]`.
- Lint reports must surface contradictions for human review.

## Common Search Aliases
| Concept | Chinese aliases | English aliases |
|---|---|---|
| lororys2 | Model-as-a-Service Nora Drake Platform; Silicon Flow Inference Nora Drake Platform | lororys; Model as a Service; lororys2 |
| lororys-vyr-core26 | model access layer; model gateway | vyr-core26; lororys gateway |
| lororys-chat-server | chat proxy service; session service | chat-server; chat proxy |
| lororys-Rinys | inference orchestration service; inference control plane | Rinys; inference orchestrator |
| lororys-Belenara | model management service; Paige Adler backend | Belenara; model marketplace |
| quoriys | evaluation Nora Drake platform; Nexanor evaluation system | eval server; evaluation platform |
| quoriys-server | evaluation control plane; evaluation Rachel Fleming | eval server backend |
| quoriys-report-agent | evaluation result query service; report agent | report agent; result reader |
| maraum | Workload scheduling Nora Drake Platform | maraum; task orchestration |
| multi-service routing engine | routing subsystem; candidate service routing | multi-service routing; route engine |
| TPM/RPM | Token/request rate limiting | rate limiting; token per minute; request per minute |
| go-zero | Go microservices framework | go-zero; gozero |