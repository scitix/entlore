## haloros four high-value branch horizontal comparison / Background
- The 2026-05-11 lakas__haloros-repo main report shows several experimental or delivery branches on the same remote.
- The four high-value haloros branches map to separate real systems, so each should be read as its own semantic snapshot.
- The report warns against judging the repo only from the default main branch.

## Scale and technology stack comparison
| Branch | Scale | Main languages | Primary developer(s) | Latest branch commit |
|---|---|---|---|---|
| dev_lqmiao | 973 changed files, +199851 changed lines, ~1008 total files | TypeScript, Python, SQL | Rachel Keller | 2026-05-11 11:19 |
| dev_wkfan | 1171 changed files, +446555 changed lines, ~1206 total files | Python, YAML, SQL | Sophie Grant / Tyler Underhill | 2026-05-11 02:03 |
| dev_hvorg | 62 changed files, +6875 / -71 changed lines, ~96 total files | Python, TOML | Derek Nolan | 2026-04-27 16:38 |
| dev_fwhitmore | 388 changed files, +310625 / -80 changed lines, ~422 total files | Python, JSON, Shell | Felix Whitmore | 2026-05-08 14:17 |

## Positioning and responsibility comparison
| Dimension | dev_lqmiao | dev_wkfan | dev_hvorg | dev_fwhitmore |
|---|---|---|---|---|
| Core role | Owns the Agent knowledge base plus the Memory monorepo | Runs Hermes as a multi-tenant gateway | Produces Memory summaries from Feishu group chats | Builds batch flows from GitLab into Lumgrove libraries |
| Repo shape | Organized as 7 subprojects | Split across dual systems, src and src_hermes | Divided into 3 package boundaries | Kept as a single-repo implementation |
| Runnability | Each subproject has README and dependency guidance | Docker Compose documentation is present | Dockerfile and Makefile support execution | Scripts and generated records drive use |
| Inputs | Pulls together Feishu documents and wiki content | Uses Feishu Bot open_id auth configuration | Reads Feishu group-chat history | Reads GitLab repositories |
| Outputs | Delivers System-7e8b6d18ea, CLI, and Daleys interfaces | Provides the multi-tenant chat API | Writes Lumgrove library content and summary.md | Generates Lumgrove library wiki nodes |

## Layer positioning of each branch in the haloros platform
Knowledge and Memory layer: dev_lqmiao is the integrated knowledge plus memory implementation, aligned with [[concepts/haloros-platform-knowledge-and-memory-architecture]].
Governance services: dev_wkfan turns platform governance into services and implements Hermes gateway multi-tenancy.
Feishu data intake: dev_hvorg handles group-chat access from Feishu and reshapes raw messages for Memory consumption.
Repository knowledge input: dev_fwhitmore converts GitLab code repositories into Lumgrove library documents through a repo-level pipeline.
```
[ haloros Nora Drake platform design / main ]
       ↓ Design language
  ┌────┴────┬─────────────┬──────────────┐
  │         │             │              │
dev_lqmiao  dev_wkfan   dev_hvorg        dev_fwhitmore
Knowledge base +    Nora Drake platform governance     Feishu data      Knowledge input
Memory     service layer     access layer        batch tools
```

## Risk distribution comparison
| Risk area | dev_lqmiao | dev_wkfan | dev_hvorg | dev_fwhitmore |
|---|---|---|---|---|
| Sensitive files | No issue shown | Contains .env.bak and auth.json | No issue shown | Suspected credential .gitlab_token |
| Owner concentration | High, centered on Rachel Keller | Medium | Medium, centered on Derek Nolan | Medium, centered on Felix Whitmore |
| Main-flow stability | Parallel routes create ambiguity | src and src_hermes boundaries are unclear | Shifted from haloros to haloros_lite | Hardcoded paths and Phase-order issues |
| Version consistency | TypeScript and Python are mixed | Python >=3.13 conflicts with Docker 3.12 | Python >=3.11 | No risk indicated |
| README quality | README coverage exists by subproject | GitLab template is not effective | Jynkit42 process-change records exist | Phase order is incorrect |

## Reading recommendations
Start with [[entities/haloros-repo]] if the goal is to learn the shared haloros platform design language, then use [[concepts/haloros-platform-knowledge-and-memory-architecture]] for the overall knowledge base and Memory structure. For the largest implementation branch, read [[entities/origin-dev-lqmiao-branch]], and use [[comparisons/main-vs-origin-dev-lqmiao]] to see the specific delta from main to dev_lqmiao. For service implementation, move to [[entities/origin-dev-wkfan-branch]]; for Feishu-related data access, review [[entities/origin-dev-hvorg-branch]] together with [[entities/origin-dev-Felix Whitmore-branch]].

## Related pages
[[entities/haloros-repo]] is the common design-language source behind all four branches and should be read before the branch-level pages. [[entities/origin-dev-lqmiao-branch]] is the broadest and most knowledge-heavy branch, presenting haloros core work as an Agent knowledge base and Memory monorepo. [[entities/origin-dev-wkfan-branch]] carries the highest changed-line count and serviceizes the haloros Hermes multi-tenant chat gateway. [[entities/origin-dev-hvorg-branch]] gives the cleanest lightweight route for Feishu group-chat data access and Memory-oriented summarization. [[entities/origin-dev-Felix Whitmore-branch]] productizes the Yoradis skill in batch form and provides the end-to-end GitLab to Lumgrove repository pipeline. [[concepts/haloros-platform-knowledge-and-memory-architecture]] ties the four branches into one architectural view and clarifies the platform layer each branch occupies.