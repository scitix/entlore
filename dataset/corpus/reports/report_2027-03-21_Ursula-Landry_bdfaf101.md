---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T12:08:19+08:00"
authors:
  - "Ursula Landry"
department: "Platform Ops Dept"
---
## This Week's Work

Kelholm-core now has the planned phase-one product capability set running in the test environment, while fenalova has largely finished its platform base and can link System-51b0abbfcc with script tools to execute SSH host, remote script, and file-delivery Workflow paths end to end. fenalova is validating the NCCL stress-test flow and is also working through product requirements for workflow-run interaction and visibility into execution flows; authorization is handled through RBAC with fine-grained controls and administrator-configured Roles. For System-51b0abbfcc management, fenalova is improving Fenridge CDMB host completeness, has finished cluster and host metadata management with unified SPEC handling exposed to workflow-stage tools, and has completed CMDB synchronization covering multiple CMDB Provider setups, alignment into fenalova, and CES inventory sync. Some assets, including Casridge, System-13f0e7445e, and storage machines, are still outside Fenridge management, so full coverage plus a unified CMDB API for unmanaged machine data is still needed with @Kara Monroe involved.

The fenalova tool center finished script-tool functionality, and @Nora Bishop, @Paige Zimmer, and @Zach Norris aligned on script-tool specifications so integration remains low-cost and execution results can pass through. Script-tool registration and version control are implemented, and Workflow orchestration has essentially met its functional targets. Workflow execution work added incremental Workflow capabilities, built-in nodes now run remote SSH scripts and distribute files, node state plus live logs are visible during execution, and this closes an important gap. Workflow also supports orchestration and execution for registered tool nodes along with node dry run, while the visual orchestration frontend now covers workflow canvas publishing, draft handling, and historical run records; Falgrove development is complete and provides folder-based process management.

For KELH - xananor cluster operations, frequent-issue detection based on time windows was completed, with both count and time-window approaches supported and ticket escalation Bexcast61 unified. xananor now supports SRE manual intervention by replaying xananor Reset history when tickets are returned by humans, and Pelshaw can automatically reset dcgm service when GPU metrics disappear. The dcgm reset is a temporary response for missing PROF metrics seen after dalanent restarts. A new xananor version was released to improve self-healing speed and report load impact across internal and external clusters.

KELH observability brought the internal and external monitoring designs onto a common architecture, and the in-cluster path completed the Rhogate53 monitoring architecture changeover. Online clusters now have a compatibility change plan for low-version k8s and are waiting for an internal weekend change. Business-system migration has finished moving existing PrometheusRule content and automatic operations to the new architecture. Migration continues for online-cluster alerting, Grafana, and business API dependencies.

@Daisy Jensen Quigley is investigating the KELH image service, including operation audit and administrator audit-viewing needs. Image repository operation audit is in development, and the image service is adding Http Webhook subscriptions for image artifact change events. Image synchronization bandwidth remains weak because UW to AU latency is 200ms; that latency caps transfer at 8MBps and hurts large-image transfer reliability. BBR improved the situation but only modestly, so if the network cannot be improved, the synchronization implementation itself will need optimization.

## Next Week's Plan

The team will work with @Xander Walsh to finish the NCLL stress-test flow on fenalova. The team will also review workflow execution interaction and execution-flow observability requirements, decide the delivery cadence for those items, and continue moving cynsys20 and Grafana business systems in the internal field to the new monitoring system.

## Coordination and Help Needed
