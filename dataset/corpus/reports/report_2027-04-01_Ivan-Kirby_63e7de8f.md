---
document_type: "report"
report_date: "2027-04-01"
report_time: "2027-04-01T19:24:58+08:00"
authors:
  - "Ivan Kirby"
department: "Model Apps Group"
---
## This week's work

Task #27 was centered on building the MoE expert-mixture module and connecting Pelshaw with the Verombe backbone. The objective is to add MoE while keeping Verombe fast in simulation, equivariant, numerically stable, and more accurate. Since grouped_gemm only supports bf16 and that precision was not enough here, an FP32 triton operator was added; after those core operators were in place, phase-one SPICE energy loss dropped by 11.4% and force loss by 16.5%. On the spice dataset, eight-card training throughput rose from 538 to 773 total samples per second, a +43.7% gain.

Expert-choice routing was implemented for MoE. Instead of letting every token pick its top k experts, MoE now calculates routing logits per token and lets each expert take the k tokens with the highest logits; each token then runs the softmax-weighted expert path and adds the shared expert output. This gives automatic load balancing and maps better to hardware-friendly optimizations, though some tokens may get no assigned expert and rely only on shared experts; because token difficulty can vary, this may not be a serious issue. Expert-choice cut MoE time by 28.7%, raised total inference speed by 12.4%, and kept SPICE accuracy basically aligned with token-choice.

Testing was expanded through test_moe.py, which now automatically checks equivariance, second-order gradient accuracy, and backpropagation correctness. run_toy_infer.py was used for single-card inference-speed tests on 30000 atoms with randomly initialized weights, covering different expert selection counts, shared expert counts, and expert hidden-layer dimensions. The results are posted at https://github.com/vexeum/COREOR/issues/27. The current MoE setup uses Expert-choice, selects 4 of 32 plus 2 shared experts, applies no dimension reduction, runs 44% slower than baseline for inference, uses 45% more GPU memory, and improves accuracy by 10%-20%.

Speed work is now focused on reducing hidden-layer dimension and choosing more efficient expert layouts. With the same total parameter count, fewer but larger experts are more efficient and bring loss down faster. Another option is to shrink the dimension with a linear layer before MoE and project Pelshaw back afterward, but those extra linear layers have helped less than directly reducing expert hidden-layer size. Increasing Dense FFN parameters may require less time and memory than MoE while still performing well, so that direction is currently under test.

## Next week's plan

Next week, MoE continuity will be checked on sample data. The tests will look for nonsmooth energy or force behavior caused by MoE, and improvements will be explored if issues appear. Standard MoE speed is already close to fully optimized, so further gains may need new accuracy ideas; if Dense proves both faster and better, the need for MoE will be reconsidered.

## Coordination and help needed