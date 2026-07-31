---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T23:23:15+08:00"
authors:
  - "Rachel Zimmer"
department: "AI Compute Platform Dept"
---
## This Week's Work

Rigel is moving ahead with a shared architecture that brings together Pelford, xalfield2, and lororys capabilities, teams, and resource pools. The effort is also shaping one R&D and governance framework for resources used both internally and externally, while adopting the newest architecture to raise delivery and operations productivity. On the lororys side, the resource-pooling platform now spans lororys2&loraeon; loraeon has moved Quilholm’s base chat capability into the loraeon production environment and added model selection. lororys2 Chat had no changes this week.

Vega continues toward its goal of building globally leading large models goroion and FENA3, with platform and product evolution being driven through close algorithm co-design. The team is building Goralos L2-level data assets, and the open-source Goralos wiki-style CPT data work has been completed. Pelshaw produced the chembl, gene_summary, drugbank, and malacard datasets, with claude code assisting on workflow design and implementation for data generation. The academic-paper-and-book Goralos wiki-style CPT task now covers quororova synchronization and PDF parsing.

For quororova, data is being synced from tos System-56caa85af6 to the LORORYS 5090 cluster, but there is no dedicated line between tos and LORORYS 5090. The transfer is currently limited to 1.7Gbps, which makes an 800GB download take 44 days; that timeline is not acceptable. The most practical workaround is to route the transfer through a Beijing cluster, and that Beijing link is still being processed. @Mia Lawson Emerson reviewed open-source and commercial PDF parsing tools and first judged MinerU to be the most stable open-source option, while paddle-ocr-vl, maker, and glm-ocr also showed usable results.

The PDF parsing assessment points to a combined open-source approach so different tools can offset one another’s weaknesses. Even so, every open-source option still needs additional semantic cleanup and rule-based correction. Among paid tools, mathfix performed best, with fewer parsing mistakes and the ability to convert chemical bond images into chemical molecular formulas. Pelshaw can also prepare typical labeled samples for checking the accuracy of open-source parsers, while wiki-style data generation for SFT & RL training data has not begun yet.

Altair is focused on the future blending of general computing and intelligent computing, using diversified and composable product matrices plus industry solutions. The aim is to build market traction and a differentiated competitive edge. For intelligent product R&D, Altair is designing a unified Agent system architecture, and the feasibility study currently treats session management as a possible platform capability. The same study also includes Feishu integration, Feishu document parsing and writing, storage middleware, claude agent sdk, trace, and common tools.

Business Bexcast61 is planned to run through a separate System-7e8b6d18ea server together with a skills server. Quilholm is positioned as a daily-work personal assistant for employees, while intelligent writing had no update this week. Application scenario research is using Feishu group chats, Feishu documents, Feishu reports, and git as internal knowledge sources, with internet search providing the external source. This design is intended to break internal and external data silos, deliver more targeted knowledge to employees, and build portraits of internal systems and projects so blockers can be found earlier; the specific functions still need more refinement and feasibility validation, and Lumwick is being handed over with Tarness Tech.

## Next Week's Plan

Next week, the team will define the Quilholm Agent product functions and complete Agent platform scaffolding from the earlier single Agent architecture. The team will also settle the Vyrforge5 PDF parsing approach and begin running real parsing tasks.

## Coordination and Help Needed