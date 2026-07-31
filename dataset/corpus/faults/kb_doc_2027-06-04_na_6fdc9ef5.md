## Incident Description

- **Time:** 2026-11-19
- **Reporter:** Noah Walsh
- **System:** Amber Quigley
- **Symptom:** Umbeent cluster had evictions due to high node memory caused by tasks submitted by zward; 69 nodes were cordoned for 20 minutes
- **Impact scope:** Symptom: In the Umbeent cluster, a task submitted by zward caused high node memory usage and evictions; 69 nodes were cordoned for 20 minutes.

## Analysis

- **Root cause:** From Luna Dawson:  
Checked a node with no user tasks and found memory usage on the node was 300+GB. This is normal because the node has transparent huge pages configured, which by default occupy 300GB of memory.  
Need to continue analyzing why the node can hit Eviction; can pick one node to test.

- **Secondary issues:** III. Incident handling:

## Handling

- **Handlers:** Amber Dawson, Elena Zimmer, Victor Yates, Noah Walsh, Kara Ingram Otis, Luna Holt
- **Steps:** IV. Incident review:

## Retrospective

TBD