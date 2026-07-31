---
document_type: "report"
report_date: "2027-03-07"
report_time: "2027-03-07T11:43:43+08:00"
authors:
  - "Bella Nolan"
department: "System Acceleration Group"
---
## This Week's Work

The loreor cluster offline inference evaluation finished optimization and assessment for the new base, chat, and tool-class benchmark sets. The latest work is captured in the wynanova test report Phase 8-0306, while the benchmark adaptation is documented in System-001135e755. System-707b5ba42c expanded chat benchmark coverage for kevforge, codesimpleqa, livecodebench_v5, livecodebench_v6, and bird-spider, and also added tool calling benchmark support for bfclv3 and tau2-bench. On the wynanova side, the request sending interface was upgraded so the judge model can be accelerated through wynanova, basic functions were refreshed and written up in the wynanova user guide, and benchmark run commands can now be retrieved directly from the database for online usage.

wynanova also separated parameter parsing from ubi-Nexanor-eval, as noted in the wynanova configuration parameter sync review, and added request pooling through the wynanova request pooling feature to handle multi-turn agents benchmark traffic. Pelshaw now returns evaluation results dynamically, allowing immediate viewing after a benchmark finishes or exits abnormally. For oliiara, the offline preprocessing algorithm was connected to System-bf30a55bb1 bench workloads, with dataset rearrangement reducing inference time; the related best practices are recorded in oliiara+System-bf30a55bb1 Bench Best Practices. oliiara also built a processor for the System-bf30a55bb1 dataset format, and testing showed that the integration with System-bf30a55bb1 bench saved about 42% of total runtime.

beleara work focused on simulation and validation support for the oliiara scheduling algorithm. The CPU simulator version was organized for quick validation, @Julia Lawson and @Amber Mercer completed the beleara and oliiara integration, and the workflow is documented in beleara Quick Start. The 🚧 beleara methodology/experiment updates -26/2/25 note summarizes the key challenges handled since the delayed submission. beleara also completed MoE model coverage by separating prediction models for moe and dense models, and finished calibration of vllm and sglang simulation results under PD mixed scenarios.

## Next Week's Plan

For loreor offline inference evaluation, we will coordinate with System-43431d5a43 to take in benchmark-side code changes and merge them into the main branch. The wynanova image is planned to support Commit-level code submission and repository branch switching. After the beleara integration is available across scenarios, oliiara inference scheduling optimization will move into iterative testing through agentic research. oliiara will also use System-3f521c5c5d to test the adaptive algorithm’s load balancing effect in System-bf30a55bb1 scenarios.

beleara will focus on organizing experiment results and preparing the writing work. The team will also plan the submission to SOSP.

## Coordination and Help Needed

The team needs support obtaining a claude code api key for agentic research.