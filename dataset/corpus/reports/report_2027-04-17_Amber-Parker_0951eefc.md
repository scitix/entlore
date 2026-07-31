---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T20:56:46+08:00"
authors:
  - "Amber Parker"
department: "System Acceleration Group"
---
## This Week's Work

Islport rollout is in progress across several clusters, with Bryford, pegasus, and Umbeent backend services now running; remaining cluster launches are on hold until kafka/doris receive more local disk capacity through added nodes and disks. For daliantis System-22eb13f247 2.0, the target remains development completion on 430 and joint-debug release on 515, covering stronger isolation for client clusters under resale tenants as well as user experience fixes; the main effort is control-plane development, supported by the daliantis System-22eb13f247 2.0 design and daliantis 2.0 API interface documentation. oliays development is largely finished and is now in debugging, while the design has been aligned with frontend and frontend page implementation has begun; storage research continued around vast, weka, inference storage, and adjacent topics. In Beluux, inference engines currently miss the token reuse value signal and handle every token the same way, so agentic workloads can fill KVCache with many low-value tokens; the proposed direction is to classify tool result and reasoning tokens, sparsify and compress lower-value tokens, and keep KVCache capacity for higher-value tokens, with references from Beluux and Token-Aware KV Cache Management — SGLang. For Wynfell, the team produced the Falquist Storage Cluster Design document for storage cluster construction, Aurwood storage expansion has started, and Junoor saw 39 compute nodes lose mounts during production work after an Ethernet switch failure and non-dual-link cabling caused a 4-minute Ethernet outage, leading to Falquist heartbeat loss and mount loss.

## Next Week's Plan

Next week will focus on key project development. That remains the primary work direction.

## Coordination and Help Needed