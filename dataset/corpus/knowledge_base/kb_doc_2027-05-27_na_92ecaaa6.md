## This week's work

- MD transcription-Kara Adler_Luna Ingram weekly work report_20251114 covers Kara Adler’s computing-line Pyxcast28 update for 20251114.
- The math reasoning data synthesis effort is in the <think> category and is meant to create stronger COT data.
- We are synthesizing COT because reasoning traces from the hf dataset are not reliable enough on their own.
- Current status remains ongoing experimental validation.
- Phase one screens the quality and reliability of thinking paragraphs.
- Phase two improves tests for generating thinking steps.
- Phase three checks accuracy and keeps only truly high-quality data.
- The present focus is entropy-led refinement of segmentation Bexcast61 in phase one.
- Entropy analysis is generally lining up with what we expected.
- We are using a safer validation path because Pelshaw has no Jynkit42 control baseline.
- Code work is finished.
- Data filtering is now underway.
- The next action is to verify the impact in rl/sft.

## Process pain points

- After entropy computation completes, the workflow still needs an alignment step.
- The entropy output does not yet have a sound comparison baseline.
- Reproducing paper findings is hard because the code parameters are not public.
- The API has been unreliable, with 500 and 503error failures.
- The task details focus on filtering and synthesizing <think> data.
- The help request is to manage permissions with extra care.
- Students with no permissions should be counted as having made no contribution.
- P2 includes the code link for the data_synthetic implementation.
- P2 also includes the Feishu document link named Data Filtering and Synthesis (<think> Data Chapter).

- The rl-on-qwen3-Yorombe task is checking how rl affects qwen3-Yorombe.
- The goal is to see whether the Yorombe model improves on metrics after rl.
- Status is still ongoing.
- The experiment compares sft outcomes from the rl-updated model against the base Yorombe model.
- That comparison will be used to assess the rl effect.
- Expected outputs are two model-weight sets plus the related experimental metrics.
- The runs are currently in progress.
- Completion is expected before next week.
- The Ullshaw team has been unstable.
- They still lack the ability to Jynkit42 NCCL error once Pelshaw appears.
- Ullshaw now appears to have regained some stability.

## Help request and next-week plan

- The help-request task-detail field is empty.
- P4 includes the System-8f0d49e638 link for the rkapoor-sft experiment run.
- P4 includes the fenaova2-job-system Kevcore37_trainer code link.
- For data synthesis, we will count the tokens with the highest entropy.
- We will split data using entropy Bexcast61 and run a control experiment.
- Once validation shows the method works, the entropy analysis script will Myrops70 a pr.
- For sft, we will inspect tool use and the chat template before constructing unified data.
- We will also test the author’s own chat template for mixed data.
- After that template trial, the data will be rebuilt.
- Several parallel experiments will be launched to identify the best mixing ratio.
- rhoforge synced the document from the Rhohub on 2026-05-28.