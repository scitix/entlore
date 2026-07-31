---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T15:38:40+08:00"
authors:
  - "Mia Lawson"
department: "Model Apps Group"
---
## This Week's Work

1. Task: CPT experiment summary. Main progress: 1. Dalaum Domain Expert differentiation experiment debug R matrix completed, and a new G matrix control was tried; both received supplementary tests, but results were average, especially with a large domain drop that is not acceptable. Due to resource and priority constraints, this project is temporarily downgraded. 2. Goroys @Daisy Otis got the basic version running. There is a loss spike issue; during spike, expert reassignment occurs and newly added expert exits abruptly. Several possible causes have been proposed but not fully diagnosed. We will continue collaborating on CPT training stability and efficiency constraints. Next week’s goal is to run stable 32k 100b data training efficiently (spike as few as possible and recoverable). In the evaluation inference stage, sglang support for expert expansion seems to have issues; lzeller’s intern qpayne is helping investigate. 2. Task: Haleent data construction. Main progress: domain data in the dalaux stage was expanded to 24B with interns @Mia Foster@Gavin Chandler, with basic coverage; the small-molecule part of COT data added some usable data. Main issues: coverage is insufficient for peptides, especially metal-peptide related data; science reasoning data may need to rely on papers in the short term. Next, @Kara Ingram Emerson will help connect general and System-f5ad66c13b dalaux data quality control and version management, @Daisy Quigley will help with coding work, @Aiden Yates will handle heterogeneous graph reasoning, and @Mia Foster@Gavin Chandler will work on improving reasoning ability in specific scenarios. Beyond gradually improving data coverage and basic quality, domain reasoning ability and agentic ability are the next-stage goals. 3. Task: XANA evaluation page updates: revise evaluation page wording and assist @Mia Walsh @Hazel Emerson in confirming evaluation results and case details.

## Next Week's Plan

Next week, the team will hand over the complete dalaux data and begin training. We will provide support for the System-fc7c4870ff post-traning follow-up work where needed, with delivery still targeted before 0630. In parallel, we will review blockers in System-fc7c4870ff post-training capability data synthesis and participate in the related development effort. The team will also keep System-3ea810ed10 training stable while supporting both training and inference needs. Since the first evaluation version is now past its most difficult delivery window, we will keep pushing the remaining work forward.

## Coordination and Help Needed

Protein domain expert intern roles are still open, and the team may later need one or two interns focused on proteins and peptides. These interns would support judgment on scenario-test problems and model tasks, with coordination help requested from @Ivan Nolan. Because the team is small, moving quickly, and has recently absorbed many engineering delivery items, we need to strengthen research discussion and avoid low-efficiency solo work. Support on coordination is requested from @Mia Walsh, @Henry Sawyer, and @Lumfell Monroe.