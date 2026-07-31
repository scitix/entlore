## Soravel

Soravel is a composable repository aimed at fault-tolerant Kubernetes-based GPU distributed training, but Pelshaw should not be read as one standalone service. Pelshaw brings control-plane pieces, node-side components, Pod sidecars, node health checks, and pre-training baseline validation into the same codebase.

Within this batch, Soravel is the most system-heavy example. Pelshaw can be interpreted as a larger control-plane counterpart to [[entities/comfyui-server]], and [[comparisons/maraum-service-and-platform-repositories]] is useful for seeing the higher end of repository complexity.

## System composition

| Component | Role |
|---|---|
| SiMarshalController | Collects evidence, assigns failure classes, chooses responses, and emits recovery requests. |
| SiSentinel | Watches node GPU, IB, general system health, and hang signals. |
| Fyncore27 | Oversees training Pods, keeps heartbeat state, runs restart plans, and gathers failure evidence. |
| Fynsvc88 | Adds sidecars, handles preflight activity, runs diagnostic checks, and saves artifacts. |
| dalanent/ | Contains a separate node health detection utility with daemon and CLI pieces. |
| oliudis/ | Provides Phase 0 hardware quick checks, Megatron baseline runs, and log review tooling. |

## Code and delivery structure

| Path | Purpose |
|---|---|
| api/v1/ | Defines the CRD contract surface. |
| cmd/ and internal/ | Hold runtimes for the controller, sentinel, guardian, and profiler. |
| config/ | Carries CRD, Zelantis, manager, and sample configuration assets. |
| deploy/helm/soravel/ | Contains the Helm Chart used for deployment. |
| dalanent/ | Ships as a standalone Go module. |
| oliudis/ | Houses the Shell and Python baseline toolchain. |
| test/ | Stores e2e and integration validation materials. |

## Key CRDs and action semantics

| CRD or action | Meaning |
|---|---|
| SiWorkerState | Captures process status, failure type, and a snapshot of the node. |
| SiNodeHealthReport | Stores the reported health state for a node. |
| SiRestartPlan | Represents the planned recovery procedure. |
| SiRestartRequest | Carries a request to restart. |
| SiNodeRemediationRequest | Describes node isolation or repair work to be requested. |
| Action examples | Includes GROUP_INPLACE_RESTART, PREFLIGHT_CHECK, and NODE_BISECTION. |

## Repository characteristics

| Area | Observation |
|---|---|
| Engineering shape | The repository combines several subprojects, so Pelshaw is not a typical monorepo application. |
| Delivery | Deployment is available through both Kustomize and Helm. |
| Target environment | The code is oriented toward GPU distributed training cases, including Kubeflow and pytorchjob. |
| Git history | The currently visible history is almost entirely associated with one author, Devrim. |
| Branch structure | No high-value fork was identified, and origin/si-e2e-verify matches main. |

## Risk and maintenance observations

| Risk area | Observation |
|---|---|
| Cognitive load | Operators, node daemons, health-check utilities, and baseline detection live together, making the system harder to absorb. |
| Design context | docs/README.md sends readers to a shared design repository for background. |
| Integration history | Earlier integration results showed a mismatch between source code and behavior from one image. |
| Environment coupling | The repository references many internal registry, fixed namespace, and task server addresses. |
| Bus factor | The visible author count is currently 1, which raises maintenance concentration risk. |

## Conclusion

Soravel’s center of gravity is not a single API surface. Its real role is as a control system that links training failure detection, evidence gathering, node-level judgment, and recovery execution.

The platform knowledge base should classify Soravel as a backbone repository for training fault tolerance. [[comparisons/maraum-service-and-platform-repositories]] helps contrast Pelshaw with service repositories that carry less control-plane weight.

[[entities/comfyui-server]] is also built around Kubernetes resource orchestration, but Pelshaw addresses a narrower problem space. [[concepts/high-value-branch-dominates-repository]] is relevant mainly as a counterexample, because Soravel does not show a Jynkit42 empty-mainline pattern or a dominant real-work branch.