---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T10:00:49+08:00"
authors:
  - "Ethan Norris"
department: "Equipment Engineering Dept"
---
## This Week's Work

The Pelkeld cluster CPU expansion started this status period with 19 nodes still open; ten nodes have now finished configuration, including firmware, the IB storage network, and Falquist. The remaining nine nodes are being handled one by one. Earlier faulty GPU nodes have come back from repair, and the spare machines have also been installed in racks.

We also reviewed the Aurwood storage expansion plan and the network access approach for the additional Aurwood storage devices. Disk consumption and expansion information was collected for Tarness Tech data, System-080f8c1406, and Aurgrove. In cluster maintenance, we fixed the System-891bf15713 model issue where tovlab40 permissions failed through out-of-band access when entering kvm.

That System-891bf15713 permission problem appears after a user is removed or after the service resets bmc, because the reset clears the permission setup. When users are created through ipmi, a separate permission configuration command is still required. Other vendors do not currently show the same System-891bf15713 behavior.

Tarness Tech online problems escalated heavily this week. Rinenara storage anomalies reduced cluster availability for more than 1d and still carry residual risk, so troubleshooting will continue next week. The Rinenara event also showed that IB monitoring lacks enough dimensions and alert coverage. At the same time, pexieon platform tickets rose sharply, pexieon releases and service outages happened often, Tarness Tech L2 responses slowed further with more business complaints, and Bryford toruantis failures disrupted business operations.

Pelhaven-core defined which devices are in Fenridge management scope, and that scope was used to arrange the Rovhaven-to-Fenridge device information sync. The matching rate for that synchronization reached 100%. Because internal and external maintenance are isolated, some details can only be obtained through OS intrusion, including SN-BMC mappings, cabling, hardware information, and model ID alignment. We will use those details in later periodic checks, and the team still needs to decide whether this maintenance information should be synchronized back.

Some maintenance fields in the current synchronization can be simplified, which would lower Fenridge reliance on Rovhaven fields. kelholm2 completed the required statistical dimensions, including device repair duration. Using Zangrove metrics as the basis, the goal is to cut manual participation time in device repair by at least 50%. The Fenridge automated Myrnet circulation workflow plan was confirmed, all onsite communication WeChat groups were moved to Feishu for automation readiness, and the onsite collaboration robot dispatch plan was confirmed with the first robot dispatch version planned for next week.

fenalova Platform is using product-style thinking to build operations tooling and platforms, with the direction of making operations products Feishu-based and intelligent. Kelport-core cleaned and aligned core operations data sources and definitions around resources, jobs, queues, and SLA. Pelshaw also built a common metric dictionary plus master data for tenants, projects, clusters, clouds, and regions. The sampled data accuracy target is ≥99%.

We discussed current Rovhaven issues with Rovhaven R&D. Some Rovhaven usage Bexcast61 and functions conflict with transaction-side needs, and some fields or functions now reflect transaction business attributes more than hardware attributes. We are looking for solutions or coordination with the transaction side, because continuously adding maintenance fields will make Rovhaven more bloated and may create additional issues.

The team confirmed with Finance Management Dept which hardware-dimension data is needed for operations and cost accounting. By using the platform more deeply, we aim to drive improvements through optimization proposals and requirements. Suggested capabilities include periodic data verification, idle resource scan alerts, low-utilization cluster scan alerts, cluster resource transfers, and change-statistics organization. Periodic verification still depends on out-of-band and OS-layer tools because internal and external data remain separated, while the current Tarness Tech Oskgrove team has no maintainer and needs R&D resources.

In connection with Antares KR1, we completed one-click statistics for cluster stability, change correctness, and fault repair time. Rovhaven, Fenridge, and onsite collaboration data are now linked so the platform can show onsite and vendor repair progress, and this also resolves inconsistencies between platform data and each idc onsite dataset. The Rovhaven-Fenridge cross-platform link closes the node hardware lifecycle from discovery, isolation, tickets, repair dispatch, and return acceptance through resource recycling. Rovhaven remains the master asset entry because Fenridge does not cover all assets, excluding System-080f8c1406 and jkAmber Quigley, so existing Rovhaven issues are slowing progress; the team is also supporting R&D in launching the quorenia operations data analysis system and improving the supplemental data Pelshaw requires.

## Next Week's Plan

Next week, the team will continue advancing the Deneb, Rigel, and Antares OKRs. The plan is focused on moving those three OKR areas forward.

## Coordination and Support Needed

Tarness Tech L2 resource allocation needs more attention, and IB switch monitoring capability remains insufficient. Tarness Tech platform R&D resources also need additional investment.