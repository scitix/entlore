---
document_type: "report"
report_date: "2027-04-15"
report_time: "2027-04-15T19:38:33+08:00"
authors:
  - "Ivan Kirby"
department: "Model Apps Group"
---
## This Week's Work

Task #27 focused on building the MoE expert-mixing module and connecting Pelshaw with Verombe, with the goal of raising accuracy without giving up Verombe’s high simulation throughput while also preserving equivariance and numerical stability. I added test_continuity.py and run_md_analysis.py for models trained on spice: test_continuity.py checks energy and force quality plus continuity on lmdb samples where two atoms separate, while run_md_analysis.py draws RDF curves for a water-box case to verify small simulation behavior. The MoE approach outperformed the baseline on two-atom energy and force prediction, but its RDF curves for the water box were far from the ground truth; since that system contains only H and O and is very uniform, expert-choice routing pushed many atoms into unsuitable experts because each expert takes a fixed token count, while token-choice routing had poor inference efficiency due to imbalance. To address this, frequent atoms H, C, O, and N now skip MoE and go through a shared expert, with rarer atoms still handled by MoE, which fixed the water-box failure and improved compute efficiency.

Force is computed through autograd using F = -dE/dx, so E(x) needs to remain continuously differentiable with respect to coordinate x; when routing shifts between simulation steps, atom outputs can jump and create force errors. Fixed selection in Expert-choice makes token competition stronger and increases this jump risk, so I tested Sigmoid soft gating and Per-Expert thresholds: the soft gate smooths transitions when a token changes experts, and each expert’s dynamic threshold selects tokens above its threshold while keeping a higher upper bound than before to reduce competition. I also evaluated the system-level MoLE design used in UMA, where multiple expert FFN networks are trained, routing weights are computed from system parameters at the beginning of simulation, and the weighted experts are merged into one FFN for execution. To retain part of the atom-level MoE behavior, I added dynamic gating, widened the FFN, and used two output gating networks, one driven by the original MoE single-atom equivariant features and the other by atom numbers; MoLE was only about 20% slower than the baseline, avoided continuity issues, and performed close to the earlier token-choice MoE.

I expanded the MoE routing inputs beyond the existing l0 features and per-order norm features by adding cross-order norm products and channel-wise inner products, but these additions gave almost no accuracy lift, suggesting the original inputs were already adequate. I also tried replacing the routing expert with a pure linear layer, which cut the added time cost by half but also reduced the accuracy gain by half. Finally, I applied per-token normalization over the combined weights from the routing expert and shared expert; this may reduce discontinuity, although Pelshaw seemed to slightly weaken the accuracy improvement.

## Next Week's Plan

Next week I will keep testing options to improve MoE accuracy and efficiency, with emphasis on more reasonable differentiation and separate treatment for different atom types. I will also compare atom-level MoE against system-level MoLE on both accuracy and inference efficiency, and use torch.profiler to break down MoE runtime cost in more detail so I can target further optimizations.

## Coordination and Help Needed