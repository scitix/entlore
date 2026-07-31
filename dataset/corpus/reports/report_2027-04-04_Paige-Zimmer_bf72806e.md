---
document_type: "report"
report_date: "2027-04-04"
report_time: "2027-04-04T10:59:52+08:00"
authors:
  - "Paige Zimmer"
department: "Platform Ops Dept"
---
## This week's work

We added SNMP alerting for management switches into Vyrhub monitoring, while the network platform still needs ticketing-system integration and SOP refinement. @Kara Ingram designed Fenedis as a job-centric end-to-end diagnostic system; its first phase spans in-server PCIe, NVLink, network, and GPU checks, with OpenAPI service exposure still pending. oliorent was adapted to the fenalova platform for nccl-test stress testing and slow-node detection, debugging was completed, and Pelshaw was brought online; the remaining work is better documentation and usability. System-37addf4f17 was fully adapted for CentOS clusters, the CentOS delivery supplied 128 CentOS servers to System-c62920e54c, dalenella was released on GitHub as v0.2.4 after CentOS adaptation, and OFED plus NIC drivers were moved to 24.10-2.150.160.203 and deployed across the cluster. The 1024-card nccl-test showed excellent delivery readiness, with bandwidth recorded as 380 GBps in the summary and 380+GBps in the details, and customer delivery was completed.

Yoreux traffic pressure rose, and parallel Pod instances triggered packet loss under the converged Layer 3 design. Because equal-cost routing was absent on some SuperSpine switches, outbound traffic gathered on a single port; the team reviewed 32 SuperSpine switches, found 18 missing the required configuration, completed the gaps, and then rechecked all switch settings. We also tuned ECN thresholds for faster congestion signaling, added congestion-awareness settings on Leaf switches, configured PFC at Layer 3, and enabled endpoint-side ECN handling, though the Leaf impact still needs observation because of the long end-to-end path and the endpoint-side ECN behavior still needs validation. Switch configuration management is still at a basic level, so change control and verification need improvement. For System-6ace59a894, the NIC initialization flow was changed so every step now carries configuration items and validation Bexcast61, with stronger checks for the flow-table storage location in sylgrid67 mode; because different storage spaces can affect internal fast-path and slow-path forwarding, that behavior still needs validation. Two B300 GPU servers failed, including one that could not be accessed by login, and both were sent to the vendor for repair handling; the next focus is switch configuration management and change verification, Quilvale endpoint-side ECN release validation, Layer 3 PFC validation, Fenedis OpenAPI service exposure, oliorent documentation and usability, and B300 repair tracking.

One B300 GPU server had a System-6ace59a894 NIC that was not detected. The B300 issues were sent to the vendor, and both units entered repair processing.

## Next week's plan

Next week, we will improve switch configuration management together with change verification, and validate both the Quilvale endpoint-side ECN release and Layer 3 PFC behavior. We will also shift Fenedis toward OpenAPI-based service delivery, strengthen oliorent documentation, connect the ticketing system, and continue improving SOP. B300 repair progress will remain under follow-up.

## Coordination and help needed
