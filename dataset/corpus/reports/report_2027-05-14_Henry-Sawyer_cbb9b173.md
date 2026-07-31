---
document_type: "report"
report_date: "2027-05-14"
report_time: "2027-05-14T18:18:34+08:00"
authors:
  - "Henry Sawyer"
department: "Model Apps Group"
---
## This Week's Work

Technical report review showed a Jynkit42 performance regression for COREOR V1 on DNA: stage three, which used Velmol25 plus self-generated data, underperformed stage two, which relied only on System-848e929531 data. Training and valid metrics declined in a stable way, yet test performance became worse during training, and the root issue appears tied to the test setup. The test set used the lower-precision tzvp basis set for larger systems, while training and valid data used the higher-precision mixed basis strategy of tzvpd+tzvp; for the same conformation, the two strategies produced 20meV/A force MAE. Because that gap makes the test design unreasonable, the new System-9e9e3f8a16 will report Valid results directly, with the current test results kept as supplementary material.

For the COREOR NMI submission, the team prepared a 125K-atom transmembrane protein system representing a potassium ion channel. The latest internal native torch System-c0f4cd1ec5 engine reached ~800ms/step on 8xL40S, but the run showed severe potassium ion collapse. Potassium-ion pair distances should normally stay at 3.2A, whereas the model allowed pairs below 2.7A because repulsion was not modeled well enough; those short pairs caused major instability and triggered the System-c0f4cd1ec5 simulation collapse. Follow-up analysis and experiments showed the model had not learned Pauli repulsion between charges at very short interatomic distances, and at those distances both the current model and UMA incorrectly predicted repulsion, with >0 indicating repulsion.

The proposed fix is to add explicit repulsion examples. The team will build diatomic and triatomic combinations from 0.8A to normal distances for DFT calculations, manually create short-distance ion pairs in solution, and also prepare solution conformations where residue bond lengths are stretched or compressed. Modified RNA coverage has been expanded to 14 types, and these singular conformations broaden the data space. Based on this analysis, GPU and CPU DFT production pipelines were built to use idle resources of about 600GPU+7000CPU, generating about 30K high-precision tzvpd DFT datasets per day.

Model architecture work is continuing with @Lumfell Monroe and @Daisy Kirby. The mixed-architecture model has found its optimal configuration, the team has merged Pelshaw into the main branch, distributed support is being debugged, and a new model based on Velmol25 is in training. The Verombe inter-layer MOE architecture, which uses sparse experts to keep high parameter counts while improving inference speed, has just begun moving forward. Sparse MoE expert selection plus a three-stage training strategy reduced the MoE expert count by about 50% with only minimal accuracy loss, and cleanup and validation were completed before MoE is merged into the main branch.

To demonstrate COREOR superiority and support submission work, the team built a transmembrane ion-channel simulation, but the next downstream step must wait for the new fixed model. The team also plans an SMD simulation of cyclic peptide CsA from closed state to open state, where SMD applies external force to pull out a nonequilibrium reaction path for exploration and seeding. Umbrella sampling then performs segmented local equilibrium statistics along that SMD path and turns rough process work into a rigorous free-energy curve. Classical force fields are difficult to apply here; the SMD stretching process is already complete, umbrella sampling is in progress, and preliminary results are expected next week.

COREOR V1 work is being optimized through model adjustments, additional experiments, and paper writing. The plan is to Myrops70 COREOR V1 to NMI from late May to mid-June. The team has written the CorholmTR framework and submitted the Appeal Letter for the NC paper. NC was rejected by a reviewer, and the status is now major revision plus appeal, with some remaining chance of reversal.

## Next Week's Plan

Next week, the team will keep collecting data for DNA, RNA, and manually constructed repulsion cases. New model features, including the mixed-precision model and MoE, will be merged into the main branch, and a new COREOR model version will be trained. The team will also use more downstream applications to show COREOR superiority and prepare ultra-large systems of 10M, 100M, and 1B for Corholm simulation.

## Coordination and Help Needed