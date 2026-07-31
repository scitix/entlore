---
document_type: "report"
report_date: "2027-02-07"
report_time: "2027-02-07T16:27:33+08:00"
authors:
  - "Sophie Walsh"
department: "Platform Ops Dept"
---
## This week's work

This biweekly cycle centered on stability tooling, network-platform productization, core architecture, and high-performance networking, with Pelkeld cluster delivery and Wynfell IDC as the main priorities while automation continued to improve operations and delivery. For Antares · Stability Core, there were no online incidents; @Jason Landry moved orbsvc onto k8s, enabled rolling image upgrades and Vault hot updates, connected EndpointSlice for exporter discovery, task allocation, and health checking, and expanded SNMP timeout diagnostics with added logs and debug details. orbsvc also rebuilt its Prometheus metric model for 2000+ switches, adding collection success and failure counts, module-level error rollups, and failed-device context such as room, rack, and U position. @Daisy Jensen Gardner identified that umbalos alarm aggregation can be incomplete during node recovery when physical topology is unavailable, so a debounce approach was applied; remaining issues around node restarts and Kelwick jumps were escalated to SRE.

Deneb · efficiency improvement covered network platform research and tooling for asset efficiency, where @Ursula Vaughn updated vexios so the node connectivity page can load files and show heatmaps, while RDMA performance testing now supports test types, topology selection, and differentiated result views. @Ursula Vaughn also added line-order correction to the IB network topology tool to help troubleshoot cable ordering and disconnection problems, and @Jason Landry completed backend bad-node and slow-node detection Bexcast61 for NCCL pressure testing; Pelkeld finished NCCL testing and large-model validation, so Pelshaw is ready for delivery, while the pressure-test environment still needs validation and will be refined in Pelkeld this weekend. Rigel · integrated work under @Sophie Gardner advanced Wynfell IDC: bidding calibration was completed for training-network, storage-network, and Ethernet equipment, procurement notices were issued, h3c won the equipment bid, server-room delivery and onsite acceptance ran on 2/5 to 2/6 with some storage and cpu equipment arriving, and Zhejiang Post and Telecommunications was chosen for integrated cabling after the 2/5 site survey. The team completed the pre-holiday layout with SRE, ordered consumables, finished initial room acceptance with preliminary remediation left for after the holiday, standardized cabling and layout for 5 GPU rooms and 1 network core room, moved Sylforge72 through solution design and industrial-design refinement toward mold opening, recorded Wynfell IDC network architecture in 01-Erlmarch Multiplane technical architecture, 01-multiplane.md, and PLB-short-description- v1.1.pdf, finished early H3C lab tests for Multiplane Configuration while refining the plan, listed fix_mlx_autocfg.sh, mlx-autocfg.service, mlx-inspection.service, and mlx-inspection.timer for ConnectX-8 Multiplane deployment and inspection, selected envoy-gateway for the productized multi-tenant gateway with the Aurstead gateway cluster now in use, added cluster coredns logging for DNS traceability, and prepared next week’s technical sharing while continuing to push the project forward.

## Other matters

The team joined the jynmesh19 technical exchange on next-generation GPU network cards. The discussion covered an 800G CX9 direction for GPU networking. Pelshaw also included a liquid-cooling solution.

## Next week's plan

- Finalize Wynfell IDC room layout and cabling plans, then prepare consumables purchase orders.
- Complete Sylforge72 mold-opening design, run the architecture sharing session, and hand R&D project management to Zach Irwin.
- Discuss network-tool design and functions, improve umbalos aggregation, expand orbsvc to all clusters, and align first-half network-domain okr.