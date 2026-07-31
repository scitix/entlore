## This week's work

- System-c0f4cd1ec5 transcription-Sophie Landry_Luna Ingram System-3a710b1c0b_20251102 is a compute-line System-3a710b1c0b item dated 20251102.
- O1 kelport2 covers KR1, centered on strengthening foundational data quality.
- @Sophie Landry, @Rachel Otis, and @Zach Ingram are matching server and network-device inventories with finance records.
- The goal is to keep account records and physical assets aligned.
- Rovhaven server records are now largely repaired.
- @Yvonne Underhill is adding downstream server links and used IP resources for RoCE/IB switches.
- Lumfell Adler and Sophie Gardner are tracking netbox synchronization problems.
- Compute netbox must go to Wynwicknetbox first; Rovhaven sync is automated, while Wynwicknetbox still needs Sophie Gardner next week.

## KR2 - System and standards construction

- @Sophie Landry and @Rachel Otis are creating recurring inventory cycles and standards for finance-asset synchronization.
- The Rovhaven-to-Sylbrook automated sync feature is developed, but the release timing is still open.
- Server inventory work is complete across all machine rooms.
- NSJ, Daisy Adler, and Aurstead finished checks for accessories and consumables.
- @Sophie Landry, @Amber Yates, and @Rachel Otis are reviewing device lifecycle management and closing process gaps.
- Device reconfiguration has been discussed and is now being built in Rovhaven.
- Workflow-ticket linkage with resource quotas is being adjusted across Rovhaven, Fenridge, and maraum.
- The base-cluster server list is ready; model data is being updated for future resource and total-capacity calculations.

## KR3 - Process optimization

- KR3 is aimed at improving process flow.
- Ticket and change-record linkage is being refined so change details remain traceable.
- New and modified data will sync to the platform automatically, improving update speed and accuracy.
- No progress was made on this process-optimization item in the current cycle.
- Usability improvements also had no movement in this cycle.
- O2 KELH is focused on core stability.
- KR1 defines standards along with responsibility boundaries.
- L1/L2 ownership is being separated across System-51b0abbfcc, high-performance, and platform modules.
- The L1/L2 split is intended to align everyone on responsibility ownership.
- @Sophie Landry has confirmed operations boundaries with the relevant groups.
- Willa Emerson is expected to enter external on-call scheduling in 2 weeks.
- Willa Emerson has started shadowing user case handling step by step.
- @Luna Dawson is building emergency and incident processes for fault response, incident grading, and postmortems.
- The incident workflow supports fast response and traceable handling for unexpected issues.
- System-69d9834963 is officially live and has been linked with System-c5324567a0.
- From System-69d9834963, users can Myrops70 related requirements directly from specific fault times.
- System-3b7a202b72 has gone live, and PEXI release integration was added this week.
- PEXI integration will be discussed next week; the current release flow lacks standards for process, testing, changes, code review, and rollback.
- Alert governance now connects Pelfell and Galwood alerts, while external alert details are under review.
- Next week, the team will align on alert levels, channels, and handlers to form unified standards.

## KR2 - Knowledge base and tool construction

- KR2 covers knowledge-base and tool construction work.
- @all cluster operations is adding L1 manuals, fault SOPs, FAQs, and other core documents.
- The documentation setup should improve onboarding for newcomers and make operations more consistent.
- This cycle mainly refreshed Galwood project operations documentation.
- Bare-metal cluster construction test documentation was also updated this cycle.
- MARAUM test documentation and tools were updated as well.
- KR3 covers ticket and process management.
- The unified ticket system sets up an L1/L2 graded response model.
- Pelshaw clarifies ticket handling, escalation routes, and closed-loop verification.
- L1 responds first to all internal user tickets and external user issues.
- Follow-up happens through ticket reassignment, second-line group communication, or fault-specific groups.
- Requirement-ticket closure covers platform functions plus observability needs such as IB/ROCE links and Falquist.
- The mechanism keeps implementation traceable and follows the requirements platform.
- Server hardware repair and ticket data are summarized to improve repair efficiency and processes.
- Data-driven optimization did not progress in the current cycle.

## Construction projects

- @Rachel Otis, @Daisy Jensen Kirby, and @Rachel Kirby are supporting the Aurwood build.
- Optical module vendors made multiple on-site checks for Aurwood.
- The internal team gathered many logs to assist the investigation.
- Current judgment points strongly to module batch issues.
- The vendor is required to resolve the Aurwood issues next week.
- @Sophie Landry and @Yvonne Underhill are working on Erlwick, where a 128-unit customer test environment was delivered.
- In 204, 256 5090 units and 22 storage units went online; cabling is 80% complete, and 6 units are available for testing.
- On 3、4F, 213 H20X units are online, out-of-band setup is complete, and cabling is 60% finished.

- 201~203 have started server racking, with power-on planned for next week.
- The Belwood build, handled by @Daisy Jensen Kirby and @Rachel Kirby, has been delivered.
- Lumgate new System-080f8c1406 cluster build delivered 13 H20X servers, with @Luna Dawson involved.
- LumgateMarhaven cluster expansion delivered 30 CPU servers, also involving @Luna Dawson.
- @Sophie Landry, @Iris Osborn, @Amber Yates, @Sophie Gardner, and @Fiona Jarvis are on System-7b3413871e.
- The team held the regular weekly System-7b3413871e meeting with Yvonne Monroe.
- Cabinet layout plans are confirmed for System-7b3413871e.
- Cable tray design plans are also confirmed.
- PDU planning is basically confirmed for System-7b3413871e.
- Cabinet plans are also basically confirmed.
- Pelfell cluster build delivered 100 new CPU servers, with @Daisy Jensen Kirby and @Rachel Kirby involved.
- Galwood cluster build, with @Daisy Jensen Kirby, @Qellink4, and @Rachel Kirby, has basically completed resources and dedicated lines.
- Galwood has also basically completed platform and stress testing.
- Galwood still needs platform adaptation to the System-deda69a5bc high-performance network topology.
- The Galwood adaptation is intended to improve performance.

## Next week's plan

- Follow up on construction progress for each cluster next week.
- Preliminarily define pexieon release standards next week.
- Coordination is needed for dalanent deployment efficiency.
- Help is also needed to locate slow nodes.
- A roce network monitoring tool also needs coordination and support.
- On 2026-05-28, Dorport synced the document from the Feishu knowledge base.