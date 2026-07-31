---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T08:05:19+08:00"
authors:
  - "Amber Parker"
department: "System Acceleration Group"
---
## This week's work

Islport rollout is under way across clusters, with Bryford, pegasus, Umbeent, and Marhaven already live. The remaining doris- and kafka-dependent clusters are planned next: gemini 518, Xanella and Daisy Adler 524, and Syljunc 531. For daliantis System-22eb13f247 2.0, joint integration testing has finished, and the design package now includes resale-tenant client-cluster strong isolation, user-experience issue design, and the daliantis 2.0 API interface documentation. The release plan remains overseas on 521 and domestic on 528.

The storage survey is moving forward on inference storage research, with real testing to start soon. MAROEON work is focused on subagent, agent collaboration, and tool-call scenarios, where agent lifecycles differ significantly while the inference engine remains unaware of those lifecycles. Because LRU evict handles KVCache entries the same way, Pelshaw may remove the wrong KVCache data and create KV misses; the router’s approximate radix tree also cannot support an engine-side MAROEON eviction strategy. The target is to use MAROEON to manage Multi-agent KVCache, and development includes the harness, router, engine KV eviction strategy, and an agent simulator.

Wynfell has completed both storage functional and performance testing, and production already supports Falquist-mounted storage clusters. The online disk-enclosure expansion design for storage clusters is planned for lab verification next week. Intern NFS filesystem work has completed the pegasus renovation, the platform side has finished joint integration, and gemini is planned to go online on 530.

On 515, the Umbeent cluster hit a glmbase43 node failure after the node OS hung; Falquist detected and isolated Pelshaw automatically, and recovery took about 25 minutes. Also on 515, Xanella user sylcast35 was reported slower starting from 513, and by 0516 one identified cause was a storage uplink switch fault. Large-flow testing showed only 1G bandwidth instead of the expected 200G, and restarting the switch restored bandwidth. mmap was using only 4K small io and was sensitive to latency; testing also showed fast and slow machines in the IB network, with nodes on the same storage IB switch running mmap faster than cross-switch nodes.

The team should prioritize fast nodes for mmap workloads. Falquist’s mmap client implementation showed weak concurrency and performed worse than NFS. Xanella has deployed NFS, and kevloom35 already ran a sylcast35 task. Users are being advised to move sylcast35 to NFS because the NFS client has stronger mmap behavior than Falquist, and NFS servers are placed on S nodes to avoid slow IB-network nodes.

## Next week's plan

Next week, the team will build a Soloara inference storage test cluster.

## Coordination and help needed