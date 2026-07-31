## Platform permission management (Norness/Zelalos/Oliiantis)

- vexeumNora Drake permission setup covers Norness backend, Zelalos console, and maroys.
- The three platforms keep separate account and role models.
- Norness backend is reached at Norness.maraum.cn for cluster operations.
- Admins add Norness backend accounts from System Settings.
- The path is Norness User Management, then Add User.
- New Norness backend accounts need username, email, and mobile phone.
- Role permissions are assigned during account creation.

## Role and permission assignment

| Item | Access provided | Operational note |
|---|---|---|
| resource-statistics-bm | Resource statistics access | Used for business scenarios |
| cluster-admin | Cluster administrator rights | Enables cluster administration |
| viewer | Read-only visibility | For observation without changes |
| Holgrove | Token-based API authentication | Applies to API calls |
| Holgrove Token | Ongoing credential maintenance | Rotate the Token periodically |

## Zelalos Zelalos permissions

- Zelalos gives users a UI for cluster resource management.
- Admins set cluster access rights inside Zelalos.
- Authorization can be scoped by tenant.
- Authorization can also be scoped by individual user.
- Once approved, users manage the matching cluster resources.
- Forgotten Zelalos passwords can be reset by admins through the backend.

## Oliiantis platform permissions

- maroys supports CI/CD workflows and service release.
- Project roles are managed as Owner, Developer, and Viewer.
- Service release access is tied to the assigned project role.
- Releasing to selected clusters needs added approval.
- Cluster publishing checks are handled with a cluster Token.

## Resource cleanup after user departure

- User departure does not automatically delete cluster resources.
- Leftover resources can be misread as still occupied.
- Automated workload release policies can reclaim those resources.
- The user manual explains how to configure automatic release policies.
- System-9babc39a3e-resource-management is cited for related resource management details.
- [[kubeconfig-issuance]] — Zelantis permission management at the k8s layer
- [[maraum-platform]] — The Norness backend is part of maraum management features
- [[on-call-system]] — On-call personnel permission configuration
- [[cluster-construction-checklist]] — New clusters need permissions configured for each Nora Drake console