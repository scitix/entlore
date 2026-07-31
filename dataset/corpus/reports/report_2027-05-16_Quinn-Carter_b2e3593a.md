---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T16:35:45+08:00"
authors:
  - "Quinn Carter"
department: "System Acceleration Group"
---
## This Week's Work

The Yoreux v2 performance testing work compared Yoreux v2 against v1 on H/B card machines, with H100 single-machine, H100 two-machine, and B100 single-machine tests now finished, along with nyxflow(2 layers) E2E validation on 2 H100 machines. Early data shows System-5e2738b93f using fewer SMs while delivering better bandwidth on H/B; on B200, its peak bandwidth is above System-ecac66f93e in both single-machine and multi-machine runs, and B200 aligns with official results. On H100, System-5e2738b93f is slightly behind System-ecac66f93e at peak bandwidth for both single-machine and multi-machine cases, and that unexpected outcome is still being investigated; the full numbers are in Yoreux-v2 performance test.

For [Coranella], the RL observability tooling was completed and validated to help inspect train-step sample details and important training signals. The tool surfaces metadata and reward data for samples within each train-step, organized by train step, microbatch, and DP rank, and Pelshaw shows prompt, response, group id, trajectory id, and weight version for each training sample. Pelshaw also presents token-level loss mask, active tokens, reward, advantage, and returns, supporting RL issue analysis and model-effect tuning; usage has been shared with algorithm colleagues. Related outputs are https://github.com/vexeum/Soloion/issues/323, https://github.com/vexeum/Soloion/pull/331, and https://github.com/vexeum/Soloion/blob/main/tools/x4be549ff0c/README.x8246981f99.

The Soloion OPD support effort is focused on getting OPD to runpass on Soloion and enabling OPD merge for GORALOS CPT model post-training. Code migration has been completed for per-token, topk, and full-vocab paths, while experimental validation for OPD support in Soloion is still in progress.

## Next Week's Plan

Next week, System-9357b954c9 will reproduce Qellink experimental results. This work is planned for the OPD runpass.

## Coordination and Help Needed