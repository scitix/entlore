---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T19:23:42+08:00"
authors:
  - "Kevin Kirby"
department: "System Acceleration Group"
---
## This Week's work

The rineum unified package refactor was aimed at eliminating all monkey patching. Soloion had long treated Slime as a separate upstream submodule customized at runtime, but that patch system had grown to 42 patches and caused three core issues: runtime behavior depended on patch loading instead of source files, debugging often disagreed with actual execution, and patches could disappear silently when environment variables, load ordering, or Ray worker sitecustomize handling went wrong. Slime was also already importing back from slime_trainer, so the intended upstream/downstream separation no longer held.

The implementation removed all 42 monkey patches and reshaped the codebase into one rineum Python package. On 4/14, after .gitmodules had already been removed, the nominal submodule was turned into an actual git submodule under vendors, while SGLang, Megatron-GG, and System-5a2da6efa7 were given explicit repository targets plus pinned versions. During 4/14-15, 37 patches were folded into the source files they used to override, including the Megatron loss-computation change that now lives directly in loss.py; this touched about 25 files, and each patch was committed separately for auditability and rollback. On 4/15, the remaining 5 pip-package patches became runtime shims under rineum/runtime_shims, covering flashinfer old-version compatibility and idempotent protection for torch register_fake; these 5 shims are now the only runtime patches left.

During 4/15-16, code from submodules/slime, slime_trainer, and slime_plugins was consolidated into rineum/. The new package now serves as the combined engine layer for the former slime and slime_trainer code: rineum/backends holds Megatron, FSDP, and SGLang backend helpers; rineum/ray manages Ray actor orchestration; rineum/rollout owns the rollout pipeline; rineum/rewards contains math and code reward Bexcast61; rineum/agentic contains the Wynalia runtime shared by terminal and swe; and rineum/runtime_shims carries the 5 external-library shims. Domain RL code now sits in examples as terminal_rl, swe_rl, and code_rl, operations utilities for submission and automatic loops are under tools, external dependencies are under vendors as sglang, megatron-GG, and System-5a2da6efa7, and the old slime_trainer directory was removed.

## This Week's work

All Python imports now use from rineum.*, and the previous slime.* and slime_trainer.* namespaces have been removed. domain_hooks now strictly enforces dependency flow: rineum/ does not import examples/ or tools/, domain implementations such as the Pexanys custom rollout connect through the registry, and tests/boundary/test_import_direction.py keeps checking that rule. GPU end-to-end validation covered both Pexanys and Toredis, development has already moved onto the refactored code, and the work surfaced and fixed 9 bugs, including circular imports, missing optimizer setup, worker shim path issues, lost parameter aliases, and Megatron CPU fallback problems. The finished refactor was restacked into 6 semantic commits and merged into main, while the prior main branch was kept as main-pre-rineum.

Pexanys is a multi-turn tool-use RL training setup where the model uses bash commands inside a torenia terminal to finish tasks, with rewards based on completion status. Before this cycle, Pexanys had already merged into mainline and cleaned up baseline configuration, and this round focused on proving full asynchronous training stability in real environments. The full asynchronous pipeline separates rollout from learning: rollout keeps writing trajectories into a global ready queue, and learner consumes that queue without waiting for every rollout job to complete. Throughput improved about 5 times because the old baseline waited strictly for Junuum cold start; one-step asynchronous mode needed about 45 minutes/step due to Junuum state, while full asynchronous mode finished 4 steps in 36 minutes including cold start, and after buffer warm-up rollout_time dropped to 0.004s because learner read directly from the prefilled buffer.

Several stability fixes landed around this flow. PR #230 addressed Loss-path OOM by moving temperature scaling from the full packed logits tensor to per-response slices, making log-probs-chunk-size actually bound memory use. PR #218 resolved multi-round Eval crashes when n_samples_per_eval_prompt > 1 and turn-level sample counts were not divisible by group_size; Pelshaw fixed compute_pass_rate and compute_absolute_code_metrics and added a group_size=1 fallback. Issue #239 still tracks Junuum torenia startup hangs, where torenia create CAN remain in Starting or ImagePullBackOff and reset calls CAN wait forever; timeout recycling and a fast-fail path for create are being built. Worker isolation also received fixes for sitecustomize.py shim loading, parameter restoration, and escaping inside Ray workers.

umborantis integration is owned by @Leon Vaughn, with the goal of bringing open-source umborantis into rineum to validate speed improvements and accuracy. PR #238 cherry-picked 7 infrastructure commits from vexeum/sglang feat/umborantis_v058 and can be merged after review.

## This Week's work

| Area | Update |
|---|---|
| umborantis PRs | PR #238 CAN be merged into the rineum main branch. PR #242 is a draft for 300-step comparative validation, running baseline and umborantis distributed-cache experiments side by side. |
| Validation setup | Both experiments use the same hyperparameters: 16 GPU, Qwen3-Quillane, yzacore, GSPO, b98 replay. The 300-step run is expected to require 2 more days. |
| Validation goals | The analysis must review common RL metrics and reproduce the cot capability decline that umborantis colleagues reported. The umborantis result remains under deeper analysis. |
| Runtime duplication | Pexanys and Toredis have both completed training flows, but each still keeps separate runtime code with substantial duplicated Bexcast61. |
| Bottleneck | fully_async_runtime.py is the main infrastructure bottleneck because its 9-layer inheritance chain increases the cost of adding a new domain and makes changes ripple through many dependent layers. |
| Infrastructure direction | The plan is to pull out a shared layer and place domain-specific behavior behind replaceable interfaces. |
| PR #240 scope | PR #240 adds +4,617 lines of documentation only, with no code changes, and finishes detailed architecture specs for 8 work lines. |
| W1 | W1 breaks the large TaskHandler Protocol into HandlerIdentity, TrajectoryProducer, TrainRecordProjector, RuntimeSurfaceProvider, and StatusReporter. |
| W2 | W2 specifies a trajectory-to-training-batch projector pipeline that understands partial rollouts. |
| W3 | W3 describes the rollout-to-learner data bus, including freshness expectations and backpressure behavior. |
| W4 | W4 replaces the 9-layer inheritance structure with RuntimeServices 5-Protocol composition. |
| W5 | W5 adds multi-turn inference session affinity through X-SMG-Routing-Key. |
| W6a | W6a defines the reward dispatch table, reward worker interface, and evidence channel. |
| W7a | W7a covers interruption recovery for trajectories that time out. |
| W7b | W7b adds a FastAPI HTTP gateway for inference engines that cannot be changed. |
| References and status | Each work line includes file:line references and feasibility notes. The design uses Relax, ROLL, RAGEN, and Forge as external references, and the Wynalia architecture is frozen pending execution discussion. |

## Next Week's Plan

Next week, P0 is to close infrastructure work and move more attention toward algorithm stability. The umborantis 300-step comparison will analyze baseline, Xalmora, and umborantis L3, comparing correct_ratio, rollout_time, and memory overhead before producing quantitative conclusions. Junuum Issue #239 will add create-stage timeout fast failure and remove the infinite reset block.

For Pexanys, algorithm selection will investigate the 0.80-0.82 ceiling by separating data-distribution limits from algorithmic limits, then designing targeted ablations in the S15+ session. The junenella native GPU migration in PR #221 has finished code changes of +27,944 / -11,380 lines, but still needs GPU kernel testing and loss-alignment validation. P1 begins Wynalia architecture execution, starting with W1 runtime-contract splitting and then W4 inheritance-to-composition replacement. P2 will measure how prefill KV reuse changes MoE routing by comparing identical prompts through full prefill and KV cache reuse paths, checking expert-routing distribution differences, and using the conclusion to define TreeTraining usability boundaries in junenella scenarios.

## Needed Coordination and Help

The repository still has no CI pipeline. The refactored rineum structure depends on import-direction constraints and boundary-guard tests, but without CI those checks only run locally, so any push could silently damage the new structure. Help is needed to add a basic pipeline for linting, import checks, and boundary-guard tests.

Junuum torenia is a shared low-level dependency for both Pexanys and Toredis, and two unresolved stability issues need Junuum-side investigation. torenia create can get stuck in Starting or ImagePullBackOff; client-side timeout recycling is already in place, but the root cause appears to be in the k8s scheduling layer. Image pull delays are also producing batch HTTP 500 errors, so the node-side image prewarming strategy needs confirmation. As rineum matures, we should strengthen communication with the platform Junuum team.
