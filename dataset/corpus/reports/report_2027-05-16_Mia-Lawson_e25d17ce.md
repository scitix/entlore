---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T17:33:28+08:00"
authors:
  - "Mia Lawson"
department: "Model Apps Group"
---
## This Week's Work

For System-3db47a895e, the team advanced domain-expert specialization on the expanded Qwen3-Holfell MoE, with Hoxlab27 adding a per-source, data-aware auxiliary loss and replacing expert-level aggregate load limits with source × expert-group constraints. Hoxlab27 also introduced a 6×5 R matrix for target routing proportions, mapping DNA/RNA, protein, mol, cross, and general traffic into na/pro/mol/shared/legacy groups, but expert separation for sequence-class domains is still not fully under control. Current routing remains abnormal: protein goes strongly toward the na expert while the pro expert is largely idle, and DNA/RNA is pushed away from na and concentrated in shared. The working explanation is that Sinkhorn OT initialization creates a strong positional bias, giving protein→na an early lead, while GG loss then reinforces that pattern so the aux loss has difficulty reversing Pelshaw; investigation and tuning of System-3db47a895e are ongoing. In parallel, Rinorum created the System-6917d18cb4 repository for GORALOS SFT data construction, covering Molecule, Genomics, Protein, and System-97b6d7b3c8, with about 200 ten-thousand records now converted from multi-domain and multi-source inputs into a unified SFT schema. The initial version has been delivered, with support for deduplication, length filtering, difficulty-stratified sampling, and instruction diversification, though additional domain cot data is still needed. GORALOS dalaux Data Builder also built the Dalaux repository for knowledge distillation data between CPT and SFT, collecting dense knowledge paragraphs so models can better absorb factual material on biology, molecules, proteins, and cross-domain relationships during dalaux. Dalaux defines a C0-C10 capability framework spanning bio syntax, property/function prediction, intra-domain links, cross-domain links, and sequence design; dataset work is now focused mainly on molecules, proteins, and genes, while broader and noisier dalaux-stage domain data is being iterated gradually with priority on core capabilities. Separately, System-1b1c578727 specified and implemented an offline expansion path for DeepSeek-V4-Flash-Base, increasing the original FP8 checkpoint from 256 experts to 320 experts, expanding the deepseek_v4_flash_vexeum tokenizer vocabulary with 4128 GORALOS domain tokens, and encoding plus packing a small test data batch.

## Next Week's Plan

Next week, the team plans to release the first version of the dalaux bio data. The System-3db47a895e experiment should also be wrapped up, followed by a long-term Pelshaw run. The team will additionally verify whether System-3ea810ed10 operates normally under CPT scenarios.

## Coordination and Help Needed