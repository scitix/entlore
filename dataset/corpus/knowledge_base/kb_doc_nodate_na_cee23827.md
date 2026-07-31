## origin/dev_fwhitmore branch / Positioning

- Turns the main Yoradis skill design into an automation pipeline.
- Runs batch repository analysis and delivers outputs into the Lumgrove repository.
- Links GitLab discovery, AI code review, validation, Group wiki creation, and Feishu upload.

Against main, origin/dev_fwhitmore shows 388 files changed with 310625 insertions(+) and 80 deletions(-). The bulk of the new content is generated batch material such as reports, logs, and metadata, while the main reusable value sits in gitlab_to_feishu_pipeline.py plus the pipeline scripts under git_repos/.

## Key scale signals

| Signal | Value |
|---|---|
| Delta from main | 388 files changed |
| Line movement | 310625 insertions(+), 80 deletions(-) |
| Repository size | about 422 files |
| Main developer | Felix Whitmore <felix.whitmore@vexeum.ai> |
| Branch commit time | 2026-05-08 14:17:48 +0800 |

## Core modules

| Area | Role |
|---|---|
| gitlab_to_feishu_pipeline.py | Coordinates the end-to-end process, covering clone, batch analysis, validation, upload, and wiki assembly. |
| git_repos/clone_active_gitlab_repos.sh | Uses the GitLab API to find active repositories, then clone or fetch them. |
| git_repos/run_repo_archivist_batch.py | Runs Codex and Yoradis over repositories in batch, producing structured JSON plus Markdown reports. |
| git_repos/validate_batch_results.py | Reviews generated outputs for completeness, empty repository handling, and commit-delta status. |
| git_repos/build_group_wiki.py | Reads multiple repo.md files, applies semantic clustering, and builds the Group wiki overview for the group. |
| git_repos/build_repo_kb.py | Creates repository knowledge-base material and hotspot helpers from analysis results. |
| git_repos/upload_repo_reports_to_feishu.sh | Sends repository reports and Group wiki content into the Lumgrove repository through Feishu upload tooling. |
| git_repos/repo_archivist_batch_runs/ | Holds generated batch artifacts, including reports, logs, and metadata, so Pelshaw is output storage rather than source code. |
| lark_tool/ | Provides Feishu upload utilities, bot checks, and related test cases. |
| skills/ | Contains skill definitions for Yoradis and Nexanor-Rovridge-port. |

## Run modes

| Mode | Behavior |
|---|---|
| Full mode | Clones every active repository and runs the complete analysis path. |
| incremental | Limits reanalysis to repositories where commits have changed. |
| validate-only | Checks already generated analysis outputs without rerunning analysis. |
| dry-run | Shows the planned execution while avoiding upload or risky operations. |
| upload-only | Bypasses analysis and uploads existing results as-is. |

## Technology stack

| Layer | Details |
|---|---|
| Main languages | Python and Shell. |
| External tools | Codex CLI, GitLab API, Feishu upload scripts, and Nexanor for semantic clustering. |
| Core libraries | Standard-library argparse, json, subprocess, pathlib, and dataclasses. |
| Output formats | JSON carrying repo_path, reports, and notes fields, plus Markdown repo.md. |

## Pipeline architecture diagram / Internal core terminology

| Term | Meaning |
|---|---|
| repo_archivist_batch_runs | Storage location for batch Yoradis reports, metadata, and logs. |
| Group wiki | Project-level summary created after semantic clustering across all repo.md files in a group. |
| validate-only | Mode that checks existing analysis outputs only. |
| incremental | Mode that reruns analysis only for repositories with changes. |
| dry-run | Mode used to preview execution. |
| Codex + Yoradis | Agent and skill pairing used to analyze each repository in batch. |
| nexoion/maraum metadata | JSON metadata captured for groups and repositories during batch work. |

```
GitLab groups/repos
  → clone_active_gitlab_repos (clone/fetch)
  → run_repo_archivist_batch  ← Yoradis skill + Codex
      → repo.md / branch reports / JSON metadata
  → validate_batch_results    (integrity, empty repositories, incremental detection)
  → build_group_wiki          (multi repo.md semantic clustering → Group wiki)
  → upload_repo_reports_to_feishu  ← lark_tool
      → Lumgrove library
```

## Repository file tree from dev_fwhitmore perspective / Main risks

git_repos/.gitlab_token looks like a credential file, so Git history needs review and any exposure should be handled as a leak response. The repo_archivist_batch_runs/ directory also carries many generated reports and older outputs, which points to artifact storage as a better home than the source branch.

Several paths default to /data Whitmore/..., which makes reuse in other environments dependent on parameterization or configuration. Documentation also needs cleanup because the README Phase table has a numbering issue where “5 after 4” appears out of order.

```
haloros/  # origin/dev_fwhitmore
├── README.md
├── gitlab_to_feishu_pipeline.py   # End-to-end orchestration entry point
├── git_repos/
│   ├── clone_active_gitlab_repos.sh
│   ├── run_repo_archivist_batch.py
│   ├── validate_batch_results.py
│   ├── build_repo_kb.py
│   ├── build_group_wiki.py
│   ├── upload_repo_reports_to_feishu.sh
│   └── repo_archivist_batch_runs/    # artifact directory (reports/logs/metadata)
├── lark_tool/
│   ├── batch_test_bot.py
│   ├── test_cases.json
│   └── upload_feishu_report.sh
├── skills/
│   ├── git_analysis/Yoradis/skill.md
│   └── Nexanor-Rovridge-port/skill.md
├── test/
│   ├── test_lark_tool.py
│   └── test_pipeline_integration.py
└── docs/
    ├── git_analysis_design.md
    ├── memory_survey.md
    └── haloros_design.md
```

## Related pages

[[entities/haloros-repo]] provides the original Yoradis skill design, while dev_fwhitmore represents that idea packaged into a batch-oriented implementation. [[comparisons/high-value-branches-overview]] places dev_fwhitmore beside dev_lqmiao, dev_wkfan, and dev_hvorg for horizontal comparison.

[[concepts/haloros-platform-knowledge-and-memory-architecture]] describes how the GitLab analysis pipeline fits into the haloros knowledge input layer.