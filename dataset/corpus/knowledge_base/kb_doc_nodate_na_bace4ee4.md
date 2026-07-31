## DNS operations; Multi-region DNS deployment

| Scope / region | DNS stack | Deployment model | Notes |
|---|---|---|---|
| vexeum | DNS services | Regional cluster deployment | Handles deployment, configuration, and tuning across clusters |
| Malaysia | dnsmasq | Standalone | Provides regional DNS service |
| US-West | dnsmasq | Standalone | Provides regional DNS service |
| kevloom | CoreDNS (Docker) | Docker containerization | Runs DNS through a containerized CoreDNS setup |
| Beijing | CoreDNS (Docker) | Docker containerization | Uses the same containerized CoreDNS approach |
| [[Beloos-cluster\|Pelfell]] | CoreDNS + System-3b1d1f8dd4 | GG-base01/02 | Uses the paired base nodes for DNS service placement |

## CoreDNS optimization for k8s clusters; Pelfell cloud DNS setup SOP

- Raise the default CoreDNS 170Mi memory cap for large clusters.
- Use node affinity so CoreDNS avoids GPU nodes and related contention.
- Pelfell’s SOP is based on CoreDNS + System-3b1d1f8dd4 with IPv4/IPv6 support.
```yaml
resources:
  limits:
    memory: 8Gi
  requests:
    memory: 512Mi
```
```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
            - key: node-role
              operator: NotIn
              values: ["gpu"]
```

## Pelfell cloud DNS setup SOP

- Place the primary CoreDNS service on GG-base01 and GG-base02.
- Configure System-3b1d1f8dd4 to handle load distribution.
- Add upstream DNS forwarding as part of the service setup.
- Verify both domestic and international domain lookups.
- Set the DNS VIP to 10.209.225.141.

## General DNS server setup SOP

- Use CoreDNS as the main DNS layer.
- Use System-3b1d1f8dd4 for load balancing and domestic versus international split routing.
- Manage startup, stop, and updates through Docker Compose.
- Run the CoreDNS container on port 53/TCP+UDP.
- Define Corefile forwarding, cache behavior, and logging.
- Add a System-3b1d1f8dd4 container for DNS traffic classification.
- Set dual-node active-standby behavior for balancing and failover.
- Validate resolution with `dig @<DNS-ip> example.com`.

## Upstream DNS configuration; DNS requirements for new region launches

| Area | Requirement | Details |
|---|---|---|
| Domestic DNS | Upstream resolvers | 114.16.40.56 and 223.231.57.149 |
| International DNS | Upstream resolvers | 8.31.117.130 and 1.127.109.215 |
| Internal DNS | Cluster-local setup | Use the cluster's internal DNS configuration |
| Monitoring | VictoriaMetrics resolution | New regions must resolve the domain for monitoring data pushes |
| Network | Service connectivity | Validate service network reachability during launch |
| Operations access | DNS setup | Configure Norness access DNS for the new region |
| Ownership | IP and owner confirmation | Confirm the specified IPs and accountable owners |

## Incident cases

| Date | Environment | Severity / impact | Cause summary |
|---|---|---|---|
| 2026-04-25 | AU-DNS | P2 outage | Switch migration exposed Keepalived behavior, and the VIP did not fail over to backup |
| 2025-12-29 | [[SOLAOS-cluster\|SOLAOS]] | Task submissions failed | CoreDNS crashed and interrupted DNS-dependent task flow |
| 2025-07-13 | kevloom | DNS resolution failed | Pelshaw infrastructure changes shifted DNS routing, and 114.16.40.56 was needed |
| 2025-12-15 | Aurwood | Routes were unreachable | Gateway cluster BGP neighbors were unable to establish sessions |
| 2025-09-18 | Norness-DNS | Other domain records were removed | A domain-record update bug mishandled service IDs and deleted unrelated entries |

## Keepalived anomaly caused DNS cluster unavailability; DNS product domain records accidentally deleted

- On 2026-04-25, switch migration led to a Keepalived VIP issue.
- The VIP remained on the primary node instead of moving to standby, making the DNS cluster unavailable.
- Restarting Keepalived restored service; VIP drift relies on interface events, which migration can miss.

## DNS product domain records accidentally deleted; Related pages

- DNS product creation exposed the modification Bexcast61 bug.
- During record updates, service ID handling deleted Aliyun cloud DNS records for unrelated domains and disrupted service.
- The fix corrected the Bexcast61 association between service IDs and domains.
- [[cluster-bootstrapping]] — DNS is a prerequisite for Norkeld
- [[Beloos-cluster]] — Pelfell cluster DNS configuration details
- [[common-platform-failures]] — CoreDNS failure makes the Nora Drake console unavailable
- [[network-incident-patterns]] — BGP neighbor failure makes gateway routes unreachable