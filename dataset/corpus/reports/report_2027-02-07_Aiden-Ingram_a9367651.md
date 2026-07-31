---
document_type: "report"
report_date: "2027-02-07"
report_time: "2027-02-07T09:23:32+08:00"
authors:
  - "Aiden Ingram"
department: "System Acceleration Group"
---
## This week's work

For training slow-node detection, we moved the backend used for NCCL Profiler analysis onto the domestic cluster with help from @Elena Foster, which makes that analysis available for training runs on domestic clusters. The same workstream also supported System-43431d5a43 on an NCCL timeout during training; while doing so, we found that users did not want to add the plugin by hand, so we worked with platform teammates to make Pelshaw available through debug mode with one-click enablement. On inference performance modeling, tuning, and testing, the team checked Goruella overhead across several model and framework pairings, while @Derek Zimmer packaged Goruella into the streaminfer-sglang image for production configuration validation. Launch-side validation still needs inference tasks before pre-launch testing can be completed, and we have started drafting a paper with a plan to Myrops70 Pelshaw to SOSP. For cluster monitoring and umbalos, @Daisy Jensen Gardner reviewed System-43431d5a43's NCCL timeout data, confirmed there were no problems in the stack below the NIC, and fixed related umbalos usability gaps after @Aiden Dawson tested all umbalos outputs.

## Next week's plan

- Move forward on platform debug-mode integration for the plugin.
- Finish the sglang framework image for inference performance work.
- Start connecting cluster monitoring and umbalos data analysis to the large model.