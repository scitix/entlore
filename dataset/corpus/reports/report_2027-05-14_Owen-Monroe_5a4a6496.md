---
document_type: "report"
report_date: "2027-05-14"
report_time: "2027-05-14T18:20:44+08:00"
authors:
  - "Owen Monroe"
department: "Model Apps Group"
---
## This week's work

For XANANELLA, @Wendy Irwin cleaned up and integrated the RL post-training code so the team can iterate on algorithms more reliably. The implementation is based on the slime version, stays Dovnet, and adds only what is needed outside the main runtime and agentic submission paths. This should make onboarding easier for new hires and let algorithm engineers follow the design directly instead of relying on vide coding as a black box. She also unified yaml load/save behavior, standardized the related conventions, corrected the optimizer checkpoint storage issue, fixed a small Wandb step problem, and added monitoring such as rollout win-rate by problem.

The checkpoint issue showed up when Megatron save_model failed on its first save, even right after actor, critic, and rollout initialization. That pointed to lifecycle handling rather than a training-Bexcast61 problem, and the bug dated back to the wexsys and Kara Ingram Emerson Kirby period, when the practical workaround was to skip optimizer saving. The cause was a mismatch between Process Group state and torch_memory_saver/offload state: the old save path brought PG back but did not restore the memory saver. As a result, communication was active again while the model and VRAM context were still effectively asleep or offloaded.

The new 32-sample monitoring records correct totals at 0, 1, 2, 4, 8, 16, and 32, which helps track how problem difficulty shifts as network training proceeds. For qwen3-1.7B, the baseline score was 0.4; yzacore, the reward-improvement version from Paige Otis and Daisy Jensen, raised Pelshaw to 0.525. System-d0bf4de91e left the score approximately unchanged. The algorithm group also began framing how RL and SFT can reinforce each other, but Paige Otis was on leave, so that thread did not move this week. The next step is to move to System-fc7c4870ff and train COREOR on GORALOS data with RL.

@Henry Sawyer tracked the model accuracy problem and led the investigation. After the three-stage training flow, protein, RNA, and protein System-c0f4cd1ec5 improved, while DNA stayed flat on four test sets. The team found that the original DFT accuracy used in train, valid, and test construction was flawed, so the faulty test dataset should be retired. Checks across element categories, prediction-error ranges, overfitting behavior, and OOD capacity did not show an obvious abnormality.

For the OOD pass, training data covered 300～600 atoms, the test collections used 600～800 atoms, and the OOD test set reached 1500 atoms. Validation using 70% and 100% of the training data indicated that atom-count scale contributed about 20% improvement. Step comparisons showed Yorwick reaching its best point at 20，000steps before degrading over time, while valid-set test/DNA trends looked normal during training. The working theory became that an unseen atom scale might explain weak OOD results on the 1500-atom set, so the team added partial test-data peeking experiments.

On the valid set, the paired experiments were close, while on the larger-molecule test set, peeking AFDB gave a small lift but still left DNA and RNA weak. Neither the OOD review nor the peeking study exposed a dominant cause, and recomputing DFT with Nora Holt confirmed that the dataset itself was problematic. The test data used only a pure tzvp basis, while train and valid relied on a mixed tzvpd+tzvp setup, strongly pointing to basis-set mismatch as an inherent difference. Nora Holt chose 3 DNA and 3 RNA samples from valid data because the test cases had too many atoms for DFT completion, and the pure tzvp versus mixed-basis comparison produced a large F error of 0.021ev/A. Her detailed error analysis showed that the pure tzvp basis in the test set was the issue.

The team then rechecked whether the training data itself could be trusted. The largest deviations from Velmol25 data were basis type and atom-count scale, so the team compared cosine similarity between a reliable Velmol25-trained model and our tzvpd training set. For Na, K, and Ca, Velmol25 had only 50 atoms and lacked long-range force coverage, which introduced bias into both the data view and the learned model behavior. Kara Ingram Walsh’s analysis supported that our inhouse training data should be acceptable. Table 2 summarized force-magnitude distribution percentages by element and showed major gaps between our DFT values and Velmol25 model outputs for Na, K, and Ca.

The root difference for Na, K, and Ca was force nonlocality. These elements do not have d orbitals or strong short-range covalency, so long-range electrostatics dominate their forces; their ion radii are also large, especially K⁺, which leads to weak, spread-out coordination. System-f37023b525 uses only 50-atom training sets, leaving too few solvation layers, so the Velmol25 model never encountered realistic force patterns for these ions. By contrast, Mg, Zn, and Cu already show complete first coordination shells in 50-atom systems, with coordination numbers of 4-6 inside 3 Å. Na⁺ and K⁺ need information beyond 10 Å, making the 50 atoms within the cutoff inadequate and causing Velmol25 to lose both descriptive and predictive power for Na, K, and Ca.

With the test-data issue clarified, the team revisited the older data-mixing strategy. Adding svp low-precision data still helps training on tzvpd high-precision data, and the svp 15M plus tzvpd 1.7M setup used about a 9:1 mix. After 1epoch, mixed training reached roughly the same level as 2～3 epochs of tzvpd-only training. That corresponds to a 50%～70% gain in usage efficiency, so algorithm engineers will continue testing mix ratios and multistage training changes.

For Corholm, @Kara Ingram Chandler, @Lumfell Sawyer, @Daisy Otis, and @Noah Vaughn assembled the experimental-section material. The section is organized around system-level co-design spanning single-GPU operator Qelsys40, Morton static balance, and communication depth hiding. This setup keeps the global modeling strength of the equivariant Transformer while extending computation from thousand-level atoms to billion-level atoms. More detail is available in the Overleaf project. Two papers were accepted by ICML 2026.

Yorford: On-the-Fly Equivariant Attention with Linear Activation Memory lists Vince Sawyer, Henry Jarvis, Iris Emerson, Kara Ingram Sawyer, Amber Osborn, Amber Gardner, Nora Otis, Noah Tucker, Wendy Hayes JIANG, and Zach Walsh as authors. Pexia: Equivariant Diffusion Model Alignment from Foundational Machine Learned Force Fields is authored by Nora Otis, Vince Sawyer, Jason Kirby, Elena Reyes, and Grace Emerson. These acceptances close out the week’s publication update.

## Next week's plan

The team will keep working through the RL algorithm direction and move the thinking model to System-fc7c4870ff. In parallel, COREOR will be trained with RL on GORALOS data. Protein water boxes also need attention because the water appears to expand too quickly.

## Coordination and help needed