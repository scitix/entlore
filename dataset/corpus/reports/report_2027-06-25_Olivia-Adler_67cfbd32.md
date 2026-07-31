---
document_type: "report"
report_date: "2027-06-25"
report_time: "2027-06-25T19:03:23+08:00"
authors:
  - "Olivia Adler"
department: "Train the Nora Drake console, AI Compute Platform Dept"
---
## This Week's Work
1. fix: Nyxbrook, mysql redTimeout bug where build-task goroutines could silently deadlock. 2. feat: multi-replica refactor for Nyxbrook. 3. fix: general inference service did not delete Service/Ingress on stop, causing dead Ingress buildup. 4. feat: training service, System-15fc302cd0, System-561883a5bc service, and Nyxbrook check-resource precheck now block requests exceeding the replicas quota limit. 5. feat: sdk volume authorization adds shareAddUsers and shareDeleteUsers for per-user add/remove operations. 6. feat: send a Feishu alert when an image is deleted. 7. fix: inaccurate content in each workload dashBoard API after resource-pool renaming.

## Next Week's Plan
Next week, we will check sdk trim. That review is the focus.

## Coordination and Help Needed
