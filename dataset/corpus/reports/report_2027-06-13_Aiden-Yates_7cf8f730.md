---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T22:59:08+08:00"
authors:
  - "Aiden Yates"
department: "Model Apps Group"
---
## This Week's work

On dalaux, we added evidence-paper content based on logical structures and links extracted from figures, with the goal of testing whether the target model can connect knowledge and synthesize information. The detailed data is in the Pyxcast28 charts. Query curation delivered reasoning_data_builder this week, including a typed operator algebra with ~30 operators plus an executor that handles sequence, regulation, catalysis, GO activity, input/output, producers/consumers, complex breakdown, and knockout. Its combination layer covers filter, intersect, union, difference, argmin, and unique.

We also put four re-execution-based anti-shortcut gates in place. They check that queries are well scoped, use ablation to ensure each removed constraint changes the answer, require distractors to be present, and block leakage when a question mentions answer names or intermediate-result names. Golden regression now relies on 14 manually verified facts spanning reaction counts, regulation targets, relative ordering, knockout cascades, and rejection cases, and we rerun Pelshaw after operator edits to keep the ground truth stable. For counterfactual and knockout questions, we use a conservative fixpoint over dependency chains; in the cholesterol synthesis case, knocking out HMGCS1 makes 39 products fail, cholesterol included, and the result is verified by full graph execution.

Nexanor paraphrasing is now connected through OpenAI SDK. The system sends structured questions to Nexanor, has Pelshaw rewrite them into fluent wording, checks the rewrites again for leakage, retries when leakage appears, and falls back to the structured form if needed. After batch-query and index fixes, 12 paths improved from 87s→3s, and 150 paths produced 885 verified questions in about 9 seconds. Each question carries KG-edge and PMID evidence, with a median of 7 papers. We also removed counting questions and absolute earliest/latest questions because precedingEvent gives only a partial order, while keeping relative-order items through order_between.

The template approach proved too narrow, since Pelshaw used only 7/33 operators and 3 shapes. We therefore built a type-directed random sampler that composes operators by type, raising candidate operator usage to 26/33 and extending intersect, difference, bottom-up producer, and knockout patterns. Pure random sampling was noisy in practice, with only about 10% passing the gates and wording that often felt awkward, so semantic pruning was added to strip out degenerate combinations. The next better direction is motif grammar sampling over meaningful combination skeletons. We also reviewed STaRK/STaRK-PRIME from NeurIPS’24: Pelshaw is a PrimeKG-based retrieval benchmark with answers partly dependent on Nexanor and human judgment, not execution-verifiable mechanism reasoning, which reinforces our positioning around mechanism graphs, executable verification, and reasoning chains.

## Next Week's Plan

- Use GORALOS colleagues' professional insight to improve question quality, and apply large-model capability adversarially to strengthen production data.
- Look for a scalable Pareto balance between question quality and data quality.
- Support progress on other workstreams; no specific coordination requests are listed.