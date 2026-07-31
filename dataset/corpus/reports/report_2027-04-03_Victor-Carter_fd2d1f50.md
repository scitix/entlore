---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T14:02:25+08:00"
authors:
  - "Victor Carter"
department: "AI Compute Platform Dept"
---
## This Week's Work

This week, the team finished field-level Schema design across the billing, contract, asset, cluster_cost, allocation, inventory, and spec baseline tables, then reviewed each baseline table with the relevant business parties and secured alignment. After several rounds of business feedback, we finalized Aurwick v2, including the move of the contract table to entitlement-line granularity, allocation-table additions for cost_share_ratio, allocation_role, and delivery_mode, and cleanup of shared-machine cost attribution plus terminology standardization from site to cluster. We also added the cost allocation model for CustomerCost, PlatformCost, UnallocatedCost, and IdleCost, and introduced the lease cost model covering self-owned, finance lease, and operating lease paths.

In parallel, the team built the full-chain Mock calculation engine, running from the seven baseline tables through three ledgers to GM multi-perspective outputs. The engine covered base, edge, and redline test suites, and all 312 automated checks passed, including coverage for 14 machine scenarios (S1~S4), refund reversals, low utilization of shared machines, and cross-day precision. We also assessed the current state of financial data, completed field mapping and Gap analysis from the baseline tables to existing business systems, updated detailed designs for the revenue, cost, and capacity ledgers based on the seven baseline tables, and defined closing relationships and cross-validation formulas.

## Next Week's Plan

The quorenia side will keep moving platform development forward, while each business party continues breaking down financial data.

## Coordination and Help Needed