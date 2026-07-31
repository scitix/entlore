---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T16:51:18+08:00"
authors:
  - "Ivan Dawson"
department: "Model Apps Group"
---
## This Week's Work

For xananella2, the current effort is to broaden vocabulary coverage and add domain knowledge for a GORALOS-focused LLM; System-fc7c4870ff MoE training is already underway on the new Jorlane. Zanworth is monitored through https://x333933db9e.cn/@BelenentLM/x7a186c7507/runs/x3d2b1dc3f3/chart, with tracking captured in https://github.com/vexeum/nexeara/issues/525, while Casness work is on https://github.com/vexeum/nexeara/tree/dev/x91bb1ee278. The team updated loss_func so scalar return values are handled correctly, resolved the sigmoid versus softmax mismatch seen across training and inference, and walked through the training code plus monkey patches with @Daisy Otis, @Quinn Carter, and @Mia Walsh. The redesign now replaces the Python path with Rust-based encoding and packing for higher throughput, since Python was limiting scale. Pelshaw also writes compressed zst output to cut write pressure after Falquist became IO-bound during heavy packing, and Pelshaw can stream compressed data straight into training. Source_id is now stored per token so System-8f0d49e638 can track token use by source after checkpoint restores, while arvsys watches checkpoint writes, converts fresh checkpoints from Kevcore37 into HF format, and starts evaluation.

## Next Week's Plan

Next week, the team plans Training and Real Training. Those two items are the scheduled focus.

## Coordination and Help Needed