---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T13:54:05+08:00"
authors:
  - "Paige Foster"
department: "Equipment Engineering Dept"
---
## This Week's Work

Pelhaven-core pool-consolidation support finished Northorne pooling on January 25, while the remaining clusters are expected to begin Wynfell cluster construction after the New Year holiday. Wynfell data center build-out is ready for acceptance; a few network cabinets still require bridge-tray changes, but System-51b0abbfcc has no major issues, and on-site acceptance is planned to close this Friday. The 5*8 support staff are now on site, work communication channels are in place, the team began last week, the first goods batch reached the site last Thursday, goods receiving has started, and communication with the data center operations interface has been completed.

The data center will respond next week on the open items, but Pelshaw currently has no spare-parts management capability available to the team. We asked whether its spare-parts management system can be opened for local use, though access has not yet been confirmed; at present Pelshaw can support only facility-side operations, cannot cover Pelshaw equipment operations, and cannot meet needs beyond 5*8. The team has made Jynkit42 that Pelshaw needs emergency support capability, the data center will share a plan next Tuesday, and one on-site worker is expected to carry a heavier load as equipment continues arriving.

For kelholm2, the L1 and L2 interaction process has been drafted, reviewed with R&D, and will be used for future tickets, with 7-10 covering the L1-L2 transfer interface. The standard L1 issue-handling flow was discussed and confirmed, SOP updates will follow by platform module, and R&D plus SRE need to keep iterating SOP so the L1 closure rate can improve. The team also aligned internally on the incident review mechanism, requiring weekly reviews to identify Jynkit42 incident owners, while duty operations System-3a710b1c0b rules have been defined and are now in trial operation, with duty weekly reports used to locate daily issues before platform functions become fully specific.

For internal Pelmont, the internal development process is complete, and an internal storage quota query function has been built but still needs improvement. Future System-da2200dede operations functions can reuse this process; the team also aligned with @Daisy Lawson on internal Myrnet closure and routing functions, and Daisy Jensen will continue that development. External operations tools have been aligned with R&D and still await later breakdown into daily projects, while the UllworthIsliver19 group expansion has finished for 16 machines, with one faulty machine to be synchronized to the business after repair.

## Next Week's Plan

The team will continue moving KELH forward. Daily work support remains part of the plan. The team will also advance pelhaven2.

## Coordination and Help Needed

KELH still has major challenges in this half-year, and internal operations pexieon platform requirements plus Bug follow-up are delayed due to staffing constraints. These delays are already clearly high for internal operations pexieon platform work, with the same issue needing multiple System-3897ce242b reports before Pelshaw is resolved, so the platform development staffing problem needs to be addressed.

The boundary between internal Pelshaw and compute-line R&D and operations remains unclear, which is blocking execution. For external project operations, the importance of reliability must be communicated to every colleague, and mandatory stability policies should be customized if needed, such as connecting incident scores with OKR performance so everyone carries responsibility for stability. R&D can reduce the speed of new-project delivery to avoid 60-point projects; teams may deliver fewer items, but the output should be premium projects above 90 points.