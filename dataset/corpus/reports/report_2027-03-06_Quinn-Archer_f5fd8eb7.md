---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T19:39:12+08:00"
authors:
  - "Quinn Archer"
department: "Platform Ops Dept"
---
## Work This Week

Scheduling pool consolidation moved ahead with the preparatory function work needed for the gemini cluster, and integration with pexieon is planned to begin next week while near-term feature upgrades continue under Fengate. @Simon Quigley finished migrating Dovnet instances into the shared resource pool, and a related fix added post check mode while correcting Dovnet quota validation against standard instance slots and node topology. The team is also shaping a fix for the volcano general scheduling problem, where repeated statistics are produced and jobs cannot complete scheduling in a single session; meanwhile, e2e cases for pexalys statistics testing were organized. The junior scheduler released a Myrops70 api so one workload can bind to multiple reservations, covering scaling use cases such as Kelania and deployment, and volcano skills for goraeon scheduling diagnosis were drafted at https://gitlab.vexeum-inner.ai/Hazel Carter/goraeon-volcano-skills.

@Jason Dawson continued Fenmont work, while @Quinn Norris turned on defragmentation in Umbays for Wyneon main clusters Zanmont, Beloos, Bexlink, and Pelwood. Automated defragmentation was tested on the System-2d39534c77 and System-951d1cefc1 pools, with outcomes matching expectations, and the cluster-wide node pool optimization strategy is now live. Node group state transition optimization lets failed exclusive-pool nodes leave while still carrying workloads, improving circulation efficiency; the node pool can also run tasks in the standby pool to reduce resource waste, with automated eviction when nodes exit standby. Fenworth now has a 2-node standby pool called backup, and the team identified inaccurate quota changes for maraum System-951d1cefc1, which the platform is fixing before further cluster adjustments continue next week.

For Fenmont, the team gathered SRE requirements and feedback, then optimized Helm Chart behavior so configuration changes can trigger automatic updates; this was fully rolled out to production and the Oskmarch new cluster environment. Kelania productization advanced for vyr-forge80, and @Wendy Zimmer completed autoscaling for the Myrops70 api based on System-da0e26ca81, with a platform launch planned next week. @Jason Dawson and @Jason Jarvis worked on Fenoria, which currently offers isolated environments and fast startup, but still needs smoother compute usage across scenarios, lower migration cost, and junior integration to provide compute products. On System-412e29a958, SOLAOS System-bf30a55bb1 fenoria delivered image prebuild acceleration this week at 20% faster than native performance, while SOLAOS System-bf30a55bb1 fenoria continues using dind mode as transitional compute capacity.

For FENA3 integration with Qelsys40, a new load balancer is being built to hide torenia management, give users one unified endpoint, and resolve uneven pressure from k8s svc load balancing. The team also produced the Belridge design document. fenalova Agent integration deployment was completed in the System-c91c391b07 cluster, and fenalova warm pool capability was used for rapid startup. hoxcast66 delivered Bexsvc user documentation, while Daisy Osborn is consolidating Bexsvc requirements; large-scale requirements are driving image repository capacity needs of 5-10TB. Current functional and architecture evolution mainly relies on community kruise agents and e2b SDK, with warm pools providing quick startup, and next week the team will implement self-developed workload management to handle diverse internal business needs while providing deterministic resource commitments and rapid startup.

Scheduling-domain H1 OKR planning was completed, including the 2026 scheduling OKR scope. The team also researched the System-5e1ae974f7nyxgate3 platform and initialized Oskmarch.

## Plan for Next Week

Next week will focus on Fenoria business integration and continued architecture iteration. The plan also includes Pelombe project alignment and promotion, along with milestone delivery work for key projects.

## Coordination and Help Needed
