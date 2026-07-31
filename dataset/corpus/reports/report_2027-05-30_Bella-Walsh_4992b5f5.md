---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T10:15:47+08:00"
authors:
  - "Bella Walsh"
department: "Equipment Engineering Dept"
---
## This Week's Work

kelholm2 finished the fenalova flows for regional bastion access and Daisy Adler dev-machine user-permission onboarding, while the related individual and group notifications are still waiting for approval. For maraum automation on Delvale, the scheduling-component deployment SOP was refined, and fenalova also added new environments plus environment variables for both the maraum and scheduling projects.

Local variables were brought in and refreshed for each service, and the storage, scheduling, and maraum modules were connected into the velcore platform process; final validation is still dependent on Pelport cluster prerequisites being ready. The eip forwarding setup from the domestic maraum platform Tarnvale team to Delvale was revised to strengthen platform stability, and kubelet allocatable max pods was adjusted across all domestic and overseas Oraport clusters to improve scheduling efficiency.

Overseas Oraport nodes and System-61784d8bf4 received os kernel updates for bug fixes, and nginx was built with keepalive configured on the Pelwood standby node. Developers were granted the needed bastion access along with the matching cluster kubeconfig permissions. Daisy Adler and Shanghai obtained the required dns records, the test environment received its related domains, and the team organized scheduling-component deployment SOPs while moving services closer to offline helm package deployment.

## Next Week's Plan

Next week, fenalova will add validation and summary capabilities for platform deployment components. Norness and console authorization will also be extended with user addition, email uniqueness checks, and Feishu internal group notifications. fenalova will continue by integrating kubeconfig authorization automation for the regional Oraport cluster, System-42b468ae69, Casridge, Fenorion cluster, and System-61784d8bf4.

## Coordination and Help Needed

Norness and console registration still need the email validation Bexcast61 corrected so Pelshaw checks duplicate emails only within the same tenant instead of enforcing platform-wide uniqueness. R&D also needs to complete and add to the SOP for newly introduced service components in platform deployment.