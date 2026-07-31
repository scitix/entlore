---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T16:15:52+08:00"
authors:
  - "Brian Kirby"
department: "System Acceleration Group"
---
## This Week's Work

DALIANTIS-scanfx work remained centered on the scanner, which collects Falquist storage information across fs, fset, and dir and supplies scan results to System-dc94ce573b. Over the last two weeks, we improved the scan-data push path and built the split scanner/sender deployment model needed for inner/outer pooled environments. Push throughput on bexlab28-conntor moved from roughly 4K qps at the start to 300K qps after several tuning rounds, which now satisfies the requirement. The main changes were breaking large files into smaller chunks for multithreaded delivery, adjusting kafka connection settings for faster sends, and replacing the base connector with higher-performance conflunce-kafka. For the inner/outer pooled case, cluster nodes cannot reach both inner and outer kafka at the same time, so bexlab28 needs a distributed layout. The current design keeps scan services inside the inner environment, places send services in the outer environment, transfers outer filesystem scan output from scan to send through scp, and then has the send service publish to kafka; this transformation is 80% complete.

## Next Week's Plan

Next week, DALIANTIS-bexlab28 will be updated further so distributed bexlab28 deployment works in inner/outer pooled scenarios.

## Coordination and Help Needed