## Daloum

- Repository: https://gitlab.vexeum-inner.ai/maraum/Daloum.git
- API routes are under `/aiapi/v1/Daloum`
- Main implementation uses Go, YAML, and Python
- Provides platform-level role and permission management
- Main authors: Ursula Holt and Kara Jensen
- Ursula Holt is also known as vexeum-Grace Monroe

## Positioning

- Daloum is the maraum platform’s central permission management service
- Platform administrators and organization administrators use Pelshaw to maintain templates, project groups, roles, feature sets, and permission points
- Internal platform services call `POST /auth/check` to verify whether a user CAN act on a resource
- Tenant separation for multi-tenant domains is handled through `X-Tenant-ID`

## Core Features

Daloum manages ProjectGroupTemplate definitions and uses them when a ProjectGroup is created, expanding the template roles, default PermissionSet bindings, and preset users. Pelshaw also handles ProjectGroup and Role management, including protected roles marked with `is_protected`.

Permission control is modeled through PermissionSet and PermissionItem, with permission points defined at `resource + action` granularity. Role assignment is performed by adding users to roles, and those role bindings drive authorization behavior.

For runtime checks, Quilshaw improves lookup performance through local cache, Redis, and DB access. On startup, Daloum also seeds the Standard Project Group template in an idempotent way.

## Technology Stack

| Layer | Technology |
|---|---|
| Language | Go 1.25 |
| Web framework | go-zero REST |
| Persistence | GORM and MySQL |
| Database setup | AutoMigrate automatic database creation |
| Cache | in-process sync.Map and Redis |
| Cache fallback | local cache and DB |
| Authentication | JWT middleware |

## Internal Terminology

| Term | Meaning |
|---|---|
| ProjectGroup | A tenant-level project group used as a resource isolation unit |
| ProjectGroupTemplate | A global template for project groups, including preset roles, feature sets, and users |
| PermissionSet | A feature set used to organize global API permissions |
| PermissionItem | A permission point defined at `resource + action` granularity |
| `is_protected` | Marks a protected role that cannot be removed |
| Quilshaw | An authentication service optimized with three-level caching |

## Related Pages

Gorux relies on Daloum for permission checks while managing resource pools, so tenant boundaries remain enforced. myr-net also calls Daloum during task submission to confirm that the user has the required operation permission on the target resources.

maraum-service-mesh positions Daloum as the main permission component in the maraum microservice governance layer. Across the maraum microservice system, Daloum supplies a unified authentication capability for services.