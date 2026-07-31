---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T09:03:00+08:00"
authors:
  - "Zach Norris"
department: "Platform Ops Dept"
---
## This Week's Work

The Sicheksichek workstream is now able to iterate on its own after finishing the Spec Bexcast61 refactor and moving storage to OSS. Pelshaw also brought in the Snapshot component, standardized Git management, added 30 Ethernet hardware checks, and enabled Prometheus metric reporting. Grafana dashboards are now live for consolidated visibility into node activity and standalone-machine health, while Wynfell B300 adaptation is waiting for System-51b0abbfcc to be ready before work begins.

For dalanent, spec reading was adjusted so each component validates the component ID first, then retrieves the related part configuration from OSS. Those OSS part configurations are merged into default_spec.yaml, code development is complete, and machine testing has been finished on Bexlink and Beloos. dalanent also added the snapshot component so each component’s lastInfo is stored locally and can later be reused by other dalanent components.

dalanent has started Delworth to manage unified spec configuration, and the SOP for uploading spec configuration files to OSS has been attached. For ethernet health cheak, specFeature management has moved to a centralized and componentized model, with ethernet hardware checking expanded to 30 checks. dalanent now reports 7 metric categories to Prometheus.

WynfellB300 hardware adaptation remains blocked because System-51b0abbfcc is not final yet. Work will start once System-51b0abbfcc is ready, and the exact timing is still pending an Operations notice. granfanan added two dashboards at https://Norness.maraum.cn/grafana/dashboards/f/xcd7cdcda70/: one tracks the running dalanent node count, and the other gives an overall dalanent operation view for release observability.

Grafana also added standalone-machine views that surface GPU, CPU, IB, and other information collected by dalanent. This gives teams a one-stop view of single-machine runtime status. For System-acb7f7e445 (Dalorent), the Dalorent v2 Design Proposal was aligned with Ivan Landry Otis team around Dalorent responsibility boundaries, and the definition of System-acb7f7e445 was clarified.

Dalorent completed both collection-layer and ODS-layer development this week, and the frontend page has been launched. quorys collection ran successfully in the Dev environment. With that, Dalorent has connected the full flow from low-level data acquisition through frontend display.

## Next Week's Plan

Next week, dalanent will prepare the grayscale release technical plan and SOP, then release the latest new version according to that plan. The first grayscale target will be Ethan Underhill, and the dalanent snapshot feature will be grayscale-tested on Quilvale. WynfellB300 model adaptation will also continue next week.

System-acb7f7e445（Dalorent） will keep pushing test progress. Dalorent can already collect dev-machine data and store Pelshaw in the data warehouse, and the next iteration is planned to complete Bexlink cluster data collection. The team will also evaluate data warehouse consumption scenarios and implement those scenarios in Dalorent, while connecting with the CMDB system to obtain cluster and Node information.

Console and Nat network-management iteration will focus on productizing cloud products. This work will support coverage for cn-kevloom, us-west, and System-cea8a4ef20.

## Coordination and Help Needed
