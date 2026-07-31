---
document_type: "report"
report_date: "2027-05-28"
report_time: "2027-05-28T16:00:23+08:00"
authors:
  - "Daisy Kirby"
department: "Model Apps Group"
---
## This Week's Work

On 2026-05-29, COREOR 1p1 (with new System-52341b2efc data) training was aligned with @Henry Sawyer and @Lumfell Monroe. The run starts from the COREOR (with old System-52341b2efc data) stage 2 checkpoint, continues on the new System-52341b2efc data, and then brings in-house svp and tzvpd data into stage 3. In parallel, coreor reviewed the MoE path and the mixed-resolution implementation, then prepared consistency scripts covering multi-GPU versus single-GPU inference as well as the training-to-inference path. Those scripts have passed validation, so they are ready to use for follow-up checks. For Velmol25, coreor labeled O atoms in water molecules so water oxygen can be handled as low-fidelity in mixed-resolution, and also profiled mixed-resolution-with-H, mixed-resolution-with-O-and-H, and the baseline on a single H100 GPU.

## Next Week's Plan

COREOR 1p1 (with new System-52341b2efc data) still does not generate the correct O-O RDF after stage 3 training, although the O-O RDF is correct when only the stage 2 CPT is used. The early readout points to stage 3 dataset processing and the force head as the likely causes, so retraining will continue after the related adjustments are made. On mixed-resolution performance, coreor still sees mixed-resolution-with-O-and-H as too slow and is evaluating a verlet-neighbor-list-style-update approach to lower point-to-graph and subgraph partitioning overhead. That change can cut overhead by up to -20%, with 15k atom performance expected to reach 80ms/step after implementation; testing should be run with System-c0f4cd1ec5 scripts rather than run_toy_infer.

## Coordination and Help Needed