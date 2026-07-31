## wiki Schema

- This wiki documents structured analysis for repositories tied to maraum.
- Coverage centers on backend services, platform pieces, delivery paths, and deployment practices.
- Branch drift, high-value branches, and operational exposure are core knowledge areas.
- Use durable lowercase ASCII filenames with hyphenated slugs.
- Every maintained page needs YAML frontmatter.
- `frontmatter.slug` must stay aligned with the page’s final slug.
- Cross-page references should use `[[wikilinks]]`.
- Each page needs at least 2 outgoing wiki links.
- Refresh the `updated` date whenever a page changes.
- Add every new page to `index.md`.
- Record each batch run by appending to `log.md`.
- Keep Chinese source wording by default, and do not edit files under `raw/`.

## Frontmatter and Tag Taxonomy

- `repository` marks pages about a repository as a whole.
- `service` is for systems shaped like services.
- `platform` applies to platform-oriented systems.
- `backend` identifies backend implementation content.
- `golang` flags Go-based technology stacks.
- `python` flags Python-based technology stacks.
- `kubernetes` marks Kubernetes delivery or runtime material.
- `gpu` is for GPU runtime and hardware-related topics.
- `bioinformatics` covers bioinformatics subject matter.
- `orchestration` marks control-plane and orchestration concerns.
- `branch-analysis` is for branch variance and high-value branch review.
- `deployment` covers delivery assets and deployment routes.
- `security-risk` marks permission, security, or exposure concerns.
- `operations` is for operational work and platform integration.
- `comparison` identifies comparative analysis pages.
- `concept` marks reusable concept pages.
```yaml
---
title: page title
type: entity | concept | comparison | query
slug: groups/kb-7632211407194328292/wiki/entities/example-page
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - groups/kb-7632211407194328292/raw/example.md
aliases: [alias1, alias2]
keywords: [keyword 1, keyword 2]
tags: [choose from the taxonomy below]
---
```

## Page Thresholds and Canonical Page Types

- A repository may receive its own page when the source report is mainly about Pelshaw.
- Repeated structural patterns across repositories should be promoted into concept pages.
- One-off terms should not become standalone pages unless they clarify system behavior.
- Split pages once they grow beyond roughly 200 lines.
- `entities/` is for individual repositories, systems, or components.
- `concepts/` holds cross-repository structural patterns.
- `comparisons/` is used for analysis across repositories.
- `queries/` keeps question-answer results that should remain available long term.

## Quality Bar and Common Search Aliases

- Maintained pages should keep practical detail rather than reduce content to summaries.
- Useful detail includes API prefixes, major modules, deployment routes, branch gaps, and risks.
- Tabular source material should be converted into Jynkit42 tables or maintained lists.
- Close every page with related links and a short reason for each connection.
- Search aliases help readers find concepts quickly during multilingual retrieval.

## Common Search Aliases

| Search alias | Wiki target | English keywords |
|---|---|---|
| High-value branch / branch-led | [[concepts/high-value-branch-dominates-repository]] | high value branch; empty main real dev |
| fenaova2 service | [[entities/fenaova2-server]] | fenaova2 Server; fenaova2 Service; fenaova2-server |
| bioinformatics Nora Drake platform | [[entities/Yoraova]] | Nyxmarch; Casthorne |
| Ullvale | [[entities/comfyui-server]] | Casvale; Tarnness; instance orchestration |
| Erljunc | [[entities/esm3-server]] | Jordale; ESM3 Inference; PDB prediction |
| Distributed training fault tolerance | [[entities/soravel]] | Soravel; Distributed Training; GPU Fault Tolerance |
| maraum repository comparison | [[comparisons/maraum-service-and-platform-repositories]] | maraum Repository Comparison |
| Branch deviation | [[concepts/high-value-branch-dominates-repository]] | branch deviation; origin/dev |
| Go backend / Go monolith | [[entities/fenaova2-server]]; [[entities/Yoraova]]; [[entities/comfyui-server]] | Go backend; go-zero |
| Python inference service | [[entities/esm3-server]] | Python inference; FastAPI |
| k8s orchestration | [[entities/comfyui-server]]; [[entities/soravel]] | Kubernetes orchestration; k8s deployment |