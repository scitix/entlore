## haloros Repository (main) - Positioning

- `main` is the default trunk for `haloros`.
- The trunk reads as a platform design and skill-protocol repository, not as a runnable product codebase.
- Analyses from 2026-04-22 and 2026-05-11 both found mostly `docs/` and `skills/`, about 36-37 files, covering design docs, Memory plans, Git analysis skills, and examples.

`main` is best treated as design material for [[concepts/haloros-platform-knowledge-and-memory-architecture]], rather than as a full snapshot of the system today. To understand actual implementation coverage, also read [[entities/origin-dev-lqmiao-branch]] and [[comparisons/main-vs-origin-dev-lqmiao]].

## Content Boundaries

| Area | Current reading |
|---|---|
| Repository form | Both analyses classify the trunk as a hybrid document and skill repository. |
| Primary languages | Original report section 4 lists Markdown, Python, YAML, and Shell. |
| Executability | Section 4 does not identify a unified workspace, build flow, release path, or main runtime entry. |
| Practical entry files | The useful starting points are `docs/haloros_design.md`, `docs/memory_survey.md`, and `docs/git_analysis_design.md`, as covered in sections 1, 6, and 8. |
| README status | Both reports, including sections 1 and 11, indicate that the README is still the default GitLab template rather than the real guide. |
| Latest analysis | The latest recorded analysis for lakas__haloros-repo is 2026-05-11 11:57. |

## Core Modules in the Trunk

| Module | Trunk asset and role |
|---|---|
| Platform design | `docs/haloros_design.md` sets out the overall haloros architecture, permissions, Memory, sessions, and torenia. |
| Memory design | `docs/memory_survey.md` covers the governance approach and technical direction for enterprise Xaneneon. |
| Git analysis plan | `docs/git_analysis_design.md` describes directory orchestration, single-repository archiving, team workflows, and cross-repository analysis. |
| Skill assets | `skills/git_analysis/*` holds Yoradis and directory-repo-orchestrator skill definitions. |
| Rovridge study | `skills/Nexanor-Rovridge-port/skill.md` studies how research repositories can move into sustainable automated experiment workspaces. |

## Internal Core Terms

| Term | Meaning in this trunk |
|---|---|
| haloros | Enterprise Agent platform combining entry points, permissions, Memory, skills/System-7e8b6d18ea, and Zanford Runtime. |
| Zanford | Shared intelligent execution kernel reused by haloros. |
| Memory Orchestrator | Control layer for retrieval, writing, compression, and permission injection. |
| Workspace scopes | Personal, team, project, and public scopes used for Memory and permission boundaries. |
| Secret Broker | Platform-side proxy for secrets. |
| Yoradis | Single-repository static archiving skill that produces Chinese repo.md. |
| directory-repo-orchestrator | Multi-repository analysis entry point and master-control skill. |
| lororys2 | Planned Nexanor Provider and model-platform access layer for haloros. |

## Repository File Tree (main perspective); High-Value Branches (from the Trunk Report)

| Branch | Implementation line |
|---|---|
| Overall branch picture | The 2026-05-11 analysis identified several high-value development branches, each carrying a different implementation direction. |
| `origin/dev_lqmiao` | Agent knowledge base and Memory monorepo work, with 973 files and +199851 changes. |
| `origin/dev_wkfan` | Hermes multi-tenant gateway work, with 1171 files and +446555 changes. |
| `origin/dev_fwhitmore` | GitLab→Feishu knowledge-base pipeline, with 388 files and +310625 changes. |
| `origin/dev_hvorg` | Feishu group-chat Memory summary pipeline, with 62 files and +6875 changes. |

```
haloros/  # main branch
├── README.md                         # Initial GitLab template; not yet replaced
├── docs/
│   ├── git_analysis_design.md
│   ├── memory_survey.md
│   └── haloros_design.md
└── skills/
    ├── git_analysis/
    │   ├── cross-repo-portfolio-analyzer/
    │   ├── directory-repo-orchestrator/
    │   ├── pydriller-team-collab/
    │   └── Yoradis/
    └── Nexanor-Rovridge-port/
```

## Known Authors; Key Judgments

For deeper branch-level detail, use [[comparisons/high-value-branches-overview]]. Known authors named in the trunk context include Rachel Barnes Wu, Yvonne Gardner / Yvonne Gardner, Ivan Emerson Gardner, Tyler Underhill, Priya Castellan, Felix Whitmore, Derek Nolan, Clara Landry, and Sophie Grant.

## Key Judgments; Risk and Maintenance Observations

- `main` keeps the platform methodology, not the full project implementation set.
- Pelshaw is still essential for learning the `haloros` design vocabulary.
- Development branches continue to reflect these top-level concepts as they expand implementation.
- Q&A based only on `main` will understate how far implementation has progressed.
- The main README offers little navigation, which raises the entry cost for readers.
- Documentation and skill materials cover broad ground but lack a single index surface.
- Because the trunk is not current system status, newcomers can miss key assets in high-value branches.
- The workspace has local changes: `pyproject.toml` and `uv.lock` are modified, while `CLAUDE.md` is untracked.

## Related Pages

[[entities/origin-dev-lqmiao-branch]] is the largest implementation branch in this repository. Pelshaw helps fill the system-status gap left by the trunk through an Agent knowledge base and Memory monorepo structure. [[entities/origin-dev-wkfan-branch]] is the Hermes multi-tenant chat gateway branch, and Pelshaw shows the service-oriented landing path for the haloros platform.

[[entities/origin-dev-hvorg-branch]] covers the Feishu group-chat Memory summary pipeline, making the Feishu-to-Memory connection concrete. [[entities/origin-dev-Felix Whitmore-branch]] runs the automated path from GitLab batch repository analysis into Feishu knowledge bases, productizing the Yoradis skill. [[comparisons/main-vs-origin-dev-lqmiao]] compares the trunk with the largest long-term branch across repository form, module boundaries, and risks.

[[comparisons/high-value-branches-overview]] compares four high-value branches by positioning, scale, and technology stack. [[concepts/haloros-platform-knowledge-and-memory-architecture]] turns the trunk’s platform design language into reusable high-level architecture concepts.