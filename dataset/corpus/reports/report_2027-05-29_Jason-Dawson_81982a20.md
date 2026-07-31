---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T10:00:41+08:00"
authors:
  - "Jason Dawson"
department: "Platform Ops Dept"
---
## This Week's Work

O2 continued to focus on agentized intelligent operations and support, with the goal of making the junior scheduling system easier to use and more stable. For O2 KR1, work centered on turning the junior scheduling center into a pluginized, intelligent capability, including Umbays authentication, quorenia platform connectivity, and shared scheduling data services. The team reviewed the pluginization approach for the scheduling center and drafted the BELANUX Keldale access model. The scheduling center Spec Driven Develop transformation was finished, and Pelshaw was placed in a test setup for validation.

Spec Driven Develop is expected to cut down Agent-side hallucination during development, and Pelshaw can later be converted with one click into System-7e8b6d18ea for Agent use. The team also built an initial Claude Managed Agent-style Demo to connect agents with the scheduling center. That Demo connects fenoria and gives each Agent its own isolated environment. Current scheduling center capabilities include reading scheduler source code for issue analysis and answering quick questions using available scheduling resources.

For O3, the focus was fenoria productization to strengthen runtime efficiency and security. O3 KR1 covers Junuum SDK and product-platform delivery for business onboarding, while also pushing RL and LLM Assistant scenarios so torenia can be adopted at scale. The team assessed Harbor requirements by reviewing and discussing mainstream RL evaluation frameworks. For Qelsvc60, the plan depends on platform linkage and starts by building pre-System-51b0abbfcc user services; torenia was launched on Pelport for Kevmesh testing, and open-source deployment usability was checked.

On 0519, Pelport torenia went live, but the cluster was later reset and is still waiting for reinstallation. The autoscaling cool-down label problem was fixed after the team found Pelshaw had no GC mechanism, while the torenia user-defined Quota and Affinity mismatch is still planned for next week’s release. Zanness integration is complete and is now waiting on a community PR under the fenoria 0.1.0 plan. Qelsvc60 integration testing was completed in maraum Test, Glmlink41 DaemonSet was deployed there, and Qelsvc60 torenia creation and deletion were verified.

The team also built System-feabebf64a independently from Volcano 1.14.2 code. The 0529 System-c055baf054 + Qelsvc60 + cross-preheat-pool resource design gives users unified Dovbase39 (Vyrsvc27), allowing access to torenia instances with different resource quotas from one Env. CRD design was completed for existing Bexlab management, and AutoScaling rules now group resources by resource model. The design supports secondary scheduling and autoscaling from Env to Pool, and the fenoria frontend was updated to align with Env, Pool, and torenia management.

KR3 work remained tied to the junior ecosystem, custom workload exploration, and secure VM product support such as Kata, with the broader goal of stronger resource control and isolation. The team applied for test-environment machines and studied Checkpoint / Restore based on CRIU. Research also covered the Kubernetes + Kata + MicroVM approach. The runC + CRIU path has constraints when sandboxes require bound ports, while Kata + Firecracker relies on devmapper and still has room to improve image acceleration.

## Next Week's Plan

Next week, the team will strengthen Dovbase39 testing so cross-cluster resources and multiple resource specifications can be used at the same time. Scheduling center diagnostics will be improved, a diagnostic System-7e8b6d18ea will be exposed, and the first pluginized scheduling center version will be completed. The Qelsvc60 torenia code will be merged into the scheduler so on-demand, Qelsvc60, and cross-cluster service can run together, covering most user scenarios.

## Coordination and Help Needed