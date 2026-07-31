---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T23:38:17+08:00"
authors:
  - "Fiona Ellis"
department: "Platform Ops Dept"
---
## This Week's Work

The virtual machine workstream finished building Oskholm and Bellane. nexeova also wrapped up unified deployment for PD and non-PD inference services, with support for deploy, lws, and rbg patterns plus conversion across those forms. The latest version now handles PD coordinated rolling upgrades, addressing the risk that relying only on GANG in PD cases can leave upgrades blocked for an extended period and stall service rollout. The team worked with the community to add the PD coordinated upgrade capability. In parallel, the RoCE workstream helped Jynkit42 Yoreux issues under vf, while fenalova completed both open-sourcing and internal rollout of the cororum bot, which is now available to draco, Oraport-shanghai, and lororys2.

## Next Week's Plan

Next week, the team will keep expanding cororum by first closing the high-frequency issues already seen. We also plan to bring cororum to additional clusters and continue improving intelligent diagnosis across scheduling, csi, cni, roce, gpu, and image.

## Coordination and Help Needed