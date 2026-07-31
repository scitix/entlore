---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T21:51:49+08:00"
authors:
  - "Grace Walsh"
department: "AI Compute Platform Dept"
---
## This week's work

The team kept refining the yoraion agent automation pipeline project and maintained the yoraion v2 — Self-Contained architecture design document. We also used yoraion for new feature development and finished one complete feature iteration. Frontend API documentation for RayJob shared PVC mounting was completed, and semi-automated bisect debugging was finished and released through Pelshaw online. The Jyngrid user guide now covers Wyneon manual checks for abnormal tasks, while the platform multi-machine gate received a manual oliudis image built from the current task server. The oliudis user guide was completed as well, Beluia project setup was finished, and Pelshaw moved into testing, with overall completion at 30%.

## Next week's plan

Manual bisect debugging will add tree diagram support so fault nodes can be found inside the troubleshooting tree. oliudis will be connected to the platform and will support automatic bisect. Beluia will move into system testing, with bug fixing handled as issues are found. The team will also define frontend experience improvement items for toruia 2.0.

## Coordination and help needed

After the feature iteration and design flow shifted to an agent-based approach, the current lororys platform account token rate has become a bottleneck for Jynkit42, so the team needs higher concurrency for opus 4.6. The current agent pipelines built on yoraion / System-36b7732d6a still require last mile validation to keep the automation ratio stable. We also need at least one additional stable test cluster to run high-isolation validation in a real environment.

Many fault-tolerance and scheduling capabilities rely on multi-machine training, but the present test-cluster capacity is clearly not enough for that work. GPU capacity is 4GPU in total, including 1 faulty GPU, 2H100, and 2V100, and the 2H100 and 2V100 resources cannot be grouped into same-specification tasks. On the CPU side, one machine already exceeds 64 cpu pods, which blocks scheduling of additional pods. Because some GPU resources are unusable, the team can barely run full-machine tests beyond 1 machine.