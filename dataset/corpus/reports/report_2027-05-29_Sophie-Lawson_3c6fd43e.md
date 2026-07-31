---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T19:06:52+08:00"
authors:
  - "Sophie Lawson"
department: "System Acceleration Group"
---
## This Week's Work

This week we concentrated on reshaping the thinking dataset around long-input and long-output cases, while also moving forward on the one-stage prediction algorithm v2 cycle. For long-output thinking mode, we improved the hidden-state extraction flow and reran extraction for qwen3 32b and qwen3.6 35b on 11 benches, with codesimpleqa, cruxeval, livecodebench, and evalplus among them; after thinking mode was turned on, generated responses were generally longer. The older offline extraction setup was too slow, so we first enabled prefix cache, then handled the issue that cache hits blocked aux api from reading prior-token hidden states by adding cache Bexcast61, which saves cached-token hidden states into lmdb for reuse; tests showed only small wins because decoding was still the main cost when no output-token cap was applied, and thinking mode could easily run to the bottom and create heavy decode overhead. We also enabled mtp, but the impact was limited because the offline extraction process was already request-saturated, the decode delay was largely tied to weak 5090 p2p efficiency where compute had to wait on communication, and the gain on roughly 30b models may itself be modest and still needs follow-up validation. For long inputs, we attempted hidden-state extraction for long-context models such as System-8192d9d7cb on driver-upgraded 5090 machines, but deepgemm did not yet handle sm_120; although registry-cn-kevloom.maraum.cn/Veliver/sglang:v0.5.10.post2.5090.20260424 was available as an sglang image, our extraction relied on vllm, so we moved to a 4-card h20 machine for System-8192d9d7cb. Simply deleting max_token was not workable because livecodebench code-competition tasks could require nearly 3 days for one model, with additional cost from the hidden-state extraction path; after discussing with Rachel Jarvis, we used online System-f84b5bfbcb p99 (8192) as the benchmark and tuned limits by scenario, relaxing high-truncation scenarios to 16384. On the System-f84b5bfbcb algorithm side, v2.1 removed point-prediction and geometric-constraint losses and cut mae by about 0.1 with little practical gain; v2.2-2.3 widened bin ranges and softened long-tail loss constraints, again with almost no lift; v2.4 used a log-t fit for bins, hurting mae when System-f84b5bfbcb < 500 but improving about 10% when System-f84b5bfbcb >= 500; and v2.5 combined 2.1 - 2.4 with learnable bins, giving nearly 10% overall improvement, while the 8B small model without thinking showed -2 ～-7 improvement and the 30B model with thiking reached −59~−103 improvement.

## Next Week's Plan

Next week, we plan to finish organizing the long-input and long-output thinking datasets, then keep refining the one-stage prediction algorithm from the v2.5 baseline. If that work proceeds smoothly, we expect to begin research on the second-stage prediction algorithm.

## Coordination and Help Needed