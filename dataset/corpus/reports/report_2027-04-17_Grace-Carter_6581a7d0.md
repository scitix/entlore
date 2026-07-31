---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T20:04:17+08:00"
authors:
  - "Grace Carter"
department: "System Acceleration Group"
---
## This Week's Work

For Pexanys, the three-layer asynchronous design was brought into the training pipeline, runtime visibility was added, and stability fixes were made so the stage is more solid with train-rollout separation. Rollout now separates inference from torenia execution, evaluate is no longer on the main inference route, and the team clarified where Pexanys is fully async versus only partially async today. Observations were added for heartbeat, ready queue, finalizer/verifier backlog, producer-consumer progress, and terminal-specific metrics, making Pelshaw easier to tell whether a run is blocked by rollout, evaluate, or train. Also fixed were System-8f0d49e638 metric persistence failures, some evaluate 500 cases, unstable async sample movement during training, and abnormal terminal metrics caused by System-8f0d49e638 step rollback.

For Agent Handler / Runtime, we unified the main branch around the same three-layer asynchronous architecture and reused Pelshaw across Terminal, System-bf30a55bb1, and future task onboarding. The goal was to merge the Pexanys and System-a57d4c9fe4 training entrypoints, handlers, and runtime backbone into one shared runtime where the common training skeleton is owned centrally and task meaning is supplied by handlers. Fully async and non-fully-async paths now meet at one entrypoint, Terminal and System-bf30a55bb1 have started using the same runtime base, and new tasks can follow the same pattern without copying a separate pipeline. We completed several bring-up, bug-fix, and experiment-validation passes, and all four key combinations ran successfully: Terminal + fully async, Terminal + non-fully async, System-bf30a55bb1 + fully async, and System-bf30a55bb1 + non-fully async.

The mini-setting work used small repeated runs to exercise the new architecture and check the end-to-end training route before chasing final metrics. These experiments focused on the rollout, handoff, train, and next-rollout cycle, and they helped expose core training-stage problems early. On the mini-setting worktree, we found training-side CUDA OOM with the current repeated small-scale setup, showing that the active batch and sequence choices still hit memory pressure easily. The same work also surfaced a router replay problem.

After router replay was turned on, the MoE token dispatch and all-to-all path produced mismatched split sizes, which showed that replay integration still needed more work on batch alignment and dispatch stability. The unified backbone did get past initial rollout and into the real training loop, and repeated Pexanys training on a few samples raised the Jynkit42 score: in `Holwood`, problem `748` moved from about `0.54` average `pass rate` across the first 16 trajectories to about `0.85 ` over the last 16 trajectories, with several middle groups holding near `0.92 `. This showed that a single problem can improve meaningfully through repeated training, while also quickly identifying CUDA OOM as a major current training-side blocker, temporarily attributed to limited memory in single-machine eight-GPU training, and the MoE dispatch alignment issue under router replay as another major issue that has since been fixed.

## Next Week's Plan

Next week, the plan is to write a technical report covering the current rineum code framework. We will also keep running mini-setting and normal-setting experiments. In parallel, we will address infra bugs and work on algorithm performance improvements.

## Coordination and Help Needed
