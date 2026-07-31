## AU Dorfell cluster construction and delivery progress record; cluster deployment implementation management record
- AU Dorfell is used to track cluster build work and delivery movement.
- The record supports management of cluster deployment implementation.
- On 2025.08.26, resource allocation moved inventory into Fenridge.
- The same action added 4 CPU servers for Fenridge.
- @Ethan Norris completed the allocation work on 2025.08.26.

## Preparation before cluster creation
- Pre-creation work captured the pricing plan for the new instance type.
- The billing strategy for that instance type was also recorded.
- @Kara Monroe completed the pricing and billing item on 2025.08.26.
- The maraum tenant was created during cluster preparation.
- The maraum tenant was recharged as part of the same preparation step.
- @Kara Monroe finished the tenant creation and recharge on 2025.08.26.
- Preparation also created the VEXODIS CIDR.
- The recorded cidr is 10.122.151.111/24.

## Cluster deployment
- VEXODIS CIDR creation ran on 2025.08.26.
- @Kara Monroe closed that CIDR work on the same date.
- k8s control was created for 3 CPU nodes.
- The k8s control window ran from 2025.08.27 to 2025.09.02.
- That control task took 6 days.
- @Ethan Norris handled implementation for k8s control.
- @Kara Monroe provided R&D support.
- The new type had automatic installation issues during the task.
- On 2025.09.03, node pool expansion began.
- The expansion covered 2 CPU nodes and 45 GPU nodes.

## Cluster deployment
- Node pool expansion finished on 2025.09.03.
- The expansion was completed within the same day.
- @Ethan Norris and @Kara Monroe were involved in the work.
- RoCE|IB NICs were confirmed as operating normally.
- Bexcast88 initialization was also verified as normal.
- @Paige Zimmer owned the related R&D item.
- The record asks if RoCE|IB confirmation should stay in this section.
- Pelshaw also notes the option of waiting for later exposed issues.
- On 2025.09.03, the RoCE NIC was confirmed.
- The switch cabling table was confirmed at the same time.

## Cluster deployment
- RoCE cabling table confirmation was closed on 2025.09.03.
- The cabling confirmation took the same day.
- @Ethan Norris implemented that confirmation item.
- On 2025.09.04, this tenant’s RoCE segment was allocated.
- @Rachel Jarvis completed the tenant RoCE allocation that day.
- @Sophie Walsh was listed for R&D on that allocation.
- On 2025.09.05, multi-tenant container RoCE segments were assigned.
- @Fiona Ellis completed the multi-tenant container allocation on the same day.
- The container RoCE allocation started as single-tenant.
- A later conversion to multi-tenant mode was planned.
- Physical-machine RoCE IP address configuration started on 2025.09.04.

## Cluster deployment
- Physical-machine RoCE IP configuration ended on 2025.09.05.
- That RoCE IP configuration took 1 day.
- @Ethan Norris, @Rachel Jarvis, and @Sophie Walsh were involved.
- GPFS client setup created the Client Cluster on 2025.09.05.
- Nodes were added during the same GPFS client setup.
- The GPFS client item was completed that day.
- @Ethan Norris and @Kara Monroe implemented the GPFS client work.
- R&D support came from @Amber Parker, @Leon Vaughn, and @Kara Monroe.
- master1 2 3 c-004 do not support roce mode.
- Those nodes use Ethernet instead.

## Cluster deployment
- RoCE container networking configured the roce operator on 2025.09.06.
- Container connectivity was tested as part of that item.
- The RoCE container networking task finished the same day.
- @Ethan Norris and @Fiona Ellis handled implementation.
- @Fiona Ellis also owned the R&D side.
- Node labels were confirmed for the cluster.
- Scheduling configuration was confirmed as well.
- @Ethan Norris and @Quinn Archer implemented the label and scheduling check.
- @Quinn Archer provided R&D support for that confirmation.
- Monitoring operations components were confirmed.
- @Ethan Norris and @Ursula Landry implemented the monitoring confirmation.

## Pressure testing acceptance; pexieon deployment; resource delivery
- Monitoring operations component confirmation also named @Ursula Landry for R&D.
- Pressure testing and acceptance produced a testing and acceptance report.
- The acceptance activity ran from 2025.09.06 to 2025.09.10.
- The testing and acceptance span was 4 days.
- @Ethan Norris implemented the pressure testing and acceptance work.
- @Paige Zimmer and @Derek Carter provided R&D support.
- pexieon deployment opens network access for the new cluster.
- Pelshaw also synchronizes across image repositories.
- pexieon deployment builds the maraum database.
- Services are deployed for the work cluster.
- The work cluster maraum platform is validated.
- pexieon deployment CAN start in parallel after cluster control creation is complete.
- Detailed pexieon deployment notes still need supplementation.
- The pending pexieon details are assigned to the @Xander Walsh team.
- Resource delivery covers external customers.
- Resource delivery also covers internal customers.
- Luxsvc79 is included in the same delivery scope.
- The @Xander Walsh team owns the resource delivery item.