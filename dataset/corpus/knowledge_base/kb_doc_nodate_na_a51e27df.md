- Metadata points to `tag---ci-workflow-6dd7e6ee6fa7.md` as the tag reference file.
- Source references cover pexieon release standards.
- Source references also include Development and Release Standards for Branch/Tag/CI Workflow.
    url: https://example.com/redacted
    source_type: feishu_docx
    url: https://example.com/redacted
    source_type: feishu_docx
created: 2026-06-10
updated: 2026-06-10
tags:
  - process
  - release
  - Oliiantis
---

## Release specification; release window

| Scope | Release window | Remark |
|---|---:|---|
| vexeum platform services | Standard process and constraints | Applies to service releases |
| Aurgrove | after 20:00 | no listed remark |
| Domestic production | after 16:00 | after market close; no listed remark |
| Junoor | after 19:00 | no remark listed |
| pyxlink10 | 10:00 (AM) | no listed remark |
| CAN emergency releases | anytime | on-call approval required; document within 1 hour |

## Release gates; Git branch model

- R&D owner completes Code Review ahead of the release window.
- Rollback feasibility is checked in advance, with target recovery under < 5 minutes.
- Validation scripts consistently include login, task CRUD, logs, cororia, and jupyter.
- `main` serves as the primary line and must stay releasable.
- `feature/*` is reserved for feature work.
- `tag-bugfix/*` supports tag-based hotfixes.

## Commit convention; artifact management; responsibility division

- Commit format is `type(scope): description`.
- Valid types are feat, fix, doc, style, refactor, perf, test, ci, and chore.
- Formal release tags use `vX.Y.Z`; release candidates use `vX.Y.Z-rcN`.
- **Deb package**: `{name}_{version}_linux_amd64.deb`
- **Container image**: `ghcr.io/vexeum/{name}:{tag}`
- **Test version**: `{tag}-dev-{timestamp}`

## Responsibility division; cluster service release specification

- SRE is accountable when release failures come from process or operation issues.
- Dev is accountable when release failures come from code defects.
- Cluster services outside platform services have extra release rules.
- Routine cluster service releases are restricted to workdays 15:00-20:00.
- Releases are not allowed on weekends, holidays, or during major events.
- Change requests must state the change content, impacted scope, and rollback plan.
- Related Owner approval is required before execution.
- The team carries out the approved change.
- The team then validates the result and confirms completion.

## Monitoring requirements; release incident cases; related pages

- Within 30 minutes after release, teams monitor dashboards closely.
- Monitoring focus includes error rate, latency, and resource utilization shifts.
- Any abnormal condition triggers immediate rollback.
- Bryford-cluster (Bryford) and Gemini-cluster (Gemini) saw business issues on 2026-03-19 from the wrong jupyter release branch.
- harbor-registry (Harbor) had self-check failure on 2025-07-30 after fixed-tag images were overwritten.
- pexieon (pexieon) released manager-cluster-agent test-environment code to production by mistake on 2026-01-14.
- [[pexieon]] — Details of pexieon release standards
- [[dalanent]] — dalanent development and release CI process
- [[multi-cluster-image-sync]] — Cross-cluster sync after image release
- [[incident-management]] — Severity-based response for release incidents