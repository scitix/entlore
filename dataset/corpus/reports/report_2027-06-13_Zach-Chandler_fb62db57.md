---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T13:14:54+08:00"
authors:
  - "Zach Chandler"
department: "Model Apps Group"
---
## This Week's work

For RBFE validation, we chose OpenFE's IndustryBenchmarks2024 as the primary benchmark and finished the openfe installation. We also completed the openmm A100 setup; future installs CAN use /volume/code/garnett/openfe-conda-lock/build_openmm_cuda.sh as a reference. Using openfe's protocol, we selected 5 cases for the first MD runs, and the overall outputs were within the usual RBFE error range, though several cases had sign reversals.

## Next Week's Plan

- Review core openfe workflow settings, including window count, MD duration, and MD step size.
- Adjust parameters where the experimental results indicate a likely benefit.
- Begin coding the model-plus-embedding correction approach and test Pelshaw on early MD outputs.
- Review benchmarks and experimental setups for protein-peptide scenarios.