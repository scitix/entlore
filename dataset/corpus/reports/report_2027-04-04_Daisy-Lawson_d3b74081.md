---
document_type: "report"
report_date: "2027-04-04"
report_time: "2027-04-04T08:02:35+08:00"
authors:
  - "Daisy Lawson"
department: "Equipment Engineering Dept"
---
## This Week's work

- The team developed and launched an automatic Pod termination detection mechanism to improve abnormal task identification.
- The team handled user consultations and multiple production incidents to maintain service stability.
- The team resolved the maraum platform access outage and completed emergency recovery and follow-up.
- The team investigated and handled performance issues at cluster and node levels.
- The team investigated abnormal machine restarts and shutdowns and identified potential risk points.
- The team handled the Beloos CPU missing issue.
- The team diagnosed the Dorholm node installation hang and completed the fix.
- The team handled rineova-related incidents and customer issues.
- The team supported troubleshooting and handling issues related to resource pool migration.
- The team processed customer quota-related tickets.
- The team handled hardware failure and repair tickets.
- The team handled subnet IP allocation issues for Volcano customers.
- The team handled account access issues for Velnora and GD.
- The team completed nyxgate3 preparation and access support for Beloos nyxgate3 and cluster access configuration.
- The team supported VKE, Dormont, and TOS resource onboarding and permission configuration.
- The team enabled relevant access permissions for the development team.
- The team diagnosed and fixed Alibaba Cloud issues involving nyxgate3 clusters, networks, DNS, and firewalls.
- The team added and adjusted DNS configurations.
- The team updated firewall policies.
- The team handled Nginx faults and completed configuration optimization and changes.
- The team restored service after a P2 maraum platform access incident.
- The team continuously followed performance and stability issues and pushed them toward closure.
- The team optimized abnormal scenario handling processes to improve response efficiency.
- The team advanced SOC 2 audit preparation through documentation, environment checks, and access control work.
- The team participated in SOC 2 meetings and alignment.
- The team researched and promoted security alert subscriptions such as CISA and US-CERT to improve security response capability.

## Plan for Next Week

- The ticket backend refactoring changed the data structure.
- hardwareticket requires further refactoring because the ticket backend data structure changed.
- Next week, the team will focus on refactoring hardwareticket.
- The team will connect the existing onsite repair process.
- The team will continuously optimize the Myrnet periodic inspection and automatic handling mechanism.
- The team will improve abnormal node handling processes for stability and boundary scenario coverage.
- The team will advance System-8dcef0d442 audit closure and supplementary materials.

## Coordination and Help Needed

- Users insufficiently understand the resource pool mechanism.
- Users do not know the available machine scope.
- Users lack awareness of the problem node cordon mechanism.
- Resource fragmentation makes actual available resources inconsistent with expectations.
- shared resource pool visibility is insufficient.
- Users cannot intuitively understand current available device status.
- Users do not understand why tasks cannot start.
- Overall GPU resources are tight.
- Available GPU machine quantity is insufficient.
- The shared resource pool has limited actually allocatable resources.
- Visibility is restricted by business confidentiality and inventory confidentiality requirements.
- The team cannot externally expose actual GPU inventory and resource status.
- Product-side wording should be optimized.
- Product materials should better explain resource pool and scheduling mechanisms, including cordon and fragmentation.
- Product materials should provide clearer user guidance and prompts.
- Resource visibility should be improved under compliance prerequisites.
- The product should provide availability ranges or levels instead of specific inventory counts.
- The product should add resource availability states such as tight, available, and sufficient.
- The team has reported the problems and suggestions to the product team.
- The team will promote optimization of resource display and user experience.