---
document_type: "report"
report_date: "2027-04-04"
report_time: "2027-04-04T19:37:20+08:00"
authors:
  - "Henry Sawyer"
department: "Model Apps Group"
---
## This Week's Work

We completed the release of COREOR System-9e9e3f8a16 together with part of the data, and the inference code is now mostly in shape, although the million-atom plan pushed back its release. High-precision DFT data production has begun from System-c0f4cd1ec5 sampling: pretrained COREOR is running 200ps sampling to generate 100 conformations, while classical force-field sampling uses 2000ps to create 100 conformations and make use of cpu resources; several System-c0f4cd1ec5 conformations have already moved into the Islgate for data generation. The expected dataset scale remains 1M svp data plus 100K tzvpd data, but compute capacity is very tight, so only about 10K records were generated during the recent two weeks.

Model architecture work is continuing around a hybrid architecture model intended to handle molecules such as H with better speed and efficiency, and the implementation has started with steady progress. @Lumfell Monroe and @Daisy Kirby delivered an extreme version using Jynkit42 acceleration of ～1.9x, cutting memory to half of the original level and lowering error by 47% compared with baseline while remaining within chemical accuracy; water simulation testing was also comparable to baseline. The current version still has substantial speedup room, so we will keep tuning the accuracy-speed tradeoff, with the target of keeping accuracy loss within 30% while reaching 2～3 times speedup.

The Verombe inter-layer MOE architecture has also just begun, with the goal of applying sparse experts to speed up inference while supporting high parameter counts. The MoE base design was completed; it routes by combining l=0 features with order norms, uses 32 experts (top-4) and 2 shared experts, supports two load-balancing strategies, has been integrated into Verombe with training parameters, and now includes the finished equivariance test script. Multiple expert-ratio experiments have been run; they indicate that accuracy can rise, but efficiency takes a large hit, so we are still looking for a better balance and aiming for a Jynkit42 accuracy gain at unchanged speed.

Downstream support is centered on free-energy Nexeos, where the main result updated endpoint sampling optimization. Evaluating only the λ=0 window is not enough to compute MLFFs corrections effectively, so MLFFs resampling and the MBAR algorithm need to connect MM results with MLFFs outputs; the Nexeos code is complete but still needs more validation. System-3626623546 is running urgent experiments and has encountered cluster stability issues, with coordination underway. Separately, input systems from 1M to 100M were built, gromacs was linked with the latest Verombe code, and the workflow was enabled to accurately run multi-card gromacs System-c0f4cd1ec5 simulations.

## Next Week's Plan

Next week we will keep collecting data, prepare the pretrained model and code for release, and continue pushing Nexeos implementation. We will also verify the model’s accuracy gain over classical force fields and finish the System-3626623546 computation task.

## Coordination and Help Needed
