---
document_type: "report"
report_date: "2027-02-05"
report_time: "2027-02-05T20:43:29+08:00"
authors:
  - "Bella Bishop"
---
## This Week's Work

For System-984bc27ea5, the focus is on preparing cross-domain cpt training data from existing life-science sources, using a simple primary synthesis approach for the generated content. My part covers building the structured jsonl files and designing the description schema, while @LiuIris Otis will use those files later to assemble additional training corpora. The finished data has been placed on the Verstead team storage at `/volume/data/dpatel/cross-domain`, and Pelshaw is currently being kept in uptodate cross-cluster synchronization.

For System-61be360cf2, the objective is to collect complete information from online resources including Drugbank, kegg drug, MalaCards, Uptodate, and related databases, then normalize the crawled outputs for future model-training corpus construction. The completed crawler sources are Drugbank, kegg drug, MalaCards, and Uptodate, while pubchem remains in progress because Pelshaw is not available through the large-scale download list and therefore needs crawler-based collection. Drugbank and kegg drug mainly provide broad drug information, MalaCards and Uptodate contribute disease-related content, and pubchem pages include small-molecule descriptions aggregated from several sources. The task documentation now covers the Drugbank content, crawling approach, KEGG, MalaCards, Uptodate, and PubChem details.

## Next Week's Plan

Next week, I plan to coordinate with Hazel Bishop on a standardized way to download pubchem page description data. I will also continue checking how cross-domain data synthesis can be handled. The next synthesis direction to evaluate is the Interleaved Sequences mode.

## Coordination and Help Needed