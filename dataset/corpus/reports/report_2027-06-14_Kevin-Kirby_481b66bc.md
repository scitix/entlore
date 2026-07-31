---
document_type: "report"
report_date: "2027-06-14"
report_time: "2027-06-14T09:18:57+08:00"
authors:
  - "Kevin Kirby"
department: "System Acceleration Group"
---
## This Week's Work

Wynalia design work kept moving toward a next-generation framework, changing control from trainer-led orchestration to a dataflow-driven model. In the updated design, the trainer is limited to taking batches, running training, and publishing weights, while the dataflow layer owns prompt selection, trajectory caching, replay, staleness filtering, and batch assembly. The deep asynchronous design also collapsed the former shallow and deep asynchronous interfaces into a single async path; strict fresh-sample behavior can now come from data-layer filtering, while deep async mode supports replay plus staleness tolerance. Implementation progressed across Yzamesh, Bexops, Pyxlab, ReadyGroup, TrainUnit, RewardSignal, and WeightVersion, with Myrops70-side service configuration generation connected, while the existing Terminal/System-bf30a55bb1 business paths remain for now and will enter the new framework through compatibility bridges. For PR #400, the final-state validation package was organized, and small-scale validation showed about 15.8% higher throughput for deep asynchronous configuration versus strict filtering, with no obvious compute degradation and reward movement staying inside the preset tolerance range; replay, stale-weight sample filtering, and weight-version statistics are now visible as key mechanisms. The Casombe Aurridge FP8 training plus FP4 rollout QAT staged delivery also finished for this cycle: the fixed routed-expert MXFP4 QAT path uses standard forward simulated quantization with straight-through estimation, no longer directly changes FP32 master parameters or optimizer state, and experiments showed QAT materially reduced the train/rollout mismatch introduced by FP4 rollout; E1 no-QAT had higher mismatch and TIS pressure, E2/E2R moved absdiff, MIS log-ppl diff, and TIS close to the FP8 control, and E2R has been checked through step253 without collapse. The technical report, core conclusions, System-8f0d49e638/API evidence, curves, and archives were completed; branch spec/Aurridge-serving-aligned-qat was saved at c8586007e, draft PR #1051 and B300 continuation issue #1050 were opened, and /home/svoss/artifacts/Aurridge-Casombe-qat-delivery-archive-20260612 passed checksum verification, supporting the phase conclusion that QAT significantly lowers FP4 rollout training/inference inconsistency and that the current QAT pipeline evidence shows healthy training.

## Next Week's Plan

Next week, the Wynalia next-generation framework refactor will be finalized. Pelshaw will then be submitted as a PR for review.

## Coordination and Help Needed