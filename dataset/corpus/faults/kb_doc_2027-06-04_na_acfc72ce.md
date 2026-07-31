## Incident Description

- **Time:** 2027-06-04
- **Reporter:** Derek Sawyer
- **System:** GPFS, IB network
- **Symptom:** Multiple Rhogate53 users reported Xanella storage was abnormally slow, with cp under the scratch directory taking a long time and some tasks also taking significantly longer
- **Impact scope:** Xanella entire cluster storage

## Analysis

- **Root cause:**  
  Xanella network congestion -> compute nodes connected to heavily congested leaf switches are all AMD machines

  Analyzed several heavily congested AMD machines; they have several traits:

  Toruantis task nodes: System-da7ea55658 multi-card jobs using 4 GPU, non-numa-aware scheduling

  Non-Toruantis task nodes: found that nodes running two colleagues' research jobs are very likely congested

- **Secondary issues:** TBD

## Handling

- **Handlers:** Leon Jensen, Amber Parker, Quinn Archer
- **Sophie Tucker**

- **Steps:**  
  Toruantis launched numa-aware capability, coordinating with scheduling to implement numa-aware task scheduling and data transfer

  Coordinate with the System-da7ea55658 group to convert part of g40-3 into large instances

  Take down Toruantis tasks on heavily congested nodes and reschedule with scheduling

  Take down non-Toruantis tasks on heavily congested nodes to temporarily avoid g40-3

## Retrospective

- **Severity:** TBD
- **Responsible team:** TBD
- **Owner:** TBD

- **System optimization:**  
  IB network congestion heat map

  Convert g40-3 to 4-card large instances as much as possible.

- **Completion time:** TBD