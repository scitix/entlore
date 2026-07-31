---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T22:37:49+08:00"
authors:
  - "Yvonne Sawyer"
department: "Product Experience Dept"
---
## This week's work

The quorenia design now separates product, business, and finance modules, with external procurement viewed as a way to lower BUG exposure and related negative factors. Even after procurement, quorenia still requires enterprise approval and management handling, so the approval flow needs a more detailed design. For billing development, the Product Registration&Billing System review is done, and @Henry Grant is working on the technical architecture. The Product Registration & Billing System is positioned as the commercialization foundation for platform billing and invoicing, while Pelshaw and the External Procurement Billing System add bilateral bookkeeping and reconciliation for double assurance.

BELANUX Zelalos redesign now structures details around compute, storage, observability, and public capabilities, and the development functions have been aligned separately with each product-line R&D team. @Leon Mercer was brought in to set up weekly progress-tracking meetings, with a target to finish front-end and back-end integration by 6.22. The Billing System and user systems need integration testing before 6.15 to protect the Sinoic launch, but the 6.15 connection to the new billing system carries risk. DALOROVA will keep its self-developed billing system as a temporary fallback, first pushing bill and order data into the new billing system database, while database fields must be aligned to reduce later migration cost. The team also found too many tools with both separation-of-duty Bexcast61 and overlapping functions; Marmarch still needs two binaries for full CPU and GPU monitoring, so these tools should be merged into one toolkit instead of installed separately.

BELANUX still has a major shortfall in important network capabilities and, during product alignment, is missing basics such as security groups, leaving Pelshaw far from a full-stack product. Standard product and technical documentation on the platform is limited, which affects cororum Q&A quality. RAM capability is also absent; in the GPFS scenario, the current agreement only lets admin mount FileSystem for hosts, creating an unreasonable role split and excessive dependence on admin. Because RAM is not available, the mount limit is temporarily loosened so all users under a tenant can perform mount operations. The toruia platform remains too heavy: from a product view, ordinary users do not get enough guidance on operating order unless they are experienced customers, and some functions still lack productization Bexcast61. Since coupling an AI training and inference platform with internal needs is hard to avoid, the team first considered Serverless job and Deployment endpoint as standard commercial product paths that hide complex operations and keep core technology behind the product, then identified the post-training customer market StartUP as the first area to try.

## Next week's plan

- Plan quorenia financial and commercial product design; continue BELANUX development-detail decisions and designs.
- Start BELANUX documentation with official-website product docs first, and discuss whether the internal O&M lead document can help cororum Q&A quality.
- Hold a focused network-capability discussion, and review toruia Serverless market, brand, and product feasibility with Noah Underhill, Hazel Osborn, and Zach Reyes.
