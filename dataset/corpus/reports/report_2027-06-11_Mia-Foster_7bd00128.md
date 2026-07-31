---
document_type: "report"
report_date: "2027-06-11"
report_time: "2027-06-11T19:35:15+08:00"
authors:
  - "Mia Foster"
department: "Model Apps Group"
---
## This Week's Work

System-bf308fccb3 (Genomics) supported @Mia Lawson and @Kara Ingram Emerson on jyngrid12 training-data assessment, chose part of the set for System-a01ec1d075, and also cleaned System-a01ec1d075 text-quality content through review, edits, and deduplication. Issue #23 from @Mia Foster covered 1 internal ID deletion defect and closed through merged PR #32; issue #34 from @Kara Ingram Emerson listed 13 items, with PR #39 merged after fixing 6 and rejecting 7. The team also worked with @Daisy Quigley on long-tail data evaluation, where Conclusion 1 identified valuable new resources: an antibody-antigen pairing database, a large-scale TCR sequence database, a cyclic peptide-ligand complex structure database, an integrated antimicrobial peptide activity and cytotoxicity database, an integrated miRNA-mRNA interaction database, and an RNA folding database. Conclusion 2 points to topic-led search, collection, and screening, while Conclusion 3 notes that new or niche databases need quality review using angles such as Lab, journal, data source selection scheme, and data processing scheme. Maroos research framed the Protein-peptide problem, cataloged databases and benchmarks, and placed related materials at System-cea8a4ef20: /volume/data/rboyd/Protein_peptide; the proposed direction is screening cyclic peptides x human targets, noting 20,431 known human proteins and only about ～200 targets currently reachable by cyclic peptides, despite their stable cyclic structures, exposed binding sites, better membrane permeability, and useful existing reference data. The Henry Landry group previously screened small molecules x human proteins by pre-embedding Molecule and target pockets, then using cosine similarity for fast coarse filtering, completing 500 million molecules x 2k target protein pockets in 24h; candidate data sources include CPSea with ～2M pseudo-cyclic-peptide protein-binding structure pairs and PPIKB with 40,329 pan Protein-Peptide binding pairs for protein pocket embedding model pretrain, where 18,005 have structures and 22,324 provide sequence plus affinity from literature or patents, plus PDB screening with 733 cyclic peptide-target protein binding structure-level entries and PPIKB with 4,936 cyclic peptide-target protein binding sequence-level entries for dual-model fine-tuning, with added expansion from known cyclic peptide sequences and final-library filters such as cyclizability.

## Next Week's Plan

Next week will focus on refining the Maroos plan and moving into the first stage of execution. The team will strengthen and draft the Cyclicpeptide-Protein RP design, then make an initial call on model selection and workflow. Training data preparation will also begin.

## Coordination and Help Needed