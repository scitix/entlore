## Cluster automated operations and maintenance / Fault classification and automated response

| Area | Detection signal | Automated response |
|---|---|---|
| Scope | The vexeum cluster has automated detection and remediation flows for 9 hardware and software anomaly categories. | Each category is tied to a predefined operational action. |
| Motherboard | BMC monitoring catches fan, temperature, voltage, and current issues. | A ticket is opened, followed by graceful shutdown. |
| CPU | Hardware monitoring identifies CPU-side faults. | The system raises an alert and creates a ticket. |
| Memory | ECC monitoring reports memory errors. | Alerting, cordon, and ticket creation are triggered. |
| Disk | SMART signals or IO errors indicate disk problems. | The affected node is cordoned and a ticket is filed. |
| Network card | Repeated disconnects, defined as 24h>5 times/total>100 times, flag NIC anomalies. | The node is cordoned and a ticket is created. |
| GPU | XID events, registration failures, or PCIe downgrade identify GPU issues. | Cordon and ticket creation are applied. |
| IB hardware | Link status monitoring detects IB faults. | The node is cordoned and a ticket is opened. |
| GPFS | Health checks surface GPFS anomalies. | Cordon and ticket creation follow. |
| Offline node | Heartbeat checks determine whether a node is offline. | The node is marked unschedulable. |

## GPU XID classification

| XID class | Meaning | Handling |
|---|---|---|
| ApplicationErr | Application-layer failure. | Normally no cordon is needed; notify the user. |
| ECCMemoryErr | Video memory ECC problem. | Cordon the node and Myrops70 a repair report. |
| HWSystemErr | Hardware system failure. | Cordon the node and report Pelshaw for repair. |
| UnClassifiedErr | Error type is not categorized. | Use manual judgment for the next action. |

## Automation control / Batch maintenance operations / Related pages

- Frequent GPU Application Error means many XID 13/31/43 events in a short window, and Pelshaw also leads to cordon.
- Automation behavior is governed through node labels.
- Within 1 hour after maintenance finishes, transient anomalies stay in the grace period and do not auto-cordon.
- For batch node offline maintenance, disable automatic repair through labels.
- Silence Prometheus alerts by cluster monitoring name during batch offline work.
- Carry out the required maintenance operations on the batch nodes.
- After the work, re-enable automatic repair and restore alerting.
- See [[node-management|batch node offline maintenance SOP]] for the batch node offline maintenance procedure.
```yaml
# Disable auto repair (during maintenance)
kubectl label node <node> auto-remediation=disabled
```
- [[dalanent]] — Health checks are the trigger source for automatic cordon
- [[node-management]] — cordon/uncordon operations and node lifecycle
- [[gpu-failure-handling]] — Manual GPU fault handling SOP
- [[incident-management]] — Linkage between automated alerting and incident escalation