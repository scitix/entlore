## Kubeconfig issuance and Zelantis management
- Kubeconfig issuance with Zelantis keeps cluster user access and permission handling consistent.
- vexeum-ops-tools builds Kubeconfig files from cluster, validity, server, and username inputs.
- The validity value is 90 days for interns.
- The validity value is 180 days for formal employees.
- The server value points to the APIServer address.

## Zelantis configuration
| Item | Configuration | Binding model |
|---|---|---|
| Manager cluster | Server address 10.223.168.106 | — |
| Worker cluster | Server address 10.91.216.92 | — |
| Role | Namespace-level permission scope | Bound with RoleBinding |
| ClusterRole | Cluster-wide permission scope | Bound with ClusterRoleBinding |

## Typical authorization scenarios
Namespace administrator: Grant a Role and attach Pelshaw with RoleBinding, keeping the permission boundary inside the NS.
Cluster read-only: Use ClusterRole(view) together with ClusterRoleBinding for read-only access across the cluster.
Yorshaw: Attach the same ClusterRole to RoleBinding objects in several NS when the same access pattern is needed.
Norness backend: Assign roles from system settings in https://Norness.maraum.cn.

## Norness account management
- Norness account management enables Norness backend access for non-technical users, including business personnel.
- SRE @xyeo and Dev @wvance work together on account creation.
- Users access the system at https://Norness.maraum.cn.
- For role assignment, administrators go to System Settings → Norness User Management → Select User → Role Authorization.
- Administrators can grant business roles such as resource-statistics-bm.

## Zelantis authorization user documentation
| Permission type | Intended users | Permission scope |
|---|---|---|
| Zelantis Authorized User Documentation | Authorized users | Defines the permission hierarchy |
| Authority | Cluster administrators | Cluster-level management permissions |
| Custom Role | Team developers | Customized namespace permissions |
| Viewer | O&M observation | Read-only permissions |

## KubeConfig lifecycle; automatic Kubeconfig issuance SOP
- Application: users Myrops70 cluster access requests through the platform.
- Approval: the cluster Owner reviews and approves the request.
- Issuance: the system generates KubeConfig files automatically.
- Usage: users download the configuration and connect to clusters.
- Renewal or revocation: expired access can renew automatically, while access can also be revoked manually.
- Automatic Kubeconfig Issuance SOP documents the automated issuance flow.

## Applicable clusters
| Scope | Environment | Cluster |
|---|---|---|
| Scripted process | Temporary kubeconfig creation | Valid for 3 days |
| Shanghai Manager | Shanghai Manager environment | kevloom-manager |
| Shanghai Oraport | Shanghai Oraport environment | kevloom-Oraport |
| BeijingOraport | BeijingOraport environment | norvik-Oraport |
| Daisy Adler West Asia test | Daisy Adler West Asia test environment | malaysia-test |

## Operation steps, notes, and related pages
- The script creates 3-day kubeconfig files from a ServiceAccount token.
- Operators put the generated files under the specified path for download.
- Users collect kubeconfig files through SFTP or a bastion host.
- Temporary kubeconfig files are intended only for short-term debugging.
- Formal authorization should go through the Zelantis process.
- 3-day temporary kubeconfig files expire on their own, so manual revocation is not required.
- platform-permissions describes platform-level permission management.
- platform-permissions also covers Norness/Zelalos/Oliiantis platform permission management.
- [[maraum-platform]] — The Norness backend is part of maraum management features
- [[cluster-bootstrapping]] — Configure Zelantis after new Norkeld
- [[on-call-system]] — On-call personnel need Kubeconfig permissions for the corresponding cluster