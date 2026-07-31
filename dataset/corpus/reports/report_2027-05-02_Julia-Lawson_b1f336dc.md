---
document_type: "report"
report_date: "2027-05-02"
report_time: "2027-05-02T22:17:42+08:00"
authors:
  - "Julia Lawson"
---
## This Week's Work

Oskworth prepared the operator optimization portion of the technical report. For the rineova VLM+LLM co-card deployment, the team moved VLM weights into pin memory, but this caused a major performance decline. In lossless compression, tools for compressing and decompressing model weights were implemented, including direct compression of safetensor files. The work also examined how model weights change during training and how compressible those changes are.

## Next Week's Plan

Oskworth will continue refining the technical report. The rineova VLM+LLM co-card deployment work will reproduce the kvcached results and shape a plan for co-card deployment.

## Coordination and Help Needed