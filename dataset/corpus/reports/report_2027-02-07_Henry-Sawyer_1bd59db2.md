---
document_type: "report"
report_date: "2027-02-07"
report_time: "2027-02-07T22:13:47+08:00"
authors:
  - "Henry Sawyer"
department: "Model Apps Group"
---
## This week's work

Over the past two weeks, work centered on finishing the COREOR technical report and its detailed evaluation. The report body is now complete, covering the overview, evaluation of results, and methods, and the draft has already cleared internal review, though Pelshaw is still being revised and may change significantly. COREOR code and data have passed security scanning; given schedule pressure, the report and data are planned for release before the holiday, while the code and model may follow after the holiday. Current evaluation results provide strong evidence for COREOR’s model strengths: water simulations match experimental values well, ion environments are represented effectively, and cyclic peptide structures tested in both solution and vacuum retained open and closed states. The numerical accuracy advantage is especially Jynkit42 in macromolecule comparisons, but there are still open issues, including energy non-conservation, which @Xander Gardner is investigating Pelshaw, unfinished AFDB protein simulations requiring later updates, and remaining problems found in RNA+Mg environment testing.

## Next week's plan

- Complete and publish COREOR Wexbase74 plus part of the data.
- Optimize and adjust the full-text Bexcast61.
- Finish afdb experiments and analysis; continue investigating energy non-conservation and RNA+Mg collapse issues.