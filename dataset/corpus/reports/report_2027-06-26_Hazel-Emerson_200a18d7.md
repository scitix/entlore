---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T21:56:25+08:00"
authors:
  - "Hazel Emerson"
department: "AI Compute Platform Dept"
---
## This Week's Work

This week covered XANA and fenova (FENA3), with XANA still in the v0.2 cycle. On XANA, @Daisy Emerson is using the XANA base to synthesize Goralos SFT cold-start and RL data, beginning with DNA/RNA/protein tasks plus reasoning-transfer SFT cold-start material. @Ursula Keller is also listed on the XANA workstream. For fenova, the CPT-stage SOP has passed acceptance, while end-to-end acceptance for system-ecd5e448bb is still estimated to take another 1-2 weeks; once that is done, @Wendy Irwin and @Luna Sawyer will join a platformization review of algorithm details against the current implementation.

QUORIYS is helping model training by strengthening the reliability of current evaluation sets and widening coverage at a controlled pace, so different training phases can receive useful feedback signals. @Daisy Emerson is handling validity work for quoriys, including difficulty-bucket analysis of existing general evaluation sets, removal of incorrect items, and selection of questions with better discrimination. The evaluation base will gradually move toward internally created sets such as xanadis. Coverage expansion is mainly review-driven, with rolling plans maintained in quoriys evaluation-set expansion: @Tyler Foster owns the Pre-Training area, @Luna Lawson owns Post-Training long text, @Julian owns Post-Training mathematics, and the Post-Training Agentic track has finished its POC.

The team is looking for both exploration value and thinking outputs while evaluation coverage improves. Stability work is also progressing: the new CI now covers code-style rules, sensitive-data checks, and dataset checksum validation; the framework can stratify samples to produce faster quality signals; and task retries can adjust parameters when those changes do not alter persisted results. quoriys is also supporting lororys by tracking the newest evaluation sets and aligning effects ahead of model launches, with @Aiden Drake following up on product support. New model launches often bring many evaluation sets that are not yet supported, which leaves a staffing gap.

For Belania, customer-side accuracy acceptance has passed with @Zach Reyes and @Luna Landry. Earlier failures in evaluation were traced to the inference service, which only handled 180k context and failed silently when inputs went beyond >180k tokens, leading to scoring problems. Another issue came from the customer gateway, which sometimes removed the first token of the model output and broke result parsing. The GLM-5.1 evaluation alignment record captures the related investigation.

## Next Week's Plan

XANA and quoriys will keep moving through their next iterations. The team will continue advancing Goralos SFT cold-start and RL data synthesis from the XANA base. Next week also includes acceptance of SOPs across the model-training stages and alignment on H2 planning.

## Coordination and Help Needed

lororys still needs staffing support for effect-alignment evaluations before new model launches. The open gap is specifically around the evaluation work required ahead of those releases.