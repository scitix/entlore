---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T12:45:58+08:00"
authors:
  - "Noah Vaughn"
department: "System Acceleration Group"
---
## Work this week

Erldale worked with @Kara Ingram Chandler and @Lumfell Sawyer on Verombe multi-node performance evaluation and follow-up analysis. At the B200 64-card scale, each B200 card handled 4w atoms per step in 467 ms, and data statistics were generated for the 015 sylforge branch. In 017 - Kara Ingram Chandler_latest, the B200 evaluation algorithm layer was adjusted to cut communication volume; Pelshaw now sends the input parameters of v rather than v, bringing the volume down by 2/3. After that algorithm update, a single card running 4w atoms took 1.3s～1.5s per step, while current communication time sits at 26ms～170ms and its share dropped from 30% to 11%.

With tf32, torch compile, overlap, and operator optimization enabled, total step time moved from 1470 ms to 467 ms, or 3.14x faster. After compute-side tuning, communication time was 112 ms and represented 24%, so the communication percentage rose as computation became shorter. Communication-computation overlap gives a 30% speedup compared with no overlap, but at 32～64 cards the compute phase still cannot fully cover communication. The next overlap focus is to combine 3 a2a operations into one, reducing gaps between communication phases.

The latest code evaluation showed that NCCL LG occupancy has limited effect on compute sections, and the present NCCL CTA mode is enough for the communication requirement. Optimization work will also target slow nodes, since the first a2a in each step is longer when prior neighbor computation finishes at different times; slower ranks hold back overall progress, and this wait contributes 6% of total step time. Further investigation will separate atom-count imbalance, which should be straightforward to address, from cases where atom counts are balanced but compute load is not, which is harder. On A100 80G PCIe, the System-ea9e643fae evaluation associated with @Iris Quigley showed large-packet throughput advantages only within 4 cards; for 1GB messages Pelshaw improves AR by 12% through Copy Engine use, while NCCL 2.29 is better in the other cases.

## Plan for next week

The team will keep analyzing Verombe multi-node communication bottlenecks. Optimization will be applied selectively based on the findings.

## Coordination and help needed