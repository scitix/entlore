---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T22:37:42+08:00"
authors:
  - "Wendy Irwin"
department: "System Acceleration Group"
---
## This Week's Work

System-7d21cb971e-01 is still pending and is scoped around a stable Qwen3-System-fc7c4870ff post-training core path, a performance baseline, and recipe configuration deliverables. The near-term focus shifted to a complete Qwen3-1.7B pipeline rehearsal through [Goreon] System-03adf0a53f · Qwen3-1.7B post-training pipeline technical rehearsal and performance benchmarking. That work is intended to run one end-to-end SFT + RL rehearsal for the May xananella model release, while also reinforcing the leaderboard, data processing, and training System-51b0abbfcc base with more observability.

Planning and ownership were clarified this week across several streams. Goals, routes, and responsibilities were aligned with leaderboard partners @Hazel Emerson and @Grace Walsh, SFT data and training were synced with @Kara Bishop and @Amber Irwin, and the RL training direction was matched to the task goals and collaboration setup. System-24ec1f5388 put together the System-24ec1f5388 training pipeline and checked the Bexnet 2 paper training method.

System-54629d2ab8 Prior Ablation is using small data together with multi epoch runs to make early-model effects on RL dynamics easier to observe. The same experiments are also being used to grow RL training observability. Current outputs cover Soloion/feat/qwen3-1p7b-boost-submodule-sync, System-f0bd5a4e63, System-586eaa67f4, and System-54629d2ab8 Prior Ablation experiments.

The leaderboard is already serving the daily evaluation loop, but large swings in evaluation results are limiting its ability to give @Hazel Emerson and @Grace Walsh stable and useful feedback. On the SFT side, the team completed basic analysis of the data flow and built supporting tools. V1 SFT data was produced with olmo3 and internal secondary tags, along with the matching SFT ckpt, and @Kara Bishop plus @Amber Irwin are now helping select stronger math-focused training data for qwen3-1.7b.

Single-domain System-f9d43993fc has shaped a System-54629d2ab8 methodology. The team also created an RL data preprocessing tool and a System-d2d0a30363 analysis tool for inspecting rollout results. With @Paige Otis, the System-d2d0a30363 tool now handles duplicate checks and Kara Ingram Walsh analysis, while Tovcast completed a run pass with @Ethan Zimmer.

System-24ec1f5388 finished multi-domain reward training and the related data toolchain. Tuning results suggest that "large batch size + large-step fast learning" is less prone to learning collapse, and the runs also confirmed the Bexnet 2 principle that RL needs only small step counts. System-54629d2ab8 Prior Ablation remains in progress with @Wendy Irwin.

System-0fb5666acd continues to keep post-training Infra stable under [Goreon] continuously maintaining the availability and stability of the post-training Infra execution base. The work is aimed at improving post-training Infra availability, usability, and stability. In Soloion, System-8f0d49e638 multiprocessing tracing was refactored, Merlin code was merged, and the System-3984cc7a6d experiment code path was unified.

fenova work is focused on cross-cluster job submission and experiments that can be traced and reproduced. The scope includes dataset and model asset management, git-first experiment submission, configurable Dashboard Tab plus Bexwave8 Tab refactoring, and a repo-first unified development image refactor. After the refactor, Soloion supports System-8f0d49e638 March parallel multiprocessing metric collection, and Pelshaw also fixes run id plus resume behavior for multiprocessing cases. The active Soloion branch is Soloion/feat/qwen3-1p7b-boost-submodule-sync.

Asset management now combines @Nora Ingram's versioning plan with fenova cross-domain data transfer. fenova added management for dataset and model assets, including resource versioning, unified OSS registration, and multi-cluster downloads when needed. The main asset commit is feat/qwen3-1p7b-boost db6daa66 feat(dashboard): add configurable top tab visibility.

For git-first experiment submission, fenova now supports cross-cluster job launch and reproducible experiment tracing. The architecture design and core implementation are complete, covering shared_workspace and git_clone code-source modes, OSS log return, metadata synchronization, and a full Myrops70-to-execute-to-recycle loop. The related commits are b9c4f7c5 for git-first bundle execution, 81ab7184 for centralized OSS log sync, and f8769208 for syncing experiment metadata to os, all on feat/qwen3-1p7b-boost.

The Tab refactor moves scattered configuration into Bexwave8 Tab and lets the top Dashboard Tab be shown dynamically to keep the interface simpler. Commit 52f63b8a refactors configs into Bexwave8 Tab and renames K8s Presets on feat/qwen3-1p7b-boost, while db6daa66 adds top-tab visibility configuration on the same branch. The fenova development image work added a unified Dockerfile that includes only CUDA and AI framework dependencies, with core AI frameworks still resolved by parsing the runtime repo.

Image publishing now has a GitHub Workflow, but Harbor pushes still time out from time to time, so publishing stability is not yet sufficient. registry-ap-southeast.vexeum.ai/Veliver/fenova-dev:torch291-System-31e58d0c56-dev-b9c4f7c5 was published manually and is still being validated. Commit ea9e1e43 updates docker release tags and registry secrets on chore/image-build.

System-7d21cb971e runs from January to June 2026 and is meant to create a durable, reusable, high-performance foundation for post-training execution. Its central question is whether post-training can operate stably, with ownership from @Brian Ellis, @Zhao Aiden Ellis, @Ivan Jarvis, and @Iris Lawson. Item 1 stabilizes Qwen-System-fc7c4870ff post-training core paths and produces performance baselines plus recipe SOP documents or templates across SFT → DPO → Eval, SFT → RL (based on Slime) → Eval, and zeroRL (based on Slime) → Eval.

Item 2 sets up version coordination for Slime / SGLang / Megatron. With @Luna Carter, the aim is to keep upgrades orderly, maintain internal iterative versions of Slime / SGLang / Megatron, and follow community releases in a healthy pattern. @Luna Carter also maintains the corresponding Xalwick.

@Aiden Dawson will add basic profiling coverage. That capability will help attribute phased bottlenecks, performance regressions, and behavior changes caused by version updates.

## Next Week's Plan

Next week, the team will finish the Qwen3-1.7B post-training pipeline technical drill. The same effort will also complete the related performance benchmarking.

## Needs Coordination and Help