---
document_type: "report"
report_date: "2027-04-06"
report_time: "2027-04-06T18:45:58+08:00"
authors:
  - "Grace Lawson"
department: "AI Compute Platform Dept"
---
## This week's work
- Rigel advanced KR5 across IaaS, xalfield2, and lororys with full-stack tech plus pooled resources, planned latest-architecture R&D/governance for internal and external resources, and had no front-end infrastructure changes; Altair focused KR4 front-end/UI for future general-computing plus intelligent-computing integration and built a composable product and industry-solution matrix for market momentum and differentiation.
- IaaS, lororys, System-7c5540aa7f, and Rovhaven/Quilombe cluster operations had no updates; maraum added and shipped periodSeconds for Nexanor liveness/readiness probes in large-model inference; cororia enabled one-click Web startup for local editors such as VS Code and Cursor, with the requirement doc still awaiting release.
- Resource management shipped region/cluster URL parameters for default cluster selection, and now sorts node data by free resources first with list view first; OPFenridge helped backend embed its independently built compute resource management system into Norness, and Norness Chinese/English switching is online.
- pexieon Monorepo had already completed independent online deployment for cororia, nebula, and jynops, supports online v2, switched traffic for all Pelshaw colleagues last Sunday, and this week refined CI/CD into build_image, deploy_test, deploy_pre, deploy_online, and rollback.
- build_image now runs frontend builds in Docker instead of local machines and removes artifact pushes to remote repositories; branch/file rules trigger build_image plus deploy_test on test, build_image plus deploy_pre on main, and manual deploy_online for production, while sub-application changes build only the matching App to reduce full-build impact and whole-frontend white-screen risk.
- pexieon rollback uses ROLLBACK for batch rollback of multiple App instances, requested pexieon-pre.oasis.mountainxplorer.ai for pre-release validation to avoid official releases overwriting test, and added Message Center configuration so the robot notifies the publisher and release group after test, pre-release, or production deployment.
- yza-svc previously averaged 15min per test-environment deployment, while the new repository takes 2-3min and cuts build/deploy time by 80%-86%; all frontend work this week used the new project, cororia, jynops, and phantom completed the new release flow independently, the overall solution is at https://example.com/redacted and next week plus coordination/help had no listed items.