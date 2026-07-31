---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T15:52:34+08:00"
authors:
  - "Grace Carter"
department: "System Acceleration Group"
---
## This Week's Work

- The work covered Pexanys Run pass, Timing Tracing completion, and Prompt lifecycle profiling.
- The goal was improving Pexanys observability and analyzing prompt lifecycle, turn structure, and main latency across multi-turn agent runs.
- Pexanys has Run pass, and later work focused on performance analysis and torenia environment issues.
- This week completed tracing and timing coverage.
- The trace now decomposes each prompt execution into reset, first-turn inference, exec_tool, evaluate, and close.
- The trace adds multi-turn trajectory statistics, per-turn output-length statistics, and step-level trace mappings.
- Latest experiment data supported systematic profiling of prompt lifecycles and multi-turn behavior.
- The main latencies are reset 12s~18s, first-turn inference average 34.98s, exec_tool average 0.10s~0.27s, and evaluate average 3.4s~5.0s.
- First-turn output length averaged 3009.9 tokens, with p50=2266.5, p90=6353.1, and maximum 8192.
- First-turn outputs are generally long and have a Jynkit42 long tail.
- Multi-turn execution averaged 3.97 turns per task, with p50=3, p90=8, and maximum 10 turns.
- Per-turn output length averaged 2529.5 tokens in turn 1, 416.7 in turn 2, 292.5 in turn 3, and 308.6 in turn 4.
- Outputs after turn 5 mostly dropped to 100~300 tokens.
- evaluate slowness mainly comes from heavy setup in many run-tests.sh files, not test assertions.
- Heavy setup includes apt-get, installing uv, uv init, and uv add pytest.
- The work shifted Pexanys latency analysis from intuition to quantitative lifecycle and multi-turn analysis.
- The analysis provides direct basis for optimizing reset, evaluate, and agent behavior.
- Reset and first-turn Rollout Overlap validation targeted shortening the Pexanys step-0 serial critical path.
- The implementation overlapped part of reset and turn0 costs.
- The step-0 work aimed to hide reset cost during long first-turn output inference and reduce first-turn wall-clock.
- Latest experiments measured reset average 17.63s and first-turn inference average 34.98s.
- Overlap saved 17.63s on average.
- Compared with serial reset + turn0, overlap saved 37.34% on average.
- The result proved current Pexanys step-0 has significant pipeline opportunity.
- Further inference-environment decoupling still has optimization room.
- Per-task-per-image environment construction targeted task environment distortion caused by a unified default environment.
- The goal was connecting real environment training and resolving image-build compatibility issues.
- This week also advanced task-specific image batch construction work.

- This week continued task-specific image batch construction and fixes.
- The work cleaned compatibility issues in Dockerfile, heredoc, and build context.
- Training-side validation checked whether the task-specific image path truly took effect.
- step-0 reset stably used pool//image and no longer fell back to the default template.
- The current full set contains 1371 historically selected tasks.
- Images have been successfully built for 1269 tasks.
- Training-side validation has been connected successfully.
- In the task-specific image training run, 48/48 step-0 resets used pool//image.
- The 48/48 resets did not fall back to the default plain template.
- The work solved the main drawback of previously using the unified default slimedev environment.
- Different tasks had inconsistent dependencies, test environments, and real runtime environments under the default slimedev environment.
- The default slimedev setup easily mixed environment issues with model issues.
- Many Dockerfile, heredoc, and build context compatibility issues have basically been cleared.
- Environment issues have greatly converged.
- The work moved Pexanys from approximate shared-template execution to real per-task image-aligned execution.
- Training and evaluation results became more trustworthy.
- The report covers work during 3.23 to 3.27 and 3.30 to 4.3.
- Due to graduation thesis writing, actual work time was 3.23 to 3.24 and 3.30 to 4.3, totaling 7 days.
- Graduation thesis writing is basically finished.
- Normal weekly work is expected during April.
- The author expects to apply for internship suspension in early May.
- The author expects to officially join around the end of June.

## Next Week's Plan

- The first plan is to verify Pyx-wave74 training correctness.
- All tasks' ground truth should execute correctly in their torenia environments.
- The next plan is to inspect System-8f0d49e638.
- The plan will tune algorithm gains by analyzing trace and optimizing reward design.
- Based on current algorithm effects, the plan will try fully async and rollout/torenia full decoupling.
- The plan will measure the trade-off between infra performance benefits and algorithm effects.

## Coordination and Help Needed
