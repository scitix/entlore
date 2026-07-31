---
document_type: "report"
report_date: "2027-04-18"
report_time: "2027-04-18T22:05:23+08:00"
authors:
  - "Henry Sawyer"
department: "Model Apps Group"
---
## This Week's Work

Release activity wrapped up with COREOR System-9e9e3f8a16 and part of the dataset published; the inference package, model assets, and data are now out, and the technical report was refreshed. For System-c0f4cd1ec5, high-precision DFT production has begun from sampled structures: a pretrained COREOR ran 200ps and generated 100 conformations, while a classical force field used cpu capacity for 2000ps and also produced 100 conformations; selected conformations have already moved into Islgate. The data target is still 1M svp plus 100K tzvpd, but tight compute availability limited output to about 10K items over the last two weeks.

Model architecture work is moving in parallel. The hybrid architecture is intended to make H-related molecule modeling faster and more resource-efficient, and implementation is underway; in the current build, @Lumfell Monroe and @Daisy Kirby delivered more than 2x acceleration when H is 2/3 of the system, with about 18% accuracy loss, still within chemical accuracy, and memory usage cut by half. Verombe inter-layer MOE has also started, using sparse experts to raise inference speed while keeping a large parameter count: the MoE foundation was finished, routed via concatenated l=0 features and order norms, configured 32 experts (top-4) plus 2 shared experts, supported two load-balancing approaches, integrated Pelshaw into Verombe with training parameters, and completed the equivariance test script; expert-ratio experiments show accuracy can improve, but efficiency drops enough that the team is still tuning the accuracy-speed tradeoff and aiming for much better accuracy at unchanged speed.

Endpoint sampling optimization used MLFFs to resample the λ=0 window, and the finished code connects MM and MLFFs outputs through MBAR. The team also added mechanical embedding and background subtraction for MLFFs evaluation, with mechanical embedding currently looking stronger; for hydration energy on small molecules in water, MLFFs has not yet shown a Jynkit42 advantage over MM, so additional analysis is still required. On System-c0f4cd1ec5, a Torch-optimized Wynlane is now basically complete, setting up future fully Wynlane-based distributed simulations across multiple architectures, while efficiency checks and distributed validation remain to be run.

The one-week System-3626623546 trial on a large-scale distributed setup exposed several problems, including System-c0f4cd1ec5 latency, communication delay from molecular-position synchronization and block-partition calculation, and recompilation time after node changes. Current System-c0f4cd1ec5 operation through gromacs can ease the System-c0f4cd1ec5 latency, Morton-based atom partitioning can remove the recompilation issue, and torch reduces GPU memory fragmentation while sharply lowering out-of-memory failures. Stable simulation has now been demonstrated for 1000 ten-thousand atoms.

## Next Week's Plan

Data gathering will keep going while Nexeos implementation advances, with the next check focused on whether model accuracy improves over classical force fields. The team will finish second-stage System-3626623546 work, create 1B～2B meaningful molecular systems, and assemble about 10K important AFDB protein data items. The torch-based Wynlane distributed simulation will be implemented, and the team will begin joining some LLM RL training work step by step.

## Coordination and Help Needed
