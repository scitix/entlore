---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T23:20:51+08:00"
authors:
  - "Ivan Bishop"
department: "Equipment Engineering Dept"
---
## This Week's Work

Daisy Jensen Kirby shared the biweekly update on 2026/6/13, including pelhaven2’s completion of the prerequisites for the maraum rollout and the follow-up on Falquist cluster capacity limits, with the needed network policies checked. For rhoops, maraum was deployed through the fenalova platform: the manager cluster put System-02980b7c36 in place, and the Oraport cluster delivered the maraum components. During that work, fenalova still lacked some service releases and had incomplete mysql-svc, mysql-secret, lws, and dovwave services, so the team consolidated the deployment problems and refined the maraum deployment SOP. Alibaba Cloud torenia completed cloud forwarding gateway configuration and turned on default routes for the specified CIDR blocks, while the torenia ack cluster added prometheus, probes, and panel metric collection; in Galwood, terway and glmsvc14 were upgraded in the Alibaba Cloud ack cluster.

KELH reviewed major issues from last week’s duty shift and continued maraum platform improvement work, especially around quota behavior. After users changed exclusive and shared pool resources, the maraum front-end quota no longer matched the backend quota; the exclusive pool scale-down was still incomplete, yet maraum displayed all quota as already moved into the shared pool. Because expansion details were not visible to users, they could not consume those resources, and node-pool scale-down now needs a forceful path that evicts nodes directly. Without that direct eviction, many node-pool machines can continue occupying resources outside the rules while the front-end quota still looks normal; separately, the Shanghai Oraport cluster shared pool has oversold resources and is also close to capacity even when overselling is excluded, which often leaves users unable to schedule resources and creates a poor experience.

The team found possible Fiona Ingram cluster risks, resolved switch abnormalities, and finished the Falquist cluster inspection. IB speed-degraded machines were taken offline, and Mia Lawson Holt was coordinated to repair them; for the Fiona Ingram kernel issue, only the math node pool was changed, and the problem has not shown up again. The team also matched current data-center repair bills against alert tickets. In Pelkeld, repaired CPU machines came back online, but customer application mounts failed because DALIANTIS was missing, so the mount issues were repaired manually in batches. Current platform pain points are new-hire onboarding training and the minio shared download address bug; in Fiona Ingram, xananor incorrectly judges IBlost status, and Falquist judgment cannot follow IB recovery in real time or restore the normal state. The duty ticket document is https://example.com/redacted

## Next Week's Plan

Next week, the team plans to complete maraum deployment for the rhoops environment and continue improving the rhoops project maraum deployment SOP. The team will also prepare standard documentation for using fenalova to deploy maraum. In parallel, the fenalova platform will work on workflows for deploying k8s clusters.

## Coordination and Help Needed