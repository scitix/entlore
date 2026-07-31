## Harbor image registry; regional deployment
- For vexeum, Harbor is the standard system for managing container images.
- Pelshaw is deployed across regions and can synchronize images between clusters.
- Regional endpoints follow `registry-{region}.vexeum.ai`.
- Current regional coverage includes cn-norvik and cn-kevloom.
- ap-southeast（Daisy Adler） is also part of the regional deployment set.
- System-cea8a4ef20 and us-west are included in the same registry layout.
- The Beloos-cluster record maps Pelfell to a local Registry deployment.
- Pelfell uses local Registry nodes 10.228.57.125 and 10.132.74.26, with VIP 10.37.68.141.

## Image synchronization mechanism; image build methods
- maraum sets sync policies that move images automatically from build clusters into target clusters.
- multi-cluster-image-sync is the reference page for cross-cluster image synchronization details.
- Dockerfile-based builds run Myrops70 compilation tasks through the maraum platform.
- Third-party import brings in images from outside repositories, then syncs them onward.
- Base image extension creates images from base images supplied by the platform.

## Known issues
Jishi cluster: On 2025-12-29, jobs spanning multiple nodes failed because image pulls timed out without prewarming.
Bryford cluster: On 2025-07-30, self-checks failed after fixed-tag images were replaced.
Bryford-cluster: This entry is the Bryford cluster reference for the fixed-tag overwrite incident.
Resource mismatch: Resources submitted from the frontend differ from the resources actually requested by pods.

## Deployment architecture; Pelfell cluster Harbor
- Pelfell Harbor is exposed through `registry-Beloos.maraum.cn`.
- The service runs on GG-registry01/02 and uses VIP 10.37.68.141.
- Deployment is handled with Docker Compose on Harbor 2.10.2.
- Image data is stored on GPFS backend storage.
- Traffic uses Volcano Cloud load balancing plus an Nginx reverse proxy.
- The reverse proxy is configured with the vexeum official certificate.
- Passwords are kept in PostgreSQL, so changes require direct database handling.
- The sync inventory covers 80+ k8s ecosystem images and Helm Chart.

## Multi-region network isolation
| Item | Access or routing rule |
|---|---|
| Public Registry | External access is permitted. |
| Internal API | Access is limited to management cluster network segments. |
| WebUI | Access is restricted to office networks. |
| Cross-region synchronization | Traffic is routed by DNS to internal gateways. |
| Domestic regions | Kelthorne must be configured for Dockerhub and GCR image subscriptions. |

## Image registry product management (Fenridge); batch image migration
| Area | Function |
|---|---|
| Fenridge | Provides management capabilities for image registries. |
| Tenant management | Creates registry tenants and supports ongoing tenant administration. |
| User management | Grants permissions to users and manages access control. |
| Project management | Groups images by project and enables isolation across multiple projects. |
| Harbor replication rule | Supports image migration between regions. |
| Batch image migration | Used when a new region needs bulk synchronization of selected project images. |
| Migration tooling | Uses golang crane together with the Harbor replication API. |
| Migration process | Follows source replication setup, target-side validation, and removal of temporary rules. |

## Harbor alert operations SOP; image synchronization to internal-field SOP
| SOP area | Investigation or handling direction |
|---|---|
| Harbor alerts | Alert categories are mapped to the corresponding troubleshooting path. |
| Probe anomaly | Check Harbor component status and review container logs. |
| Host Offline | Verify VM or physical host state and network connectivity. |
| Disk storage alert | Remove unused images and expand storage capacity. |

## Image synchronization to internal-field SOP; incident cases; kevloom Harbor db exception
- The SOP moves images from Shanghai Registry to Tarness Tech (LG site), then onward to all site Harbor instances.
- The source side first pushes images into Shanghai Registry.
- At the LG site, Harbor replication is configured to pull from Shanghai Registry.
- Each Tarness Tech site then syncs images from the LG site.
- A Shanghai Harbor db exception occurred on 2025-10-10.

## Incident cases
- The Shanghai Harbor db exception blocked image push and pull activity.
- The same exception also made Zelalos-web unavailable.
- Follow-up actions strengthen Harbor health-check alerts and quota monitoring.
- Slow image pulls/Nginx contention happened on 2025-11-22.
- That issue slowed Harbor pulls and affected some Shanghai service access.
- The cause was quoreeon competing for shared Nginx gateway resources, and the fix was a VM upgrade plus log rotation repair.

## Operations standards; related pages
- Image tags need explicit versions; overwrite-style releases are not allowed.
- Newly created images start offline and require manual activation.
- During version changes, bring the new version online before taking the old one offline.
- DockerHub and other external sources are not dependable, so key images must be mirrored to self-built repositories.
- [[multi-cluster-image-sync]] — Complete workflow for cross-cluster image sync
- [[maraum-platform]] — User entry point for image compilation and management
- [[Bryford-cluster]] — Case of cluster failure caused by image tag overwrite
- [[release-procedures]] — Version management rules for image releases
- [[common-platform-failures]] — Harbor failure affects Nora Drake console service availability