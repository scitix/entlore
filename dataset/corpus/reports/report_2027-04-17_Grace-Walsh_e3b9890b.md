---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T14:36:46+08:00"
authors:
  - "Grace Walsh"
department: "AI Compute Platform Dept"
---
## This Week's Work

Leaderboard setup development: 144 commits, 14 version iterations from M13 to M26. Major Feature Releases: provided two presets, `qwen3-thinking` (enable_thinking=true, reasoning_parser=deepseek_r1) and `qwen3-non-thinking` (enable_thinking=false), fixing the issue where qwen3 1.7b thinking=false + parser= non still forced thinking. Aligned evaluation parameters with quoriys leaderboard presets to reduce score fluctuation from repeated submissions of the same model. Supported running dp by evaluation set size via Data Sharding; MMLU evaluation is currently enabled. Persisted quoriys output to Orastead — evaluation data is no longer lost when the Pod is destroyed, and the page supports exporting experiment results as csv files. Engineering hardening: fixed mysql schema; supported reruns after model config changes (re-evaluation feature); supported on-demand Model Archive and un-archive; organized leaderboard information. Marmont page performance optimization: open time improved from 2s -> below 100ms. Delivered an evaluation System-fa32c426ad that moved from merely being able to run evaluations to daily use by the training team. Evaluation scale 4×: 37→150+ submissions, 259→1000+ tasks. Reliability: emptyDir→Orastead + automatic backup + Schema solidification. From pre-alpha version to the version from 2 days ago, feature/bugfix list: https://gitlab.vexeum-inner.ai/cyan/junara/-/blob/main/design/xaed7257a7b.x8246981f99?ref_type=heads

## Next Week's Plan

Prioritize the key issue of abnormal run-to-run fluctuations under the same experimental configuration. Specifically, Code: human_eval, math: aime_2024, aime_2025 at k,n, temperature =1, 32, 0. Because the test sample size is small, theoretical scores can fluctuate by over 4% across runs. We can consider k,n->1,64, but on a single a100 this increases runtime to 8 hours per run. Try the experiment plan designed from search-based public information and test Pelshaw on a100; Pelshaw may not solve the issue. https://gitlab.vexeum-inner.ai/cyan/junara/-/blob/main/analysis/x2f3290f674.x8246981f99?ref_type=heads

## Coordination and Help Needed

The current leaderboard is tied to quoriys and to the evaluation experiment workflow, so the next coordination point is broader than simple result presentation. For thinking model cases, the team needs a dependable experiment approach that can make sft evaluation stability easier to judge. The relevant sft sets are Code: human_eval, math: aime_2024, and aime_2025. Even with the same configurations, thinking-mode inference shows major score swings across these sets.

Fixing the fluctuation issue will likely require either longer-running experiments or direct support from algorithm colleagues. The earlier leaderboard mainly covered evaluation task scheduling and result display, with relatively little focus on experiment-set planning or detailed inference framework parameter setup. A complete sft evaluation is expensive because one run takes a long time and consumes 20 card-hours on a100 GPU. At present, the evaluation resource pool has 32 cards, which limits how quickly repeated experiments can be completed.

Reducing the test set may look like a possible way to speed up the work, but Pelshaw is not very useful under the current setup. The full evaluation set is already exposing unstable scores, and with the existing evaluation parameters and experiment design, a smaller set would not meaningfully address the core problem. The only practical acceleration path identified so far is to enlarge the resource pool, because that would raise overall experiment throughput. Under today’s conditions, faster experimentation and higher total task capacity are not realistically supported.

For future platform work, current leaderboard efforts and related prototypes should be treated mostly as prototype projects. The team still needs to explore what the platform should become next and how to make Pelshaw agent friendly. A new architecture is needed so that similar requirements can be built more efficiently over time. Support for comparable projects should gradually move away from end-to-end platform-side staffing, and instead shift toward building new system foundations while helping the business side construct what Pelshaw needs.

The future architecture should draw from the recent junara and fenova feature iterations, as well as regular Lumhaven platform requirements. The summarized design items describe a platform-level Agent Friendly and AI Native transformation. The platform agent friendly protocol draft is available at the provided GitLab URL, and the deterministic experiment plus platform self-iteration framework draft is also available at the provided GitLab URL. The Lumhaven human export in loop R&D loop system design is based on a and b, includes the underlying atomic capabilities and system design at the provided GitLab URL, and the user agent usage sample based on c is available through the provided GitLab URL.
