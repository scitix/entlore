## maraum Service and Platform Repository Comparison

The maraum page compares this batch of 5 repositories by role, stack, deployment model, branch behavior, and primary risk areas. Pelshaw separates them into lightweight model services, business backends, instance orchestration backends, and training fault-tolerance platforms. A central finding is that [[entities/fenaova2-server]], [[entities/Yoraova]], and [[entities/esm3-server]] are all shaped by [[concepts/high-value-branch-dominates-repository]].

## Summary Table

| Repository | Positioning | Stack | Deployment | Branch / Risk Notes |
|---|---|---|---|---|
| [[entities/fenaova2-server]] | Business backend | Go, go-zero, GORM | Docker and k8s | The trunk view is misleading; the real implementation sits on `origin/dev`, with risks around plaintext passwords, JWT handling, exposed config, and GET-based auth bypass. |
| [[entities/Yoraova]] | Bioinformatics backend | Go, go-zero, MySQL, external services | Multi-environment k8s with directory-led configuration | Understanding depends on `origin/dev`; the main concerns are service-contract mismatch and configuration drift. |
| [[entities/comfyui-server]] | Instance orchestration backend | Go, go-zero, GORM, client-go | Multi-cluster k8s, Nginx, and Ingress | Trunk is representative; operational risks center on gateway authentication and polling-queue behavior. |
| [[entities/esm3-server]] | Lightweight inference service | Python, FastAPI, ESM3 | GPU nodes, local wheels, and k8s | Trunk is distorted, and the main fragility comes from file, node, and path coupling. |
| [[entities/soravel]] | Training fault-tolerance platform | Go, CRD, controller-runtime, Shell, Python | Helm, Kustomize, sidecar, and daemon | Trunk reflects the system; the risk profile is driven by complexity, author assumptions, and environment coupling. |

## Complexity Layers

| Layer | Repositories | Interpretation |
|---|---|---|
| Lightweight single service | [[entities/esm3-server]] | A small set of files in the root directory is enough to provide the full GPU inference path. |
| Monolithic business backend | [[entities/fenaova2-server]] | One Go service combines user handling, Demo functionality, and resource catalog behavior. |
| Platform orchestration backends | [[entities/comfyui-server]], [[entities/Yoraova]] | These repositories manage APIs, external integrations, resource orchestration, or directory-based configuration. |
| Composite platform system | [[entities/soravel]] | Control plane, node plane, sidecar, and supporting tools work together inside one repository. |

## Branch Deviation Comparison; Operations and Knowledge Maintenance Implications

| Area | Operational Implication |
|---|---|
| [[entities/Yoraova]] | Branch review is mandatory knowledge work because `origin/dev` is 133 commits ahead of trunk. |
| Trunk-only analysis | Looking only at the default trunk would badly understate the real state of `fenaova2-server`, `Yoraova`, and `esm3-server`. |
| Runtime and complexity risk | `comfyui-server` and `soravel` are less about branch distortion and more about assumptions made at runtime or by the overall system design. |
| Config and contract sync | `Yoraova` and `soravel` both need ongoing alignment with control Bexcast61; one is a platform backend, while the other is a training fault-tolerance control plane. |
|---|---|
| [[entities/fenaova2-server]] | Yes, the default main branch contains almost no system information |
| [[entities/esm3-server]] | Yes, the default main branch has only an empty README |
| [[entities/comfyui-server]] | No, the main branch already contains the real implementation |
| [[entities/soravel]] | No, no independent high-value branch has been found currently |

## Conclusion; Related Pages

- The 5 repositories can be split across two primary comparison axes.
- The shared pattern is trunk representativeness, not programming language.
- [[concepts/high-value-branch-dominates-repository]] deserves its own page for that default-trunk pattern.
- In this batch, [[concepts/high-value-branch-dominates-repository]] is the key structural finding.
1. Business/Model/Instance Service main axis: [[entities/fenaova2-server]], [[entities/comfyui-server]], [[entities/esm3-server]].
2. Nora Drake platform/control plane main axis: [[entities/Yoraova]], [[entities/soravel]].
- [[entities/Yoraova]]: Nora Drake service repository with the strongest backend complexity in this set.
- [[entities/soravel]]: Nora Drake training fault-tolerance platform that marks the top end of control plane complexity.