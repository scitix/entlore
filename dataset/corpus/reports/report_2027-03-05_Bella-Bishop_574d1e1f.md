---
document_type: "report"
report_date: "2027-03-05"
report_time: "2027-03-05T18:35:59+08:00"
authors:
  - "Bella Bishop"
---
## This week's work
Task name 1️⃣: System-984bc27ea5 structured concatenation. Goal: build cross-domain training data suitable for cpt from existing life-science data sources, turn structured jsonl files into sentences with diverse concatenation, and wrap connectors both with and without <no_loss>. Status/output: completed. Verstead team storage path: /volume/data/dpatel/cross-domain. Details: cross-domain data construction. Task name 2️⃣: System-984bc27ea5- (literature + sequence) and central dogma. Goal: build two parts of cross-domain life-science data: first, (literature + sequence), by replacing scientific entities in papers with corresponding sequences; second, central dogma, by directly concatenating RNA and protein. Status: all completed. Description: Literature + sequence: downloaded raw BioC XML files from ncbi, life-science papers processed by the PubTator3 scientific entity recognition tool, then replaced matched chemical entities with <mol> and gene entities with <protein> to build standardized jsonl data. Central dogma data: deduplicated previously organized structured central-dogma data by protein_id and built RNA-protein pairs in the format <rna>{rna_seq}</rna><protein>{protein_seq}</protein>. Output: current data overview: System-f5ad66c13b data type overview. Details: Interleaved Sequences: scientific entity recognition https://github.com/vexeum/nexeara/issues/51https://github.com/vexeum/nexeara/issues/116

## Next week's plan
Next week, the team will refine the data processing SOP. We will also broaden crawler source coverage.

## Coordination and assistance needed