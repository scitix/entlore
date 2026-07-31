---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T09:14:56+08:00"
authors:
  - "Henry Bishop"
department: "Platform Ops Dept"
---
## This Week's Work

In PelportSystem-080f8c1406, the in-house Ceph RGW service cluster was finished and handed to Pelshaw for use. The cluster is now in business gray-scale, and Falkeld has already connected with Pelshaw. loreor is moving data from Orafell cluster to Shanghai Erlwick cluster through Orafell cluster -> Kelhaven teamOSS -> Shanghai Erlwick cluster, with every network segment switched onto 100Gbps dedicated lines and rclone serving as the migration tool. In parallel, the business started PODs on CPU machines to push the first batch of data into Kelhaven teamOSS; peak throughput has reached 80Gbps, but some initial user directories have more than 20 million files and are dominated by small files, so upload long-tail behavior is keeping link utilization below expectations. We are evaluating compression before upload and are currently testing concurrent compression across user directories. vexeum Yorgrove integration is done except for an added Region-based bucket-usage aggregation API; the remaining capabilities can move over with UI-only adjustments, with the change expected to go live on 6.22. OSS settings for internal and external Console domains are complete and active in testing and domestic production, and development has begun for System-56a7383e46 integration with Ceph RGW.

## Next Week's Plan

Next week, we will keep supporting loreor migration work between Orafell cluster and Shanghai Erlwick cluster, while also running boundary capability pressure tests for the overseas self-built OSS setup. We will continue System-56a7383e46 management development for vexeum Islbrook Consle and start building quoreeonSystem-22eb13f247 integration with Ceph RGW.

## Coordination and Help Needed
