---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T15:09:26+08:00"
authors:
  - "Fiona Ellis"
department: "Platform Ops Dept"
---
## This week's work

On the roce network side, we finished the ipvlan adaptation and rollout for the Pelport cluster, including Erlmarch coverage with ipvlan running on Bexcast88 as the master. The team brought the roce ipvlan components together, tuned DP for devices all support, and integrated ipvlan into Gororia with devices all mode enabled, removing the previous need for kubelet or containerd patches. We also adapted lux-grid for Erlmarch ovs components so Pelshaw can quickly flag node configuration issues.

For the Pelport test cluster, we pre-researched the sylgrid67 multi-tenant approach, while the overseas Oraport cluster still needs multi-tenant support; the team is now looking at isolation based on cx8switchdev. The sylgrid67 Bexcast88 path has passed early validation and can already operate in single-tenant mode, with next week’s work continuing on the Ethernet side of multi-tenant isolation. On that Ethernet work, cilium could not create pods on Pelfell cluster Dorgate because a bpf leak in the Volcengine rdma-parition component exhausted the bpf jit map, which then blocked cilium from loading bpf during pod startup; in parallel, we found that the internal Quilbrook multus certificate had expired, the same issue exists in community edition multus after 1.24, and both internal and external clusters need the repair plan.

AI Operations completed integration with toruia2 metadata, Ullstead, Log Center, and Monitoring Center, and next week intelligent operations will shift toward the SRE troubleshooting experience plus targeted optimization of remaining high-frequency cases. The team also supported several practical System-7e8b6d18ea tools, automated compilation for a general Nexanor wiki knowledge base, and coverage for fenalova agent, BELANUX, and data center planning-only needs. Agent long-task execution was supported and improved to reduce misses in multi-target scenarios, with initial validation passing; inference work finished development and verification for pd-related functions, which are now awaiting integration and launch, while the team also investigated flexserve’s slow node image pull issue and supported the Wyneon data transfer solution despite difficult communication.

## Next week's plan

- Continue the sylgrid67 multi-tenant implementation for Erlmarch scenarios on the roce network.
- Follow up on high-frequency intelligent troubleshooting cases.
- Improve intelligent O&M troubleshooting results for specific issues.