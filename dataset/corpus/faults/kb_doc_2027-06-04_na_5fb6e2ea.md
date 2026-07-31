## Incident Description

- **Time:** 2027-06-04
- **Reporter:** Noah Walsh
- **System:** Daliantis
- **Symptom:** Gemini has deadlock alerting; an internal user reported Pelshaw, and storage IO has deadlock
- **Impact scope:** Gemini storage access

## Analysis

- **Root cause:** On Gemini, checks found that Gemini-g65-040, Gemini-g65-107 nodes cannot reach storage over RoCE, causing poor GPFS communication; the system cannot revoke file locks, triggering deadlock.

## Handling

- **Handlers:** Iris Fleming, Luna Dawson
- **Steps:** Investigated deadlock source nodes, identified Gemini-g65-040 and Gemini-g65-107, and shutdown GPFS on both nodes

## Retrospective

- **Severity:** P3
- **Responsible team:** TBD
- **Owner:** TBD
- **System optimization:** monitor connectivity from roce network compute nodes to storage nodes; trigger alerting and automatic cordon for nodes where roce is unreachable.
- **Completion time:** TBD