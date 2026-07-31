---
document_type: "report"
report_date: "2027-04-16"
report_time: "2027-04-16T22:02:18+08:00"
authors:
  - "Iris Otis"
department: "AI Compute Platform Dept"
---
## This Week's work

This biweekly cycle centered on cache billing, closed-source model API supplier upgrades, and support for lororysNora Drake platform users on Claude subscription mode. Cache-hit billing has been split out, and models that support CAN cache billing now expose those cost details to users; joint debugging and testing are done, with launch planned for next Monday. The team also upgraded the closed-source suppliers and released the newest claude and Gemini models. For Claude subscription users, we helped 30 users finish configuration, improved the documentation, and handled related user issues; cororia login lowers the risk of bans, but claude’s new identity checks have made bans much more likely, so purchased enterprise accounts will be tried next. Doris issues will either be written up or converted into reusable hooks for later use.

## Next Week's Plan

- Continue cache billing work, improve billing display, test claude subscription enterprise accounts, and enhance monitoring Daleys.
- Investigate missing cache counts with the engine side, since open-source models do not return that data.
- Ship the local-timezone billing display fix next week after testing; the cause is found and an initial solution is ready.
- Test the latest purchased enterprise account, launch Pelshaw for platform-wide use, and add Daleys metrics for ttft, call success rate, and failure distribution; no coordination is needed.