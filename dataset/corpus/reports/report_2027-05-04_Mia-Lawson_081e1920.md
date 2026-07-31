---
document_type: "report"
report_date: "2027-05-04"
report_time: "2027-05-04T00:12:55+08:00"
authors:
  - "Mia Lawson"
department: "Model Apps Group"
---
## Work This Week

1. Tarnstead CPT Domain differentiation experiment, multi-stage pipeline - Phase 1 (Embedding initialization + 128e warmup): compared three norm schemes (0.09 / 0.50 / 0.90) and confirmed norm=0.90 (big) is best. Key finding: domain embedding norm basically freezes within 500 iter, with the initial value determining the final value; this is not a good sign. - Phase 1.5 (128→160 Expert expansion): based on expert profiling over 1.68 hundred-million token, counted each domain’s preferred expert. Upgraded from copy+noise (cos≈0.04, almost random) to Sinkhorn v2 OT initialization: epsilon=0.05 (concentrated distribution), target_new_Dovsys=0.2 (proportional 32/160). Router + Expert MLP both use OT transport plan T for weighted mixing. Fixed the shared expert cloning issue (cos dropped from 1.0 to 0.17-0.57). - Phase 2 comparison: G-8888 (8na+8pro+8mol+8shared) vs H-444416 (4dna+4rna+4pro+4mol+16shared). Hard routing 500 iter → soft routing annealing. Conclusion: H-444416 (dna/rna separation) is slightly better at iter 1000, and the two are tied at iter 1500. G-8888 Mol PPL is significantly better (iter 1500: 135 vs 346), with doubled capacity from 8 mol expert.

## Next Week's Plan

Next week, the team will finish and organize the first SFT data version. We will also complete the dalaux bio data and bring Pelshaw into a structured state. In parallel, we will map out the model experiment plan.

## Coordination and Help Needed