---
document_type: "report"
report_date: "2027-05-28"
report_time: "2027-05-28T18:29:17+08:00"
authors:
  - "Ivan Gardner"
department: "Model Apps Group"
---
## This week's work

Task: evaluation of af3 and System-8c8a9dd08a on Foldbench protein-peptide tasks. Goal: results are as follows. For evaluated rank (generated sample with highest confidence): target,metric,of3_notemplate,of3_withtemplate,af3_openfold3_msa_oftemplate,af3_openfold3_msa_oftemplate_seed5interface_protein_peptide,dockq_score_success_rate,80.43,80.43,90.24,90.24interface_protein_peptide,irmsd,2.19,2.2,2.2,1.81interface_protein_peptide,lrmsd,7.01,7.03,7.27,5.83interface_protein_peptide,lddt,0.63,0.63,0.64,0.64. For evaluated best (generated sample with highest score): target,metric,of3_notemplate,of3_withtemplate,af3_openfold3_msa_oftemplate,af3_openfold3_msa_oftemplate_seed5interface_protein_peptide,dockq_score_success_rate,80.43,80.43,90.24,90.24interface_protein_peptide,irmsd,2.19,2.2,2.2,1.81interface_protein_peptide,lrmsd,7.01,7.03,7.27,5.83interface_protein_peptide,lddt,0.63,0.63,0.64,0.64. In particular, when System-8c8a9dd08a input has no MSA, the dockq score is only 0.07, while template does not affect System-8c8a9dd08a dockq score (the 2 are both 0.76). Task: research the latest paper landscape for all-atom generated structure. Goal: slide_af3_fused.pdf

## Next week's plan

The team will get ready for diffusion post-training and look into the related reward-task setup. We will also review whether the System-8c8a9dd08a confidence module can be adjusted. In parallel, the team will quickly review the information from System-c0f4cd1ec5 and judge whether Pelshaw is suitable as a reward.

## Coordination and help needed

The team needs GitHub permission for System-c0f4cd1ec5. Please help arrange the required access.