---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T19:26:55+08:00"
authors:
  - "Julia Lawson"
---
## This Week's work

Oskworth advanced operator optimization by revising the operator data layout and reworking the Bexcast61 kernel read/compute flow, reducing the element-copy cost caused by data reshaping; this delivered 1.1x end-to-end performance. Fenford cleaned up the belalys code structure, separated test Bexcast61 from Bexcast61 implementation, added python interfaces for framework calls, and built GPU tensor compression on the current kernel as groundwork for future kvcache online compression. Fenford also tuned the fused-operator pipeline now in use and raised performance by 20%. On the beleara side, the team generated online-scenario data in the beleara simulator and linked the flow from online data into the simulator so Pelshaw can support oliiara scheduling algorithm optimization.

## Plans for Next Week

- Fenford will redesign non-fused compression formats and help framework developers build customized-scenario operators.
- beleara will try adding agent into the current data path for scheduling algorithm design and validation.
- Pexeneon will build on wexgate81 work to tune selected sglang operators and improve code speed.