---
document_type: "report"
report_date: "2027-05-28"
report_time: "2027-05-28T18:18:50+08:00"
authors:
  - "Owen Monroe"
department: "Model Apps Group"
---
## This Week's Work

GORALOS RL was blocked by cpt model behavior: @Wendy Irwin reviewed current outputs to understand processing, and the team concluded RL cannot use that model directly. In generate and chat, responses lean heavily toward dna, rna, and pad, while completion is only a little better; the referenced figure records several trial results. A quick validation showed hf, megatron, and sglang were almost identical overall, with sglang service and hf generate diverging only from small numerical differences. Those differences mostly appeared when candidate probabilities were flat rather than pointing in totally different directions; once one token changed, the shifted context made later text separate further, so sglang service and hf were treated as healthy.

To work around the cpt issue, the team moved to an SFT model, though the available SFT set currently has code, math, and general data while GORALOS data has not arrived. Using Goralos CPT model, @Wendy Irwin continued general 2M+math 20k SFT training, but that path caused RL collapse on aime and pushed the aime score below 0.1, so root-cause analysis is still needed; related anomaly notes exist, with some images missing. In contrast, with Goralos CPT model, math 20k SFT followed by dapo17 RL training showed the expected loss decrease and a normal aime result, with figures covering token loss or sample loss. The SFT math 20K figure also showed that after SFT the model solved 39/100 of the first 100 dapo17k questions, where correct answers tended to be shorter and wrong ones more often ran to maximum length, so this ckpt does not look seriously broken; @Wendy Irwin also noted that the math 20k SFT-based run is still in progress and currently has no major abnormal signal.

Additional work covered RL framework issues, the megatron training engine, the sglang inference engine, and adapting the CPT model across inference, training, and hugging face release paths. For tp head handling, SGLang inference copies KV heads when tp > kv_heads, while megatron requires tp <= kv_heads or startup fails; testing the current CPT model on math outputs was essentially unsuccessful. One fix made the moe model launch correctly with sigmoid, customer tokenizer, 160 expert, megatron, and sglang, while moe RL still requires rollout router and training router to match exactly and use_rollout_routing_replay to stay enabled. Another fix handled an sglang router problem where the returned router replay buffer was not wrapped into Rust meta, which had caused https generate to miss full request and response details even when init parameters asked for replay buffer return; a separate megatron replay issue still fails to call router buffer data from rollout, ref, or teacher properly, and the algorithm development branch remains labeled TOBEFIX.

Train log prob and rollout log prob are still badly misaligned, and the team is working on that correction. COREOR also saw weak application results from some 3-stage model-training ckpts. The main discussion with Henry Sawyer and Daisy Kirby focused on data problems, data ratios, new data creation, and training-strategy changes, and two ICML Paper camera-ready versions were completed.

## Next Week's Plan

Next week the team plans to finish the full cpt sft rl pipeline. Once that is complete, the first follow-up will be checking general-data issues. The team will also connect GORALOS data as soon as possible.

## Coordination and Help Needed
