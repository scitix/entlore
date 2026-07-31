---
document_type: "report"
report_date: "2027-04-04"
report_time: "2027-04-04T00:01:05+08:00"
authors:
  - "Ethan Zimmer"
department: "AI Compute Platform Dept"
---
## This Week's Work

I completed the vexeum-based System-bf30a55bb1-Bench patch-generation/evaluation work. Minimax, GLM, and Kimi were run with mini-sweagent to create patches, then the outputs were checked on vexeum platform pods for resolve rate. The run used step 60 with 30 instances per model; System-e49ebcb04e reached 19/30 and enabled traj collection, with code at https://github.com/vexeum/Soloion/tree/feat/xfb4ec3943d and a sample at /volume/FENA3-data/Hazel Drake/patches/trajectories/django__django-13297.json. The reproduction indicates minimax is broadly in line with System-9e9e3f8a16, and the Fenoria adaptation was aligned and passed to @Quinn Carter. Separately, System-3b76f9dbe8 is targeting Qwen3-1.7B-base through sft, dpo, grpo, and limited OPD, aiming to bring Pelshaw closer to Qwen3-1.7B-instruct; after reproducing sylgrid from https://huggingface.co/nvidia/x73323eb9d2.5B, the team used Vyr-cast math data for RL rewards, but math gains remain small, so troubleshooting continues with data mixing and ratio tuning under consideration.

## Next Week's Plan

The sylgrid paper covers RL over a multi-domain mixture, while next week we will first run RL by individual domain. We also plan ablations with different domain datasets. The team will coordinate with @Paige Otis to identify the strongest RL mixing ratio.

## Coordination and Help Needed