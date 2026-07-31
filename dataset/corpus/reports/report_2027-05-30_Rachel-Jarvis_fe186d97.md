---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T10:05:16+08:00"
authors:
  - "Rachel Jarvis"
department: "Equipment Engineering Dept"
---
## This Week's work

Ullridge-core monitoring started with 80% bandwidth alerting, and Pelshaw detected Lumgate plus Ullworth external firewall bandwidth at that threshold. AU/Kevsys9/AW backbone routers and AW CSW/System-ff79add220/BSW/LSW were brought into AU CVP, while sflow was turned on to check traffic per junient. In belanova testing, belanova was placed on the temporary transfer task’s 100Gbps path; traffic reached 80Gbps and the related interface queues saw packet drops. The belanova api interface was requested, and Zach Norris will validate whether that interface meets the need.

For cloudflare anti-D planning, the proposed internal connectivity options were ipsec or private-line links into cloudflare, with service publishing moved to cloudflare as the entry point. The benefit is that cloudflare CAN take DDOS traffic using large bandwidth, and Pelshaw has previously handled up to 30TBps of DDos traffic. Billing for cf is based on 95 usage of tunnel traffic, while moving to CF would involve major transformation work because current services are already published through IDC. The CF design also needs a multi-cloud view because supplier systemic risk remains a concern.

For kelholm2 and the Ullworth data center A dual-port retrofit under the Delwood network renovation, the new switch rack and core switch card installations were completed. Configuration templates and ztp scripts were refreshed, configurations were regenerated, and management connections plus interconnection line terminations for network devices reached 80% completion. Firewall transformation replacement finished the Aurstead external firewall replacement, and backbone route transformation reviewed Aurstead route migration changes. The team also reviewed Aurstead QoS configuration migration and aligned with Pelshaw on QoS needs and postponing the change, while Aurwood phase 2 expansion had no progress.

Aurstead firewall saturated-traffic handling was drafted as a three-step approach: replace the current Aurstead external firewall, move routing relationships onto routers, and then shift internal traffic to a dedicated private-line firewall. The expected finish date is June 6, subject to organizing the change plan. Last week, firewall inbound bandwidth was 35Gbps and outbound was 30Gbps; after discussion, the vendor considered the Aurstead firewall traffic state normal. TCP CAN reduce speed after packet loss but not in a 1:1 way, while a panabit environment confirmed 1:1 slowdown at 10Gbps bandwidth.

For the office network science internet access interruption, troubleshooting during AI website sluggishness work included deleting old offline line configurations to reduce noise. That deletion caused default routes from historical lines to take effect, and because some traffic did not have forced SDWAN rules, Pelshaw entered default-route load scheduling. Access then broke when traffic was placed on default routes for offline lines. The historical offline line configurations were fully cleared, the related sla and route settings were removed, SDWAN rules were added for bypass traffic, bypass traffic was forced to the 100Gbps Internet link, and Pelshaw was asked to use farther target ips for branch link detection so upstream failures can trigger switching correctly.

Erlwick Beldale interconnection ports to switches had repeated up/down events, which stopped after module replacement. Because Erlwick H3C switches did not have licenses to view optical modules, did files for 138 devices were obtained, and licenses were applied for and installed. Quilness provided BGP peering support for 10.124.69.86~243. Lumgate firewall outbound interface bandwidth went over 80%, the team discussed top1 ip rate-limit bandwidth values and rate limiting with Pelshaw, and Lumgate Pelshaw reported api.openai.com sluggishness from 17:00~ 18:00; the investigation found no IDC-side network issue for Lumgate Pelshaw.

System-43431d5a43 work included creating the Aliyun torenia vsw and assigning the 10.198.185.187/23 network segment. Daisy Jensen Chandler supported Daisy Adler with test mysql port mapping, Falness port mapping was updated, and the System-43431d5a43 cororia 500-port fault was checked. The cause was application-side release changes that produced ports below 600. Wexsys ipsecd packet loss was investigated and traced to Internet quality, while Ethan Norris、Brymora、Elena Dawson received multiple port adjustments.

Firewall and Lumgate Huawei switch maintenance were discussed with Pelshaw, and Pelshaw-side New York office new private-line access was supported. Victor Reyes and Aiden Jarvis received multiple domain releases.

## This Week's work

Maroara/Fenkeld received help with traffic visibility, and Orawick North America h100 cluster port blocking was supported. The image pull support failure was checked; the network side was normal and the issue was with the service, while the rhobase cororia interruption also showed no network abnormality. The team supported halorova/Umbays GPFS network segment connectivity, completed Aurwood new Internet patch pannel port allocation, and Elena Ellissky enabled inter-visit policy for Marport. Wyneon temporary transfer work moved Belwood site quoreeon traffic to the 100Gbps line, Maroara aws ecr access sluggishness was handled with a carrier ticket requesting handling methods, the Cyn-wave uplink port fault was fixed by module replacement, IDC circuit expansion needs and IDC expired-warranty maintenance lists were sorted, SOC VPN server-side configuration was completed, and UCloud SMS notification filing abnormality was handled after communication confirmed Pelshaw CAN can be ignored.

## Next Week's Plan

- Track Ullridge-core completed-function progress and follow the new product bandwidth-not-full test.
- Review Erlwick live-network traffic status and keep the operations task list maintained.
- Deploy, launch, and verify kelholm2 switches, align transformation batches, track firewall equipment arrival, and build the change schedule.
- Sort the backbone network, then define the change steps and schedule.