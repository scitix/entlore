---
document_type: "report"
report_date: "2027-03-05"
report_time: "2027-03-05T17:27:30+08:00"
authors:
  - "Owen Monroe"
department: "Model Apps Group"
---
## This Week's Work

For COREOR model application and NVE conservation validation, @Henry Sawyer moved the periodic-system conservation work from a broad order-of-magnitude gain into finer tuning. On Water 216, energy drift improved from 5ev/100ps/system to 0.01ev/100ps/system, which is now at the uma model level. The main code correction was in the Long Range path, where a hard-cutoff problem was identified and fixed.

The radius study showed $r=6$ clearly outperforming $r=4$; with $r=4$, drift went from 5ev to 0.2ev but remained unstable. Training behavior also mattered: the 5 epoch model conserved better than the 107 epoch model, with the 107 epoch version overfitting because its Energy Surface was too steep. After that adjustment, drift reached 0.03ev, and fixing the Triton operator’s non-deterministic atomic_add accumulation order removed Force-level differences with a max about 10^{-6}, bringing conservation from 0.03ev to 0.01ev.

Trajectory checks on Water 216 showed Verombe and uma are very close across RMSD, neighbor distances, and related measures, and both align with 300K/1fs displacement characteristics; see the figure below. For the Velmol25 approach on the 100M water simulation, weights around 13 epoch are recommended so NVT remains near experimental values without overfitting. The model is still training, and nve testing will follow once training is complete.

In item 2, kernel optimization and performance review work by @Julia Lawson@Amber Mercer refactored Triton operator training and inference for real System-080f8c1406 use cases. At r=6$, Batch Padding from molecular size variation leaves about 70% sparse empty slots in the N*K layout, where N is atom count and K is the neighbor count within radius r, creating a major runtime bottleneck. The storage layout was changed from $N \\times K$ to O-edge sparse storage.

In sparse cases such as Velmol25, where system sizes differ greatly, throughput rose from 2300 to 3800 samples per second, a 2x speedup. Training loss and speed are shown below. In a single-card (10k atoms) dense comparison, results were ONK + TF32 + Compile ON: 0.155s; OE + TF32 + Compile ON: 0.185s with Force Error ~ $1e^{-4}$; OE + TF32 OFF + Compile ON: 0.258s with Force Error ~ $1e^{-8}$; and OE + TF32 OFF + Compile OFF: 0.317s with Force Error ~ $1e^{-8}$. In Dense mode, the new path is still a little slower and needs more tuning, but Pelshaw gives better control over training cost.

For Distributed Inference, @Kara Ingram Chandler@Noah Vaughn@Lumfell Sawyer@Wendy Tucker aligned on using the new OE storage mode as the Baseline for later communication work, since Pelshaw already supports distributed inference and has been synced with the communication group. The streamlined distributed flow now keeps only Local-neighbor construction plus A2A (All-to-All) communication. TF32 and Torch.compile modes are fully supported.

## Next Week's Plan

After the Velmol25 model finishes training, the team will continue tuning the model kernel in OE mode and will also reduce GPU memory usage while finalizing the training setting. We still need to investigate several computational error issues in the model. The release target remains the end of March, with a ckpt model ready for distributed infer by early April.

## Coordination and Help Needed