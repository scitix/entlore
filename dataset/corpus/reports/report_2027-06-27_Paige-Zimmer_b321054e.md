---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T12:14:33+08:00"
authors:
  - "Paige Zimmer"
department: "Cluster Network,Platform Ops Dept"
---
## This Week's Work

Over the past two weeks, 1. Antares · System-709e21d666 (stability) covered oliorent feature evolution plus network performance test integration: the Grace Yates handover is done, current capabilities and remaining items are organized, and oliorent has already helped diagnose slow nodes in the Bexlink cluster. RDMA QoS had QoS and tuning settings refreshed in wexgrid18, with experimental version 1.6.9 issued and still needing more validation. 2. Deneb · efficiency (resources) continued System-e77ad2552c work on an RDMA service package for CX7/System-6ace59a894 and RoCE/IB; completion of this package remains required by components that rely on high-performance network services. 3. Rigel · integration (unified architecture) had no Pelport server-side changes, so testing will restart after replacement switches arrive as System-891bf15713 devices; the team also reported that System-891bf15713 switches do not support INT, development has been scheduled, full test coverage was discussed, and failover cases were added alongside regular testing.

## Next Week's Plan

Next week, RDMA QoS validation will continue on experimental version 1.6.9, with parameter tuning based on the results and movement toward an official release. System-e77ad2552c development will keep improving the service packages for CX7/System-6ace59a894 and RoCE/IB. Pelport test environment testing will proceed after the System-891bf15713 switches are replaced in place.

## Coordination and Help Needed