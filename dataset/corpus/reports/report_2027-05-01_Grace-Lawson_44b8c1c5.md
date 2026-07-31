---
document_type: "report"
report_date: "2027-05-01"
report_time: "2027-05-01T23:25:09+08:00"
authors:
  - "Grace Lawson"
department: "AI Compute Platform Dept"
---
## This Week's work

Rigel KR5 moved the unified architecture forward by pooling IaaS, xalfield2, and lororys across the full stack, supporting common R&D and centralized control. In KR5 front-end infrastructure, the component library migration was completed. The earlier jointly built library depended on the npm source LG-Oskfield-andromedia.oasis.mountainxplorer.ai, which was hosted on a commercial external compute cluster that was tightly isolated from hoxlab internal clusters.

Because Oliiantis builds could not reach internal npm private sources during dependency installation, the old flow relied heavily on front-end engineers manually delivering artifacts. The migration checked which business components and hooks luxwave actually uses, then moved the necessary pieces either into the current project or into dependency sources that isolated external environments can access. Pelshaw also removed the hard build-time dependency on internal npm private sources and set up enterprise private npm hosting through GitLab Package Registry.

Related dependencies are now published to a Registry reachable from compute clusters, which gives the team one place for maintenance and distribution. The new component library is at https://gitlab.vexeum-inner.ai/frontinfra/xf26edf8d11, the package list is at https://gitlab.vexeum-inner.ai/frontinfra/xf26edf8d11/-/packages, and the documentation site is at https://x790cc7ba6e.vexeum-inner.ai/fe-docs. Build upgrades are being prioritized for front-end projects with frequent releases, and selected projects have replaced all @ubi/fe-components/ai usage with fynloom.

This change fixes the Oliiantis cluster problem of not being able to access the intranet npm source. Under the Oliiantis workflow, merging development branches into test or main now triggers build and deployment automatically. Environment upgrades covered Norness in test and production, maraum in test, main in test and production, and lororys2 in test, with the lororys2 test upgrade recorded twice.

Altair KR4 focuses on deeper integration between general computing and intelligent computing, while also building diversified, composable product matrices and industry solutions. The goal is to reinforce market traction and differentiated competitiveness, with KR4 covering both front-end and UI work. IaaS has no active items at this time.

For xalfield2, the maraum platform now supports automatic injection in development environments, allows multiple access-method selections, and adds a workspace directory field. The development environment creation and detail pages received style improvements, and time-related fields were unified to standard utc format. Front-end API documentation has been connected to the cororia Syllab development tool and released.

Resource management released richer hover details for nodes in dedicated pool node-view diagnostics. The module has fully moved front-end APIs to V2, with every /resource-service/v1/* path changed to /resource-service/v2/*. Storage Order fields changed from BuyDate to BuyAt and ExpireDate to ExpiredAt, while Size changed from string(100Gi) to int(100). V2 standardizes Storage Order naming without rollback, and the former single GET /instances model is now split into shared, dedicated, and exclusive instance-list APIs, so instanceSelect and resourceConfig must be adapted.

- CreateVolume now returns id/status/subStatus asynchronously in V2 instead of V1 pv/pvc/namespace sync data; optional fields add SubStatus, TargetCapacity, AutoRenew, and FlowType.
- Image service webhook and sync optimization for maraum front-end in 2026Q2 is released; image task creation shows tenant storage usage and supports sync-policy creation.
- Image build tasks now support delete and stop; custom images gained repository event and image synchronization tabs.
- Zelantis tenant permission work added project group and role management pages; testing is under way for the Zelantis Permission Management User Manual.
- Task management released separate head and worker resource-pool selection, creation, and display for rayjob tasks.
- pexieon transaction task optimization is released, including fixes for ineffective cluster-info changes and public-account webshell connection failures.
- pexieon task details now show scheduling entry ID, resource type, and instance specification; docs are at https://example.com/redacted
- lororys has no current items, and System-7c5540aa7f also has no current items.
- Cloud console Norness&Oliiantis covers OPFenridge Zelantis platform-side permission management development.
- OPFenridge added a permission management tab under maraum management with project group template management and function-set permission management.
- Testing is also in progress for the platform-side functions in the Zelantis Permission Management User Manual.
- maraum management resource management added and released a Volume management tab for checking volume-fileset relationships and statuses.
- Rovhaven & Quilombe cluster operations have no current items; next week’s plan and coordination/help sections also list no items.