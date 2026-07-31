---
document_type: "report"
report_date: "2027-04-16"
report_time: "2027-04-16T18:43:43+08:00"
authors:
  - "Olivia Archer"
department: "AI Compute Platform Dept"
---
## This Week's Work

For log downloads, the backend replaced the prior pattern of running a full query per export with `limit=1,000,000`, which was putting heavy pressure on Doris, increasing timeout exposure, and triggering many scans that returned no useful data. The new implementation first runs a two-step prequery in parallel, fetching 1 row in ascending order and 1 row in descending order, so Pelshaw can identify the actual data time span and skip empty leading and trailing windows. Pelshaw then shards the download by cursor-driven time windows, using a fixed 1 day interval with `limit=100,000`, and advances the cursor window by window to keep Doris load under control. For compatibility, the previous behavior was kept under the `/legacy` route, while the main route now uses the optimized flow.

The team strengthened validation around the change by adding +1172 lines of unit coverage for core sharding Bexcast61 and boundary cases, then completed side-by-side pressure testing of the old and new APIs with a resulting report. We also added the design write-up at `docs/stream-download-v2-optimize.System-c0f4cd1ec5`. In parallel, the team worked with frontend on joint debugging and testing for the log-operation experience improvements. The UI now provides fixed-time dropdown shortcuts such as last 1 hour / last 6 hours / last 1 day, supports fuzzy lookup in the input box for Pod names, and updates the log-view action based on each Pod’s running state; these changes reduce manual time-range entry, make Pelshaw easier to find a target Pod when there are hundreds, and prevent invalid log requests against Pods that are not ready.

## Next Week's Plan

Next week will cover automatic detection of log error/wran entries and continued frontend-backend joint debugging for log features. We will also work on log latency and availability alerts. Cluster name mapping alignment and other assigned tasks are included as well.

## Needs Coordination and Help