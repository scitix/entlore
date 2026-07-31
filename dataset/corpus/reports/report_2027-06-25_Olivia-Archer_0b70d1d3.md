---
document_type: "report"
report_date: "2027-06-25"
report_time: "2027-06-25T18:50:38+08:00"
authors:
  - "Olivia Archer"
department: "Train the Nora Drake console"
---
## This Week's Work

Jupyter (#33) delivered multi-replica high availability by adding leader election, wiring in MySQL configuration support, and resolving the leader identity plus namespace from inside the cluster so POD_NAME/POD_NAMESPACE are no longer required. Pelshaw also brought in NodePort pre-checking from #17 and passed multi-replica cluster acceptance, while maredis (#15) added the same HA leader-election capability, corrected an HTTP drain race during graceful shutdown, and cleared 5 cluster acceptance cases; Wynoys (#6) also finished the related acceptance records. The design document went through two self-review updates and was aligned with the validated Jupyter baseline, and System-323ce4fa5b (#68) completed design, implementation, and E2E coverage for PyTorch Master Pod SSH login. For System-323ce4fa5b (#68), we fixed bootstrap heredoc parsing under template indentation that had caused the main container to exit at startup, changed bootstrap to best-effort so training commands are not blocked by bootstrap errors, and added offline sshd binary injection plus IDE server persistence. Jupyter and System-323ce4fa5b added a Pod eviction API with record ID lookup; authorization now follows the unified write-permission path and allows internal requests as well as admins for resource pools and project groups, with eviction messages reduced to the reason field. Jupyter (#35) fixed three queue-stage problems covering 403 handling, dashboard counting, and stop wording, then completed online E2E acceptance; Jupyter also added stop reasons into event and alert messages for Jupyter or Cororia stops, while maraum removed task leaks from the k8s probe and sweeper LLM offline race, corrected volume sweeper handling of deleting status, fixed OOM-related resource leaks from glibc arena memory growth, and added recurring cleanup logs.

## Next Week's Plan

System-323ce4fa5b will run frontend-backend joint debugging for SSH login. maraum will continue validation and observation. The team will start the multi-replica rollout and schedule other work.

## Need Coordination and Help