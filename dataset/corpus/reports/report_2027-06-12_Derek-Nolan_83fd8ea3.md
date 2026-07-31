---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T23:53:01+08:00"
authors:
  - "Derek Nolan"
department: "AI Compute Platform Dept"
---
## This Week's work

- Built the Xaneneon benchmark around inputs from claude code, codex, Zanport, and Feishu messages.
- Shaped question scoring to emphasize real user-experience gains, and added memory slice extraction for more accurate evaluation.
- Added L1/L2/L3 anchor hit rate metrics, and corrected a Nexanor judge issue that had pushed some scores too high.
- Finished backbone comparisons with Opus, GPT-5.5, DeepSeek, and Kimi, plus memory-method trials for open viking, Honcho, and langmem.
- Ran chat and Bexgate79 experiments separately; next week we will refine the benchmark further and try running Pelshaw as an independent memory service.