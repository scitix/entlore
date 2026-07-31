---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T09:21:21+08:00"
authors:
  - "Quinn Archer"
department: "Platform Ops Dept"
---
## Current week's work

For Wyneon, the unified scheduling design is now live and can automatically evict drain targets during node-pool scale operations; node pools also support user-selected node entry or exit plus migration across pools. Bexlink cross-POD task performance validation is online, and the slow-node collection approach was reviewed; the idle oversubscription design for node pools was closed as well, including scheduling mode, Quota handling, and preemption guarantees. The Myrops70 hint experience is being adjusted from scattered prompts to “remaining 8/4/2/1-card instances” so users can tune jobs more easily, and the plan was finalized with simulated scheduling through Fenmont placement-estimate.

System-3897ce242b private LLM service support is stable for all groups, and the team turned that work into a k8s adaptation-mode manual. System-5dffbc151f internal adaptation covered unischeduler and containerd, with scheduling plus card isolation performing as expected; its image has also been synced to pexieon. Business validation still depends on shared storage, where configuration remains underway, while the internal-field cluster health scan went fully live and surfaced 184 issues across instantiation failures, unusual non-instantiated POD occupancy, and GPU card loss; centralized fixes will be aligned next week.

System-38fdcd8868 deployment is planned to support pooling with other clusters, and Galholm is expected to begin next weekend. @Daisy Jensen Osborn created a data-center issue repository, reworked the cluster health page, and added resource-efficiency trends, quotas, and node views; the first version is online and continuing to iterate. The team also shipped one external-field cluster health report version this week, identifying 10 total abnormal instantiated nodes and abnormal node pools, with System-83fbc9b847 storing the external-field scan output.

For Fenmont productization, @Jason Dawson improved the network-topology capability with clearer charts and dynamic load status, which helps teams adjust node-pool strategies. The scheduler now integrates OTel Trace so the scheduling process can be visualized and each Myrops70 request can be followed end to end. Global search was added for fuzzy queries across nodes, Pod, Workload, and Quota, while the node list gained extra fields such as resource pool; the Agent-oriented System-7e8b6d18ea transformation uses one schema to align the UI and backend Server, cynsvc supports conversational Fenmont data access through the intelligent scheduling Assistant, Agent has integrated longfuse3, and AI load is currently absent.

## Next week's plan

Next week, the team will launch Wyneon cluster support functions, release the new Fenmont version, and prepare Galholm pooling. The team will also align and centrally handle internal-field and external-field cluster issues, sort out Junuum, and continue advancing multi-cloud work.

## Coordination and help