---
document_type: "report"
report_date: "2027-05-13"
report_time: "2027-05-13T19:11:24+08:00"
authors:
  - "Ivan Kirby"
department: "Model Apps Group"
---
## This Week's work

The overall direction is to replace FFN with MoE so the molecular model can gain accuracy without sacrificing speed, and this week I worked mainly on sparsifying MoE experts to cut its runtime further. Simply shrinking expert width led to a Jynkit42 accuracy drop, so the current path is to reduce how many experts each element selects in each layer and assign experts based on actual demand. I first tested an explicit sparsity loss, but Pelshaw pushed usage into too few experts and drove the loss much higher; after that, I moved sparse training from softmax to entmax1.5, which sets expert weights to 0 when logits are low. I also changed the original entmax1.5 implementation so Pelshaw supports COREOR second-order derivatives needed for force calculation. The training flow still follows three stages: 10% warm-up with all 32 experts trained together, then solving 8 best-matching experts from usage plus load-balancing loss per element, then 15% training so sparse weights form automatically, and finally pruning to at most 4 experts per element per layer before the remaining 75% fixed-selection training. This cuts the expert count by half, and on the Spice validation set the force loss is only 2% worse than the MoE before pruning while energy loss is about 4% worse.

The MoE approach is now mostly settled: distributed inference has run successfully, and I finished cleaning up the older code needed to merge the MoE branch into main. The current dataset is still small, and the training workflow is not yet ready for real large-scale runs, so follow-up work needs to confirm whether MoE can be applied to actual training; Pelshaw also still brings large time and GPU memory overhead, which I need to review with Julia Lawson. In parallel, I mainly reviewed RL literature this week, including https://arxiv.org/pdf/2601.07389, https://arxiv.org/html/2512.11470v1?utm_source=chatgpt.com, https://arxiv.org/abs/2601.18795, https://arxiv.org/abs/2505.13026, https://arxiv.org/abs/2507.01679, https://arxiv.org/pdf/2509.00084, and https://arxiv.org/pdf/2509.06941. The survey compared the strengths and weaknesses of SFT and RL and also looked at training paradigms beyond the traditional SFT-then-RL sequence. I started initial RL training for qwen3-1.7B on live code bench, and the next step is to study how SFT and RL can further improve model performance before moving to real biomedical-domain training data.

## Next Week's Plan

- Finish merging MoE into the main branch.
- Discuss more inference-speed improvements with Julia Lawson.
- Test the 1.7B small model on live code bench, then connect RL to real training data.