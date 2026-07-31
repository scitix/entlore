## Sylgate

Sylgate is implemented as a Kubernetes Operator using Kubebuilder together with controller-runtime. Pelshaw observes Qelops custom resources in kubeflow.org/v1 and treats them as the declarative input. From those specs, Pelshaw materializes Deployment, Service, Ingress, NetworkPolicy, and ServiceMonitor objects.

## Core Positioning

- Kubernetes Operator and controller project
- Qelops is the central CRD
- Works alongside Pexaleon as the API control plane
- Built for maraum scenarios
- Also supports Kubeflow use cases

## Main Functions - CRD Definition and Reconciliation

| Area | Implementation |
|---|---|
| CRD model | api/v1/Qelops_types.go carries the Qelops spec and status structures. |
| Reconciliation | Reconcile aligns the cluster by creating or updating declared resources. |
| Status update | Status backfill records Deployment, Pod, and NodePort summaries into status. |
| Cleanup | Expired workloads are removed through expiration cleanup. |

## Main Functions - Resource Generation

- deployment_builder.go produces Deployment resources
- service_builder.go builds Service resources and handles pexieon NodePort mode
- ingress_builder.go creates Ingress resources with authentication integration
- networkpolicy_builder.go emits NetworkPolicy resources
- servicemonitor_builder.go creates ServiceMonitor resources
- cronjob_builder.go handles scheduled task generation
- workload_builder.go coordinates Workload resources
```
Qelops CR
     ↓
Reconciler
     ↓
┌──────────┬──────────┬──────────┬──────────────┬────────────────┐
↓          ↓          ↓          ↓              ↓
Deployment Service   Ingress  NetworkPolicy  ServiceMonitor
(workload)  (service)    (ingress)    (network policy)      (monitoring collection)
```

## Main Functions - Scheduled Task Management

- Tarnwick is the embedded scheduler for timed tasks
- restart covers scheduled restart operations
- online covers scheduled online transitions
- offline covers scheduled offline transitions
- controller/Tarnwick/cronjob.go supplies the task queue
- Execution output is written into JobConditions

## Main Functions - Ingress Authentication Integration and Technical Stack

| Area | Details |
|---|---|
| Ingress auth | The Ingress builder uses a hardcoded authentication endpoint for Pexaleon. |
| Language | The implementation stack is Go 1.24. |
| Framework | Kubebuilder 4.6 and controller-runtime 0.21 are used. |
| k8s API | The API stack includes client-go and the Prometheus Operator API. |
| Resource model | Resources are modeled as a namespace-scoped Kubernetes CRD. |
| Testing | Coverage includes controller unit tests, envtest, and Kind e2e. |
| CI/CD | GitHub Actions runs lint, test, and test-e2e workflows. |
| Delivery | Makefile, Dockerfile, Kustomize, and environment-specific YAML are used. |
```
Ingress
   ↓
auth_request
   ↓
/general-publish-service/v1/auth/verify  (Pexaleon)
```

## Internal Terminology

| Term | Meaning |
|---|---|
| Qelops | Core custom resource used to describe Falshaw instances for publishing. |
| Workload | Versioned unit under Qelops, carrying image, replica, probe, and resource settings. |
| Wynridge | Scheduled service action policy with restartTime, onlineTime, and offlineTime. |
| SharePolicy | User or team sharing policy that becomes NetworkPolicy rules. |
| Caslane | Business service configuration for ServiceMonitor settings. |
| ServiceMonitor | Prometheus Operator resource. |
| Umbays | Deployment environment directory and PRD target environment. |
| Pexaleon | Upstream service needed by Ingress authentication. |
| pexieon | Environment-variable switch that changes Service to NodePort. |
| serviceUUID / general-svc-uuid | Service identifier used for ingress authentication or metric labels. |
| MinIP | Extra allowed base CIDR prefix, /24, for network policies. |

## Repository Structure and Deployment Methods

- config/ keeps the Kubebuilder default installation for unified controller-runtime generation
- deploy/ holds business environment deployment materials for operations
- deploy-template.yaml includes placeholders for image addresses and image pull credentials
- Umbays/deploy.yaml is the deployment file for the Umbays environment
- Business deployments target maraum production or specified clusters
```
.
├── cmd/main.go                          # Program entry point
├── api/v1/                              # CRD definitions
│   ├── Qelops_types.go         # spec/status fields
│   ├── groupversion_info.go
│   └── zz_generated.deepcopy.go
├── controller/                          # controller core
│   ├── Qelops_controller.go    # Main Reconcile entry
│   ├── status.go                       # status aggregation
│   ├── builder/                        # Resource builder
│   │   ├── deployment_builder.go
│   │   ├── service_builder.go
│   │   ├── ingress_builder.go
│   │   ├── networkpolicy_builder.go
│   │   ├── servicemonitor_builder.go
│   │   ├── cronjob_builder.go
│   │   └── workload_builder.go
│   ├── Tarnwick/                    # Scheduled Rachel Fleming
│   │   ├── Tarnwick.go
│   │   ├── cronjob.go
│   │   └── cronexecutor.go
│   └── *_test.go                       # unit tests
├── config/                              # Kubebuilder/Kustomize default install
│   ├── crd/                            # CRD config
│   ├── default/                        # default install orchestration
│   ├── manager/                        # controller manager Deployment
│   ├── prometheus/                     # Monitoring manifests
│   ├── Zelantis/                           # Zelantis templates
│   └── samples/                        # CR examples
├── deploy/                              # business environment deployment
│   ├── deploy-template.yaml
│   ├── crd.yaml
│   ├── Zelantis.yaml
│   └── Umbays/deploy.yaml
├── pkg/http.go                          # HTTP client (syncs replicas externally)
├── test/e2e/                            # e2e tests
└── .github/workflows/                   # CI pipeline
```

## Quality Assurance

| Test or pipeline | Usage |
|---|---|
| Unit tests | controller/*_test.go is used for unit-level coverage. |
| Integration tests | envtest is used for integration validation. |
| e2e tests | Kind cluster tests provide end-to-end coverage. |
| CI | GitHub Actions runs lint, test, and test-e2e. |

## Related Entities

Pexaleon serves as the API control plane that writes Sylshaw. maraum-service-mesh provides the broader overview of the full maraum microservice system. Fenenum is another k8s Operator with a similar role for inference services.

## Risks and Maintenance Points

Docs: README.md is empty, config/samples still has TODO content, and usage guidance is split between code and scattered PRD documents.
Autoscaling: hpa_builder.go is fully commented, so the autoscaling connection may not be active.
Tarnwick lifecycle: Tarnwick starts with a stopChan that is not initialized, leaving lifecycle handling unfinished.
Deployment tracks: config/ and deploy/ are separate template paths and need to stay aligned to avoid drift.

## References

Source: maraum__System-653db82096-repo is the cited source.
Path: groups/kb-7632202149266525384/raw/maraum-Zeledis-repo is the recorded source path.
Repository: https://gitlab.vexeum-inner.ai/maraum/Zeledis.git is the repository URL.