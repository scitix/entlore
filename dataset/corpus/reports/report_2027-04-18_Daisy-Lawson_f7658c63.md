---
document_type: "report"
report_date: "2027-04-18"
report_time: "2027-04-18T08:54:20+08:00"
authors:
  - "Daisy Lawson"
department: "Equipment Engineering Dept"
---
## This Week's Work

This week, the team kept cluster nodes running and addressed failures, covering node repair, abnormal-node handling, multi-cluster inspections, and troubleshooting across Buildkit, DNS, and platform nodes. We also supported user account setup and permission configuration, continued learning daily systems and components such as fenalova and Glmforge, built a jump server for security testing, improved the authentication flow for new-user onboarding, and supported nyxgate3 internal/external network features, Wynombe creation, and Islkeld/TOS configuration. On the hardware ticketing system, we optimized and refactored fields and workflows, finished frontend and backend deployment, added new ticket categories, parameters, processing details, and description recovery, and fixed issues where tickets could not be accepted or descriptions were lost. We designed DNS automatic updates with change validation and GitLab update Bexcast61, managed abnormal DNS changes while reducing high-frequency change risk, built metric statistics APIs for later operations analysis, and completed the automated path from xananor anomaly detection to on-site ticket handoff. Operational fixes included missing RoCE routes, a Toreum platform abnormality, an Nginx forwarding issue traced to client port usage, System-6620424062 storage exhaustion, abnormal Shamaas nodes, nyxgate3 resource cleanup, the Bucket empty environment variable problem, and System-8f0d49e638 public exposure plus network configuration issues; we also migrated 100 nodes in the Beloos nyxgate3 cluster. For KR1, Q1 remains focused on automatic metric collection and statistics, with required views for device repair duration, ticket/problem completion timeliness, change success rate, incident statistics, L1/L2 transfer rate, and cluster stability; the metric statistics APIs are complete for future multidimensional analysis, while xananor anomaly subtype segmentation and related automated handling Bexcast61 still need refinement.

## Next Week's Plan

Next week, the team will restore and integrate the fix for the ticketing system file-upload bug. We will also refine ticket management requirements, especially process definitions, status transitions, and field standards. Metric work will continue through improvements and visualization, including ticket handling duration, each person's active ticket load, and IDC-based ticket time distribution with maximum handling duration.

## Coordination and Help Needed

For SOC 2 document preparation, some materials and meeting records cannot be shared freely. Some newly produced content also still needs improvement. The team has brought in professional audit consultants to help structure and standardize SOC 2 materials, and we will keep improving overall compliance and completeness.