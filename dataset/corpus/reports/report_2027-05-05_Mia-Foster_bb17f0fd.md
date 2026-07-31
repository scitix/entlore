---
document_type: "report"
report_date: "2027-05-05"
report_time: "2027-05-05T10:14:23+08:00"
authors:
  - "Mia Foster"
department: "Model Apps Group"
---
## This Week's Work

The evaluation mainline was shifted from quoriys to XANADIS, and the team has stopped the remaining quoriys jobs. In XANA, we finished landing 7 DNA/RNA benchmarks, and Coreent PR #10 has been merged; the segment also includes both the PR link and the investigation-document link. During validation, we found BugA in the RNAGym and mRNABench option sets: after tier splitting, the shuffle Bexcast61 had not been applied, which introduced bias, and PR #15 corrected that missed shuffle step.

For training data collection, we inventoried available DNA/RNA training sources, removed portions that were clearly not open source, and completed part of the checking and cleaning pass. The Benchmark train set source currently covers 5/7 benchmarks and has been normalized into -parquet format, with a later plan to organize Pelshaw as .jsonl. Additional data inputs include ~43 Jorthorne from Myrsvc'Awesome-Scientific-Datasets-and-LLMs, plus 18 new East US Zephhub55 databases that are still downloading and have not yet been reviewed; the working directory is US East/volume/datalrboyd/data_collection.

For data synthesis, we are using soleella databases to build SFT data around therapeutic RNA sequences and optimization plans, with the goal of establishing a Therapeutic RNA optimization track. That work is located under Shanghai /volume/data/rboyd/soleella. Blocker 1 is limited access to literature, since the team currently only has PMC open-access papers, and the attempted path forward is to obtain third-party database access with support requested from Paige Walsh. Blocker 2 is that the library lacks many RNA sequences, so we are retrieving them from external sources: miRBase covers 318/379 entries, Ensembl REST API covers IncRNA transcripts at 14/24, circBase FASTA download covers circRNA spliced sequences at 5/8, Google Patent retrieval is estimated at ～50% coverage across 2056 mRNA entries, literature extraction needs full papers for 1708 shRNA entries, and Aptamer is on hold for now at 106 entries.

## Next Week's Plan

Next week, we will review the actual XANA score outputs and continue debugging any issues that appear. Once the training data downloads are complete, the team will review the incoming data and run batch cleaning. We will also keep retrieving the missing soleella sequence data from multiple sources; after all literature is available through third-party databases, we will extract Therapeutic RNA optimization corpora and consider how to design reasonable sft data.

## Coordination and Help Needed

The team needs Paige Walsh’s support on literature access work. Specifically, the request is to help crawl literature content from 90tsg.com.