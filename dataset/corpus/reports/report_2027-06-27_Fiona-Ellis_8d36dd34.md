---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T10:11:08+08:00"
authors:
  - "Fiona Ellis"
department: "Platform Ops Dept"
---
## This Week's work

For container high-speed networking, the RDMA approach tied to GPU allocation was confirmed as workable at the technical level, but Pelshaw did not fit the product direction because Pelshaw would alter how RDMA is assigned on both GPU and CPU machines. The earlier OVS plus flow-table design was dropped due to latency in OVS rule delivery, and NV did not provide an alternative after follow-up discussions. The current direction is to add readiness checks in CNI so Pods are started only after the network is prepared. The VLAN Tag path will pre-stage OVS flow rules on the host, then apply VLAN Tag + IPPool configuration when the container starts. The Erlmarch case still needs validation, including switch trunk setup, while Luxlink has finished and improved support for the PelportCX8 case.

On agent and platform work, cororum finished access for Feishu private-chat and group-chat channels and now enables third-party agent invocation through the A2A protocol. One-click diagnosis now has streaming output, quick feedback is available through likes, dislikes, and comments, and the native multimodal model can take PDF and image inputs. Junuum improved the automatic idle-exit behavior, while observability and operations connected langfuse for agent call auditing. Knowledge base automation can compile through claude skill, platform capability construction is still underway, and skill work added cluster alias translation plus RoCE troubleshooting improvements for Bexcast88 occupation, including root-cause analysis. BELANUXVermarch team and diagnostics have completed backend agent capability development; the gateway supports the shopping-guide agent, the capability is ready, the knowledge base consumption path has passed verification, and launch can move quickly once product documentation is complete. Frontend development for the conversation interface is continuing.

## Next Week Plan

- Continue VLAN Tag-based multi-tenant isolation for the Erlmarch scenario.
- Keep iterating agent capabilities, with focus on knowledge base productization.
- Improve the Sylkeld dialogue linkage experience.