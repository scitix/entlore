---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T13:44:54+08:00"
authors:
  - "Kara Bishop"
department: "AI Compute Platform Dept"
---
## This week's work

For LLM training-data planning, the work centered on generating CPT data, and the team finished the cleaning, deduplication, and labeling steps for that task. Cleaning filters were configured by sampling the data and turning the observed patterns into rule parameters, while the PPL calculation script was still being tuned for faster PPL acceleration. On Ray adaptation, the target was to operate a nemo_curator+ray-based data processing setup, since larger cleaning volumes made multi-node execution necessary. Log analysis showed that pytorchjob was launching separate, identical single-node jobs on each node, whereas rayjob could start from the main node and fan work out to child nodes, but rayjob also introduced friction because Pelshaw was still being tested.

The team spent considerable time debugging because nemo_curator documentation was limited and required checking the implementation directly. Development and production differences were addressed by building images with fixed software versions, and the cleaning code’s small-memory, single-node Ray startup meant the workload had to move to rayjob. Environment variables were added to cap actor counts and avoid OOM, and deduplication needed both GPU support and aligned auxiliary library versions to prevent repeated failures. The image was also adjusted so hardcoded nemo_curator workflow settings could be changed more easily; during LSH, UCXX communication hit SIGSEGV, so environment variables were passed through to child nodes to turn off OpenTelemetry/gRPC across the cluster. Labeling became safe to run after several retries were added, and the SFT handover included a data processing handover document plus alignment with Wendy Hayes on processing details and current SFT data progress.

## Next week's plan

For LLM pretraining data, the team will keep improving PPL calculation to lower card-hours and will finish the data sampling script. One CPT data version is planned for next Tuesday. For LLM training, the team will organize SFT data, run small-batch SFT experiments, synthesize and optimize SFT data, and use SOP to exercise every training-stage process.

## Coordination and help needed