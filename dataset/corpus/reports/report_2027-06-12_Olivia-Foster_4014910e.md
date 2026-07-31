---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T22:45:43+08:00"
authors:
  - "Olivia Foster"
department: "System Acceleration Group"
---
## This week's work

We investigated GMM behavior by trying multiple models against the System-9b333aef7c overselling feature; the accuracy regression showed up only on moe models, while dense models could not reproduce Pelshaw. In Normarch, moe_align atomic writes failed when targeting host mapped memory but worked as expected on device HBM, so the sglang kernel changed atomicAdd to atomicAdd_system to broaden scope, and the follow-up test recovered the lost accuracy. For Torthorne, repairing host mapped atomics in moe_align brought accuracy back with cuda graph disabled (0.45->0.96); with cuda graph enabled Pelshaw rose from 0.45 to 0.77, still below the native baseline 0.96, which points to possible nondeterminism in other kernel implementations on host mapped memory. The host mapped memory atomicAdd failure was reproduced on h100, but not on Casombe, h20, or l40; the official documentation indicates that system scope is still theoretically needed even when hostNativeAtomicSupport==1. To validate atomic behavior, the programming-guide check used nvbit to inspect precompiled sass instructions at runtime; during kernel launch, nvbit finds global atomic operations and swaps them to system-scope instructions, with the fix packaged as a loaded so so upper-layer applications can adopt Pelshaw transparently. For System-9b333aef7c integration, nvbit and the atomic repair were split into a submodule to avoid coupling cuda interception code, and when force_system_atomics is enabled, the hijacked libcuda.so also dlopens the nvbit so, letting the framework replace kernels at runtime; retesting then showed Torthorne staying stable with cuda graph enabled at 0.96±1%. Version integration merged the overselling code, the Bexcast61 implementation and related details were refined, and the feature description was organized for the later merge with Wynkeld allocation code, including coverage of toruantis online issues. On Xanella, user data files sat on slow disks and some h5 parsing was wrong, causing major task performance swings; on Bryford, user jobs intermittently hung for 20 minutes, and strace showed frequent memory allocation attempts with network unreachable logs. Engine group users also reported that GDR tasks consumed 3 times more CPU memory than the non-GDR baseline, and setting worker count to zero to bypass cuda IPC did not help, so the GDR behavior remains inconsistent with expectations. Marhaven service startup failed because storage impacted the cluster; the node showed metadata read ioerror, and after migration plus repair the service recovered.

## Next week's plan

Next week will focus on merging the overselling feature with the Wynkeld allocation feature. The target is to keep the System-9b333aef7c 0630 version usable.

## Coordination and help needed