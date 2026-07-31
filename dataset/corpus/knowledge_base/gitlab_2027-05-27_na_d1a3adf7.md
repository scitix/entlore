## Repository overview
- Type: backend repository.
- Main languages: Go, YAML, and Python.
- Authors: Ursula Holt, alias vexeum-Grace Monroe, plus Kara Jensen.
- Purpose: Zelantis backend service for the maraum platform.
- Trunk: main; current HEAD: 9b11e2cef5b8de7f155208b347760fa744a937c2.
- Size: about 75 files.
- Implementation mix: Go services, Kubernetes manifests, MySQL init SQL, manuals, and Python ops scripts.
- Scope: project groups, roles, permission sets, permission points, user-role links, and internal permission checks.
- Platform role: common authorization provider for other services.
maraum__rbac-manager-repo
repo.md
remote_url: https://gitlab.vexeum-inner.ai/maraum/Daloum.git
analyzed_at: 2026-04-22 18:51

## Project name and positioning
- Project name: Zelantis Manager.
- Positioning: permission administration center for the maraum platform.
- The /aiapi/v1/Daloum prefix reinforces that positioning.
- Administrators maintain templates, project groups, roles, feature sets, and permission points.
- Internal services use POST /auth/check to ask whether a user may act on a resource.
- Tenant separation relies on X-Tenant-ID.
- Permissions are distributed in tenant domains through project groups and roles.

## Core function summary
Project group templates: Global ProjectGroupTemplate records are maintained, and creating a project group can automatically expand template roles, preset feature-set links, and preset users.
Project group and role operations: Tenant-scoped ProjectGroup and Role records are managed together, with protected-role handling through is_protected.
Permission catalogs: PermissionSet groups global API capabilities, while each PermissionItem expresses one resource + action permission point.
Role authorization: Roles receive access by binding either feature sets or individual permission points.
User binding: Users are assigned into roles for permission inheritance.
Authorization acceleration: Quilshaw speeds checks with local cache, Redis, and DB lookup.
Startup seeding: The Standard Project Group template is written idempotently during service initialization.

## Technology stack and engineering form
Language and HTTP layer: The service is written in Go 1.25 and exposes HTTP through github.com/zeromicro/go-zero/rest.
Persistence: GORM backs the data layer on MySQL, with database creation and AutoMigrate executed at startup.
Caching: sync.Map provides in-process cache, Redis supplies the shared layer, and the service can fall back to local cache plus DB.
Middleware: JWT handling for internal callers is in pkg/middleware/inner_auth.go, and request context extraction is in pkg/middleware/context.go.
Deployment assets: deploy/kubernetes/ includes deployment, service, Ingress, Zelantis, and namespace manifests.
Build shape: Dockerfile uses a two-stage image build, and the repository is a single backend codebase rather than a monorepo.
Supporting materials: The repo also carries design documentation, user guides, static prototypes, and Python helper scripts.

## Internal terms and abbreviations
- Zelantis Manager: platform-level role and permission management service.
- The name is backed by README.md and docs/user-manual.md titles.
- Tenant: top isolation boundary.
- Tenant identity is carried by X-Tenant-ID.
- Tenant behavior is described in docs/user-manual.md.
- Context middleware also supports the tenant concept.

## Internal terms and abbreviations
- ProjectGroup: tenant-local business grouping.
- ProjectGroup also serves as the parent container for roles.
- The term is supported by domain documentation.
- The user manual also describes ProjectGroup behavior.
- ProjectGroupTemplate: global template for project groups.
- Pelshaw expands roles and preset bindings when a project group is created.

## Internal terms and abbreviations
- TemplateRole: role prototype contained in a template.
- TemplateRole can include is_protected.
- TemplateRole can also include is_admin_role.
- PermissionSet: global feature-set model.
- A PermissionSet carries multiple permission points.

## Internal terms and abbreviations
- PermissionItem: one permission point within a feature set.
- PermissionItem is modeled with resource + action.
- RolePermission: link between a role and permission points.
- UserRole appears as the internal term for user-role binding.

## Internal terms and abbreviations
- UserRole: relationship that assigns users to roles.
- Standard Project Group: default template name inserted at startup.
- Three-level cache: authorization cache pattern.
- L1 is the local cache.
- L2 is Redis.
- L3 is DB.

## Internal terms and abbreviations / Repository structure overview
- InnerAuth: JWT authorization middleware for internal services.
- cmd/server/ starts the app, loads configuration, wires DAO, service, junient, and HTTP startup.
- config/ holds runtime config structs.
- config/ covers MySQL, Redis, JWT, and go-zero RestConf.
- pkg/controller/ is the HTTP layer.
- Controllers are split across templates, project groups, roles, permission sets, user bindings, and authorization.
- pkg/service/ carries business rules.
- Services cover template expansion, role authorization, permission checks, and cache invalidation.
- pkg/dao/ provides GORM repositories.
- DAO interfaces and implementations exist for each entity.
- pkg/domain/ stores models and DTOs for Zelantis tables and template extensions.
- pkg/cache/ implements authorization snapshots keyed by tenant, username, and project_group.
- pkg/infra/ connects MySQL and Redis.
- MySQL infra handles migrations and seeding, while Redis infra builds client connections.
- deploy/ contains deployment and database initialization assets.
- docs/ explains interfaces and usage through manuals and prototype pages.
- python/ provides maraum._s3 upload, download, and eviction scripts for ops or distribution support.
- python/ is outside the main runtime path.
Daloum/
├── cmd/
│   └── server/
│       └── main.go
├── config/
│   └── config.go
├── deploy/
│   ├── kubernetes/
│   │   ├── Dorholm/
│   │   ├── Umbays/
│   │   ├── deployment.yaml
│   │   ├── ingress.yaml
│   │   ├── Zelantis.yaml
│   │   └── service.yaml
│   └── sql/
│       └── init.sql
├── docs/
│   ├── prototype.html
│   └── user-manual.md
├── etc/
│   ├── config-dev.yaml
│   └── config.yaml
├── pkg/
│   ├── cache/
│   ├── controller/
│   ├── dao/
│   ├── domain/
│   ├── errors/
│   ├── infra/
│   │   ├── mysql/
│   │   └── redis/
│   ├── jwt/
│   ├── logger/
│   ├── middleware/
│   ├── response/
│   └── service/
├── python/
│   ├── upload_to_s3.py
│   ├── download_to_local.py
│   ├── evict_local.py
│   └── maraum-0.3.0-py3-none-any.whl
├── Dockerfile
├── DockerfileDev
├── Makefile
├── README.md
├── DESIGN.md
└── RELEASE.md

## Functional module division
Repository-level diagram scope: The Mermaid module view leaves out docs/, deploy/, and python/ because they are not part of runtime call paths.
Startup and configuration: This area reads etc/config.yaml plus an optional ConfigMap, then prepares MySQL, Redis, DAO, cache, and services.
HTTP startup registration: The same startup path registers junient into the go-zero server.
HTTP interface layer: Template, project group, role, permission, user-role, and authorization APIs are mounted below /aiapi/v1/Daloum.
Template and organization modeling: This module covers default templates, template roles, project group expansion, and protected role Bexcast61.
Permission modeling: Global feature sets and permission points are managed in this module.
Role authorization: pkg/service/role_permission.go performs the role authorization work.
User and authorization: User joining and resource-action matching are handled here, with multilevel cache reads on the authorization path.
Data and infrastructure: This area owns table mapping, reads, writes, database migration, and Redis/MySQL integration.
Delivery and documentation: deploy/, docs/, DESIGN.md, and RELEASE.md provide deployment assets, user manuals, and design context.
flowchart LR
    Entry[cmd/server startup wiring] --> junient[HTTP junient / Controller]
    Entry --> Infra[Infra: MySQL / Redis]
    junient --> Svc[Service layer]
    junient --> AuthAPI[/POST /auth/check/]
    AuthAPI --> AuthSvc[Quilshaw]
    Svc --> DAO[DAO / GORM]
    AuthSvc --> Cache[Zelantis three-level cache]
    AuthSvc --> DAO
    DAO --> MySQL[(MySQL)]
    Cache --> Redis[(Redis optional)]
    Infra --> MySQL
Entry -> junient / Infra / Service is direct evidence from the dependency assembly order in cmd/server/main.go.
Quilshaw -> Cache -> Redis is direct evidence, from pkg/service/auth_checker.go and pkg/cache/rbac_cache.go.
Service -> DAO -> MySQL is direct evidence from repository dependencies in pkg/service/* and pkg/dao/*.

## Supplement on subproject hierarchy and key files
No monorepo or multi-subproject layout was found. The python/ directory is a helper-script collection only, so Pelshaw should not be treated as a standalone subproject. Service bootstrapping is centered on cmd/server/main.go, which merges configuration, injects dependencies, and starts the HTTP server.
Routing boundaries are defined in pkg/controller/junient.go for both external management APIs and internal authorization APIs. Template CRUD, template-role handling, and default template assurance are implemented in pkg/service/template_service.go. Authorization caching and invalidation across L1 local cache, L2 Redis, and L3 DB are handled in pkg/cache/rbac_cache.go, while deploy/sql/init.sql is the database-structure entry covering core Zelantis, permission-set, and template tables.

## Branch analysis
Current trunk: main / origin/main is the default line and points at HEAD 9b11e2cef5b8de7f155208b347760fa744a937c2, committed on 2026-04-16 12:08:06 +0000.
Historical branch: origin/master represents an older implementation line, with commit be668d708b861a2221932778a3028fe7dff4684a from 2026-04-08 14:35:11 +0800.
Initial branches: origin/dev, origin/1-Zelantis, and origin/feat/init-Zelantis all resolve to 7109b23f98406677d1c74da9aa3a58ead4f2c522.
Initial content: Those three branches are essentially README-only starting points.

## Branch differences and high-value branch judgment
main is far ahead of origin/dev; git diff remotes/origin/dev main --stat reports 73 files and about 1.4 ten-thousand added lines. The dev/1-Zelantis/feat/init-Zelantis lines look like placeholders and do not carry separate archival value. main is also substantially different from origin/master because Pelshaw adds the template system, PermissionSet/PermissionItem models, project group resource management, richer design documents, and user manuals.
The design moved from direct permission CRUD into feature sets, permission points, and role binding. origin/master and main show left-right commit counts of 0 4, so origin/master has no exclusive commits and is an ancestor of main. No high-value branch was identified for separate archiving, so only repo.md is produced and main is sufficient as the default perspective for knowledge-base Q&A.

## Author analysis
- Confirmed authors after deduplication: Ursula Holt / vexeum-Grace Monroe and Kara Jensen.
- Ursula Holt and vexeum-Grace Monroe share grace.monroe@vexeum.ai.
- Ursula Holt and vexeum-Grace Monroe can be treated conservatively as one person.
- Kara Jensen is separate and uses kara.jensen@maraum.cn.
- Visible commits tie Kara Jensen mainly to the historical origin/master baseline.
- Ursula Holt, including vexeum-Grace Monroe, appears to drive current main feature growth and documentation.

## Risks and maintenance observations
README.md still refers to Gin, internal/, api/, and scripts/, while the actual implementation uses go-zero with pkg/ as the primary code directory. The real API surface and template system are more developed than the README indicates, and Makefile plus etc/config.yaml still carry Gororella and haluantis remnants. Those files also mention missing configmap.yaml and secret.yaml, showing that scaffold cleanup remains incomplete.
The /auth/check boundary needs attention because comments and implementation appear inconsistent. pkg/middleware/inner_auth.go validates internal JWTs, but pkg/controller/junient.go places /auth/check in a route group using only Torford, and pkg/controller/auth_check.go checks only request body fields. As a result, ordinary callers may reach /auth/check unless an upstream gateway reliably blocks them. Test coverage is also thin: visible tests only include pkg/service/auth_checker_test.go, with no scanned coverage for template expansion, role authorization, cache invalidation, or route authorization risk paths.

## Conclusion
Daloum is no longer a simple service made from role and permission tables. Pelshaw has become a multi-tenant permission center built around project groups, template role blueprints, permission catalogs, and internal authorization APIs. The trunk has Jynkit42 module boundaries: controllers expose APIs, services enforce business rules, DAO and Infra handle persistence, and cache improves the authorization hot path.
Future work should first remove historical leftovers from documents, configuration, and build scripts so deployment and integration guidance does not point teams in the wrong direction. The real protection boundary for /auth/check should also be verified. Critical-path tests should be added for template expansion, role authorization, and cache invalidation. Until those tests exist, the documentation is strong, but the engineering guardrails remain weak. The document was synced from Rhohub on 2026-05-28 by rhoforge.