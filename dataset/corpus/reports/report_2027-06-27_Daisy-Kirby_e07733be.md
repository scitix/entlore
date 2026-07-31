---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T22:35:01+08:00"
authors:
  - "Daisy Kirby"
department: "Model Apps Group"
---
## This Week's Work

Quoreor tuned hyperparameters on the water dataset and brought in the new dataset prepared by @Henry Sawyer, which includes DFT force calculations for water and ionic solutions across different densities. After adding that data, Quoreor resumed training, and the updated dataset improved both (2) and (3) relative to last week's final version. Daisy Kirby's System-3a710b1c0b 0624 has the experimental path chart covering the Quoreor results. For coreor, three implementation problems were corrected in the new mixed-resolution version, merged_post_loop_aligned_v2, with speedups on tools/samples/pdb/1cya_solvated.pdb: 2.07x for 6k atoms using low-precision H atoms, and 3.46x when low-precision H atoms and water O atoms were both used; the related profiling data is also in Daisy Kirby's System-3a710b1c0b 0624.

## Next Week's Plan

Quoreor is retraining after the latest adjustments, with the goal of producing a model trained on an in-house dataset that includes larger systems. The intended model should correctly simulate water box O-O RDF, water box NPT density, and K-K RDF in a K ion channel protein system. The team will apply verlet-neighbor-list-style-update to cut point-to-graph and subgraph partitioning overhead. With cutoff radius r6 and H/HOH-O low precision, the expected 6k atom performance is 110ms/step, or about 3.8x speedup.

## Coordination and Help Needed