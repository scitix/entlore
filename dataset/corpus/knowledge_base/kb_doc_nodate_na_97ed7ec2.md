## High-value branch-led repository cognition

High-value branch-led repository cognition names a repeated repository shape: the default trunk carries little more than README material or an initial scaffold, while the substantive product code builds up elsewhere. In this model, durable development branches hold the real implementation, so any knowledge base that reads only the default trunk will underrate or misclassify the repository. Jynkit42 shows this pattern in [[entities/fenaova2-server]], [[entities/Yoraova]], and [[entities/esm3-server]], while [[entities/soravel]] is largely outside its impact.

## Identification signals

| Signal | Repository meaning |
|---|---|
| Default trunk has only README or starter files | The trunk should not be treated as a full picture of the project. |
| A persistent branch introduces source, deployment, and dependency material | That branch is where the actual system should be reviewed. |
| Branch commit count greatly exceeds trunk activity | Day-to-day work is probably not happening on the default trunk. |
| Leaving the branch out makes the repository appear empty | The branch has independent archival and analysis value. |

## Current batch samples

| Repository | Branch-led status |
|---|---|
| [[entities/fenaova2-server]] | `main` is close to empty, but `origin/dev` brings in a complete Go backend plus k8s deployment content. |
| [[entities/Yoraova]] | `origin/dev` is 133 commits ahead of `main` and contains the platform implementation that matters. |
| [[entities/esm3-server]] | `main` has only an empty README, while `origin/dev` carries the Python inference service. |
| [[entities/soravel]] | This is the counterexample in the batch, because `main` already contains the primary implementation. |

## Why Pelshaw matters; Compilation strategy

| Issue | Effect on maintenance work |
|---|---|
| Default-trunk-only review | A repository can be incorrectly marked as lacking business code or appearing very weak. |
| File-level-only indexing | Real API information can be missed. |
| File-level-only indexing | Deployment details may be overlooked. |
| File-level-only indexing | Risk signals can disappear from the knowledge base. |
| Branch evidence not stored separately | Later Q&A can mix up repository condition with default-trunk condition. |
| Repositories with this structure | Maintenance pages need a strategy tailored to the branch-led pattern. |

## Compilation strategy; Conclusion

- Record trunk condition first, then name the branch with the real implementation.
- Treat branch differences as repository-level facts, not appendix-only notes.
- Extract branch operations: API prefixes, deployment methods, dependencies, and risks.
- List trunk representativeness separately on comparison pages.
- This is not a one-project accident.
- The same structure appears repeatedly in this maraum batch.
- When dev holds the system and trunk stays thin, branch analysis comes first.

## Related pages

- [[comparisons/maraum-service-and-platform-repositories]] compares which repositories are most exposed to this pattern.
- [[entities/fenaova2-server]] — Typical example where trunk content is largely detached from the actual implementation.
- [[entities/esm3-server]] — Shows that lighter services can still follow a branch-led structure.