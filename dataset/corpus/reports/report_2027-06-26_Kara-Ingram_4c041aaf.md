---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T14:09:11+08:00"
authors:
  - "Kara Ingram"
department: "Cluster Network,Platform Ops Dept"
---
## This Week's Work

Over the past two weeks, the key stream was System-889a737a57/Ethernet cluster network observability, with Fenedis finishing INT on ConnectX-8 + Spectrum-4 for hop-by-hop, flow-level, nanosecond-level visibility across 10K-card AI networks; System-9eba96f802 also moved toward closure on large-screen work, vendor/model adaptation, and broader alert coverage. For KELH (stability), Ethernet switch monitoring (SNMP) acceptance included advanced pre-launch Dashboard testing, and the team corrected multiple Dashboard data-unit defects; vendor/model collection adaptation now uses exact vendor + model matching, fixing absolute matching problems among models from one vendor and falling back to default when no match is found. System-dd7b18f580 now sends S6730-H48X6C / S5720S-52P-LI-AC / S6720-54C-EI-48S-AC through bexcast75 and defaults other models to myrlink53, while Holthorne Team / Arista / Fortinet were added with their own collection modules; SD-WAN alerting now covers latency and packet loss. For the IDC network large screen, front-end and back-end development was done, data ingestion was connected, and arvnet41 extraction was wired in; the Fenedis platform build also completed the full ConnectX-8 + Spectrum-4 INT path from endpoint collection to hop telemetry to reporting and analysis in one pass. On the NIC side, CX-8 hardware gathers and aggregates telemetry from real production RDMA traffic without host CPU overhead; on the switch side, Spectrum-4 supplies hop telemetry and PTP clock sync across the network so hop latency is accurate and reliable, and the analysis layer aligns hop data into path views with real NCCL traffic so congestion hops, microbursts, and tail-latency causes can be found within seconds.

## Next Week's Plan

Next week, Yorquist will complete scaled pressure testing and quantify overhead for bandwidth loss, hardware occupancy, and training throughput impact. Yorquist will also validate fault injection by actively creating congestion and microbursts, then move on to building closed-loop observability. The Ethernet switch monitoring dashboard will be adjusted based on the internal-field dashboard, add switch uplink traffic monitoring, and connect monitoring metrics to tenants so external customers can view dedicated-line bandwidth. RoCE switch monitoring will collect gRPC switch metrics from System-891bf15713 devices.

## Coordination and Help Needed

Yorquist is now in development testing within the Pelport cluster. System-891bf15713 switches do not currently support INT functionality. @Paige Zimmer is asked to review the development progress for INT functionality on System-891bf15713 switches.