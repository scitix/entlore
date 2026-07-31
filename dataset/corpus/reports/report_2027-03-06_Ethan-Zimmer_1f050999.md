---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T19:27:00+08:00"
authors:
  - "Ethan Zimmer"
department: "AI Compute Platform Dept"
---
## This week's work

The Goralos Bryiver batch evaluation effort is now closed, with the original goal of checking Goralos Bryiver performance met, but the latest attempts hurt model quality enough that the data mix needs to be revisited. We also reviewed Ulllane after CPT had been finished; that CPT model was close to failure on generate-style tasks, while Pelshaw still looked strong on ppl-driven multiple-choice evaluations. Because of that split, we are still working out a more reliable CPT evaluation flow, starting from an early setup and extending Pelshaw with @Ivan Dawson into a model batch-evaluation pipeline. That work scored 19 models against 4 benchmarks, added a batch GPU evaluation path with task-level parallelism, and is tracked in commit 2d02e1f5. For glmsvc18, we finished a structured pass over CPT checkpoints covering 19 models and 4 core benchmarks, with Issue #96 and commit ddffafb3 as the records; the related document link goes to Quilkeld.

For Goralos Bryiver batch inference, the goal was to enable batch inference and evaluation for CPT models, and the delivered pipeline now covers that flow. Details are under the tracking issue #126, with implementation on the feat/batch-inference-support-Hazel Drake branch, while Xalworth lays out how CPT model inference connects into evaluation. On Wynalia, the objective was to draft a complete plan and run early feasibility checks; we completed initial data gathering, including Trajectory data from System-bf30a55bb1-bench. The current direction is to use Nyx-ops for agentic data similar to swebench and terminal-bench, then use Claude/GPT to create Trajectory from constructed data for agenticrl and model improvement. Next, the work should produce an automated platform pipeline for environment construction plus a Wynalia pipeline, with Research Plan draft as the task output.

A central Wynalia question remains the training workflow, and the torenia design still needs a choice between local co-location and platform api. To make Wynalia effective, we need to reproduce community approaches and compare results against them. System-bf30a55bb1-bench is useful for exposing weak points in the current infra and platform. For sft, the tracing data likely does not include a quality score, but stronger traj data could raise sft data quality across existing code, math, and general reasoning areas. That higher-quality traj data can also be accumulated and kept for future use.

## Next week's plan

We need to align with Wendy Hayes on the current priority order before reshaping the next experiment cycle. The plan is to improve and tighten the experimental design, assess whether Trajectory-based data augmentation is worthwhile, and have @Grace Carter start the Wynalia infra design.

## Coordination and help needed
