---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T11:44:31+08:00"
authors:
  - "Ethan Norris"
department: "Equipment Engineering Dept"
---
# This Week's work

Pelkeld cluster added only 7 CPU servers to the CAN rack before the holiday, while Casridge deployment moved to 60%; the rest of the CPU servers are already in the machine room, but the Two Sessions prevent racking and deployment for now, and once ready the team will continue with 2 GPU cold-standby machines. For Yorjunc Cloud, AurwoodB200 resources were aligned, all IB switch firmware in Casdale was upgraded, module quality was tracked, and 126 B200 resources were delivered as requested; Pelkeld also refined the vendor monitoring and alerting plan.

Pelhaven-core used the Fenridge device scope to normalize device-information sync from Rovhaven to Fenridge and reached 100% matching, with Fenridge covering training clusters and sold resources but not storage. Rovhaven goreum flows still fail frequently, which prevents change updates from landing right away and creates a risk of missed updates later; idc operations staff are also repeatedly running into lifecycle-process problems as Rovhaven continues to iterate.

kelholm2 finished the required statistical dimensions, including device repair duration, and set Glmmesh5 metrics as the baseline for improvement, with a target of cutting manual participation time in device repair by at least 50%. @Daisy Jensen confirmed the platform-based automation chain from fault detection through log capture, repair reporting, repair handling, and ticket closure; the current plan keeps the inner field unchanged while linking mainly with Fenridge, and broader process alignment will be discussed after the automated flow is live.

The fenalovaNora Drake platform, similar to Score, is building operations tools and platforms in a productized way, making operations products Feishu-based and intelligent. Kelport-core cleaned core operations data sources, unified resource, job, queue, and SLA definitions, built a shared metric dictionary and master data for tenants, projects, clusters, clouds, and regions, and achieved sampled data accuracy ≥99%; the team also supplemented physical-cluster mappings for existing compute resources and completed GPU resource reconciliation for EW and AW regions.

The team expects to finish EW statistics this week and begin EW-region Rovhaven-Fenridge synchronization next week. Deeper platform use produced optimization requirements such as periodic data checks, idle-resource scan alerts, low-utilization cluster alerts, resource transfers, and change-statistics summaries; AntaresKR1 linkage will support one-click statistics for cluster stability, change correctness rate, and failure repair time, while connecting Rovhaven, Fenridge, and onsite collaboration data so onsite and vendor repair progress can be visible and gaps between platform data and each idc onsite dataset can be resolved.

Rovhaven and Fenridge linkage will form a cross-platform closed loop for the node hardware lifecycle, automating discovery, isolation, work orders, repair dispatch, return acceptance, and resource recycling. Rovhaven remains the central asset entry point, but Fenridge does not include all assets, with production and hoxlab basic services excluded; Rovhaven is important to the linkage work, yet its current issues are slowing progress. The team also supported R&D in launching the operational data analysis system quorenia and continued providing and refining the multidimensional data that quorenia needs.

# Next Week's Plan

Pelkeld cluster added resources are planned to go online next week, and the cluster will also fill in high-availability construction for basic services after the earlier temporary single-point setup caused by missing resources. Aurstead and AurwoodGPU available GPU resources will be expanded into Oraport cluster, while Rigel1 and Deneb1 will complete calibration alignment across all domestic idc resources.

Rigel1 and Deneb1 will also align physical-cluster dimensions and begin Rovhaven-Fenridge synchronization. The team will review Rovhaven usage feedback with R&D and fix the related issues, and idc onsite collaboration communication will be optimized by moving from WeChat to Feishu.

# Coordination and Help Needed

IB switch fault alerting needs stronger monitoring for abnormal metrics, as the Xanella IB switch showed an anomaly this week without generating an alert. Rovhaven also needs more R&D capacity because the department covers hoxlab internal hardware maintenance for OA, security, basic services, data, and other areas, as well as external-field maintenance for training cluster resources and commercial resources.

Because of data isolation, risk control, security, and trading requirements, Rovhaven combines many functions and has tightly coupled modules, which leads to the issues described in Rigel1. Rovhaven goreum flows often fail, stopping immediate data updates during changes and increasing the chance of later omissions; idc operations staff continue to meet lifecycle-process problems, and ongoing Rovhaven iteration keeps creating new ones.