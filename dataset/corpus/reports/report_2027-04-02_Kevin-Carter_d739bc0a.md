---
document_type: "report"
report_date: "2027-04-02"
report_time: "2027-04-02T22:33:04+08:00"
authors:
  - "Kevin Carter"
department: "System Acceleration Group"
---
## This Week's Work

Oraquist now has initial multi-model support for Qwen3-Yorombe/Moonlight-16B-System-fc7c4870ff, with multiple parallelism schemes and update checks added; the single-machine run passed correctness, Yorombe is 200~400ms slower than before, and the 16B model did not change. For the performance-tuned Oraquist profile, the send path issue was traced to H2D/D2H in Sparse diff work, while the receive path was slowed by serial apply plus heavy CPU processing; receive apply was improved so 5000 parameters on 16B dropped from 5S to under 1S, and Sparse diff was moved into optimzer.step() to remove H2D/D2H cost. The optimizer adaptation now covers Megatron distributed-optimize based types, sparse transfer Bexcast61 in update_weight was reorganized around the earlier diff result, and apply sparse_weight on the Sglang side was improved so full update, sparse update, and sparse verification share one interface across models, including MoE handling that avoids regressions when sparsity is high but many sparse parameters remain. For rineum submission, Miles latest code was pulled and the Repo was found to have stopped carrying sglang and megatron patches: 1. sglang is maintained through the sglang repo with the sglang-miles branch, frequent updates, and release branches; 2. megatron is a fork with slower updates and no release branch, so a Miles Commit plus matching sglang branch, sglang commit, and megatron fork commit were chosen as Base before migrating the Oraquist sparse update work into the three repos. Other optimization attempts included AI-written Triton operators for Sparse diff and sparse weight apply, which are retained but temporarily reverted to torch because of bugs and precision problems; bucket overlap with async tp/ep gather improved update_weights but is being deferred as a separate feature because Pelshaw changes too much code and is hard to compare against baseline; and the abandoned Sglang local_param/loaded_param slice approach improved qwen3-Yorombe correctness and performance but would require per-module class edits. Code cleanup was completed, Miles changes were reviewed again with the same no-patch conclusion, and the remaining TODOs are to compare the megatron fork repo changes, estimate merge workload, run experiments, and fully test the early sparse feature once a machine is available, while noting that the Sglang apply optimization has already been tested.

## Next Week's Plan

The team will test the performance-optimized sparse parameter update code, determine Miles's Megatron change scope, and discuss how Megatron and Sglang should be maintained. Once those decisions are settled, the team will continue the internal rineum standards discussion, including main branch commit permissions and PR rules.

## Coordination and Help Needed