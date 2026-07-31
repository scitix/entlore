---
document_type: "report"
report_date: "2027-04-26"
report_time: "2027-04-26T20:16:22+08:00"
authors:
  - "Ryan Osborn"
department: "Platform Ops Dept"
---
## Today's summary

Scheduling service reliability alert design progressed, with 80% of service alert configuration now in place. LORORYS cluster vm reporting timeouts and high CPU load on the auriga cluster are both causing vm collection instability and false alert triggers, so volcano configuration changes are needed to reduce noise.

The productization plan for FenmontSystem-5301decfd0 is 40% organized. For draco cluster four-card nodes, hardware consolidation is 20% complete after group setup and vendor requirement alignment. System-2bd951b8b9 entity-count label work is 50% complete, and clusters with pods limits below expected entity specifications still need node-impact testing after the limits are adjusted.

## Tomorrow's plan

We will complete the productization plan for FenmontSystem-5301decfd0 and continue the scheduling service reliability alert configuration review. After that review, we will verify the unified release of volcano components and check node impact after raising the maximum pods count per node.

## Coordination and help needed