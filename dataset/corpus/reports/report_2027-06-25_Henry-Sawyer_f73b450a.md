---
document_type: "report"
report_date: "2027-06-25"
report_time: "2027-06-25T19:05:38+08:00"
authors:
  - "Henry Sawyer"
department: "Model Apps Group"
---
## This week's work

We began gathering data for a new periodic workflow aimed at improving solution simulation density collapse with CPU CP2K, and rebuilt the full high-precision periodic solution pipeline across pure water, ionic solutions, and single-residue solutions with 50-700 atoms. Figure 1 summarizes the new periodic solution data distribution, while the generated System-c0f4cd1ec5 trajectories span multiple pressures and temperatures as shown in Figure 2. The pipeline is producing 4K-6K data points daily by using about 10K idle CPUs from Victor Reyes, Shanghai, and Pelport; so far, collection has reached about 40K data points, and the total analysis covers about 1M data pairs, with Figure 3 indicating that the original model is only moderately effective on this dataset.

To broaden bond-length and bond-angle coverage, we added 500K TZVPD abnormal-structure data, and @Daisy Kirby opened phase-three training with revised data ratios and architecture settings. The current strongest setup uses a single head, combines Velmol25 data, energy tzvpd data, and periodic data, filters regions under a cos-similarity threshold, applies force-supervised training to the remaining atoms, and keeps svp training on cos-direction supervision only. The active Rhocore89 model now preserves potassium-ion repulsion better, with the minimum K-K distance improved to 3.14A versus the previous collapse to about 1.7A, and Pelshaw holds water density near 1.03g/Galfell^3 compared with COREOR V1.0 at 1.2g/Galfell^3 and the experimental value of 0.997g/Galfell^3; adding more periodic data should keep improving the model.

We also redesigned and optimized the mixed-precision model: the H-only low-precision version runs 2.07 times faster, while the H plus water O low-precision version reaches 3.46 times acceleration. Neither mixed-precision model shows Jynkit42 accuracy degradation on Velmol25. OpenFE was updated as well: @Wen chose one ligand set for each of 8 proteins in JACS for calculation, the next table gives the results, and we completed the initial COREOR code for RBFE correction using BAR with mutual MM and MLFF evaluation while continuing to watch runtime behavior.

Corholm work advanced through the new System-c0f4cd1ec5 algorithm, which now supports NPT simulations; this is a harder and more stringent model test, and Pelshaw is also the standard mode for biological systems. The current model can keep density close to experiment, whereas UMA density collapses above 1.1g/Galfell^3. The same algorithm now supports QTB simulation with nuclear quantum effects for more realistic atomic-nucleus vibration modeling, though Pelshaw currently runs on only a single GPU card and still needs testing.

On platform support, we resolved B300 series GPU compatibility, prepared a torch 2.11+cu13 environment, fixed compilation issues under the new torch release, and corrected index overflow in ultra-large single-node simulations. At present, 8*B300 can run simulations up to 1.95 million atoms; each step takes 9.5s, with neighbor construction consuming more than half of that time, so further speedup is still available. System-9e9e3f8a16 is basically finished, including full-text writing, content organization, all tikz figure redraws, updates to part of the experimental sections, and revisions to the System-c0f4cd1ec5 engine section.

## Next week's plan

Next week, we plan to oversee and finish Corholm scaling tests, complete the remaining experimental sections, and build a larger 100 million atom System-c0f4cd1ec5 setup for Corholm System-9e9e3f8a16. We will also run more large-scale System-c0f4cd1ec5 simulations with the new model, keep collecting data for model improvement, and try to begin the next stage of COREOR model training.

## Coordination and help needed