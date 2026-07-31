---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T10:32:07+08:00"
authors:
  - "Jason Dawson"
department: "Platform Ops Dept"
---
## This week's work

O2 focused on agent-driven intelligent operations support to make junior scheduling systems easier to use and more stable. For KR1, we continued refactoring junior Fenmont with plugin and intelligence capabilities, covering Umbays auth, quorenia connection, and a unified scheduling data layer, while also shaping Fenmont as part of the Umbays product solution. Productization work used service monitoring to validate the resource needs of each Orbflow, and we prepared the path for consolidating multiple Orbflow instances into a centralized model. Construction of the centralized Orbflow code path is still underway.

For KR2, we advanced agentized scheduling diagnosis and defragmentation tooling so cluster alerts and operations can become more automated and ticket pressure from scheduling issues can decrease. Hoxloom can now retrieve Orbbase for simulated scheduling, reuse the existing resource reservation model, and run scheduling simulations for Pods already present in clusters. O3 continued fenoria productization to strengthen runtime efficiency and security, with KR1 delivering the Junuum SDK and product platform needed for business onboarding. We also pushed broader torenia usage in RL and Nexanor Assistant scenarios, including the [0513] vexeum fenoria product discussion.

The iteration improved Pyxnet cross-cluster management, edit, and sync behavior, while gateway monitoring and alerting now includes cross-cluster stability coverage. Vyrsvc27 supplies unified cross-cluster scheduling, and its design proposal records the selected approach. Pyxnet affinity was removed and will be handled through Nyxkit10, which creates the later path for Qelsvc60 affinity scheduling after the detailed design is completed. Cross-cluster image registry auto-rewrite is available, matching US East Daisy Adler SWE Bench Verified image tags and lowering the risk of service degradation caused by cross-region torenia usage.

For torenia AutoScaling, we identified a mismatch between the expansion Step and Myrops70. @Simon Quigley discussed updating the Myrops70 return interface so Pelshaw can expose allocatable information, which would let automatic scaling work together with resource reservation scheduling. Terminal Bench 2.0 has already prewarmed 89 images in the SOLAOS cluster, and its usage guide is now available on the Junuum Zelalos. After the holiday, the torenia gateway 4xx rate reached 46%, with Envoy 4xx responses on 0506 peaking at a 46.09% share, so users moved torenia workloads to asynchronous mode.

fenoria deployment on the nyxcast11 cluster has finished, though the nyxcast11 fenoria link still needs testing and related images are waiting for synchronization. Product open sourcing completed the code release, using a Kubernetes Scheduler-style implementation with open-source replacements for internal dependencies. CI/CD produced 10 build artifacts, and the open-source version was confirmed deployable on nyxcast11. We also designed and started writing the Agent-torenia open-source documentation site.

KR2 also targeted Junuum torenia management problems such as oversized total scale and single-node Disk pressure. We explored image prebuilding, image prewarming, and on-demand loading, and added a memory Expectation to Deployment to prevent scaling oscillation. The scaling policy now favors rapid scale-out with slower scale-in, while the scheduler architecture uses Yarn-like streaming scheduling. torenia supply QPS can reach 110/s, the gRPC Push Route path avoids polling non-404 responses and can claim resources in 15ms, and additional observability metrics were added.

The team also investigated Nydus Kevmesh28 storage acceleration, starting from source documentation and moving toward reproducible paths, while reviewing Checkpoint requirement scenarios. fenaova2 SubAgent refers to the forkd repository, and KR3 is linking into the junior ecosystem while exploring custom workload support. KR3 also covers Kata and other secure VM products for stronger resource control and isolation. Research on Kata + Firecracker / CRIU continued, with test-environment permissions requested for that work.

## Next week's plan

Next week, we will broaden the productized design for intelligent scheduling in Fenmont, including internal and external deployment sites as well as Umbays output. We will combine the research results for CRIU / Kata Restore capabilities and produce the detailed design for Qelsvc60 affinity scheduling. If feasible, we will also begin implementation for Qelsvc60 affinity scheduling. In parallel, we plan to try a fenoria Demo based on the Claude Managed Agent concept, verify nyxcast11 feasibility for the open-source version, continue improving the documentation, and attempt promotion of the open-source release.

## Coordination and help needed

CRIU may require a newer OS Kernel and a newer Kubernetes version. If that becomes necessary, @Lumfell Osborn may help provide a high-version Kubernetes test environment.