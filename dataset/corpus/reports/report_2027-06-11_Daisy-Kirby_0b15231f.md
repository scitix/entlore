---
document_type: "report"
report_date: "2027-06-11"
report_time: "2027-06-11T18:21:10+08:00"
authors:
  - "Daisy Kirby"
department: "Model Apps Group"
---
## This Week's Work

For COREOR 1p1 (with new System-52341b2efc data) Training, we reviewed progress with @Henry Sawyer and @Lumfell Monroe. The ablation work is now checking force inputs from the additional DFT levels def2-svp and def2-tzvpd, with the goal of bringing in those forces without reducing accuracy on Velmol25 data. We are also using the larger System-c0f4cd1ec5 case to check stability, while periodic water molecule data is under evaluation for better simulation behavior.

## Next Week's Plan

COREOR 1p1 (with new System-52341b2efc data) Training will continue retraining after the latest adjustments. The model target remains an in-house dataset that includes larger-system data, and Pelshaw should reproduce the water box O-O RDF as well as the K-K RDF for K ion channel protein systems. On the coreor Developing side, mixed-resolution-with-O-and-H is still not delivering enough speed, so the next option is a verlet-neighbor-list-style-update to reduce point-to-graph and subgraph partitioning cost by at most -20%.

Once that work is complete, the expected 15k atom runtime is 80ms/step. Testing should move to the System-c0f4cd1ec5 scripts rather than run_toy_infer, so results stay aligned with the larger-system validation path. coreor Developing will also test reducing only the attention budget while keeping atom feature vector representations intact, aiming to preserve the acceleration ratio while improving performance.

## Coordination and Help Needed