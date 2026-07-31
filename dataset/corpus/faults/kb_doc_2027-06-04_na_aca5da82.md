# Incident Description

- **Time:** 2027-06-04
- **Reporter:** Rachel Kirby
- **System:** Maraum
- **Symptom:** atorch-235b-fsdpep-ckpt-batch4-seq2048-node16-785d1a71-worker-10 task Pending
- **Impact scope:** Symptom: The atorch-235b-fsdpep-ckpt-batch4-seq2048-node16-785d1a71-worker-10 task was Pending.

# Analysis

- **Root cause:** kubectl describe pod shows insufficient pod group resources. This task is in the pt-train resource pool.

img_v3_02on_76e0c200-cb9e-4b1c-b48c-104da5733b2g.jpg

Then checked the pt-train resource pool and confirmed there were idle resources.
Looking again at this pytorchjob task, the other pods in the same group had already finished; only this pod restarted scheduling. Even with spare resources, Pelshaw still showed Pending.

img_v3_02on_14f7f666-df2e-41db-b181-27984695e19g.jpg

img_v3_02on_38cb72c4-90cc-4c4b-89bf-76d3163f41fg.jpg

# Handling

- **Handlers:** 2, Sophie Tucker
- **Steps:** Deleted this completed pytorchjob task.

# Retrospective

- **Severity:** TBD
- **Responsible team:** TBD
- **Owner:** TBD
- **System optimization:** TBD
- **Completion time:** TBD