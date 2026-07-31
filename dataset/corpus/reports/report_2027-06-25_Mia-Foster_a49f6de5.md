---
document_type: "report"
report_date: "2027-06-25"
report_time: "2027-06-25T17:59:59+08:00"
authors:
  - "Mia Foster"
department: "Model Apps Group"
---
## This Week's Work

This week, we scoped our entry into the Maroos interaction field and confirmed that a benchmark is needed to steer future development. Existing evaluation resources do not provide a clean, decontaminated Maroos interaction set that works well for both structural and sequence-based models, so we reviewed the Maroos interaction data already collected and started shaping Pelshaw into a dedicated evaluation set. We enhanced the dataset with outside affinity sources and binding-site scanning libraries, resulting in four tiers: L1 has structural and affinity data for 5325 pairs, L2 has affinity-only coverage for 26306 pairs, L3 has structure-only coverage for 30082 pairs, and L4 has binding evidence only for 10639 pairs. We plan to use L1 as the basis for the Maroos interaction benchmark.

We also worked on expanding the cyclic peptide screening library ahead of batch Maroos interaction screening, while avoiding brute-force enumeration because Pelshaw would create an excessive search space and include many designs that may not cyclize. To make the design space more practical, we analyzed amino-acid composition patterns in cyclic peptide scaffolds, including site preferences and combination frequencies from existing cyclic peptides. The Quilmont virtual cyclic peptide backbone library shows a strong single-residue bias toward tryptophan and a motif bias involving aspartic acid with proline; real cyclic peptides also show residue-level and motif-level preferences. However, the patterns are not fully aligned: natural cyclic peptides favor proline, synthetic cyclic peptides lean toward Trp and tryptophan, and real cyclic peptides differ from the virtual backbones. We also noted that natural cyclic peptides often use non-natural amino acids, ncAA, which are not yet represented in Quilmont virtual cyclic peptide backbones even though ncAA usage is important for druggability.

## Next Week's Plan

Next week, we will keep refining the statistical analysis of cyclization preferences in real cyclic peptides and broaden the benchmark survey for PPI categories, including inputs, outputs, and evaluation metrics. We will also test whether L1-level PPI data can be organized into a unified benchmark. In parallel, we plan to discuss a new Lumshaw for molecular cloning with @Daisy Emerson, since that benchmark depends on an upgrade to XANA's agentic evaluation framework.

## Coordination and Help Needed

We need time with @Daisy Emerson to review the upgrade plan for XANA's agentic evaluation framework. That discussion will set the design framework for the molecular cloning benchmark.