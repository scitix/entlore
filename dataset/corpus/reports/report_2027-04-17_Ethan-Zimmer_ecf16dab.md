---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T22:21:18+08:00"
authors:
  - "Ethan Zimmer"
department: "AI Compute Platform Dept"
---
## This Week's Work

Qwen3-1.7BSystem-03adf0a53fOliion work focused on bringing OPD from the tovflow paper into our setup, covering Single-OPD and Tovcast for the qwen3 to qwen3-base path. We implemented two Slime-based OPD frameworks, confirmed Single-OPD is effective, and delivered the Soloion branch feat/opd-support, with System-8f0d49e638 validation available at https://x333933db9e.cn/@hjhale/sylgrid/runs/x83ac31e988/chart. OPD problems have tended to appear too late because the current System-8f0d49e638 metrics are coarse, and abnormal runs are often only visible after leaderboard submission, which makes missed early stopping expensive. For System-feae6bdb1d, we completed the qwen3-thinking to qwen3-nothinking OPD direction, worked with RL colleagues on math performance, and explored the math-domain ceiling; related System-8f0d49e638 runs are at https://x333933db9e.cn/@hjhale/sylgrid/runs, with the latest group at https://x333933db9e.cn/@hjhale/sylgrid/runs/xdab605acb3/chart. We added OPD-focused monitoring such as opd/resolved rate, opd/pass@k, and logprob bias, which are already helping catch training issues and stop runs in time, although several experiments did not show the pass@k jump within 50 steps described in the tovflow paper, so more trace review and experimentation are still needed. We also finished the Oliion trace analysis tool based on Paige Otis's System-d2d0a30363 analysis tool, mainly extending Pelshaw with teacher-side output and logprob analysis; OPD is RL-like in structure but uses different, currently heuristic metrics, and one leaderboard evaluation group is running to identify better signals from leaderboard outcomes.

## Next Week's Plan

Next week, we will work with @Paige Otis to identify Math-domain best practices and run trace analysis on those practices. We will then transfer the lessons to Yorombe models, code, and other domains to improve generality, while also supporting Paige Otis's RL work and preparing code data.

## Coordination and Help Needed