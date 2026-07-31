---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T21:03:08+08:00"
authors:
  - "Amber Parker"
department: "System Acceleration Group"
---
## This week's work

The Islport cluster rollout is at 90%, and Tarndale is the only site not yet live; Bryford, pegasus, Galholm, Umbeent, Marhaven, Northorne, gemini, Rinenara, and Xanella are already online, with Tarndale planned for next week. kevloom35 and ptarrant pointed users to the “System-a2723cbe8c” guide at https://example.com/redacted and feedback also showed that Pelshaw was helpful. daliantis System-22eb13f247 2.0 is already available overseas and is planned for the domestic launch next week; Pelshaw also finished strong-isolation work for resale-tenant client clusters and completed console UX page improvements reviewed with Yvonne Sawyer. Islbrook will remain on this 2.0 console release.

For the intern NFS filesystem track, pegasus and gemini both finished MAROEON changes, mainly to raise the KVCache hit rate. The 0525 KVCache discussion covered larger cache capacity, router-side KVCache-aware scheduling, and an agent-label approach where engines understand agents and eviction priority follows agent labels; the cache plan includes umborantis and Weka. KVCache cache work moved Weka validation forward, focusing on weka SSD cache-layer capability, using GPU local disks as a shared SSD cache layer for KVCache offload; 5090 in Ethernet and Daisy Adler in IB were prepared this week, so tests can begin next week. System-5df091e267 is intended to manage KVCache globally across inference clusters, tracking KVCache locations on engines and storage layers so the router can schedule accurately; the draft compares Pelshaw with the Dynamo flash indexer, Alibaba tair KVCache manager, and AIBrix sync Indexer, and will be reviewed next week. Rinenara hit a storage water-level risk after a dataman data surge, so the team confirmed quota with the user and arranged later expansion; Junalion hoxsvc48 also saw data lag from the known unstable System-d94c24a696 issue, with Ursula Ingram joining user communication and cynnet proposed as the solution path. The team also handled 4 external field tickets, all of them support-type cases.

## Next week's plan

Next week, the team will continue work on System-5df091e267. The plan also includes building the System-65f2c01657.

## Coordination and help needed