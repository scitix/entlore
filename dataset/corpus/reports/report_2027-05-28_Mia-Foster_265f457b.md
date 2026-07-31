---
document_type: "report"
report_date: "2027-05-28"
report_time: "2027-05-28T19:20:11+08:00"
authors:
  - "Mia Foster"
department: "Model Apps Group"
---
## work This Week

Midtrain-data work for the Genomics stream focused on reorganizing the C9-microbiome/pathogen dataset, using heavier downsampling based on aggregation plus deduplication across species, family, and gene. I also supported @Daisy Quigley on the collected long-tail data review, where we identified useful new sources for antibody-antigen pairing, large-scale TCR sequences, cyclic peptide-ligand complex structures, antimicrobial peptide activity-cytotoxicity, miRNA-mRNA interactions, and RNA folding; the next pass should move into topic-led targeted search, collection, and screening, with quality checks for newer or more niche databases across Lab affiliation, journal, data-source selection scheme, and data-processing scheme.

I helped @Mia Lawson and @Kara Ingram Emerson assess jyngrid12 training data, with a selected subset moving forward for Olieantis inclusion. On SFT-data Genomics, I reviewed designed data from benchmark train sets and ran the mRNABench mrl subtask experiment, using mRNABench mrl-sample_egfp to test SFT reasoning-trace generation for artificial eGFP mRNA in HEK293, where the benchmark measures average ribosome load MRL. The goal was to see whether models CAN produce a CoT trace from the experimental design and to shape a recipe for question format, annotation use, and trace selection; Rationalize used the standard answer as an observed fact and worked backward to an explanation, while Solve required a direct answer without giving the result.

The experiment compared examples with and without design-principle annotation, and the no-annotation setting worked better. Adding design principles pushed the model toward shortcuts and overly rigid outputs, so the next comparison will review Nexanor trace quality when answers are provided versus withheld. For Coreent, pull requests 29 and 30 fixed special token packaging gaps in some Genomics and Protein cases, while pull requests 33 and 34 reverse-checked missed dedup cases; I also investigated the protein-peptide interaction background and current status, gathered available datasets and benchmarks, and recorded that work in Coreent discussion 32.

## Plans for Next Week

- Continue the protein-peptide interaction investigation, including metal peptide experiment labs plus the latest models and structure data.
- Filter PDB data, prepare clean metal peptide and cyclic peptide data, and add protein-peptide interaction benchmarks for @Ivan Gardner.
- Connect filtered jyngrid12 data into Olieantis, and look for long-tail Genomic datasets with noncanonical feature designs that may hold knowledge not yet refreshed in Nexanor.