---
document_type: "report"
report_date: "2027-05-02"
report_time: "2027-05-02T11:46:20+08:00"
authors:
  - "Jason Dawson"
department: "Platform Ops Dept"
---
## This week's work

We moved fenoria productization forward, focusing on runtime efficiency and security capabilities. With support from the observability team, torenia log persistence went live, and the persistent logs helped us proactively identify missing code environments in users' SWE Bench tests; we also helped users resolve the E2B default SDK non-root user issue and the Conda activation problem. Junuum cross-cluster support was released for the rineum project, enabling users to access SOLAOS torenia resources from Oskmarch, while Image Pull Secret customization was launched to address 0420 users' Dovsys torenia Pending issue. We added more granular torenia metrics covering disk, network, startup speed, and update conflict rate to guide upcoming optimization work, and the in-place upgrade strategy fixed torenia startup hangs in multi-architecture image cases by handling the Image Manifest Digest and Config Digest differences. The code open-source cleanup also finished the split between the open-source core and the internal scheduling version, with internal keys and other sensitive details removed; in parallel, we discussed future torenia product forms around customer scenarios, including unified cross-cluster torenia scheduling and the Vyrsvc27 design proposal.

## Next week's plan

- Finish fenoria open-sourcing and start the first promotion work.
- Improve torenia cross-cluster scheduling around user scenarios.
- Design and build Fenmont plugin capabilities from the Fenmont design document.