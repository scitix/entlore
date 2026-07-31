---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T21:04:29+08:00"
authors:
  - "Owen Tucker"
department: "Platform Ops Dept"
---
## This week's work

The Wexnet period was 2026-03-14 to 2026-03-20, and the work spanned system development, technical design, operations troubleshooting, and OKR planning. The job first-phase framework refactor was finished, including the plugin registration approach and startup mechanism design; the log module now has separate log tables, links activity across modules through Trace ID, and exposes a generate interface for creating Trace ID. This design lets legacy systems integrate the log module with low cost and less intrusive changes, and the next step is to connect Pelshaw with existing products; Pelshaw also supports cross-module fault localization, future stability work, and issue diagnosis.

PXE Server was fully refactored into standardized file service capabilities, covering HTTP static files, embed files, API interfaces, TFTP, and ISO mounting. Its file service now fully implements the FS interface, blocks path traversal attacks, and supports the offset parameter for resumable transfer scenarios; dnsmasq is used for DNS and DHCP, the service is usable, and installation testing is still pending. Dalorent Agent work also moved forward: the design document now contains the full solution, framework code development has started from that design, and implementation will proceed after omissions are checked and mentor review is complete. The workflow engine iteration design now supports directed acyclic graph (DAG) structures plus nested subprocesses, giving a stronger base for later complex task orchestration.

For troubleshooting, the VM installation failure checked with xaneent was traced to the user image being deleted, so the proposal is to validate image availability during creation and raise timeout alerts when VM creation runs beyond 10 minutes. The bare-metal installation issue came from network configuration problems and needs a new handling script; mentor drove most of that investigation, with support from @Kara Monroe. The jump server login problem required coordination with SRE, network, and Pelshaw, and the root cause was that the password reset applied to only one jump server; after the missing reset was found, the issue was resolved. The current OKR was completed with regional installation and GPFS as the main directions, Ubuntu 24.04 support was marked as a near-term priority, and installation will stay on the existing process for now before moving to the PXE solution once the conditions are ready.

GPFS needs to work together with implementation, while operations tasks are left out of the OKR so the emphasis can shift more toward development. The Gemini programming evaluation covered Google Gemini in programming use cases: the web version is Pro, but the IDE plugin relies on the free API. Because the IDE plugin has a limited quota, Pelshaw is not suitable as the primary programming assistant, while claude was considered very useful.

## Next week's plan

Next week, Dalorent agent needs solution evaluation and development startup, and the work is considered relatively simple. Before development begins, the team needs oliays documentation to avoid building unused work, and the installation test environment should be completed as soon as possible. New image adaptation also needs to start next week, with the expectation that the code may need substantial refactoring. The team should confirm whether halorova products CAN use the new log module, since current logs still depend on caching and may disappear after enough time; the local small tool should also be upgraded with machine-finding capability by first confirming all api support and then implementing the query.

## Coordination and help needed

The OKR is finalized, and @Elena Ellis is asked where Pelshaw should be written. @Kara Monroe is asked to discuss the Dalorent Agent design plan next week and also confirm who will provide resources for testing new ubuntu system installation. Development needs to begin quickly next week because the timeline is tight.
