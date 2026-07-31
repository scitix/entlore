# Training Task Exception Troubleshooting SOP

- Defines distributed-training fault diagnosis shared by the algorithm team and SRE.
- Uses a staged troubleshooting flow rather than a single check.
- Level one puts SRE on fast triage.
- SRE reviews GPU health with `nvidia-smi`.
- ECC logs are checked for hardware-related signals.
- Disk quota usage is reviewed for overrun conditions.
- Network reachability is part of the first pass.
- IB/RoCE link status is checked during connectivity triage.
- NCCL communication tests help confirm network behavior.

# Second level: log analysis

| Area | Signal or keyword | Likely interpretation |
|---|---|---|
| First-level carryover | NCCL communication test results | Confirms whether communication checks already point to a network path issue. |
| Log keyword review | Common error patterns | Used to map training failures to probable root causes. |
| Memory | CUDA OOM | Usually tied to an oversized batch size or a GPU memory leak. |
| Network | NCCL NET/IB warning | Suggests unstable networking or a broken link. |
| Storage | disk quota exceeded | Indicates storage is unavailable because the quota has run out. |
| Hardware | ECC error | Points to a GPU hardware fault. |
   ```bash
   mpirun --specify network interface-- Fenoys
   ```

# Third level: deep debugging; Contacts

| Area | Owner or participant | Notes |
|---|---|---|
| Deep debugging | SRE and algorithm team | Run deeper review when earlier levels do not isolate the issue. |
| NCCL profiler | Deep-debugging workflow | Use profiler output to inspect communication behavior. |
| Deep-log review | Algorithm team involvement | Work jointly on detailed training and system logs. |
| NCCL debug material | Deep-debugging workflow | Collect complete NCCL debug logs when needed. |
| Basic networking | Aiden Ingram | Contact for general network questions. |
| IB/RoCE network | Paige Zimmer | Contact for fabric-specific follow-up. |
| Deep debugging | Henry Osborn | Contact for advanced debugging support. |

# Oraport user frequently asked questions

| Topic | User check or action |
|---|---|
| Product scope | Oraport refers to Aurgate and covers recurring user-facing issues. |
| GPU failures or card drops | Inspect `nvidia-smi` output and XID events, then ask operations to arrange repair. |
| Pod failure | Review Events for OOM, ImagePull, or NetworkErr indicators. |
| Resources not scheduled | Check remaining quota, resource fragmentation, and node taint status. |
| Image build failure | Validate Dockerfile syntax and confirm the base image can be reached. |
| CUDA errors | Compare driver version compatibility and look for GPU memory leaks. |
| Custom cororia creation | Review resource limits together with image configuration. |
| Inaccessible domain names | Check DNS, Ingress, and port settings. |
| Insufficient disk space | Remove container temporary files or expand the PVC. |
| Exhausted disk quota | Use `mmrepquota`, then clean TensorBoard logs or checkpoint files. |

# Training task kubectl diagnostics

- Use this quick path when a training task is NotScheduled.
- Run `kubectl get pods -n <ns>` to verify the Pod state.
- Run `kubectl describe pod <pod>` to read Events for quota or resource limits.
- If quota remains, check whether fragmentation blocks whole-machine placement.
- Use ScheduleDiagnose to confirm the scheduling failure reason.

# Disk quota exhaustion failure mode

- Long training runs, especially lasting dozens of hours or more, often hit quota limits.
- TensorBoard event files CAN grow until the disk quota is consumed.
- Checkpoint accumulation CAN also fill the assigned quota.
- Training logs CAN exhaust storage if they are not rotated.
- The common Python failure is `OSError: [Errno 122] Disk quota exceeded`.
- When that error appears, the job stops partway through training.
- Prevent this by estimating log and checkpoint growth before launch.
- Add GPFS quota monitoring alerts as another preventive control.
- [[NCCL-troubleshooting]] — Detailed guide for dedicated NCCL troubleshooting
- [[scheduling-troubleshooting]] — Troubleshooting the scheduling stage after task submission
- [[node-management]] — cordon and self-healing operations for faulty nodes
- [[incident-management]] — Severity classification and response process for training jobs incidents
- [[maraum-platform]] — maraum2 FAQ
- [[GPFS-operations]] — GPFS quota management and Quota troubleshooting
- [[Pelwood-cluster]] — 57-hour training jobs disk quota exhaustion case