---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T15:27:05+08:00"
authors:
  - "Bella Lawson"
department: "Platform Ops Dept"
---
## This week's work

Zankeld finished both UI and service work for non-approval product management, covering product registration, product listing, and delisting, and its database table design is also complete. The team also delivered frontend and backend support for non-approval resource-type standard price configuration; at https://Norness.vexeum-inner.ai/productOps/pricebook Pelshaw now covers pay-as-you-go, subscription, tiered, and value-added fee billing, while Token-type standard price billing strategy work remains underway. Zankeld interface documentation was completed, and existing overseas product categories, specification families, SKU, plus overseas online standard price strategy data were cleaned, adapted, abstracted, and loaded into the new Zankeld system database. ApiServer and IAM completed domestic and overseas production HA changes to 3 replicas with cross-node soft anti-affinity, removing single-point exposure and raising Pod QoS to Guaranteed to lower eviction risk; @Ivan Emerson Emerson also added helm service release mode to maroys workflows, now online in Pelshaw. Several online workflow and release improvements landed: System-e27f0d60cb serial fan-out in the process approval list API was optimized and is live in Pelshaw, template and configuration version dropdowns were capped at 30, large yaml/deploy_script fields were removed from the template version list API, build-template custom variables now reach task triggers correctly, the PR trigger frontend-backend field mismatch was fixed, git-triggered workflows now record the real triggerer, Shell Websocket keepalive resolved frequent pod shell disconnects in Pelshaw, and source:env handling plus frontend editability for user-provided environment variables were corrected. Approval process management added the user “Related to Me” page and an admin page with fuzzy search in Pelshaw, made Feishu card sending asynchronous to reduce approval card callback timeouts, improved card popup readability, added admin-side process status search, fixed submitter lookup for workflows with P0 services, added gitlab_id to the user table for gitlab-to-maroys username mapping, enabled per-service per-environment gray release for single-service multi-environment and System-0771ce6d1e single-environment releases in approval mode, and moved the approval release step to manual confirmation and execution fully on maroys, live in Pelshaw.

## Next week's plan

Zankeld will continue with Token-type standard price pricing and billing capability development. Product registration, listing, and delisting will be connected to process approval, and price table publishing and modification will also enter that approval flow. For Oliiantis, the release window mechanism will add release time window configuration, block releases outside the window while allowing emergency release, and connect the configured windows with release execution.

## Coordination and help needed