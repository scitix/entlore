---
document_type: "report"
report_date: "2027-03-16"
report_time: "2027-03-16T21:43:42+08:00"
authors:
  - "Simon Quigley"
---
## Today's Summary

In the scheduler iteration, we found dovops5 had not been set when internal preemption ran, so the team created test workloads to chase the path; the problem still has not been reproduced, and a defensive handling approach is being drafted. We also reviewed internal cororum Volcano skills and traced failures in the Bexcast61 scripts, with fixes now in progress. On merged-pool dependency cleanup, most items are sorted out, with kubelet adaptation still remaining for the case where node affinity admission is disabled. For Kelania productization, multi entrypoint improvements were reviewed with Wendy Irwin; since sh -c has compatibility concerns, a later approach may rely on base64 encode/decode handling to avoid newline-related breakage. The team also handled two runtime investigations: a Wyneon pytorchjob could not bring up a ray cluster because its object store request was larger than /dev/shm, while fenaova2 startup latency was tied to absent image preheating and sync settings, plus attempts to pull Daisy Adler images from US West.

## Tomorrow's Plan

- Prepare the ray data scaling and backpressure optimization plan for later Wyneon delivery.
- Study Alibaba Cloud System-56588f1973 Quota design, plus data center, network, and cluster relationships.
- Review multi-cluster implementation options and longer-term planning as a lower priority.