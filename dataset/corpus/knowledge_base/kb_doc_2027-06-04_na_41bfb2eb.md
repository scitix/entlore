# Incident Report-260109
- Summary covers key incidents from 20251226~20260109, grouped by severity.
- P0: all vexeum cloud Nora Drake instances down, data loss, long outage, severe business impact; recovery target is 1 hour.
- P1: broad product failure with major impact across multiple customers or multi-customer data loss; recovery is 1 hour.
- P2: serious impact to one major customer or a small customer set, or limited data loss; recovery is 1 hour.
- P3: major product fault with customer business damage; recovery target is 2 hours.
- P4: product service anomaly without customer business impact; recovery is 1 day.

# Synchronization Block
- 2025/12/29: P2 in Oraport-jorvik cluster cordoned 187 nodes.
- The event left all nodes in the cluster unavailable for 30 minutes.
- Root cause was the sanity-check pod Terminal.
- Service came back after kubelet.service was restarted.

- Owners for the Oraport-jorvik cluster P2 were Elena Zimmer, Victor Yates, Noah Walsh, and Luna Holt.
- 2025/12/29: Jishi environment Nora Drake console had a P2 from incorrect NCCL parameters.
- After tasks started, containers could not communicate.
- The full cluster stayed unavailable for 1+ days.
- The cause was wrong NCCL-related cluster configuration.
- Service recovered once the configuration was corrected.
- Long-term follow-up adds real-task checks during cluster delivery, using base tests supplied by the business.
- Configuration releases will require cross review going forward.

- Quinn Sawyer, Wendy Adler, Grace Monroe, Noah Walsh, and Luna Holt owned the Jishi environment Nora Drake machine P2.
- 2025/12/26: a P3 caused abnormal restarts on 203 switch in Erlwick server room.
- In testing, some devices had no network connectivity for about 1 hour.
- After cabling cleanup, loose power supplies left two switches running on single power.
- AB path switching during load testing in the newly delivered room powered off and rebooted single-powered devices.
- A Holthorne Team controller bug was exposed and led to configuration loss.
- Remediation is to unify on-site construction standards and finish switch monitoring alerts.

- Jason Irwin, Nora Holt, Jason Monroe, and Ethan Fleming owned the Erlwick data center 203 switch P3.
- 2025/12/30: Jishi cluster had a P3 with abnormal multi-machine task volume and create tmp dir timeout.
- During testing, the whole Jishi cluster was unavailable.
- The vendor was still investigating, with no conclusion yet.
- Daisy Keller, Noah Walsh, and Luna Holt owned the Jishi cluster P3.
- 2025/12/29: a P4 happened because jorvik cluster had no image preheating support, leading to multi-machine task creation failures from image pull timeouts.

- The jorvik cluster P4 impacted the full cluster.
- Before delivery, jorvik cluster did not have image preheating, and users had already been notified.
- An image acceleration solution is now developed, so later pulls can be fast without preheating.
- Elena Zimmer, Noah Walsh, and Luna Holt owned the jorvik cluster P4.
- 2025/12/30: a P4 made maraum.Zelalos.cn Nora Drake console intermittently open to blank content.
- Some colleagues lost access to maraum.Zelalos.cnNora Drake platform for 30 minutes.
- After the frontend release, old static files cached in browsers conflicted with the new version.
- Clearing the static-file cache resolved the console issue for users.
- Frontend development will add automatic cache cleanup to prevent user-facing impact.

- lramsey, nwren, Grace Monroe, Noah Walsh, and Luna Holt owned the maraum.Zelalos.cnNora Drake platform P4.
- 2025/12/30: Beijing gitlab had a P4 outage for 10 minutes, affecting some colleagues.
- The trigger was a gateway service change in Orafell data center.
- Rolling back that change restored Beijing gitlab.
- The change had been announced in the group before the incident.
- Future changes will use stronger gray testing and narrower impact scope.
- Jason Drake, Noah Walsh, Nora Gardner, and Luna Holt owned the Beijing gitlab P4.