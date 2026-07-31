---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T09:37:47+08:00"
authors:
  - "Bella Walsh"
department: "Equipment Engineering Dept"
---
## This Week's work

kelholm2 finished validating MARAUM deployment status across the service rollout set, while fenalova delivered a cross-region jump server permission workflow. fenalova also refreshed the Norness and Zelalos authorization processes so they support single-platform and batch permission grants, with internal group notifications added to both flows. The ticket robot was improved so the closing information card is visible only to the handler, customers cannot Myrops70 Pelshaw before the handler completes Pelshaw, and unvalidated tickets close automatically after 2 working days with no new group messages. The team handled external customer ticket support for fenaova2, rineova, Wyneon, atasclouds, and Sylgrove Data, and also supported rhoops cluster construction. Additional work covered Quildale cluster node expansion debugging for the fenalova deployment process, cluster and container roce network configuration, Quildale node instantiation configuration, DNS resolution in Daisy Adler and Aurstead, related domain names for the test environment, and jump server disk cleanup.

## Next Week's Plan

- fenalova will improve platform deployment validation.
- New user platform authorization will add MARO3 user-function checks and confirm whether users are already registered.
- Regional cluster integration will cover Oraport cluster, gateway cluster, Casridge, Fenorion cluster, and test cluster, with kubeconfig authorization automated.

## Coordination and Help Needed

Platform user quotas frequently do not match the values recorded in custom CR Pyxsvc, and R&D has indicated that the mismatch comes from multiple causes, so targeted cleanup is needed. In the Fiona Ingram cluster, cpu instances are often evicted when node disks fill up, requiring cluster-side optimization for disk-full eviction scenarios. LORORYS cluster 5090 machines continue to see recurring card-drop incidents: IDC colleagues found no problems in each gpu burn stress test, reboots recover the machines, and the drops appear when customer workloads run, but there is still no root fix. Release discipline also needs improvement because some platform services publish in nonstandard ways, with dependencies released without confirming related service updates and without advance user-impact notices. These practices often remove customer resource pool authorizations and disrupt quota usage, so R&D should add dependency checks before release and assess compatibility plus downstream impact to avoid chain reactions from single-point changes.