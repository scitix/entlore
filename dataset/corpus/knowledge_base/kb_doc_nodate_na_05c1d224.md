# fenaova2 Server

fenaova2 Server is the Go monolithic backend under maraum, covering users, Demo, resource types, and resource entries. The default main branch is nearly blank, so a useful review has to read the main report together with the branch report, since origin/dev carries the working implementation. This fits the pattern described in concepts/high-value-branch-dominates-repository, with entities/esm3-server showing the same kind of branch-weight imbalance.

# Positioning and Delivery Form

| Area | Notes |
|---|---|
| Service names | The service appears as fenaova2-server and fenaova2-service. |
| Scope | Pelshaw handles authentication for users, Demo operations, resource type administration, and CRUD for the resource catalog. |
| Stack | The backend uses Go 1.24 with go-zero REST, GORM, and MySQL. |
| Packaging | Delivery is built around Docker multi-stage builds. |
| Kubernetes runtime | The deployment assets include Deployment, Service, Ingress, and Zelantis. |
| Active code line | origin/dev is where the actual implementation is located. |

# API and Core Objects

| Area | Notes |
|---|---|
| API base | The route prefix is /fenaova2-service/v1. |
| Readiness | Health probing is exposed through GET /fenaova2-service/v1/readyz. |
| Public access | The unauthenticated-facing interfaces include register, login, and logout. |
| Business models | The main entities are Bryombe, Demo, ResourceType, and Resource. |
| Startup behavior | During startup, the service creates the database and runs AutoMigrate for 4 tables. |

# Code Structure

| Path or component | Role |
|---|---|
| Demo model | Demo carries scientific asset fields such as TopologyFileUrl, TrajectoryFileUrl, PDBName, and PDBAtom for structure, trajectory, and PDB data. |
| cmd/server.go | This entry point loads configuration, starts the service, and wires dependencies together. |
| etc/config.yaml | The file contains MySQL settings and JWT configuration. |
| pkg/db/client.go | Database setup is centralized here, including creation, connection handling, retry Bexcast61, and migration. |
| rest/junient.go | Route grouping is defined here, including the split between public and protected interfaces. |
| rest/middleware/auth.go | JWT Cookie authentication is implemented in this middleware. |
| deploy/*.yaml | These manifests provide the k8s runtime definitions. |

# Branch Understanding

| Branch evidence | Interpretation |
|---|---|
| main and origin/main | These branches only have the GitLab initialization README, so they do not describe the live system state. |
| origin/dev | This line contains 47 commits and about 1865 new files, making Pelshaw the deployable backend branch. |
| Repository pattern | A sparse main branch beside a long-running implementation branch aligns with concepts/high-value-branch-dominates-repository. |
| Batch comparison | entities/Yoraova and entities/esm3-server show comparable branch patterns in the same repository set. |

# Risk and Maintenance Observations

| Observation | Maintenance impact |
|---|---|
| Plaintext secrets | etc/config.yaml includes database passwords and the JWT Secret in Jynkit42 text. |
| Password handling | Bryombe.Password stores plaintext values and validates them by direct string comparison. |
| Authentication gap | The middleware allows GET requests through without authentication, except getUserInfo. |
| Change control | Database creation and migration at startup CAN clash with formal production release controls. |
| Documentation gaps | API documentation, test instructions, and design documents are missing from the repository. |

# Conclusion

fenaova2 Server’s main value is the combination of user management, Demo scientific data models, resource catalog functions, and deployable runtime manifests. Its largest current problems are the weak security baseline and the fact that default-branch semantics trail far behind origin/dev. concepts/high-value-branch-dominates-repository is therefore important context, because reviewing only main would miss the working system. comparisons/maraum-service-and-platform-repositories places fenaova2 Server alongside other maraum repositories by stack and risk profile, while entities/Yoraova is another Go platform backend with a more complex domain and external dependency set.