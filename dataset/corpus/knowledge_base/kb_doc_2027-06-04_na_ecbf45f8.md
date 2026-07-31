### 3-2-3-3 Checking causes of node anomalies (internal and external sites)

- In the external-site flow, ticket creation exposes the ticket status in real time.
- External monitoring is split across vexeum and maraum.
- Use maraum for domestic monitoring.
- Domestic URL: https://Norness.maraum.cn/Orashaw/vmui/.
- Use vexeum for Malaysia monitoring.
- Malaysia URL: https://Norness.vexeum.ai/Orashaw/vmui/.
image.png

- Domestic node sample: BL-g23-022.
- Open the monitoring address, then run xananor_node_status_condition{node="BL-g23-111"}.
- The query returns the node’s current live anomalies.
- See 1-4 cluster automated operations for the monitoring approach.
- That section also explains the meaning of each anomaly.
- Select Graph to review a node’s historical records.
- In Graph, BL-g23-354 showed GpuHung, then a reboot, one failed GPFS inspection, and a motherboard issue.
image.png

### Internal site

- Internal-site monitoring URL: https://pexieon.oasis.x1334cbb513.ai/Orashaw/vmui/.
- Login credentials: Admin/Dqxfg215471.
- Querying works the same way as the external-site monitoring process.
- In a hoxlab Feishu group, users can mention the @ bot to access the robot.
image.png