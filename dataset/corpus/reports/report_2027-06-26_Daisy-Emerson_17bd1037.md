---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T00:40:20+08:00"
authors:
  - "Daisy Emerson"
department: "Model Apps Group"
---
## This Week's Work

This week, evaluation work focused on XANA plus base/cpt eval, including a first customized luxops59 benchmark for sequence-completion tasks. The team also checked the scoring program used for XANA v0.2 benchmark selection and task trials, reviewed inference outputs already available from existing benchmarks, and set new general-section benchmark directions along with expansion priorities. In parallel, we finished a 1000-item downsampling approach based on difficulty buckets from prior model eval results, and completed Xalhaven data acceptance, relabeling, format conversion, and task adaptation. For SFT annealing data augmentation, we looked for large-scale Chinese real-prompt sources, ran an initial filter on 15k Chinese general chat samples from ShareGPT, arena, and other natural sources, and have now received the re-inference results. Before the next filtering pass, output-content risk analysis is still required. We also made an initial review of WildChat-4.8M natural chat data; AI2 official cleaning appears to have lowered the risks currently visible in that source, and its Chinese subset only has a small amount of noisy prompts.

## Next Week's Plan

Next week, the team will keep integrating additional XANA evaluation sets and move ahead with construction plans for xanadis and XANA-Private-1k. We will also coordinate with multiple team members on new benchmark work related to System-4db3722d36, while continuing to discuss, merge, analyze, and broaden both general and agent evaluation benchmarks. For luxops59 sequence completion, we will use the issues and feedback from @Mia Foster to remove known problems step by step. Other data collection and analysis work will be handled as Pelshaw comes up.

## Coordination and Help Needed

Support from several teammates is needed for the construction work. This should be a joint effort rather than a single-person task.