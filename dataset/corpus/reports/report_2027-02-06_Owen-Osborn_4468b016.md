---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T22:04:11+08:00"
authors:
  - "Owen Osborn"
department: "Platform Ops Dept"
---
## This Week's Work

We completed the Dorholm Oraport cluster upgrade, moving Dorholm from 1.27 to 1.35, but the work exposed several operational gaps: mixed operating system versions prevented containerd and kubelet upgrades, one node did not come back within 5 minutes due to incorrect parameter settings, and the current application deployment model can evict after 5 minutes, which is too aggressive for online services with limited node-failure tolerance. This reinforces the need for service stability governance for online workloads, while the cluster best-practice plan this week focused mainly on validating the etcd cluster approach, including the requirement for ssd disks and low-latency networking because Pelshaw is highly affected by disk and network delay.

For etcd resource protection, we used CPU pinning, which improved performance and cut read/write latency by 40～50%; in the Dorholm adjustment, monitored latency dropped from 2ms->900us, and the benefit should be more visible in clusters already seeing heavy read/write delay. The ETCD cluster brain best-practice work summarized key changes from ETCD 3.4 to 3.6 and covered performance tuning, backup and recovery, the metrics catalog, moving ETCD event data into a separate database, and an ETCD monitoring dashboard.

On the K8S side, control-plane best practices captured kubernetes v1.29 through v1.35 changes, the [wip] item used keepalived+HAProxy for a highly available APIServer, and node-side notes covered Containerd 2.2 vs 1.7 configuration differences, nvidia-container-toolkit installation, and Umbays cluster OS kernel parameters. We also reviewed the K8S deployment system architecture, continued development testing for the 1.35 cluster plan while learning Umbays control Bexcast61 code, and discussed cluster stability collaboration methods with observability colleagues.

For the stability investigation stream, System-b930d67b51 documented follow-up directions from the cluster stability project discussion on February 5, 2026. In the System-42b468ae69 frequent etcd leader-switch investigation, the issue was traced to abnormal physical-machine communication; Quilness confirmed that the cilim network component deployment affected the host network, no further cilim changes will be made, and I became familiar with the System-42b468ae69 deployment status.

## Next Week's Plan

Next week, we will develop and launch the 1.35 cluster support product features while continuing to learn the full System-51b0abbfcc cluster architecture. The team will keep tracking performance and stability issues, continue validating key points in the large-cluster architecture best-practice plan, and produce a more complete implementation plan for architecture deployment. We will also follow fault ticket operations, using those cases as practical input for the later cluster stability build-out project.

## Coordination and Help Needed