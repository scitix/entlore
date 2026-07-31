## rineova inference service

- rineova is vexeum’s platform for large-model inference.
- The service covers management for online inference tasks.
- On 2026-04-05, one user action path left inference tasks stuck from deletion.
- In scale workflows, junient was removed first, so later delete steps broke.
- SRE cleaned up the affected instances by hand.
- Code safeguards were added to enforce the required operation sequence.

## External network access interruption; shared-pool resources occupied causing task clearing

- On 2026-03-25, rineova access from the external network became unavailable without warning.
- The incident matched the same underlying failure as the overseas access outage for the 2 segment.
- Firewall asynchronous mode introduced asymmetric routing in that 2026-03-25 event.
- On 2026-05-15, customer shared-pool capacity was occupied, clearing tasks unexpectedly.
- The same 2026-05-15 resource condition also caused abnormal resource-pool conversion.
- Xander Grant and Jason Irwin worked the shared-pool resource incident.
- The 2026-05-15 case is tracked with [[System-9babc39a3e-resource-management]].

## Smart-routing image pull failure; concurrent call port exhaustion

- On 2026-04-24, smart-routing could not pull its image, so the smart junient for large-model inference did not start.
- Pulls from DockerHub failed because the external source could not be reached.
- Remediation moved image retrieval to a self-managed registry source.
- The 2026-04-24 smart-routing case links to [[harbor-registry]].
- Concurrent call port exhaustion was logged as a known issue on 2026-03-26.

## Inference service domains with added Oskmarch cluster

| Item | Region | Gateway | Access | Notes |
|---|---|---|---|---|
| Large-model service concurrency |  |  |  | Concurrent backend calls used up all ports, and some requests failed. |
| Port-range remediation |  |  |  | The fix increased the available port range. |
| Oskmarch | US West | inference-Oskmarch | internal-network access | Added in 2026 to broaden global inference coverage. |
| Auriga | Beijing | inference-auriga | internal-plus-public access | Regional inference entry point. |
| Bryford | Shanghai | inference-Bryford | internal-network access | Regional inference entry point. |
| SOLAOS | US East | inference-SOLAOS | internal-network access | Regional inference entry point. |
| Bexlink | Shanghai | inference-Bexlink | internal-network access | Regional inference entry point. |
| Beloos | Pelfell | inference-Beloos | internal-network access | Regional inference entry point. |
| Dorholm | Daisy Adler | inference-Dorholm | internal-network access | Regional inference entry point. |
| Pelwood | Pelkeld | inference-Pelwood | internal-network access | Regional inference entry point. |

## Inference service lux-core-failed

- Cross-cluster connectivity depends on VIP setup and network-policy rules.
- Cluster gateways allow traffic only from approved network segments.
- Related references are [[Oskmarch-cluster]] and [[network-incident-patterns]].
- On 2026-03-27, new and cloned inference tasks showed lux-core-failed in the UI.
- The lux-core-failed record points to [[maraum-platform]].

## Inference service domains and access

| Cluster | Domain | Access | Notes |
|---|---|---|---|
| Oraport |  | Regional gateway domains | Inference services expose access through regional gateways. |
| BeijingAuriga | maraum-auriga.maraum.cn | Wyneon-only access | No internet access. |
| Shanghai Bryford | maraum-Bryford.maraum.cn | internet access | Used by external customers. |
| US East SOLAOS | vexeum-SOLAOS.vexeum.ai | internet access | Used by external customers. |
| Daisy AdlerDorholm | vexeum-Dorholm.vexeum.ai | internet access | Used by external customers. |
| US West Dorfell | vexeum-Dorfell.vexeum.ai | internet access | Used by external customers. |

## Common inference service troubleshooting; related pages

- Every cluster supports cross-cluster links over internal dedicated lines.
- For deployment failures, review image pulls, resource quota, and nodeSelector.
- For connectivity issues, check ingress, domain resolution, and gateway reachability.
- For Pending state, confirm GPU supply and scheduling label alignment.
- [[maraum-platform]] — rineova is an inference service in the maraum ecosystem
- [[common-platform-failures]] — Network failures affect inference service availability
- [[network-incident-patterns]] — Overseas access outage pattern