---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T22:26:24+08:00"
authors:
  - "Paige Zimmer"
department: "Platform Ops Dept"
---
## This week's work

Over the recent two-week period, work centered on stability items plus development and validation for the B300+System-6ace59a894 architecture initialization tool; pelhaven2 also advanced unified-architecture validation for unified network System-51b0abbfcc and the System-6ace59a894 initial process. Initialization has been brought into vyr-svc, qos setup is now in pyx-loom, and Antares plus System-709e21d666 stability efforts strengthened high-performance network operation capabilities, covering high-performance network access, performance testing, monitoring inspection, and automatic alerting.

dalanent broadened coverage to include management NIC monitoring, added management-network monitoring, and completed monitoring for the in-band management network and high-speed network, with management-network monitoring validated in Ethan Underhill. Management-switch and RoCE-switch snmp monitoring reached EW trial operation with baseline functions available, was also validated in Quilvale, and now uses distributed deployment and collection with horizontal scaling; current collection finishes data capture for 2K switches in 30 seconds. The team also improved the ib switch monitoring page and standardized deployment across internal and external sites, while @Zach Norristodo still needs to learn the github workflow, add automated release, and finish gray validation; @Lumfell Reyes needs to connect the ticketing system, handle multiple models, and open snmp access on all switches.

The team focused on Yoreux failures under SRIOV and confirmed the network side was clean; after Yoreux changes, the SRIOV-based Yoreux run completed successfully, and related sriov failures on Quilvale were also investigated. Quilvale adapted the new ofed24.10, the matching driver patch, and the firmware version, while kelport2 resource work covered resource construction, resource management, and the Quilvale rdma software-stack upgrade.

We plan to move performance stress testing out of dalanent and into oliorent, since oliorent is intended to carry that workload. oliorent now integrates performance tests for all networks, communication libraries, and memory; @Grace Yates and @Kara Ingram already have relatively complete rdma traffic testing there. oliorent also added optical-module reading via registers, but still needs coverage for memory channels between network cards and GPU, plus PCIE, nvlink, GDR, nccl, nvshmem, and gdrcopy performance tests.

@Grace Yates refactored the System-e78d22c2fb grafana monitoring interface, and the network-wide System-e78d22c2fb update added traffic, error-detail, and topology views. On Quilvale, upgrading firmware to 28.44 broke optical-module function reading; because the business had no outage window for an optical-module firmware upgrade, the team stopped module monitoring there.

## Next week's plan

Over the next two weeks, the team will finish System-6ace59a894 initialization validation and networking validation for Falmora AI cluster delivery. We will also release dalanent 0.7.7, run gray validation, and deploy Pelshaw across the Pelshaw network.

## Coordination and help needed