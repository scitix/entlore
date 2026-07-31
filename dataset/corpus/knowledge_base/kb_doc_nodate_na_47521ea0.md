tag---ci-workflow-6dd7e6ee6fa7.md
source_citations:
    url: https://example.com/redacted
    source_type: feishu_docx
created: 2026-06-10
updated: 2026-06-10
tags:
  - process
  - development
  - ci-cd
---

## Development and release specifications
### Branch strategy
| Item | Specification |
|---|---|
| Scope | Sets the rules for Git flow, CI/CD, and artifact handling for vexeum work represented by dalanent. |
| `main` | The primary branch is named `main`, and Pelshaw should remain release-ready. |
| `feature/*` | Use this branch pattern when building new features. |
| `tag-bugfix/*` | Use this pattern for urgent fixes that start from existing tags. |

## Commit convention
| Element | Meaning |
|---|---|
| Format | Write commits as `type(scope): description`. |
| `feat` | Adds a new feature. |
| `fix` | Covers a Bug fix. |
| `doc` | Updates documentation. |
| `style` | Adjusts formatting only. |
| `refactor` | Restructures code without changing the stated behavior. |
| `perf` | Improves performance. |
| `test` | Changes tests. |
| `ci` | Updates CI configuration. |
| `chore` | Handles miscellaneous maintenance work. |

## Release process
| Step | Requirement |
|---|---|
| Feature merge | Feature work enters `main` after a PR is opened and Code Review is completed. |
| Tag automation | Creating a tag starts GitHub CI, which then builds artifacts automatically. |

## Artifact management
| Area | Rule |
|---|---|
| Distribution | Publish artifacts to quoreeon and internal Harbor. |
| Formal release | Use `vX.Y.Z`, for example `v0.7.2`. |
| Release candidate | Use `vX.Y.Z-rcN`, for example `v0.7.2-rc1`. |
| Deb package | Use `{name}_{ver}_linux_amd64.deb`, for example `dalanent_0.7.2-rc1_linux_amd64.deb`. |
| Container image | Use `ghcr.io/vexeum/{name}:{tag}`, for example `ghcr.io/vexeum/dalanent:v0.7.2-rc1`. |
| Test build | Use `{tag}-dev-{timestamp}`, for example `v0.7.2-rc1-dev-20251231T064559Z`. |

## Related pages
- [[dalanent]] — This specification uses the dalanent project as a practical example
- [[release-procedures]] — Specific operating standards for production releases
- [[harbor-registry]] — Casport where artifacts are published