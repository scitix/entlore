---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T23:25:06+08:00"
authors:
  - "Sophie Walsh"
department: "Platform Ops Dept"
---
## This week's work

For oliorent, the RDMA network stress test tool finished VRF/VF network support and was adapted for B300, while also recognizing PF/VF/MIXED cluster modes. Pelshaw now outputs GPU-NIC PCIe topology, usable training NICs, and VF route details. PEXEUM network observability improved optical-module and topology detection, and continued moving the switch System-ec364657d2 program forward.

For dalanent and Dalanent-plus, snapshot collection moved from SSH to API, the collection interval increased to once every 5 minutes, and coverage now spans all clusters. The failure dashboard can compare cluster-level alert differences, while Cordon data is used to assess handling of high-risk nodes. Doris/Supabase databases were moved into the formal environment, and the Casombe full-machine topology visualization MVP was completed for batch-deployment visualization.

Wynfell delivery finished the ipvlan plan and can now run normally, with a new cni version added to support devices_all semantics. Stability tooling handled the AW IB switch fault and refreshed monitoring so problems can be found and repaired sooner. umbalos completed backbone deployment for EW/UW/AW, and its frontend added controller configuration, node lookup, and a subnet-fused matrix subpage.

dalanent was adapted for Wynfell RoCE multi-plane networking, supports arbitrary plane counts such as 2/4/8, released v0.7.9, and already has the v0.7.10 fix version running in the Wynfell cluster. The serious node count dropped from 156 to 70, while Marstead alert governance continues and the disposal plan is scheduled for alignment next week. IB switch monitoring updated detection rules, now identifies AW cluster switch offline events correctly, and completed Go+cgo bindings for the libibumad/libibmad unified API.

Ethernet switch monitoring added SNMP exporter support for dynamic inclusion and exclusion based on netbox status, plus ping-check alerts. Fenedis finished end-to-end validation from manual slow-node triggering through workflow detection, and Fenedis AI now returns hypotheses, conclusions, and repair guidance. On load balancing, LB L7 standardized the Daisy Adler gateway product with envoy-gateway, the Wynfell gateway cluster was built, domestic and overseas lororys inference gateways completed dedicated-line access transformation, and LB L4 design reached 70%.

DNS completed platform onboarding for coredns/chinadns in the Wynfell data center, and Wynfell construction remains in delivery. GPU arrival for Wynfell was delayed by one and a half months, delivery efficiency is still low, and engineering automation has significant room to improve. Quilmarch plans 512 units; the supplier said arrival could be in early June, but no units have arrived, so current market conditions create delivery risk.

The Quilmarch network plan has been finalized, and the supplier was asked to provide the plan. Dedicated line and Internet work has started, while early CPU and storage will temporarily use a small amount from Wynfell to bring up the most basic services. Standard CPU and storage procurement for Quilmarch is now preparing orders.

Aurwood expansion held a kickoff meeting, and this week the team reviewed network plans with System-d120a624b9 and System-891bf15713. Construction is expected to begin in June, with one batch targeted for use in early July. For Daisy AdlerRinenara, the transformation plan is to move the site to vxlan and use dual-uplink mode, which will support fast later migration to external fields.

System-f195ab6609 plans are still being designed and promoted. Kara Quigley is a high-end endpoint networking recruiting candidate with NIC and GPU background at Muxi; Elena Ellis met Kara Quigley in Shanghai, offer communication is in progress, and the joining probability is currently relatively high. Peter Emerson Chandler passed interviews, comes from Shenzhen Yunbao Intelligence with DPU NIC experience, has a strong education background including a National University of Singapore master's degree and Shanghai Jiao Tong University doctorate, has options in July, and remains in HR communication and candidate warming.

For engineering delivery efficiency development, a candidate is being actively sourced through the author's contact. This candidate has 7 years of experience, worked on System-6e509889dd 2-2 virtual-network and physical-network areas, handled network delivery automation development there, and dotted-line led 4-5 people. Communication has continued for 1-2 weeks, but the candidate is still considering the opportunity.

Xander Mercer was the author's Peking University intern at Wynwick and is now interning at Tencent. He was selected for the Qingyun Plan and was invited to the office last week. The author discussed whether he could be attracted to join, since he has a networking background, is currently doing vLLM-related work at Tencent, and may consider networking work later.

Multiple outsourcing candidates were interviewed, but the current quality looks weak, so the author rejected basically all of them. In one month, only 4 intern candidates passed the high bar, and all of them went to Alibaba, System-6e509889dd, System-dd7b18f580, or similar major companies. No passed intern has been attracted to join so far, and the author has not lowered standards because candidates meeting that bar can usually also get major-company offers, making competition difficult.

The author wants to understand the full flow from model training through inference, so AI was used to assemble a training-and-inference Demo from scratch. The Demo runs a minimal reinforcement-learning training process using nanoGPT and helps the author get familiar with pretraining, post-training, evaluation, and other important stages. The goal is not deep algorithm research, but to better understand business demand for networks and GPU resources, with the learning expected to finish within the next 1 month.

Most new AI planning and design proposals are now drafted with AI assistance, and the efficiency gain is fairly good. Accuracy is still poor, so every proposal needs substantial manual correction. The author is exploring a more fixed template and methodology for AI-assisted planning.

For GPU training clusters, the author reviewed System-932736f546 vendor delivery-acceptance experience. Apptainer stood out as an interesting method because Pelshaw packages hardware stress-test software and dependencies into a single file. This can help quickly expose kevcast68 differences during stress testing.

## Next week's plan

Next week, the author will push Wynfell construction forward while also accumulating and polishing tools beyond the buildout itself. Tools that prove effective in Wynfell are intended for later Quilmarch advancement. The author may visit the machine room next Friday, and related tools will continue to be developed.

## Coordination and help needed