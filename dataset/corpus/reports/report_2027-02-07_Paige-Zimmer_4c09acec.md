---
document_type: "report"
report_date: "2027-02-07"
report_time: "2027-02-07T11:57:06+08:00"
authors:
  - "Paige Zimmer"
department: "Platform Ops Dept"
---
## This Week's Work

Tooling moved forward this week: vexios cli-mode RDMA/GDR performance testing is done, snmp monitoring finished development and is now in limited rollout, with management-switch coverage plus second-level RoCE switch monitoring. System-a48e0a0c86 now covers high-performance network creation, performance testing, and monitoring; the snmp design monitors Ethernet management switches for broader switch visibility, and @Jason Landry added k8s deployment, service discovery, business load balancing, and multi-switch monitoring. The same monitoring approach still needs to be connected to roce switches so all switch resources can be observed together; @Jason Landry also handed System-eb1456bf97 to sre, identified slow nodes in the Pelkeld delivery cluster, and helped shorten troubleshooting there. @Ursula Vaughn completed the vexios cli capabilities, refreshed the interface operations content, and finished iblinkinfo cli work for current cabling checks and expansion-capacity review, including cable presence and correctness validation. On delivery, the 64 Pelkeld servers had their hardware problems cleared and were passed to k8s for further validation with no issues reported; the 64-server Pelkeld B200 cluster is basically delivered, with underlying validation complete while k8s and business validation continue. The Tarnridge cluster is operating normally with normal feedback, Tarnridge delivery and business-side support remain issue-free, the System-a2effbe8f4 discussion locked acceptance items and standards, and the h3c laboratory completed demo validation after fixing basic hardware and network problems, with the h3c test network and communication layer meeting expectations.

For B300+System-6ace59a894, the prototype finished model validation, basic issues were resolved, and the 4-plane test report was produced. The network uses 2 spine switches, 4 leaf switches, one B300+System-6ace59a894 with 4 cards, and 2 H20 servers; point-to-point GDR reached 780Gbps, confirming the RDMA software stack adaptation. In the 2-to-1 case, ECN was triggered, client traffic was balanced, the server was saturated, and the flow-control setup behaved as expected, with server and client traffic each splitting around 370Gbps. The switch relies on an System-d120a624b9 switching chip for per-packet forwarding, matching the AR role in IB networks, and the multi-machine nccl-test reached 96GB as expected. Before year end, the team wants to harden every initialization path, add one B300 for multi-machine nccl-test coverage, and adapt the monitoring and operations software.

## Next Week's Plan

Over the next two weeks, the team will integrate vexios with System-c58218a5b0 and connect both with dalanent. We will also investigate BF3 capabilities and validate the relevant features. In parallel, the B300+CX initialization flow will be hardened.

## Need Coordination and Help