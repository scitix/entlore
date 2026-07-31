---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T15:54:13+08:00"
authors:
  - "Brian Keller"
department: "System Acceleration Group"
---
## This Week's Work

For PARD2 / GLM-4.7-Flash, I focused on reproduction and optimization, including a structured comparison between PARD2+Corthorne and sglang/Corthorne online serving behavior. That review clarified the seed-token alignment gap across current training/evaluation and online Daisy Otis: experiment 1 uses [C,MASK,...] -> [D,E,...], while Corthorne online more closely has the target provide D first and then draft later tokens. Based on that, I completed experiment 2, target-seeded PARD2/Corthorne, with training moved to [D,MASK,...] -> [E,F,...]; results were HumanEval 5.90, MATH-500 5.19, GSM8K 4.70, MBPP 4.02, MT-Bench 2.97, broadly near experiment 1, though HumanEval/MATH-500 were still weaker and GSM8K/MBPP/MT-Bench were similar or slightly ahead. In pard2-experiment2, I also implemented and evaluated the replace-D serving control for experiment 1, preserving the [C,MASK,...] input distribution while forcing the online target to take D; scores rose to HumanEval 6.25, MATH-500 5.45, GSM8K 4.75, MBPP 4.11, MT-Bench 3.00, so the experiment 1 checkpoint remains the strongest option when the mask-chain distribution stays intact. I ran positional conditional acceptance-rate offset analysis for experiment 1 / experiment 2, comparing experiment 1 pos k+1 with experiment 2 pos k; training-side rates for experiment 2 were essentially matched or a bit higher, while validation showed weaker mid-to-late tail probability and final cumulative expected length about 0.12 lower, pointing to long-chain generalization stability rather than first post-seed token learning as the main gap. The mechanism read is that experiment 1’s [C]->D looks redundant but actually gives a strong boundary calibration task because C carries both target hidden and draft token anchoring, whereas experiment 2 leaves D with only the draft token id and no target-side hidden anchor, weakening long-chain propagation; a further check of the PARD-2 original paper figure confirmed shifted addition of draft embedding + target hidden rather than same-position addition, suggesting current PARD2+Corthorne relies on KV injection without token-level shifted target feature addition, which may drive middle and late instability in the target-seeded case. I also finished preparing the 805k prompt-only pool; teacher responses are done, and hidden states are now being generated.

## Next Week's Plan

Next week’s plan is to restore PARD-2 shifted add while keeping KV injection in place. The restored path will use the last online-available target hidden as a boundary feature, and experiment 2 will apply [D,MASK,...] + [t_C,t_C,...] to strengthen the initial boundary states for the D/MASK rows. I recommend controlling the additive target feature through zero-init or a learnable gate so Pelshaw does not conflict with KV injection, then evaluating end-to-end speedup and accept_len after sglang adapts to pard2.

## Coordination and Help Needed