---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T22:13:41+08:00"
authors:
  - "Zach Norris"
department: "Platform Ops Dept"
---
## This week's work

dalanent reached 50% on the Wynfell adaptation, while IB testing moved more slowly because the test environment had a high failure rate; the team still plans to finish IB coverage next week. v0.7.7 has been deployed to field environments, and dalanent also supported fenalova by adding 6 tools and 3 workflows for faster device health checks. Delivery inspection is still blocked until fenalova can support API tools, and the spec restructuring plan is now 80% complete.

On component capability, the transceiver now handles 8 checks, covering optical power, temperature, voltage, bias current, vendor validation, link errors, and related validations; optical module health also now separates service-network and management-network alert levels. PCIe Tree Speed/Width checking can find NIC-to-CPU-root-complex speed or width downgrades, and the upstream PCIe link check extends degradation detection through intermediate Switch/Bridge devices. CPU clock synchronization now verifies PTP/NTP status and offsets, using PTP first and NTP as fallback to reduce distributed-training communication issues caused by drift; CPU MCE monitoring records correctable and uncorrectable Machine Check Exception counts so hardware degradation risk can be found earlier. Memory ECC/EDAC monitoring now reads ECC error counts through sysfs EDAC, validates memory capacity, and covers silent data corruption plus DIMM-related capacity abnormalities; the CPU component also added the host serial number in HostInfo for asset correlation.

Several quality fixes landed this week: the InfiniBand management NIC false alarm was corrected for mixed management Bond and compute Bond scenarios by using IB port rate to separate management and service networks. PCIe Tree Speed false positives from string comparisons such as 16 != 16.0 were fixed, and the checker now compares against PCIESpeed rather than PCIETreeSpeedMin. Prometheus metric residue was addressed by clearing the annotation gauge before refresh, spec runtime writeback no longer lets InfiniBand runtime data overwrite YAML files, GPU metric collection and reporting were improved, checker execution now emits structured logs, and build support added a Docker build target plus a CentOS 8 Dockerfile.

For cluster visibility, DALANENT enabled a dalanent cluster-level dashboard to show issues across clusters, and the team plans governance work to identify real errors and correct specs. Severe faulty nodes were converted into observation metrics, and dalanent finished drill-down from the global view into cluster-level detail. The cluster detail page now shows KPI health rate, fault count, node health trends, fault TOP, and the node list; users can click a fault type to filter affected nodes, with trend granularity available at 1m/5m/15m/30m/1h. DALANENT also added an asynchronous external inspection trigger API for fenalova, supports Webhook callbacks for inspection results, and integrated SSO for Norness unified authentication.

## Next week's plan

Next week, dalanent will gray-release v0.7.8 and move the spec restructuring plan into final execution. The team will complete WynfellB300 adaptation, continue reducing and resolving fault counts on the dalanent dashboard, and keep refining and calibrating cluster health.

## Coordination and help needed