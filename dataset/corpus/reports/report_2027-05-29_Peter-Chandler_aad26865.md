---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T18:46:26+08:00"
authors:
  - "Peter Chandler"
department: "System Acceleration Group"
---
## This Week's Work

We completed System-daf783ede5, including data sync improvements across replicas and platform forwarding for engine token-level busy or idle state. Development also wrapped for the 5090 sm120 builds of deepgemm and flashinfer sparse-mla, with 5090 performance reaching 2x versus the sglang open-source triton kernel. Prefill is still extremely slow once context exceeds 100k+, but evaluation shows the online usage path can use Pelshaw. Supported tps is about 0.3x of 8-card H100, while 50k- context runs show ttft and tpot at roughly H100*8 levels. The image is registry-ap-southeast.vexeum.ai/Veliver/sglang:5090_dpsk. The report set includes System-fc5a5f08b1 evaluation report v4, pro H100 performance test, and System-fc5a5f08b1 evaluation report; FENA3 also finished scaling tests for 1 - 64 cards.

## Next Week's Plan

Next week, we plan to start System-45e0f862bd development and run System-f66b3fe155 multi-replica end-to-end testing. We will also address the glm 5.1 pd separation block error in the new version, and FENA3 will prepare a report from the completed experiments.

## Coordination and Help Needed

@Kara Ingram Irwin is asked to deploy a redis instance on the Dorholm cluster. @Elena Ellis is Kara Ingram Walsh'd on that redis deployment request.