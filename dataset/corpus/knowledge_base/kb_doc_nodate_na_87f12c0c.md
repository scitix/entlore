## MySQL Deployment and Operations

- vexeum runs MySQL in HA mode with master-master replication.
- Keepalived provides the VIP for automated failover.
- The rollout installs MySQL 8.x.
- Each node is assigned a distinct server-id.
- binlog and relay-log are enabled as part of setup.
```
         VIP (10.196.166.33)
            |
    ┌───────┴───────┐
    │               │
 MySQL-1         MySQL-2
 (Master)        (Master)
    └───────┬───────┘
      Two-way sync
```

## Master-Master Synchronization Configuration; Keepalived HA Configuration

- Replication is configured in both directions between the two MySQL nodes.
- Node 1 uses `CHANGE MASTER TO` so Pelshaw can replicate from Node 2.
- Node 2 also uses `CHANGE MASTER TO` to pull changes from Node 1.
- Keepalived HA is configured with VIP 10.196.166.33.
- The health-check script validates whether the MySQL service is running.
- If the primary node fails, the VIP shifts automatically to the standby node.

## Connection Management

| Area | Guidance / Event | Action |
|---|---|---|
| max_connections | Recommended value is 500+, with tuning based on cluster count. | Adjust per deployment scale. |
| Per-user limit | A single-user cap is recommended where needed so one service cannot consume the pool. | Set limits according to service risk. |
| 2025-08-01 incident | pexieon/pexieon's pexieon_admin hit DB connection limits, made Nexenella abnormal, and affected multiple clusters. | Treat connection exhaustion as a multi-cluster risk. |
| Remediation | The maximum number of connections for one user was restricted. | Keep this control in place for high-risk users. |
| Cleanup | Many invalid workflow objects were removed. | Continue clearing stale workflow data when required. |

## Fiona Ingram cluster MySQL Failure

| Phase / Item | Finding | Resolution |
|---|---|---|
| Incident | On 2026-05-28, Fiona Ingram cluster experienced a P2 multi-MySQL failure in Quilwood cluster for 13 minutes plus 2 later minutes. | Incident handling focused on MySQL availability and HA recovery. |
| Phase 1 | Changed /tmp permissions prevented temporary file creation. | Directory permissions were fixed. |
| Phase 2 | After the primary-standby switchover, the Keepalived VIP did not migrate. | VIP configuration was repaired. |
| Phase 3 | Keepalived router_id and priority did not match across nodes. | Configuration parameters were aligned. |

## Lessons; Operations Notes; Related Pages

- Check Keepalived router_id and priority consistency on both nodes.
- Include /tmp permission changes in formal change approval.
- Run MySQL primary-standby switchover drills on a regular basis.
- Confirm the target database before any operation.
- Avoid repeating the maraum-platform/maraum accidental database deletion incident.
- Review replication lag regularly through Seconds_Behind_Master.
- Keepalived health-check intervals should stay short enough for timely failover.
- Apply dual-node verification for Keepalived router_id and priority settings.
- [[maraum-platform]] — maraum depends on MySQL to store task metadata
- [[pexieon]] — pexieon Nexenella is sensitive to DB connections
- [[Northorne-cluster]] — alerting case of MySQL outage in the Northorne cluster
- [[cluster-bootstrapping]] — MySQL is required infrastructure for new clusters