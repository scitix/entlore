## Marhaven Cluster; Fault Records

- Marhaven (Marhaven) belongs to vexeum’s internal cluster estate.
- On 2026-02-10, a storage-stuck event left cluster storage fully frozen.
- The storage outage traced back to network or switch abnormalities.
- Those abnormalities made the storage layer unavailable.
- On 2026-03-12, cororia experienced a sluggishness incident.
- cororia services lagged during that event.
- OS command execution also slowed on some nodes.
- Further root-cause work was required for the 2026-03-12 case.
- Storage I/O was suspected as a contributor to poor system response.

## Scheduler Overload Causing Scheduling Exceptions; Scheduler Failure Causing All Tasks Pending

- On 2025-12-11, scheduler overload disrupted normal task scheduling.
- The incident happened after excessive tasks caused the scheduler to crash.
- Service came back once the scheduler was restarted.
- On 2026-02-09, a separate scheduler failure affected the cluster.
- All cluster tasks remained in pending state during that failure.
- The root cause for 2026-02-09 was the scheduler itself failing.
- The incident highlighted a need for rate limiting during task spikes.
- Horizontal scaling is also needed to better absorb task surges.

## Pod Network Communication Exception; Compute Node Time Synchronization Service Exception

- On 2026-02-05, some pod-to-pod network communication failed.
- The issue came from abnormal containerd behavior on Marhaven-s-004.
- Wendy Sawyer, Amber Dawson, Nora Holt, and Elena Zimmer handled the Pod network case.
- A compute-node NTP time synchronization service incident was recorded on 2026-02-03.

## Node Hard Lockup Causing Loss of Contact

- On 2026-02-03, several compute nodes had NTP synchronization failures.
- Incorrect machine time affected users’ scheduled tasks that day.
- Nora Holt, Elena Zimmer, and Noah Walsh handled the time synchronization incident.
- On 2025-09-10, Marhaven-c-064 saw repeated hard lockups and lost contact.
- The same node event evicted business Pods and was caused by kernel hard lockup.

## Operations Key Points; Related Pages

- Storage faults can surface as operating-system sluggishness.
- cororia is sensitive to storage I/O performance below Pelshaw.
- During GPFS anomalies, operators should also verify node OS responsiveness.
- [[GPFS-operations]] — General diagnostic process for stuck storage
- [[Bryford-cluster]] — Similar storage deadlock case
- [[Galholm-cluster]] — Storage failure caused by IB switch anomaly
- [[scheduling-troubleshooting]] — scheduling troubleshooting