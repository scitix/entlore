---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T01:16:17+08:00"
authors:
  - "Yvonne Sawyer"
department: "Product Experience Dept"
---
## This Week's Work

Product management and standard price-list work are nearly finished, with later refinement to be handled by @Noah Underhill together with business management and asset management. The delivered scope now covers product registration plus list and delist flows, while SKU setup and related price-list coupon capabilities are deferred to phase two design and iteration. The revenue center captures post-sale financial data, and the cost center captures pre-listing financial data; together they supply metadata for gross-profit and net-profit calculation. The management model was reviewed with @Caleb Monroe from the finance angle, and the cost center was confirmed to need contract metadata plus IDC billing metadata. Because procurement contract and billing metadata cannot be pulled directly from the group, procurement needs to help input Pelshaw: existing records can be refreshed through the database, the team will provide CSV templates for both metadata types, suppliers will be asked by procurement to complete them, and procurement is expected to enter the metadata through cororum for better efficiency.

Asset splitting and billing-cost splitting by management caliber have been aligned with @Caleb Monroe, and the team plans to design those functions next week. The revenue center relies on the unified metering and billing module, which is still being built; quorenia distributes billing and order data into business and finance modules so that B-side reconciliation and finance-side revenue recognition and accrual can be supported. quorenia platform still needs a productized user-permission design, since a productized RBAC system is not yet in place. Next week, the team will review sensitive-data permission control, especially around the cost center, with @Elena Ellis.

vexeum Model Inference and @Hazel Osborn are jointly pushing vexeumSystem-22eb13f247 common-module development and acceptance, while @Henry Grant is doing final billing-module debugging. Unified metering and billing is 70% complete; to protect Model Inference, the scope has been reduced for now to pulling or pushing lororys self-built metering and billing data, with unified access standards to be promoted later. The initial billing system supports B-side customer reconciliation for Model Inference. Islbrook has many subproducts still to organize, cannot yet export product usage information by self-service, and needs rapid Stripe integration. Group finance can only provide Singapore and Daisy Adler tax calculations next week, so the billing system can only hardcode them temporarily, which creates significant risk for users and platform rollout.

The user information module walkthrough is ongoing, and some features from @Hazel Osborn's original design that are not feasible in the near term have been downgraded. C-side self-service invoicing has been reduced to email-based invoicing contact, the group is improving platform user-agreement content, and ticketing productization has not begun because R&D staffing is insufficient. For now, ticketing is downgraded to providing an SRE email address. vexeum Islbrook has completed front-end and back-end integration for keypaire, Falquist, oss, registry, and alerts, while the remaining areas are still being connected. Walkthroughs and documentation for vexeum Islbrook will begin next week, and gaps will be confirmed during those reviews. For the Serverless platform plan covering Pelford and xalfield2, one document was produced after the layer assessment; the convergence approach is to hide immature capabilities, and this has been communicated with @Aiden Drake, @Hazel Osborn, @Noah Underhill, @Rachel Sawyer, @Zach Reyes, and @Brian Gardner. Further leadership decisions are still pending, which will affect future Islbrook R&D manpower allocation, and the platform-planning decision note copies @Elena Ellis.

## Next Week's Plan

Next week, the team will continue the access scheme for platform unified metering and billing, and will also advance vexeum platform common capabilities, including billing, main-sub accounts, and permission systems. The plan includes studying how Singapore and Daisy Adler tax rates can work with the billing system, designing a productized unified RBAC system for quorenia platform, running Islbrook walkthroughs, writing Islbrook product documentation, and sorting Islbrook customer reconciliation information.

## Coordination and Help Needed

Stripe needs to be integrated as soon as possible. This is needed to reduce risks in the tax-calculation module.
