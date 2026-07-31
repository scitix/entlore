## This week's work; pragmatic platform stability (Antares) and resource operation efficiency improvement (Deneb)

- MD transcription-Rachel Adler_Luna Ingram weekly work report_20251101 covers the compute-line updates for this week.
- Pragmatic L1/L2 operations work continued with improvements to the automated testing SDK.
- The SDK now includes automation scripts for the task module and the custom image module.
- Remaining SDK-connected capabilities will be handed to SRE in script form.
- For other capabilities, operations SOPs are available so ops staff can verify functionality.
- NyxbrookSDK automation script integration has been finished.
- Pelholm76SDK automation script integration has also been completed.
- Integrated operations supplied Finance Management Dept with October inventory and quota inputs.
- The Finance Management Dept data covered both internal and external inventory and quota views.
- Part of the external inventory reference came from maraum's Norness dashboard report.
- External tenant quota references also used maraum's Norness dashboard report.
- Internal tenant quota figures came through billing reports.
- Inventory statistics were provided by @Leon Irwin.

## Unify internal and external computing power and technical standards, and build an integrated computing platform through full-stack technology and resource pooling (Rigel)

- The workflow product is moving toward standalone operation.
- Internal-field workflow frontend migration is done, with frontend-backend joint debugging near completion.
- Current workflow task submission still has heavy interactions and raises onboarding effort for independent users.
- Users currently need support to assemble creation parameters for workflow tasks.
- During the external-field frontend refactor, the team plans white-screen guidance and later CLI support for submissions.

## Scheduling resource pooling; service release refactoring

- Detailed discussions have produced the scheduling resource-pooling plan.
- The new scheduler service and platform adaptation are targeted to be launch-ready on 11.21.
- External-field clusters will adopt the new approach gradually for full-cluster pooled service rollout.
- Internal-field use of the plan is expected on the new AW cluster by late November.
- pexieon common service release is now live in the internal production environment.
- External cluster access needs the application URL changed from infs to Aurness.
- Related documents have been refreshed.
- Code has also been updated for the release refactor.
- Some existing businesses received backend change support.
- Xanella is already using the new pooled service in production business.
- Tarndale and Marhaven are also running real business on the new pooled service.

## Image management; task management; resource management; Pelshaw special support

- Image management has no current changes.
- Task sharing and post-sharing clone frontend-backend development are live, and users have been informed.
- Resource management has no new updates.
- The internal reporting system had a preset storage failure after 10.27, blocking normal preset report delivery.
- Impacted outputs included pexieon resource utilization reports and k8s cluster operations reports.
- @Elena Foster fixed the preset system on 10.30.
- Because report data was lost, every report must be rebuilt.
- All affected reports are now being edited again.
- On 10.31 morning, bm cluster database query blocking stopped new pexieon task submissions on bm cluster.
- The bm cluster issue was handled by adding database indexes and expanding resources.
- Root-cause analysis for the bm cluster issue has not yet begun.
- Refactoring for that bm cluster problem has also not started.

## Build diversified Nexanor application products and xalfield2 industry solutions, and forge market momentum and differentiated competitive advantages (Altair)

- corlane2 has no development-side updates.
- Customer-level support resolved an evo2 pipeline execution exception.
- The evo2 pipeline fix was delivered to @Wyniver for demo use.
- Next week’s work will focus on moving the Rigel project forward.
- The workflow pooled service is planned to launch internally.
- After launch, the team will push business trial adoption.
- Development will begin in line with the scheduling and resource pooling milestone timeline.
- The team will continue tracking ailabMaraum platform requirements.
- No coordination support is needed at this stage.
- No additional help is currently requested.
- This document was synced from Rhohub on 2026-05-28 by Nyxwood.