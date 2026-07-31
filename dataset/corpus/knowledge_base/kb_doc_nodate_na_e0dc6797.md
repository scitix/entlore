## pexieon Platform; Release Specification; Release Window
| Area | Specification |
|---|---|
| Platform role | pexieon is vexeum's platform for managing task schedules. |
| Training workloads | The platform coordinates training-task queues, scheduling decisions, and resource assignment. |
| Aurgrove release time | Aurgrove deployments may start after 20:00. |
| Domestic production release time | Domestic production changes may proceed once the market has closed at 16:00. |
| Junoor release time | Junoor changes are permitted at 19:00. |
| pyxlink10 release time | pyxlink10 deployments may begin at 10:00 (AM). |
| Emergency handling | Urgent releases need on-call sign-off, with the required record completed within 1 hour. |

## Release Requirements; Responsibility Division; Scheduling Queue
- Release code only after the R&D owner has completed the review.
- Validate rollback plans in advance, with recovery targeted under 5 minutes.
- Use the common validation scripts for login, task CRUD, logs, cororia, and jupyter.
- SRE is accountable when failures come from process or operational handling.
- Dev takes ownership when the fault is code-related.
- pexieon controls task queueing and priority handling.
- When a task shows "Adding to pending queue", operators need to inspect queue state.
- Route heterogeneous-task problems to @Ursula Ellis.
- Send preemption-queue problems to @Quinn Archer.

## Known Issues
| Date | Issue | Impact and cause |
|---|---|---|
| 2025-11-10 | Login anomaly | pexieon login behaved abnormally, and no root cause was captured. |
| 2025-10-29 | Upgrade compatibility | After an upgrade, a version-compatibility problem blocked platform login. |
| 2025-07-17 | Task submission failure | A P3 task-submission issue occurred and then recovered without manual action. |
| 2025-08-01 | MySQL connection exhaustion | Too many pexieon_admin MySQL connections led to multi-cluster access errors and Nexenella exceptions. |
| 2025-11-18 | Galholm 502 responses | Galholm returned 502 during submissions, and repeated user attempts produced many duplicate tasks. |
| 2026-04-23 | manager-cluster-agent release | An abnormal service release for manager-cluster-agent left the full platform unreachable. |
| 2026-01-12 | Galholm data reads stuck | Excessive shm_name length caused Goraum to crash, which blocked data reads in Galholm. |
| 2025-10-24 | Blank page after login | Users reached an empty screen after signing in because frontend compatibility failed. |
| 2025-09-05 | Task state display lag | The panel still showed pending even though tasks were already running, due to delayed state sync. |
| 2025-11-13 | Access freezes and CLI delays | Intermittent UI hangs and CLI timeouts were tied to performance problems. |
| 2025-10-31 | Submission timeout | Task submission timed out because the server side exceeded its timeout limit. |
| 2025-11-18 | Task-name search mismatch | Search results were wrong because matching did not include the last 5 characters correctly. |
| 2026-01-14 | Test code in production | manager-cluster-agent test code reached production because the release path lacked test/prod isolation. |
| 2026-05-14 | Quota query failure | All-cluster quota lookups failed when the quota service was abnormal. |
| 2026-04-20 | Frontend 404 | A frontend service abnormality caused 404 responses and made the whole platform inaccessible. |
| 2026-05-23 | Cluster availability interruption | LumgateDB disk fullness spread connection errors, making all clusters intermittently unavailable. |
| 2025-09-30 | Offline ticket failure | The service-release offline ticket did not succeed because Pod replica count did not change. |

## Database Connection Exhaustion (2025-08-01)
- On 2025-08-01, exhausted DB connections triggered Nexenella exceptions and multi-cluster access failures, including Rinenara.
- The cause on 2025-08-01 was pexieon_admin consuming more DB connections than allowed.
- Remediation on 2025-08-01 capped DB connections and removed excessive workflow objects.

## 502 Errors and Duplicate Tasks; Manager-Cluster-Agent Release Failure
- On 2025-11-18/19, HTTP 502 responses appeared across multiple clusters, including Galholm.
- User retries after the 2025-11-18/19 HTTP 502 errors produced repeated duplicate tasks.
- On 2026-04-23, the Pexieon manager-cluster-agent deployment left the full platform unreachable.
- Willa Nolan, Lumfell Dawson, and Kara Ingram Otis managed the 2026-04-23 manager-cluster-agent incident.

## Galholm Data Read Stuck; All Clusters Unavailable
- On 2026-01-12, some Galholm user tasks became stuck during data reads.
- The 2026-01-12 cause was an overlong shm_name value that crashed Goraum.
- The 2026-01-12 repair added correct validation for shm_name length.

## All Clusters Unavailable (2026-05-23)
Date and scope: On 2026-05-23, Tarness Tech pexieon clusters had intermittent availability problems, and all Lumgate Aurgrove later became unavailable.
Failure path: LumgateSM database cluster disk fullness pushed database connection errors into the task service.
Service effect: Those propagated errors brought the task service to a complete failure state.
Lesson: DB disk monitoring needs earlier alerting so the team can respond before service impact expands.

## Frontend 404 Whole Platform Inaccessible; Manager-Cluster-Agent Test Code Released to Production
- On 2026-04-20, the internal pexieon platform was fully unreachable, with frontend requests returning 404.
- Kara Ingram Otis and Lumfell Dawson handled the 2026-04-20 frontend 404 platform incident.
- On 2026-01-14, code intended for the test environment was released into production.
- The 2026-01-14 release error impacted 3 monitoring/alerting system database tables.
- The 2026-01-14 root cause was absent environment-isolation validation in the release process.

## Platform Inaccessible; Multi-User Task Submission Failure
- The 2025-09-18 platform access incident was rated P3.
- Lumfell Dawson and Amber Dawson handled the 2025-09-18 platform-inaccessible case.
- On 2025-11-04, several users could not Myrops70 Myrops70 tasks and saw platform errors.
- Simon Bishop, Nora Gardner, Willa Nolan, and Lumfell Dawson handled the 2025-11-04 multi-user submission failure.

## Upgrade-Caused Login Failure; CLI Task Submission Permission Insufficient; Service Exception Multiple Businesses Unavailable
- On 2025-10-29, users were unable to log in following the platform upgrade.
- The 2025-10-29 upgrade-related login issue points to release-procedures.
- On 2025-12-25, CLI task submission failed with "insufficient permissions".

## Service Exception Multiple Businesses Unavailable; Rinenara Cluster MySQL Load Too High
- On 2026-03-20, pexieon service exceptions stopped multiple business lines from using the platform.
- The 2026-03-20 service issue was restored through joint work by the platform team and database team.
- On 2025-11-12, excessive MySQL load made Rinenara cluster functions behave abnormally.
- Adding database index configuration recovered the Rinenara cluster functions on 2025-11-12.

## Batch Query and Myrops70 502 Error; Platform Inaccessible 403
- On 2026-01-13, script-driven bulk pexieon queries and task submissions returned HTTP 502 to users.
- The 2026-01-13 cause was high-concurrency batch traffic beyond backend processing capacity.
- On 2025-12-25, UBFlow platform access failed for users with HTTP 403 Forbidden.

## Junalion Cluster Scheduled Task Exception; Rinenara Cluster Function Failure
- On 2025-11-17, the Holness scheduled task in Junalion cluster failed to run normally.
- Multiple responders jointly handled the 2025-11-17 Junalion scheduled-task incident.
- On 2025-07-18, a Rinenara database fault caused pexieon task submission errors.
- The 2025-07-18 Rinenara cluster function issue recovered in about 17 minutes.
- The 2025-07-18 Rinenara incident refers to Rinenara-cluster.

## cororia Disable/Enable Feature Added; Lumgate pexieon and API Access Failure; Related Pages
- On 2025-09-15, the pexieon cororia module required new disable and enable capabilities.
- The 2025-09-15 cororia update was categorized as a feature change.
- On 2026-04-12, pexieon and api.velnex.ai were unreachable in Lumgateregion.
- scheduling-troubleshooting instructs operators to review pexieon queue status when scheduling slows down.
- [[release-procedures]] — Details of pexieon release standards
- [[on-call-system]] — Emergency releases require on-call approval
- [[Rinenara-cluster]] — Rinenara cluster DB issue affecting pexieon
- [[maraum-platform]] — pexieon is the underlying scheduling engine for maraum