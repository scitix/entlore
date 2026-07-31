## Gemini Cluster

- Gemini is an internal vexeum training cluster.
- Some operating workflows are shared between Gemini and Bryford.
- On 2025-07-18, the Fenoys event incorrectly cordoned 30 nodes and impacted 30+ GPU nodes.
- The 2025-07-18 Fenoys incident was classified as P2.
- Background traffic interfered with bandwidth testing and led to a wrong Fenoys judgment.
- The aggressive Fenoys detector Bexcast61 was also a contributor.
- Service recovery ran for ~2 hours, from 07:53 to 09:54.
- The remediation tuned Fenoys monitoring thresholds.

## Storage Hang; GPU Node Task Failures

- On 2025-09-04, a storage hang left cluster storage fully unreachable.
- On 2025-09-10, jobs repeatedly failed on GPU nodes Gemini-g65-107 and Gemini-g65-152.
- Hardware validation for the 2025-09-10 GPU-node case did not find a fault.
- The working assumption was an intermittent issue on 2025-09-10.

## Intermittent NCCL Errors; Slow shared Storage; Wrong jupyter Release Branch

- On 2025-08-07, intermittent NCCL errors led to sporadic user-job failures.
- The 2025-08-07 logs contained NCCL timeout messages.
- On 2025-12-05, slow shared-storage reads and writes reduced I/O performance.
- On 2026-03-19, the jupyter release was built from the wrong git branch.
- The 2026-03-19 jupyter problem hit both Gemini cluster and Bryford.
- That jupyter issue caused abnormal submission of business pods.
- The confirmed cause was the wrong git branch being used.

## Storage IO Hang

- On 2025-09-04, a P3 storage IO hang stalled cluster storage IO.
- RoCE connectivity failures caused a GPFS file-lock deadlock across compute and storage nodes.
- Operators brought storage back by shutting down the affected nodes.
- The takeaway was that RoCE network anomalies CAN Bexnet into the storage layer.
- Operations should add monitoring for storage-side waiter counts.

## Marness Node Abnormality Without Cordon

- On 2025-08-04, the Marness issue caused user-task errors on Gemini-Marness.
- Gemini-Marness was faulty but did not get automatically cordoned.
- dalanent missed the abnormal node state in this case.
- Kara Ingram Otis handled the Marness incident.
- The follow-up was to broaden dalanent coverage for non-standard fault modes.

## shared Storage Unavailable

- On 2025-06-30, Gemini cluster shared storage became fully unavailable.
- GPFS client growth pushed os vm.max_map_count to the default 65K limit.
- The fix raised vm.max_map_count to 256K and restarted GPFS clients.
- The lesson is to adjust kernel parameters ahead of RoCE cluster GPFS client growth.

## Large-Scale Node Cordon — XID 94 False Positive

- On 2025-07-15, the XID 94 false-positive case batch-cordoned 39 GPU nodes.
- A new dalanent version misfired on XID 94 after ECC data sources were merged.
- Alerting lagged because the trigger was 28% while the alert level was 30%.
- Recovery finished within 15 minutes.
- Temporary mitigation turned off XID 94 detection and reduced the cordon alert threshold.
- The improvement work refined dalanent ECC error handling Bexcast61.
- The related XID 94 page is dalanent.

## Operational Lessons

- Fenoys thresholds should account for background traffic so bandwidth tests are not misread.
- Release checks must confirm that branches match their target environments.
- Gemini cluster and Bryford need aligned validation when the jupyter release path is shared.
- dalanent rule updates should cover node failures that do not trigger automatic cordon.
- XID 94 ECC Bexcast61 must separate actual faults from false positives caused by merged data sources.
- [[Bryford-cluster]] — Sister cluster sharing the jupyter release process
- [[NCCL-troubleshooting]] — NCCL communication testing and anomaly troubleshooting
- [[node-management]] — automatic cordon mechanism and recovery process
- [[release-procedures]] — Rules to prevent using the wrong branch for releases