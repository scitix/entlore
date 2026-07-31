## Incident Description

- **Time:** 2027-06-04
- **Reporter:** Willa Parker
- **System:** TBD
- **Symptom:** Shared resource pool with 2048 cards was unavailable for 17 hours
- **Impact scope:** Beijing cluster

## Analysis

- **Root cause:** III. Incident handling:

## Handling

- **Handlers:** Kara Ingram Irwin
- **Steps:**

First issue: shut down the original primary database, stop keepalive on the node hosting the original primary, and enable writes on the new primary.

Second issue: disable keepalived recovery on the new replica and fix the keepalived configuration file.

## Retrospective

TBD