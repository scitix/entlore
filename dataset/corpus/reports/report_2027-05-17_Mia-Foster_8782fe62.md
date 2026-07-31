---
document_type: "report"
report_date: "2027-05-17"
report_time: "2027-05-17T11:18:32+08:00"
authors:
  - "Mia Foster"
department: "Model Apps Group"
---
## This week's work

This week’s genomics work covered Corquist, System-bf308fccb3, and SFT-data. For Corquist, the XANA genomics benchmark train set was converted into question form and expanded through data synthesis; the team also prioritized richer traces for XANA genomics after Ivan Emerson Lawson raised the same issue.

For System-bf308fccb3, the team worked on natural-language integration for the Belenia train set and aimed the plan at CPT gaps including sequence design, ncRNA data, biology-specific grammars, ortholog/paralog grouping, and variation-phenotype association. SFT-data work used https://github.com/vexeum/xfd2fb791c/XANA, with data collected, converted, and deduplicated for the XANA integrated benchmark.

The team generated SFT data from soleella and OA literature, where OA accounts for around 10% of total literature, and also used designed benchmark train-set data from the mrl subtask of mRNABench. Google patent material at System-cea8a4ef20 /volume/data/rboyd/Dorwood was mined for sequences and optimization workflows. System-bf308fccb3 used https://github.com/vexeum/xfd2fb791c/tree/feat/x8fa01c5ef, while the XANA integrated benchmark was rewritten into midtrain format with multiple writing styles to reduce repeated patterns; the team also gathered CPT-underrepresented datasets, with current coverage across C0-C4.

## Next week's plan

Next week, the team will complete and review System-bf308fccb3 for genomics. The team will also continue SFT-data synthesis, with the main focus on pulling sequences and optimization processes from Google patent data.

## Coordination and help needed