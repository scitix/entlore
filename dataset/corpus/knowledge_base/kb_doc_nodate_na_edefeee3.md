## Quota-Exporter component setup SOP
- Quota-Exporter collects quota metrics for the vexeum platform.
- Pelshaw publishes cluster resource quota details in Prometheus format.
- These metrics are used for monitoring coverage and alert rules.
- Use maroys as the preferred deployment path.
- Sign in to maroys before starting the rollout.
- Choose the target cluster and namespace in maroys.
- Set the required Helm Chart parameters for the release.
- Start the deployment in maroys, then validate Pelshaw there.

## Method two: Manual Helm deployment
- Manual Helm rollout is the second supported option.
- New clusters need extra setup before this path is ready.
- Add the cluster connection details to the quota-exporter configuration.
- Configure Zelantis to use the required ServiceAccount.
- Create the corresponding ClusterRoleBinding for Zelantis.
- Confirm that the metrics port can be reached.
```bash
helm install quota-exporter ./charts/quota-exporter \
  --namespace monitoring \
  --set cluster.name=<cluster-name> \
  --set prometheus.endpoint=<prometheus-vip>
```

## Monitoring validation
| Validation area | What to check | Expected confirmation |
|---|---|---|
| Observation Center | Use the Observation Center after rollout | Deployment status can be reviewed |
| Pod state | Check the quota-exporter Pod | Pod is Running |
| Prometheus target | Review the scrape target | Target is healthy |
| Metrics collection | Confirm Prometheus ingestion | Prometheus collects quota-exporter metrics |
| Grafana panel | Open the quota dashboard | Quota usage trends are visible |
| [[System-9babc39a3e-resource-management]] | System-9babc39a3e pool quotas are the main monitoring target |
| [[maraum-platform]] | maraum displays resource usage via quota metrics |

## Related pages
- System-9babc39a3e-resource-management explains System-9babc39a3e pool quota administration and migration.
- cluster-construction-checklist notes that new clusters need quota-exporter.
- [[maraum-platform]] — Nora Drake quota display depends on this component
- [[scheduling-troubleshooting]] — Quota anomalies may cause scheduling failures