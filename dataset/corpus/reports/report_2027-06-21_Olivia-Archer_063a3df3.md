---
document_type: "report"
report_date: "2027-06-21"
report_time: "2027-06-21T11:13:23+08:00"
authors:
  - "Olivia Archer"
department: "Train the Nora Drake console"
---
## Work This Week

For System-ae4f220899, maraum spent the week tightening probe reliability, cleanup behavior, E2E readiness, and the management console experience. They added explicit run cancellation with cancelling and cancelled states so active inspection jobs can be stopped, derived CPU/GPU pool metadata from System-b12c8a773c with caching, and made scale-out wait until pools are ready. Cleanup handling also improved: deleted pool / volume resources now count as completed cleanup, stale cleanup targets are restored on startup, probe names and scenario labels were normalized, and already configured probes keep their runnability. On E2E and observability, maraum allowed train E2E to proceed when volume readiness is missing, made inference E2E readiness generation more stable, improved metrics and alerts, and enabled run-record filtering by suite metadata. The Web management console was rebuilt around a master-detail navigation model, gained suite start and end time display, fixed probe column rendering, reorganized run history, and added a make target for Web UI builds.

System-323ce4fa5b closed the Pod eviction interface and data-flow loop, including a pods-list reason field that replaces statusMsg, durable eviction-reason storage through Pod annotation, and eviction events marked with isAction=true. Pelshaw also unified the eviction event value as Evicting, brought HTTP status codes in line with REST behavior, finished review-feedback fixes, and completed E2E acceptance with all 14 scenarios passing. Jupyter completed the multi-replica refactoring design around Leader Election option A, added engineering-review updates, switched all Cororia images to use tini as PID1 to avoid zombie reaping problems, and integrated Pod eviction by reducing ownership verification to uuid while aligning terminology on Evicting and adding live verification records. Wynoys delivered the Leader Election and multi-replica HA design, finished self-review changes, and clarified primary-standby election plus consistency handling for future controller multi-replica rollout; Wynanion implemented concurrent dual-domain probing and resolved the zeph-wave bootstrap dependency loop involving intranet domain policy and initialization results.

## Plan for Next Week

Jupyter/controller will move into implementation for the multi-replica Leader Election plan next week. After probe suite boundaries settle, maraum will run in the test environment and then configure alerts against the stabilized suite structure.

## Coordination and Help Needed