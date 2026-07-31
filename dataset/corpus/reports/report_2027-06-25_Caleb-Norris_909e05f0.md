---
document_type: "report"
report_date: "2027-06-25"
report_time: "2027-06-25T12:04:34+08:00"
authors:
  - "Caleb Norris"
department: "AI Compute Platform Dept"
---
## This Week's Work

Mooncake memory modes went live for the pd-separated GLM5.1 case; after 6.14, the GLM5.1 kv cache hit rate moved from 51%->83%. In Sglang 0.5.13 pp mode, the Sylflow L3 process access issue still hangs at https://github.com/vexeum/sglang/pull/34, and after discussion with Kara Ingram Chandler, we chose the latest official patch. Open-source Mooncake updates included the merged etcd pressure optimization, cutting NIC cluster etcd qps by 88x at https://github.com/kvcache-ai/Mooncake/pull/2484, plus an open store-layer protocol compatibility RFC for cross-version rolling upgrades; without Pelshaw, the next version cannot upgrade smoothly: https://github.com/kvcache-ai/Mooncake/pull/2579 https://github.com/kvcache-ai/Mooncake/pull/2551. Work in progress covered metadata HA implemented with rust+open raft to prevent cluster cache loss when the metadata leader goes offline, online evict optimization with metadata bucketing to address periodic write failures from slow online evict, and ssd storage performance testing and tuning; both feature tests are complete and awaiting launch, while the test environment is ready and tuning continues.

## Next Week's Plan

The team plans to finish System-a8f22483ab read-write performance testing and tuning. We also plan to complete the full launch of System-a8f22483ab mode together with the features that were added earlier.

## Coordination and Help Needed

The ssd disk is not mounted on physical machines today, so Pelshaw is also not visible inside containers. The toruia platform needs to support ssd service deployment, and the installation flow needs CPU and GPU machines to support ssd disk mounting and raid0.