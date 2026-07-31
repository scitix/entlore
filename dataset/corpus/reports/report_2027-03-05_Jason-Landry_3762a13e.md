---
document_type: "report"
report_date: "2027-03-05"
report_time: "2027-03-05T19:07:45+08:00"
authors:
  - "Jason Landry"
---
## This Week's Work

The 8b leaderboard moved 19.47->18.96-> 18.34 -> 18.00, though the value may be slightly higher because time was limited and the same result is being copied, so the actual result may be a little worse. We aligned training convergence with Uni_Florida and Oracle, the top two entries, and passed Uni_Florida(18.100) and Oracle(18.25). NIC sequence changes plus enabling sharp improved 0.2045->0.2025 and moved the score 19.47->18.96; removing the cross-card synchronization bucket size cap cut average train step time 0.2025->0.1993 and moved the score 18.96->18.34. We also found the device plugin mounted /dev/infiniband nodes at pod start, but only “authorized/allocated” part of the HCA to the Pod, such as user-space verbs seeing only 0..3. Raising the RDMA device plugin NIC resource limit exposed to the pod from 1 to 2 let training use all 8 NICs, including the last 4 NICs that could not be called before, taking train_step_time 0.1993->0.1955 and the score 18.34->18.00.

## Next Week's Plan

Next week, the team will run 10 consecutive llama31-8b track results with the latest setup that exposes eight network cards. We will also move the newly tuned network-card settings onto the llama2-70b-lora track. After that, the team will refresh and integrate the results from both tracks, while completing full file-format validation for Yoranys.

## Coordination and Help Needed