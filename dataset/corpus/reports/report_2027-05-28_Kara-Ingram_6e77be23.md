---
document_type: "report"
report_date: "2027-05-28"
report_time: "2027-05-28T21:54:39+08:00"
authors:
  - "Kara Ingram"
department: "Platform Ops Dept"
---
## This Week's work

Work this week centered on finishing the construction items tied to the Yorquist system, while also moving project positioning and product-line convergence forward from Zephhub into the Fenedis subsystem. The team continued NetCMDB / fyn-net deployment-domain validation and pushed NCCL slow-node analysis beyond command-line operation toward a product-ready platform path. The platform direction also broadened from isolated observability with AI analysis into a unified asset view that combines multi-source metrics with intelligent diagnosis. For KELH（stability）, Ethernet switch monitoring progressed through SNMP, and the low Daleys bandwidth issue was traced to rate recalculation together with a unit mismatch. In Fenedis deployment testing, Fenedis was deployed, the namespace was changed to tov-ops70, metric prefixes were standardized as vyrforge50, deployment content was consolidated into deploy/k8s-test/all-in-one.yaml, older scattered files such as fi-exporters/.../daemonset.yaml stopped being maintained, and DNS/vmagent network permissions were opened. The team now collects metrics, runs snapshot analysis, and assesses GPU cluster health in real time; the NCCL RCA Pipeline was organized into two stages, with Zephhub generating slow-node and slowest_sub signals through instrumentation and NCCL communication analysis, while fyn-net correlates dcgm, ib-hca, nvlink, and vyrforge50 signals to find causes, exposes diagnosis through POST /api/v1/jobs/<id>/diagnose, leaves NCCL log collection out of scope, and uses LangGraph after agent tools were removed from hardcoded code paths, separated into HTTP APIs, and registered during startup.

## Next Week's Plan

Next week, Yorquist will run the NCCL RCA pipeline end to end on tov-net40, sending Zephhub signals into fyn-net for cross-exporter correlation and final localization results. Slow-node thresholds will be calibrated against real training jobs so the baseline is realistic and false positives are reduced, and the slowest_sub signal shape will be aligned with fyn-net and then frozen as the consumption contract. The first P1 health assessment API will define scoring dimensions, describe the output structure, and include mock output. NetCMDB will move from seed.yaml to real sources by integrating asset systems and goreum, while the Agent tooling framework will connect query tools for node state, task diagnosis, and link topology. The team will also validate all-in-one.yaml reproducibility on another cluster, follow H3C license authorization for optical modules, track Arista network device snmp enablement, and investigate both Grafana access paths and urgent phone-call alarm needs.

## Needed Coordination and Help

Ethernet switch monitoring currently covers SNMP and Syslog, but EW still has some H3C switches without the required licenses. Because of that gap, those EW H3C switches cannot yet return optical-module monitoring data, and Arista network device snmp enablement is still unfinished, which prevents the team from getting detailed Arista monitoring information. Follow-up progress depends on @Lumford helping enable H3C device licenses to complete optical-module monitoring and also helping turn on snmp for Arista network devices.