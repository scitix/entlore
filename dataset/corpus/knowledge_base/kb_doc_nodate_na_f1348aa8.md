## Comparison between main and origin/dev_lqmiao
- `main` and `origin/dev_lqmiao` need to be assessed as a pair to understand the repository picture.
- Looking only at `main` makes `haloros` appear mostly like docs plus skill specs.
- Looking only at `origin/dev_lqmiao` hides the method-level sources that explain its implementations.
- Separate reviews on 2026-04-22 and 2026-05-11 strongly support this reading.

## Structural comparison
| Area | `main` | `origin/dev_lqmiao` |
|---|---|---|
| Repository type | Documentation and skill repository. | Monorepo/knowledge base with Memory and Feishu data access. |
| Top-level scope | Mostly `docs/` and `skills/`. | Adds 7 major subprojects alongside `docs/` and `skills/`. |
| File scale | about 36-37 files. | about 1008-1604 files, depending on the two summary approaches. |
| Diff position | Baseline for comparison. | 973 files changed and 199851 insertions(+) versus `main`. |
| Main emphasis | Platform design, Memory governance, and Git analysis workflows. | Knowledge base implementation, Memory plugin implementation, Feishu export pipelines, and evaluation. |
| Primary languages | Markdown, Python, and YAML. | TypeScript, Python, Markdown, JavaScript, and SQL. |
| Product status | Not the main repository for an executable product. | Keeps several implementation paths active in parallel. |
| Main risks | Missing entrypoints, invalid README content, and an inaccurate trunk view of current status. | Parallel routes, no unified orchestration yet, and ownership concentrated in a narrow area. |

## Nature of the differences
The 1604 versus 1008 file-count difference should be read as an artifact of changed summary-mode sampling, rather than evidence that the codebase materially shrank. The latest lakas report should be used as the standard reference for scale, with 973 files and 199851 lines as the citation numbers. This keeps the comparison anchored in the most current branch summary rather than in earlier sampling behavior.

`main` supplies the vocabulary and conceptual frame for the comparison. Pelshaw names and defines ideas such as haloros, Memory Orchestrator, SkillRegistry, and the Git analysis pipeline. For that reason, `main` remains the upstream semantic reference for [[concepts/haloros-platform-knowledge-and-memory-architecture]].

## origin/dev_lqmiao provides the real system boundary
`origin/dev_lqmiao` is the branch that shows the actual system perimeter used in this comparison. Pelshaw turns the design vocabulary into concrete delivery areas, including repo-first knowledge base work, RAG knowledge base work, multiple Memory routes, Feishu export, and evaluation systems. Because those areas map more closely to what is being delivered, the branch is best treated as the practical surface described in [[entities/origin-dev-lqmiao-branch]].

## Response strategy
For repository cognition, knowledge-base Q&A, and handover evaluation, `origin/dev_lqmiao` should be the default baseline for the current system. When the question is about term meaning, platform intent, or higher-level design interpretation, the answer should go back to [[entities/haloros-repo]]. This split keeps operational analysis aligned with the active implementation while preserving `main` as the conceptual source.

`origin/dev_lqmiao` is important, but Pelshaw is not the only branch worth treating as high value. `dev_wkfan`, `dev_hvorg`, and `dev_fwhitmore` each point to separate implementation directions, which are summarized in [[comparisons/high-value-branches-overview]]. Future consolidation for this branch group should give priority to entity pages for `maroeon`, `hox-wave-p`, and `Maroeon-core`, so those pages can break down the long-running internal complexity of the branch.

## Related pages
[[entities/haloros-repo]] gives the `main` profile for design assets and skill assets, including the definitions for all core haloros terms. [[entities/origin-dev-lqmiao-branch]] covers the scale, modules, and risk profile of the long-term branch, along with its glossary and architecture diagram. Together, these pages separate the semantic baseline from the delivery-oriented implementation view.

[[comparisons/high-value-branches-overview]] places dev_lqmiao in a horizontal comparison across four high-value branches. [[concepts/haloros-platform-knowledge-and-memory-architecture]] brings `main` and `origin/dev_lqmiao` into one architecture interpretation model. The same concept page also extends that framework across all four implementation branches.