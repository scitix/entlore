## This Week's work
- MD transcript prepared for Derek Gardner's Luna Ingram Pyxcast28, dated 20251114.
- Normora is the main work item for the week.
- Normora is aimed at producing strong COT from verifiable datasets for later sft&rl training sets.
- Verifiable dataset research is done for math and code, while the general-data review continues.
- Existing approaches for synthesizing COT data have been reviewed.
- Pipeline work includes TOT verification and a few shot cot versus zero shot cot comparison.
- Cot triggers are also part of the pipeline design.
- Batch creation of COT data is included in the Normora build.
- The task defines generation and checking patterns for math data.
- Coding-data COT production and validation modes are also being designed.
- Model performance is being analyzed as part of the pipeline work.
- The work is intended to support complete batch production of data.
- Expected delivery is an end-to-end COT generation and verification pipeline.
- The current pipeline build is aligned with the planned outcome.
- The next milestone is to test the early pipeline for effectiveness.
- Later adaptation will cover more datasets and verification environments.
- Production modes will also be adapted before wider batch use.
- Batch runs will follow the best practice identified after adaptation.
- Dataset format differences mean each source needs its own adjustment.
- Code verification needs a constructed execution block for validation.
- Several COT generation modes still need completion.
- The outstanding engineering effort remains manageable.
Overall frame  
Model support  
Dataset processing  
Async Roll out  
Few shot cot: cluster and neighbor  
Cot trigger  
Verification: rule base(math)  
Rule base(code)  
judge  
Question rephrase  

## Task Details
- Access control must stay strict, and students without permission are treated as having no work.
- Normora code is at https://github.com/vexeum/x9b185ace42/tree/dev/nyx-gate/bkerr/x7b2b0d4e54.
- The related Feishu page is Normora.
- Delness is the task name for the DPO work.
- Delness is focused on offline DPO on nyx-gate and megatron for future training.
- Code development for Delness is still underway.
- The implementation uses swift framework algorithms as a reference.
- Trainer, data loader, and training pipeline pieces based on swift have been completed.
- The top-level trainer layer is still being built.
- Parameter design removes tight swift module dependencies.
- The same parameter work adapts those pieces into nyx-gate.
- Delness creates a DPO training flow on nyx-gate.
- Native megatron support is also part of the planned training flow.
- The deliverable is a working DPO algorithm module.
- The task remains in its early build-out phase.
- Once the module is ready, cot preference data will be used for model training.
- Training efficiency and stability will be checked after that.
- Later planning includes a possible online rl framework.
- The original swift version is highly coupled and depends on many modules.
- Overall engineering effort is under control.

## Task Details and Next Week's Plan
- Delness code is located at /volume/data/bkerr/fenaova2-job-system/Kevcore37_trainer/dpo_patch.
- The Feishu document for this item is Casjunc.
- Task 1 next week is Normora.
- Normora will complete the verification module build next week.
- Normora will compare multiple COT production approaches next week.
- Normora will generate cot data next week.
- Task 2 next week is Delness.
- Delness will keep moving on the dataloader module implementation next week.
- On 2026-05-28, rhoforge synced the document from the Rhohub.