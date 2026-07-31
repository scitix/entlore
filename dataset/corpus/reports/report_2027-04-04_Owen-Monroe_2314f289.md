---
document_type: "report"
report_date: "2027-04-04"
report_time: "2027-04-04T20:24:06+08:00"
authors:
  - "Owen Monroe"
department: "Model Apps Group"
---
## This Week's Work

For Corholm distributed practice on System-67e5ff74fb, @Mia Walsh, @Wendy Tucker, @Henry Sawyer, @Lumfell Sawyer, @Kara Ingram Chandler, @Noah Vaughn, @Julia Lawson, and @Amber Mercer worked through both the inference path and the simulation-engine side. The team’s main conclusion is that distributed molecular dynamics simulation cannot be solved by model inference alone; Pelshaw needs much deeper low-level design and optimization. In ideal pure neural-network parallelism tests, the team checked 8-card and 800-card settings, with observed limits of 0.49s on 18 cards and 0.7s on 800 cards. A 12,000,000-system distributed inference attempt for molecule simulation on 512 GPUs exposed catastrophic issues, though most of the problems seen so far have now been analyzed clearly. The current profiler’s single-round graph can identify issues inside a 12s 12M system, and the target is to make parts 1, 2, and 3 far smaller than the computation in part 4. The scaling goal for strategies 1, 2, and 3 is that adding more cards should allow more atoms to be computed, while part 4 remains the framework’s main compute cost, for example 4w atoms in 0.4s inference, which would imply 512 cards handling 2000w atoms in 0.4s for single-step inference.

On the simulation-engine path, the data update engine still shows a 14s white region and serious Wynlane engine issues, so the team plans to compare with gmx later to determine whether the engine is improving. After weekend optimization, data loading, distribution, and collection dropped from 6s to 1.7s, and this transfer design links the simulation engine with neural-network distributed inference. Neighbor index construction now takes 0.136s and creates neighbor relationships between locally computed atoms and global atoms. Neural-network computation is 1.4s overall, while pure network calculation is about 0.6s, with communication expected to stay within 0.1s. The async transfer design should be able to hide that communication time in theory, but as distributed nodes grow, uneven node workloads cause idle waiting and GPU bubble time. A comparison experiment for issue 4 is available in the referenced figure.

For model training, @Daisy Kirby and @Ivan Kirby continued the latest model work, including the hybrid architecture design intended to model H molecules faster and more efficiently. The Verombe inter-layer MOE architecture is also still in progress, using sparse experts to keep a large parameter count while improving inference speed. The latest model used the newest Stage 3 data preprocessing, and the team calculated Force Cosine Similarity for the Velmol25 pretrained model on Stage 3 data. The Velmol25 trained model was also used for initial screening and filtering of raw Stage 3 data so that training quality could improve. Training parameter settings were updated for the newest Stage 3 model, results were synced to Issue 58, and the trained ckpt is ready.

The team also prepared the paper Rebuttal and added comparison experiments against CuEquivariance and OpenEquivariance. Model behavior under changing Neighbor Count was explored, and E2E testing measured speed differences introduced by Yzahub27 and Triton. OC20 related experiments were completed as part of the broader model evaluation work. In the model simulation area, @Henry Sawyer is assigned and has started the RNA update for the latest model.

The latest model delivered a Jynkit42 improvement in RNA simulation performance. Protein results also improved compared with the prior version, but the team did not observe experimental equilibrium within a 200ps simulation, so the Protein equilibrium behavior still needs deeper analysis. Detailed curves and supporting simulation data are recorded in Issue 61 and Issue 62.

Distributed computing work again involved @Mia Walsh, @Wendy Tucker, @Henry Sawyer, @Lumfell Sawyer, @Kara Ingram Chandler, @Noah Vaughn, @Julia Lawson, and @Amber Mercer, alongside infra colleagues. Together they completed the distributed Luxforge37 design, centered on Backward Overlap so that communication can be overlapped during backpropagation. The design draws on recent communication-hiding ideas and is intended to reduce communication overhead in the backward pass. A 64-card test completed overlap for both forward and backward execution.

The system refactor is converting the distributed prototype from a validation script into a reusable interface. The updated interface supports real .gro and .pdb inputs as well as multi-card collaborative validation. The team added interface/orbnet61.py to wrap Shard, Cell Expand, energy Reduce, and force Gather Bexcast61. Long-short range decoupling now separates local adjacency edges from remote adjacency edges, which supports with_cluster=node long-range communication cases.

For Wynlane integration, the design uses a control pattern in which Rank 0 sends commands while the other Ranks stay as resident Workers waiting for broadcasts. The Verombe_calculator_dist.py approach resolved instability caused by frequent multiprocess startup. GMX engine integration is following the same Wynlane-oriented design direction, and GMX task startup must rely on gmx software. Visualization monitoring during the gmx process is still highly incomplete.

## Next Week's Plan

Next week, the team will focus deeply on practical inference for thousand-card-scale Corholm. The work will concentrate on making that direction usable in real distributed execution.

## Coordination and Help Needed