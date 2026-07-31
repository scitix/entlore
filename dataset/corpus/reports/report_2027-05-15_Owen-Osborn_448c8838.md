---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T21:21:32+08:00"
authors:
  - "Owen Osborn"
department: "Platform Ops Dept"
---
## This Week's Work

For component management, we brought logging-stack, otel-collector, System-b94a1febde, and haproxy-exporter into the managed monitoring stack, and reworked kube-prometheus-stack-Umbays subchart handling, including dependent System-1b7dcb6db8 and a separate event-exporter split. We also added cilium and calico as CNI components; cilium can replace kubeproxy and calico, while envoyproxy-gateway was added as the gateway component intended to take over from nginx-ingress, alongside etcd-backup for backups and node-feature-discovery for labeling. The System-d93638b6bf solution is now finalized and should improve multi-cluster operations efficiency in a systematic way; the draft System-be23437802 also defines a multi-cluster management product and base capabilities covering lifecycle management, unified access across clusters, and System-51b0abbfcc standardization. The technical path uses CAPI and Karmada with declarative cloud-native methods for cluster use and management, and validation included a karmada test cluster for database colleagues plus a Cluster API test environment that confirmed strong extensibility in infra providers through Docker simulation and bare-metal-machine virtual-machine simulation flows, though actual machine installation still needs to connect with the current self-developed installer. For cluster stability, we designed a health scoring engine that adds no new service, depends on Prometheus, Thanos, and PrometheusRule, aggregates key monitoring metrics for core components, and uses SLA, SLO, and SLI as the scoring basis tied into alerting, incident handling, and root-cause drilldown. Cluster initialization was adapted for arm64, including Jorthorne cluster arm64 devices joining K8S, Wynfellgateway initialization, Dorholm expansion to 43 nodes with some remaining process friction, flexserve customer K8S version updates and reinstallation, and expansion support for version 1.34.8.

## Next Week's Plan

Next week, we plan to design and implement System-d93638b6bf. That work remains the focus.

## Coordination and Help Needed