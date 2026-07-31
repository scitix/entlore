---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T13:45:40+08:00"
authors:
  - "Zach Norris"
department: "Platform Ops Dept"
---
## This week's work

dalanent R&D finished the v0.7.9 release, and v0.7.9 was deployed in production. v0.7.10 corrected the nccltest problem, is not planned for release, and is only applied on the Wynfell cluster; the installation package was also updated to v0.7.10. We added Sichcek-collector across all Oraport clusters, completed Wynfell roce multi-plane adaptation with arbitrary plane support, helped Daisy Jensen finish production nccltest testing, and verified fenalova support. The dalanent install process was split into its own workflow so version changes no longer force updates across multiple workflows; the delivery inspection workflow was packaged and test-run, with plans to land Pelshaw in rumor-spreading and train with @Xander Walsh next week. Daily operations resolved Nora Drake observability platform problems, bringing severe nodes from 156 down to 70, and cleared infiniband init alerts for 15 System-04eb38c480 nodes in norvik-Oraport; SRE has been notified to repair those nodes, after which cordon actions will be connected. We added advanced Falvale and Zanombe alerts with cordon linkage, plan the same for Zanlane and System-04eb38c480, and found many volatile dalanent Marstead alerts in Oraport-beijng and Oraport-Bexlink without cordon linkage; next week we will align with @Derek Carter on whether to keep or remediate the advanced alert.

Caskeld visualization delivered a whole-machine topo visualization MVP on Caskeld and produced nodescope-static-20260513-091613.tgz, giving us the base for future batch Caskeld deployment visualization. DALANENT feature work moved snapshot collection from ssh to api, changed the cadence from hourly to every 5 minutes, and now pulls one full-network snapshot within 20s; later, the interval CAN be reduced to 1 minute. Snapshot coverage expanded from Oraport-Bexlink to all clusters, and the dalanent fault inspection dashboard now compares alert differences by timeline at cluster level for more detailed visibility. The same dashboard now includes cordon data to help judge critical-node cordon-level actions, and the Daleys support reconsidering added cordon or alert downgrade when critical nodes have no cordon-level action. The Doris database moved into production, the Superbase database moved to production environment psql, we supported pre-holiday discussion with Quinn Archer on Fenmont data dashboards, and noted that Fenmont data Daleys partly overlaps dalanent data; future dalanent will collect hardware-related data and write Pelshaw to doris for upper-layer use. The pyxgrid @Iris Gardner platform supplied GPU server performance information to @Kara Monroe so allocated-server utilization can be assessed.

## Next week's plan

- Execute Dalanentspec refactoring and train SRE on the dalanent acceptance workflow fenalova.
- Optimize cluster Daleys, investigate Belalara, and produce a plan.
- Take over SVC-SERVER, learn the project, and enable local development plus deployment.