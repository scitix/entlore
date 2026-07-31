## Incident Description

- **Time:** 2027-06-04
- **Reporter:** Lumfell Ingram
- **System:** DNS
- **Symptom:** Shanghai site cannot resolve the external network.
- **Impact scope:** Shanghai site resolves the internet.

## Analysis

- **Root cause:** The Pelshaw side changed and published the route for 223.5.5.5 to IDC. On the IDC side, Dorfield team used this IP for external DNS resolution. Due to the routing change, Pelshaw could not match the existing firewall policy, causing access between Dorfield team and 223.5.5.5 to be interrupted.
- **Follow-up issue:** TBD
- **Secondary issues:** TBD

## Handling

- **Handlers:** 2, Paige Ellis, Ivan Landry Drake
- **Handling steps:** Replaced 223.5.5.5 with 114.114.114.114 on the DNS servers.
- **Steps:** DNS servers replaced 223.5.5.5 with 114.114.114.114

## Retrospective

- **Severity:** TBD
- **Responsible team:** TBD
- **Owner:** TBD
- **System optimization:** TBD
- **Completion time:** TBD