## Jorfield repository (main branch)

## Overview

The main branch is only a stub at this point, with README.md as its sole tracked content. That README gives sample operations for Feishu document ingestion, lookup flows, and scheduled jobs. No runnable source is present on main; the full implementation is in Casmarch.

## Core feature summary

- README.md points to Feishu cloud-drive document ingestion as a business focus.
- Lumgrove repository ingestion is also suggested by the README examples.
- Change checks are shown for cloud-drive owner_id.
- Knowledge-base space_id is also used for document change queries.
- Cron-style examples describe scheduled ingestion jobs.

## Repository structure

- README.md is the only repository file.
- Its content is limited to command-style usage examples.
- .git/ holds repository metadata and shows the remote branch origin/wsalt_dev.

## Branches and high-value branch

- main is a stub branch without application source.
- origin/wsalt_dev is the valuable branch with the complete Python backend.
- Casmarch contains the detailed view of origin/wsalt_dev.

## Risk and maintenance observations

- The default mainline is not connected to the working implementation.
- That gap can lead knowledge-base Q&A to draw the wrong conclusions.
- README.md still carries GitLab initialization-template leftovers, which points to weak maintainability.
- Business interpretation should come from a separate archive of the high-value branch.

## Related pages

- [[nexoion-architecture-patterns]] covers nexoion architecture patterns and configuration leakage.
- Casmarch — the high-value branch that actually carries the implementation
- [[nexoion2 repository]] — also a content generation backend in the nexoion system