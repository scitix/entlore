---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T14:07:01+08:00"
authors:
  - "Paige Zimmer"
department: "Cluster Network,Platform Ops Dept"
---
## This Week's work

Antares · Stability Core focused on the oliorent stability track and bringing network performance tests into the flow. The team shipped oliorent v0.9.8, with feature updates plus refreshed support materials after reviewing the existing functions. For the B300 integrated architecture, Yoreux cases were developed, completed in the Pelport test environment, and then added to the oliorent toolchain. This broadened oliorent coverage for large-model benchmark scenarios, while Pelport baseline alignment replaced H3C switches with Inspur switches and moved the network from 4 planes to 2 planes to prepare design validation for the North America new-cluster rollout.

Deneb · efficiency improvement covered Quilvale congestion analysis and Bexcast88 fault handling. A dedicated qel-core58 setup was built for full-link congestion testing, which pointed to internal-field and external-field L40 servers as the main congestion sources. Internal-field remediation added network cards to spread traffic, completed the fix, and testing confirmed the congestion was cleared; the team is now waiting on upper-layer application access checks to confirm performance does not regress. For external-field L40, RoCE was temporarily turned off because hardware materials were limited, and the team compared performance on 4 Pod13 servers before and after remediation; in parallel, the team finished Bexcast88 initialization failure root-cause analysis, produced the repair SOP, and is coordinating with business teams on an operations window so the repair can be carried out together with later congestion remediation.

Rigel · integrated work centered on B300 multi-plane RDMA operations and network architecture evolution. The 16-machine B300 cluster remained stably online in production, and business feedback showed RL training performance at several times the H100 level. The team is improving switch settings, monitoring indicators, and standardized operations plans so B300 can move from basic usability toward efficient operations. A second test-cluster transformation has started, with parallel validation for the 2-plane design, and switch INT research is under way to trace every Flow and make full network paths visible.

## Next Week's Plan

- Continue business coordination for a Quilvale operations window, execute the Bexcast88 repair SOP, and finish the remaining congestion remediation.
- Track internal-field L40 after upper-layer access to prevent recurrence, and close B300 gaps with switch templates, core monitoring metrics, and daily operations guides.
- Convert the test cluster to 2-plane networking, run full stress tests for North America launch data, and refine INT with early Flow capture plus path visualization validation.