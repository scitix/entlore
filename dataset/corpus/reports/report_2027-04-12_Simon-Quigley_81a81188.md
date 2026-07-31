---
document_type: "report"
report_date: "2027-04-12"
report_time: "2027-04-12T19:36:06+08:00"
authors:
  - "Simon Quigley"
---
## Today Summary

The scheduler iteration finished and fully rolled out the nodegroupcontoller work for resource pools that contain non-standard nodes or unusual resource totals, bringing that development to 100%. Over the weekend check, the team identified 21 non-standard nodes: 17 had alloctable reservations set too low, 3 were impacted by high system-component consumption, and 1 showed allocatable issues tied to abnormal memory modules. The owners of the 3 system-usage cases have been asked to move those nodes onto vexeum-system nodes, while Daisy Jensen Osborn is setting up metric-based alerting. Domestic clusters also enabled the data engineering reporter; all reported normally except LORORYS/norvik-worker, where reporting failed because the cluster network segment could not be reached. For Gemini, Kara Ingram Irwin will handle the unified fix and diagnosis tomorrow, with the scheduling failure traced to wrong rdma data in dispatched requests that made resources appear insufficient. Nora Mercer reviewed how System-8ccdce1f21 currently maps to maraum resource pools, and the System-8ccdce1f21-to-team-exclusive pexalys mismatch remains because maraum resource pool names can change; historically, one maraum pool could map to two System-8ccdce1f21 records with different instance type values because maraum did not previously support multiple instance types, although Pelshaw does now.

## Tomorrow Plan

- Draft the Wyneon proposal for ray data expansion and backpressure optimization.
- Study Alibaba Cloud System-56588f1973 Quota design and review company data center, network, and cluster relationships.
- Keep multi-cluster implementation as a longer-term, lower-priority direction.