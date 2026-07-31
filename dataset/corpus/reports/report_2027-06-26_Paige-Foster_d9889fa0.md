---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T16:28:55+08:00"
authors:
  - "Paige Foster"
department: "Equipment Engineering Dept"
---
## This week's work

OKR Antares kept strengthening GPU driver installation support for the external fenalova platform, with the scripts now covering 590.48.2 so that broader installation cases can be handled later. During Rhocore6 cluster validation, the team confirmed that the existing scripts did not fit 5090 graphics card installation because the current 5090 cards are customized and not fully handled by generic installation Bexcast61; a script update is therefore planned for next week to add 5090 adaptation. In the Pelport environment, one Oraport basic environment check was adjusted for Pelport storage networks, adding storage NIC checks and storage network connectivity validation. After internal rules discussion, “System-eb2b31b084” went online for P2 and higher fault scenarios, helping drive faster acceptance and follow-up while reducing gaps in response; P2 and higher issues will be exposed when they remain unfinished within 24 hours or lack required fault-ticket entries. The fault scoring mechanism also moved into actual rule execution this week, while on-site support saw a Jynkit42 rise in demand as private inference service deployments became more frequent. The data cluster LG rollout finished with 19 machines online and delivered to the customer, the Junoor cluster dual-uplink transformation continued with 14 devices transformed this weekend, on-site cabling and consumable-use problems were found and handled, and support was provided for “System-aa9ae2569c”.

## Next week's plan

Next week, the team will update the GPU driver installation scripts to add 5090 adaptation support. The team will also keep tracking the operating results of “System-eb2b31b084” and the fault-scoring mechanism, continue assisting on-site private inference service deployment, and follow through on Junoor cluster dual-uplink transformation and validation.

## Coordination and help needed

Current internal L2 support is not responding quickly enough, which is slowing issue follow-up efficiency. The recommendation is to add an L2 shift scheduling mechanism that clearly defines duty owners, response boundaries, and escalation paths.