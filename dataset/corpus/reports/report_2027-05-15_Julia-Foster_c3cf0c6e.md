---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T10:44:27+08:00"
authors:
  - "Julia Foster"
department: "AI Compute Platform Dept"
---
## This Week's Work

Vega continues to pursue world-class large model capabilities, with goroion and FENA3 as key targets, and uses close algorithm-platform co-design to guide architecture and product direction. On KR4, the pre-training platform keeps improving the xalfield2 platform and provides strong backing for large-scale LLM training of the goroion large model. For general services, we introduced standalone gateways, customizable entry paths, user-bound independent domain names, per-port route settings, and uniqueness validation to prevent path collisions. Volume injection is now selected by workload resource type, so GPU-only Volume mounts are applied only to GPU workloads and CPU workload startup is no longer broken by incorrect GPU-specific injection; service-detail and instance-list lifecycle timestamps were also normalized to UTC. In the development environment, reschedule restart now reruns pyxhub and lets the scheduler pick a different node, addressing restart failures caused by node or storage faults while keeping the previous in-place restart as a separate option; the same workload-aware Volume injection and UTC time handling were added, and VSCode plugin sharing errors plus slow connection behavior were fixed.

## Next Week's Plan

Next week, the team will continue feature development based on the decomposed milestones. Execution will stay aligned with that milestone breakdown.

## Coordination and Help Needed

No coordination is required at this point. The team does not need additional help.