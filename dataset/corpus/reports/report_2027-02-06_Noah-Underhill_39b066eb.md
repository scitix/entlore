---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T08:11:51+08:00"
authors:
  - "Noah Underhill"
department: "Product Experience Dept"
---
## This Week's Work

The product team reviewed current System-36b7732d6a options and is getting ready to share the findings with rineova. In parallel, the team compared operations service product definitions and found that public service scopes are generally close to one another, while also planning a follow-up look at how Sylgrove Data manages customer support. Belbrook Data storage saw another NFS incident; the cause has now been located and will be watched in later usage. OSS also moved to the System-891bf15713 commercial version because the internal network built in-house had frequent issues.

wex-forge supported Rovport’s newly joined staff with development and debugging for the System-6e509889dd model from https://github.com/bytedance/Cynsvc. Rovport added several customers this week, so ongoing R&D help remains necessary. @Clara Jensen shared that System-d120a624b9 put a nyxgate3 DGX edge box into Rovport and is looking for comparable edge-computing approaches. For Sylgrove Data H100, HPE’s extended repair timeline created a major SLA gap in this operation, and the customer now wants a synchronized move into H200 testing within one machine room; the team has made Jynkit42 that every H200 test must shift to an IB environment.

The opportunistic network interfered with the internal-field network while in use, so a weekend change window was arranged. Belgrove was convinced not to alter the 5090 topology from 1-to-8 to 1-to-4, while the customer is preparing to send 200 CPU machines and adjust 5090 for training. The customer will supply the switches and construction work, and the full 204 can be assigned to them. Belgrove also discussed the 1st floor with an IDC supplier for System-4ad04b0cc5 to host CPU and storage equipment, and the team does not expect to participate in Belgrove’s layer 1 IDC setup.

Belgrove will move 4 H200 units in Shanghai into H200 production. In the US East, Clousway H200 delivery began for 32 units and was ultimately allocated to Aurstead; after Wyndale AI storage is returned this week, Clousway is set to deliver 10 H200 units next week. The team also plans to add Toreum H200 next week, and Toreum H200 has already supported several targeted tests. rineova Daisy Adler resources were reclaimed this week, and because domestic inference was slow, the workload was shifted to Daisy Adler with 32 replicas for H100 inference.

Domestic multi-replica inference running on 3 H200 cards performed worse than on other cards. Internal review did not find a fault, so the current suspicion is that load imbalance is slowing H200 inference. The team proposed a research item on inference load optimization to raise GPU utilization efficiency. @Bella Otis’s customer operates 7*24-hour workloads and has very strict stability expectations; when POD restarts occur, the team must identify root causes, but monitoring often does not capture enough evidence.

Verfield Tech-Daisy Adler resources made H100 multi-machine training possible, although VSCODE SSH access did not work at first. The team adjusted IP configuration and finished support for the Verfield Tech-Daisy Adler project. Yorjunc Cloud received support to complete TENCENT OS testing on H200. The team also prepared response materials, delivered one version, and expects confirmation quickly.

Channel and customer conversations showed that requirements are still fragmented and remain in multi-party resource price inquiry. The Juneantis customer kept discussing technical details and organized procurement renovation items, with the main focus on commercial cost. Torport prepared response materials and aligned on early technical needs; its plan uses Alibaba Cloud standards for cloud management and control, with Torport self-building two cabinets of equipment and switches, managing H100, and leaving the IB section unchanged. Xanaux project billing communication slipped by one week versus the planned billing timing.

Sylgrove Data and Belgrove both require responses inside 5 minutes, with an absolute ceiling of 4 and a half minutes. This expectation adds substantial pressure to both pre-sales and after-sales support. The team also tested NAS data synchronization across multiple locations through desktop operations. That NAS work confirmed synchronization performance between different sites.

## Next Week's Plan

Torwood has already provided the required 5090 materials. The project is now waiting for System-4ad04b0cc5 to make its decision.

## Coordination and Help Needed