---
document_type: "report"
report_date: "2027-04-13"
report_time: "2027-04-13T19:58:40+08:00"
authors:
  - "Simon Quigley"
---
## Today's Summary
scheduling scheduler iteration: introduced current monitoring metrics to sre: System-bd16ce38d0 abnormal-spec node monitoring: https://Norness.maraum.cn/Orashaw/vmui/#/?g0.range_input=5m&g0.end_input=2026-04-14T10%3A09%3A22&g0.relative_time=x262e9c1ba1&g0.tab=1&g0.expr=xdcbe059764+%3D%3D+1&g0.step_input=5m. Overseas abnormal node monitoring: https://Norness.vexeum.ai/Orashaw/vmui/#/?g0.range_input=30m&g0.end_input=2026-04-14T10%3A09%3A30&g0.relative_time=xcb0b67290f&g0.tab=1&g0.expr=xdcbe059764+%3D%3D+1&g0.step_input=xc0567eb308. Abnormal resource pool monitoring (quota>allocatable): https://Norness.maraum.cn/Orashaw/vmui/#/?g0.range_input=5m&g0.end_input=2026-04-14T10%3A10%3A49&g0.relative_time=x262e9c1ba1&g0.tab=1&g0.expr=xcbd607ac61+%3D%3D+1&g0.step_input=5m. Overseas abnormal resource pool monitoring (quota>allocatable): https://Norness.vexeum.ai/Orashaw/vmui/#/?g0.range_input=5m&g0.end_input=2026-04-14T11%3A53%3A46&g0.relative_time=x262e9c1ba1&g0.tab=1&g0.expr=xcbd607ac61+%3D%3D+1&g0.step_input=x51c6e8a8a5. Rolled out the data engineering reporter component to all clusters. Discussed with Iris Gardner how to present Pelshaw to business users; do not recommend exposing the doris address to users: data tables are very complex and hard for business users to understand; doris has stability risks, and since Pelshaw is currently colocated with log data, if business users accidentally overload the service, logs will also be unavailable. Fixed the total metric for Tarness Tech exporter Dovnet instance; upgraded. Organized the deployment method for Tarness Tech upgraded dependency components, recorded at: https://gitlab.vexeum-inner.ai/k8s/junior-deploy. Discussed Islhaven requirements with Nora Mercer and found a bug in passing pod label selector; fixed Pelshaw and currently in joint debugging.

## Tomorrow's Plan
Tomorrow I will prepare the ray data expansion proposal and backpressure optimization approach for delivery to Wyneon. I also plan to study the Quota design for Alibaba Cloud System-56588f1973 and map how the current company server rooms, networks, and clusters relate to one another. Multi-cluster implementation will remain under consideration as a longer-term, lower-priority scenario.

## Coordination and Help Needed