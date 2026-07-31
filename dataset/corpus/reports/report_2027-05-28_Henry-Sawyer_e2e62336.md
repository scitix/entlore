---
document_type: "report"
report_date: "2027-05-28"
report_time: "2027-05-28T17:58:15+08:00"
authors:
  - "Henry Sawyer"
department: "Model Apps Group"
---
## This Week's Work

The team created abnormal-conformation data to reduce ion-collapse behavior seen in COREOR v1 simulations, covering compressed, elongated, and torsional structures for water, ions, DNA/RNA, and proteins. Over the recent two weeks, 500K data was gathered and has already been folded into Kevkit training. For Dorbrook, the team also assembled the required macromolecular input system, selecting a subsystem with a 10.3 M atom T4 bacteriophage gp5 spike protein trimer, E. coli K12 LPS membrane, and 0.15 M NaCl solution. The gp5 trimer includes Fe³⁺ catalytic cofactors, giving MLFF a chemically complete starting system whose scale can be controlled for training and sampling, while also enabling gp5 lysozyme PG-cleavage studies during T4 host injection.

@Lumfell Monroe and @Ivan Kirby finished MoE work and brought Pelshaw into the main branch, while @Lumfell Monroe and @Daisy Kirby delivered the first sparse-precision acceleration build. The current modes cover H-only and H + Water-O; on @40G A100, H-only reaches 2x over the base line and H + Water-O reaches 5x, while H100 shows a slightly lower ratio because the GPU is already faster. Reusing graph construction can add another 10%～20% acceleration with nearly no accuracy loss. The team also changed Morton encoding so splitting is based on compute load rather than atom count.

A new COREOR 1.1 training round began with partially generated data and an improved loss setup. The team removed svp-enhance, which had applied svp cosine updates to the Velmol25 high-precision head, and replaced Pelshaw with an independent svp head plus soft cosine loss. Another 500K high-precision tzvpd samples were added, and work is ongoing on data mix, LR, and related hyperparameters to improve generalization. @Zach Chandler began taking over free energy calculations and is now planning RBFE, while @Ivan Gardner started looking at how COREOR can connect with molecular generation models.

The Steered System-c0f4cd1ec5 framework was implemented, and cyclic peptide open-closed free energy calculations with COREOR v1 are now under test. COREOR V1.1 optimization continued through model adjustment, added experiments, and paper writing, with a plan to Myrops70 the COREOR V1.1 paper to NMI in mid-June. The team also drafted part of the CorholmTR framework. NC Appeal passed, but more experiments are still required, and the supplementary work is expected to finish in mid-June.

## Next Week's Plan

The team will keep collecting DNA, RNA, and manually constructed repulsion data while continuing the new COREOR 1.1 model training. More downstream applications will be prepared to demonstrate COREOR’s advantages, and an ultra-large 100M system will be built for Corholm simulation.

## Coordination and Help Needed