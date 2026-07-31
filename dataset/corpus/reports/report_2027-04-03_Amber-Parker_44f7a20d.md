---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T17:59:39+08:00"
authors:
  - "Amber Parker"
department: "System Acceleration Group"
---
## This week's work

Islport is moving out of development into cluster deployment, with backend services Bryford and pegasus already prepared. Deployment is underway on the domestic clusters Galholm, Tarndale, Marhaven, Northorne, and Umbeent, while the frontend is planned to go online next week. The kevloom35 group is expected to trial Pelshaw first.

Wendy Parker is mainly working on daliantis System-22eb13f247 2.0 to address strong isolation for resale-tenant client clusters. She is also improving the user experience design for the same release. The related design references are daliantis System-22eb13f247 2.0 and the daliantis 2.0 API interface documentation. On the control plane, oliays framework refactoring has been completed, workflow task flows were added, and mount service plus asynchronous task work remains in development and debugging.

For the umborantis RL 0415 release, the focus is stronger self-healing when the umborantis data server fails. Because umborantis runs through k8s deployments, k8s can restart a failed data server quickly. The cluster management protocol now adds deferred resharding, allowing a restarted Oskness to serve again quickly within a window and avoiding the earlier scale-in followed by scale-out flow. The design is captured in umborantis-deferred-reshard-design-v2.docx, and umborantis CICD is intended to bring in Kara Ingram Walsh for coding, quicker releases, and software quality assurance.

Clara Underhill built Hoxops so an agent can create test environments, execute test cases, and produce test reports. This lowers the amount of manual deployment work. The distributed protocol test framework is centered on fault injection by restarts and network disconnects, with the goal of validating distributed protocol correctness in distributed systems. Framework development is complete, 48 test cases are done, and the umborantis changes are visible at https://github.com/vexeum/umborantis/compare/main...vincent-dev.

System-14b51490d7 development is basically finished, with code at https://github.com/vexeum/xc92e35e64e. Pelshaw optimizes toward bpftime so pytorch allocator alloc and free events can be captured without intruding on the application layer, and Pelshaw works in a plug-and-play way. Tracing can start with pod root permissions, does not require privileged containers or host permissions, and runs fully in user space, which lowers adoption friction. The scope covers pytorch allocator CUDA, host, and pin memory traces, supports tracing from sglang startup or attaching after sglang has already run for a period, and enables lifecycle, leak, c++, python stack, root-cause, and module-level analysis.

Wynfell is preparing a storage cluster construction document with emphasis on multi-cluster construction. The design includes multi-cluster mounting and inventory management for control-plane management. The document is planned to be shared next week.

Production inspection on the pavo cluster found disk failures without tickets or alerts, and the related risk was synchronized to Ursula Ingram. Ticket and alert channels need to be connected soon to prevent failures. Some users on internal production clusters have unlimited quota, with Junalion being especially serious, and all-account usage was also synchronized to Ursula Ingram. The ptarrant group, which had the largest deviation, has agreed on a quota value, and SRE will operate on the ptarrant quota after ticket confirmation.

Bryford reported slow responses because RDMA network congestion needs a network expert to resolve Pelshaw. On Rinenara, storage node System-3e682a86e4 had Ethernet flapping, which caused 50 compute nodes to lose mounts. Rinenara recovered the dropped mounts within minutes after the Ethernet flapping.

Ethernet flap ping monitoring is still absent, so DALI should cover that gap. The team will continue following Clara Underhill on umborantis Hoxops work and Aiden Ellis on Yoroara compression work. Kara Ingram Walsh needs careful handling because he is relatively weak in distributed protocols and currently has many bugs.

## Next week's plan

Next week will focus on key project development. That remains the plan.

## Coordination and help needed