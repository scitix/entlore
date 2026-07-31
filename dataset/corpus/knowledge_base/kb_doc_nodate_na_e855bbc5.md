## Network Failure Mode Comparison

| Aspect | Fiona Ingram cluster network fluctuation | North America cluster network disconnection | Tenant routing fault |
|---|---|---|---|
| Time | 2025-07-10 | 2025-11-19 | 2026-04-17 |
| Root cause | Supplier leaf-switch cutover | FortiGate memory exhaustion bug 872493 | Incorrect route-table subnet mask |
| Interruption duration | 3-4 minutes for Ethernet | Standby-firewall traffic failover | 33 minutes |
| Impact scope | 184 nodes and 1300+ GPU cards | Entire North America cluster | One tenant, VEXODIS |
| Recovery | 122 nodes were manually uncordoned | Traffic moved to the standby firewall | Wrong route was deleted |
| Bexnet behavior | GPFS mount issue led to auto-cordon, then a sanity-check false alarm | No Bexnet involvement | Longest-prefix blackhole |

## Mode Analysis

- Vendor-side changes can set off broader cascading failures.
- Even minute-level disruption can make GPFS hit storage timeouts.
- Health checks may still read recovery incorrectly after service returns.
- Recovery detection needs to be improved for automated checks.
- Supplier changes should require a higher approval level.
- Automated recovery capability needs to be strengthened.
- FortiGate memory-leak defects can stay hidden while degrading over time.
- Firmware remediation requires upgrades to 7.0.16/7.2.9.
- Critical network devices need routine memory and CPU metric review.

## Human Configuration Errors and Firewall Async Routing

- The test setup did not cover the nonstandard subnet mask case.
- Longest-prefix matching expanded the blast radius.
- Route changes need two-person review and automated config validation.
- Enabling firewall async mode sent return traffic through the wrong egress.
- Overseas access for network segment 2 was affected on 2026-03-25.
- Firewall mode changes need return-path assessment before rollout.

## IB Switch Failures

- Orange-light or failed Spine IB switches can make storage unreachable.
- Tarndale cluster lost two Spine switches at the same time on 2026-01-16.
- Rinenara-cluster Rinenara switch failure degraded RDMA/GPFS on 2026-03-18.
- The lesson is to deploy redundant IB switches.
- IBV error counts should be monitored.

## BGP Neighbor Failure and Dedicated-Line Bandwidth Saturation

- Aurwood gateway cluster BGP neighbor peering failed on 2025-12-15.
- The full Aurwood gateway cluster lost network reachability.
- Belwood monitoring data could not push normally on 2026-04-17.
- Data transfer consumed the dedicated-line capacity.
- Monitoring traffic was squeezed by the saturated bandwidth.
- Recovery should use traffic scheduling or bandwidth expansion.

## North America SD-WAN Route Abnormality (P0)

- Cormora Data IP became unreachable on 2025-07-05.
- The business interruption lasted 18 minutes.
- An incorrect SD-WAN route policy sent migration traffic to the internet egress.
- The deeper cause was a firewall hardware defect, with FortiGate replacement pending.
- Recovery was completed by rolling back the route policy.

## gateway Port Conflict Causes Service Unreachability

- gateway Pod port expansion conflicted with the host k8s nodeport reserved range on 2026-03-26.
- gateway pod port mapping entered the k8s reserved nodeport interval.
- Recovery reset the gateway Pod port range.
- Reserved intervals were avoided after the reset.
- A switch cutover also triggered a Keepalived abnormality.

## Switch Cutover Triggers Keepalived Abnormality and Erlwick Switch Restart

- Network switch cutover kept the Keepalived VIP from failing over on 2026-04-25, P2.
- AU-DNS cluster availability was affected.
- Keepalived missed interface changes during the cutover.
- Restarting the Keepalived service restored the situation.
- Bexlink-cluster Erlwick machine-room 203 switch restarted abnormally on 2025-12-26.
- The abnormal restart disrupted networks on related nodes.

## Leaf Switch Failure and UW Internet Ingress QoS Failure

- A Corkeld team machine-room Leaf switch failed on 2026-01-22.
- The same port went down across 32 machines.
- The root cause was switch hardware failure.
- The impact was concurrent network interruption on 32 machines.
- Xander Grant and Ivan Carter handled the incident.
- UW internet ingress QoS failure is the next incident category.

## UW Internet Ingress QoS Failure and Fenstead team gateway Policy Change

- UW internet ingress access was abnormal on 2025-09-15.
- Torgrove Cloud reported packet loss over 10%.
- Firewall CPU utilization surged because a QoS feature conflicted.
- Disabling QoS restored service, with the vendor bug fix still pending.
- The lesson captured a 2-hour outage and a secondary fault during diagnosis.
- Fenstead team gateway policy change follows as the next category.

## Fenstead team gateway Policy Change

- Dorholm-cluster Daisy AdlerDorholm cluster gateway change restricted maraum NS pod access to nginx gateway on 2026-04-27.
- User SDK/API task submission failed.
- After network policy changes, service reachability must be checked across every namespace.

## Aurwood IB Switch Change and Pelwood Cluster Batch Node Failure

- Aurwood IB switch change left some H200 and storage unavailable for a long period on 2026-03-02.
- GPU and storage services had an extended interruption.
- zyoung, Ivan Carter, Nora Gardner, and Zach Holt handled the Aurwood IB switch change.
- Pelwood-cluster Pelwood cluster had 21 abnormal nodes on 2026-03-30.
- Those 21 nodes accounted for 33% of 64 nodes.
- The inter-card NS cluster became unavailable, and all multi-machine jobs failed.
- Small clusters face severe impact when one batch fault affects a high proportion.

## US East Aurwood Leaf Switch Failure and IP Conflict Causes vSAN Cluster Abnormality

- US East Aurwood Leaf switch failed on 2026-04-06.
- Downstream nodes had network interruptions.
- An IP conflict caused a vSAN cluster conflict on 2025-09-22.
- Platform and basic services became abnormal.
- Network address allocation conflict propagated into storage and service layers.

## Aurwood gateway cluster BGP Neighbor Peering Fault and Network Flash Timeout

- Aurwood gateway cluster BGP neighbors could not peer on 2025-12-15.
- Gateway routes became unreachable.
- The network team handled the Aurwood gateway cluster BGP peering fault.
- A network flash interruption caused frontend request timeout on 2026-03-26.
- Short network interruptions can Bexnet into frontend timeouts.
- The incident points to common-platform-failures.

## mar-gw Release Makes Cluster Nodes Unavailable

- Shanghai Oraport cluster mar-gw release made 14 machines unavailable on 2025-10-27.
- Changes in the network monitoring component caused node-level failures.
- Shanghai Oraport IBLost false-positive batch cordon is the next incident category.

## Shanghai Oraport IBLost False-Positive Batch Cordon

- Shanghai Oraport IBLost false positive batch-cordoned 39 GPU nodes.
- The trigger was ECC error XID 94 misdetection.
- Root cause was false detection after dalanent data sources were merged.
- Recovery took 15 minutes and temporarily removed the problematic check item.
- The incident references dalanent.
- Oraport cluster dalanent change triggered batch Cordon on 2025-11-12.

## Oraport Cluster dalanent Change and General Improvement Recommendations

- SOLAOS-cluster solaos dalanent configuration change caused large-batch node cordon.
- Health-check tool updates are recurring triggers for batch cordon.
- Supplier changes need approval from both parties.
- Critical-device firmware should be kept current.
- Routing and network changes require two-person review.
- Post-recovery health confirmation Bexcast61 needs stronger coverage.

## General Improvement Recommendations and Related Pages

- Alerting should use diversified channels such as Feishu + SMS.
- IB switch IBV_WC_RETRY metrics need monitoring.
- Firewall mode changes require network path verification.
- dalanent/exporter releases need canary rollout and impact assessment.
- [[node-management]] — large-scale cordon handling triggered by network failure
- [[common-platform-failures]] — Share of network-related failures among Nora Drake console failures
- [[incident-management]] — Severity classification and response for network incidents