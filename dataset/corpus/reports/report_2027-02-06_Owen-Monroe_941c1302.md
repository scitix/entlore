---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T08:25:28+08:00"
authors:
  - "Owen Monroe"
department: "Model Apps Group"
---
## This week's work

@Hazel Tucker reports that the stage-two and stage-three water NVT runs are now nearly clean, with results matching expectations and lining up with many experimental checks; the remaining critical problem is in NVE, where the green curve drifts during potential-to-kinetic energy exchange, creating unexplained energy that must be traced in the model internals. In recent days @Hazel Tucker has put 100% of her effort on that top-priority conservation issue while also drafting technical report material on the model structure and training strategy, including training details for an atom-level dataloader rather than a system-level dataloader so different gpu devices receive similarly sized workloads; the team also uses a more regular neighbor arrangement operation. For stage-three training, the current data-mixing tests use System-f37023b525 as the base line model and compare against System-9c622614e9 and System-98e7195cee; the inhouse-data model is reducing error by 2.5 times, and adding svp data, with lower precision and lower cost, is performing somewhat better, with the experiment results referenced in the table. @Leon Otis fixed several use compile mode problems, including recompilation when a mol kept its size but changed conformation, which made execution very slow, plus an issue where ckpt loading did not work correctly under use compile and crashed System-c0f4cd1ec5 simulations; use compile still generated many errors, and merge-back code changes caused training crashes, with no detailed fixes described in this segment. @Gavin Nolan found repeated O(N*K) atomic-add memory writes in the model's QKV triton kernel and rearranged matrices so writes dropped to O(N), with each block doing K register accumulations; this made the block 2 times faster and lifted end-to-end model speed by 20%. @Bella Otis and @Ji Mia Walsh worked mainly with @Fiona Holt and @Zach Dawson on distributed communication updates, shifting communication away from shared memory to reduce delay to computation blocks; they found local feature copies create contention across 2 streams even though the communication itself needs no extra compute, and @Luna Carter will later address Pelshaw by using remap to select the local feature directly.

## Next week's plan

The team will keep working on the technical report. Solving the model's energy non-conservation remains the highest-priority task.

## Coordination and help needed