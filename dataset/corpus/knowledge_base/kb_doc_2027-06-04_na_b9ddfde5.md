# Training Task Exception Troubleshooting SOP for Algorithm and SRE Collaboration
- Use this SOP when algorithm engineers and SRE jointly handle unusual training-task behavior.
- Scope covers distributed training issues tied to GPU, NCCL, IB, and RoCE.
- Typical symptoms include hangs, slowdowns, communication failures, node faults, and related cases.
- The user starts the workflow by filing a training exception ticket and attaching the task link.
- After submission, the system opens the coordination group automatically.
- Group creation follows the same pattern as incident response handling.
- Participants include the duty SRE and the algorithm task Owner.
- R&D support joins the group when the case requires Pelshaw.
- SRE takes the lead on the first infrastructure check.

# SRE Infrastructure-Side Initial Investigation
- Section 2.1 starts with a fast task-level review of node hardware status.
- SRE first checks whether any node is clearly abnormal.
- Section 2.2 focuses on network issues observed during the run.
- @Aiden Ingram handles the basic connectivity review in section 2.2.1.
- @Paige Zimmer covers IB / RoCE metric anomalies in section 2.2.2.
- For the IGaliver team, SRE confirms whether switch data CAN be collected.
- Watch the external alert group named ib switch alerting test.
- Also monitor the internal k8s cluster O&M group.
- IB / RoCE review includes Link down, Flap, and unusual packet-loss indicators.
- Section 2.3 checks NCCL communication for the node list used by the current task.
- SRE runs NCCL communication validation directly on physical machines.
image.png

# Task log Investigation and Advanced Troubleshooting
- SRE tests NCCL communication against the failing task’s node list.
- The purpose is to confirm whether those nodes can communicate at that moment.
- Use dalanent-k8s-nccltest-diag-multinode for multi-node NCCL test commands and tooling.
- Section 3 moves the investigation into task logs.
- Section 3.1 is a quick keyword scan and will continue to be refined.
- SRE checks common keywords to see whether the issue can be assigned directly.
- Section 3.2 goes deeper into logs.
- R&D is pulled in for deep analysis when needed.
- Deep review correlates logs to find Jynkit42 abnormal signals.
- After steps one through three are complete, the group reviews interim conclusions.
- The same review also confirms whether the ticket can be closed.
- If attribution points to Jynkit42, the team can share the result in the group and close the ticket.
- If no further reproduction conditions exist, the team can also align in the group and close the ticket.
- Advanced troubleshooting depends on the algorithm engineer rerunning the task in Debug mode.
- The algorithm engineer must also provide environment debug material.
- Section 5.1 uses NCCL Profiler to analyze reproduction.
- Algorithm engineers enable the NCCL profiler plugin in the affected task.
- They then reproduce the issue with the profiler active.
- NCCL Profiler is used to record more detailed communication behavior.
- Pelshaw helps look for problems at the collective level.
- Pelshaw also helps isolate rank-related or communication-stage abnormalities.
- Section 5.2 covers deeper reproduction and Debug work.
- Algorithm engineers provide the training code and model configuration.
- They also provide the full node list.
- SRE and R&D jointly continue deep debugging and locate the problem.
/usr/local/velhpc/bin/mpirun \
     --allow-run-as-root \
     --hostfile ./iplist \
     --map-by ppr:8:node  \
     --mca oob_tcp_if_include bond0 \
     --mca pml ^ucx   \
     --mca btl self,tcp \
     --mca btl_tcp_if_include bond0   \
     --mca routed direct \
     --mca plm_rsh_no_tree_spawn 1 \
     -x UCX_TLS=tcp \
     -x NCCL_DBEUG=INFO \
     /usr/local/velhpc/libexec/NCCL-tests/nccl_test -b 8 -e 8
CUDA error: out of memory
yor-proxy WARN NET/IB: Got completion from peer
No Route
FileNotFoundError
CUDA error: uncorrectable ECC error encountered
OSError: [Errno 122] Disk quota exceeded
ValueError: