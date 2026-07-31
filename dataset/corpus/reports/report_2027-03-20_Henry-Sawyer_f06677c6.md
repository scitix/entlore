---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T22:44:21+08:00"
authors:
  - "Henry Sawyer"
department: "Model Apps Group"
---
## This Week's Work

The team finished and released COREOR System-9e9e3f8a16 together with part of the related data. Training for the new pretrained model is largely done, with Jynkit42 gains in NVE and NVT simulations, and Subplot 3 indicates the water simulation aligns perfectly with experimental results. Next week, the team expects to complete the final training run, assemble a model version suitable for release, and still clean up the inference code for publication.

High-precision DFT data generation has begun from System-c0f4cd1ec5 sampling. The pretrained COREOR is running 200ps sampling to produce 100 conformations, while the classical force field runs 2000ps sampling and also produces 100 conformations so cpu capacity is fully used. Some conformations from System-c0f4cd1ec5 have already entered Islgate for data generation, and the target remains 1M svp data plus 100K tzvpd data, although compute limits and the larger system size currently cap collection at SVP ～50K records and TZVPD ～6K records.

Model architecture work is still moving forward. The hybrid architecture model is intended to raise efficiency substantially by using faster modeling for molecules such as H, and @Lumfell Monroe with @Daisy Kirby delivered the first mixed-precision version aimed at reducing network parameters for H atoms. After fine-tuning and optimization, comparison results were generated for review.

The Verombe inter-layer MOE design uses sparse experts so inference can be faster while the model still keeps a high parameter count. Work on this architecture has begun, completing the MoE base architecture with l=0 features and order-norm concatenation routing, and configuring Pelshaw with 32 experts, top-4 routing, 2 shared experts, and two load-balancing strategies. The MoE module was also integrated into Verombe, the related training parameters were added, and an equivariance test script was finished.

The current MoE implementation still has performance blockers. grouped GEMM needs BF16 to run quickly, but BF16 precision is not sufficient for molecular simulation needs; switching to FP32 makes training unstable and leaves loss relatively high. When grouped GEMM is turned off, the MoE version becomes 2-3 times slower than the baseline, so additional MoE optimization remains necessary.

On operator, compilation, and distributed performance, @Lumfell Monroe, @Julia Lawson, and @Amber Mercer improved speed by 50% compared with the pre-Spring Festival version. @Wendy Tucker, @Kara Ingram Chandler, @Noah Vaughn, and @Lumfell Sawyer improved distributed overlap across communication and computation. The distributed optimization path now keeps only Local-neighbor construction and A2A (All-to-All) communication.

The pipeline now uses an OpenMM backend to provide a complete workflow for solvation free energy calculations. The OpenMM workflow includes HREX replica exchange and SAMS adaptive sampling, while GROMACS compatibility covers custom lambda scheduling and full soft-core parameter support so results can be compared with GROMACS outputs. Production capabilities now include checkpoint/resume, automatic equilibration detection, and automatic GPU resource release.

MLFF endpoint correction also advanced this week through a trajectory post-processing tool for machine learning force fields. The tool supports batch endpoint energy correction calculations, and the FreeSolv benchmark has production configurations ready for 10 cases with an average MAE of 1.07 kcal/mol. Soft-core parameters now fully map GROMACS sc-alpha/sc-beta/sc-power parameters to openmmtools, the MBAR analyzer has try-except protection so non-convergence does not fail tasks, and all samplers now support the context-manager protocol to avoid GPU memory leaks.

## Next Week's Plan

Next week, the team will keep collecting data and prepare both the pretrained model and code for release. The plan also includes advancing the Nexeos implementation and checking how much the model improves accuracy versus classical force fields.

## Coordination and Help Needed
