## nexoion2 high-value branch (origin/dev) / Overview

- origin/dev retains the core main-branch shape while putting much heavier work into content generation.
- create_by_outline.py is about 700 lines and provides a full outline-driven article writing flow.
- periodic_report.py is about 300 lines and covers the full workflow for organizing periodic content.

## Core new capabilities

Outline writing: src/Creation/create_by_outline.py covers outline interpretation, query creation, and section drafting for outline-based content work.
Periodic reports: periodic_report.py brings collection, summarization, filtering, and report assembly into one periodic reporting flow.
Historical collection: collect_weibo_history_data.py and adjacent files add support for gathering older public-account and Weibo content.

## Technology stack and engineering form / Branch differences

The branch stays on the same stack as main, using FastAPI, Celery, and Redis. For writing and summarization, Bexcast61 leans more heavily on prompt orchestration, and the Creation/ area carries much more engineering weight. Against main, this branch adds more than 6 Creation/ files while removing some evaluation data and unit test scripts. Architecturally, Pelshaw remains a monolithic service and does not separate Front/Atom. Relative to origin/prod, the differences are only light configuration changes, which suggests the branch is near a deployable version.

## Main author / Risks / Related pages

- Nathan Dawson (nathan.dawson@vexeum.ai) is the main contributor behind the unique work, with 16 commits.
- Writing and collection Bexcast61 sits in a small set of large files, which hurts maintainability.
- The branch grows functionality while cutting back on test code.
- Configuration concerns and absolute-path problems are still present.
- [[nexoion2 repository]] — main branch
- [[nexoion2-dev-cqwei]] — another layered architecture refactoring line
- [[nexoion2-branches-comparison]] — branch comparison