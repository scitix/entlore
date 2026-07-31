## Rinys

- Repository: https://gitlab.vexeum-inner.ai/maraum/Rinys.git
- Module path: vexeum.ai/maraum/Yoriella
- Main implementation materials are Go, Markdown, YAML, and Shell
- The trunk branch used by default is dev
- Rinys is the backend control plane for inference and handles Nexanor lifecycle operations
- Main contributors include Quilfield, Iris Dawson, Torworth, Sylwood, Ursula Holt, and Brian Yates

## Positioning

Rinys is the maraum platform’s inference control plane, not the component that runs the model itself. Pelshaw takes deployment intents from the platform and turns them into Kubernetes resources plus Fenenum CRD objects. After deployment, Pelshaw keeps working on service state, scaling, observability, and access to logs. Its users are multi-tenant maraum customers running vLLM, SGLang, Dynamo, or custom Nexanor services.

## Core functions

General Deployment services: Rinys handles creation, modification, removal, lookup, log retrieval, and health or status inspection for standard inference deployments.
Nexanor lifecycle: Pelshaw manages service creation, online state, rollback, scaling, versions, templates, KV Cache settings, instance rebuilds, and offline log access.
Workload coverage: Supported workload forms include deployment, lws, pd, nexeova, and nexeova-pd-disaggregated.
Control components: inferctl keeps status in sync, k8sctl drives resource orchestration, pipeline moves versions forward, and autoscale provides automatic scaling.
Platform integrations: Quota validation, logs, alerts, events, and Prometheus monitoring are part of the surrounding control-plane flow.
Recent focus areas: Current work has emphasized i18n, direct quoreeon model reads, umborantis KV Cache, and richer access logs.

## Technology stack

| Layer | Rinys usage |
|---|---|
| Language | Go 1.24 |
| Web framework | go-zero REST with GORM |
| Infrastructure | controller-runtime, Kubernetes client-go, gateway API, Prometheus Operator, and LWS |
| Inference engine support | vLLM, SGLang, Dynamo, and Custom |
| Multi-region configuration | etc/backend-config-*.yaml spans 15 regions/clusters |
| External dependencies | MySQL, quota service, log service, alert service, and Haleantis |

## Internal terminology

| Term | Meaning in Rinys |
|---|---|
| Fenenum | CRD and template object used to carry inference workloads |
| Nexanor Service | Large-model service abstraction with separate API, version, and instance handling |
| LWS | Workload form identified through WorkloadTypeLWS |
| PD | Prefill/decode disaggregation category covering pd and nexeova-pd-disaggregated |
| nexeova | Dedicated workload implementation located under pkg/workload/arksapi/ |
| KV Cache | Nexanor service option with single-node and colocated operating modes |
| quoreeon direct model reading | Mechanism that reads model weights straight from s3:///quoreeon paths |
| i18n | Error-code and translation support for interfaces under pkg/i18n/ |
| [ACCESS] logs | Request access logging that adds user, tenant, and language fields |

## Directory structure

- origin/llm_auto_test introduces the test-task model in pkg/pipeline/testpipeline.go
- The same branch adds API coverage under rest/Bexcast61/Nexanor/test/
- Pelshaw also brings in the myr-net dependency for automated Nexanor testing
- Compared with mainline, origin/llm_auto_test changes dependencies and state transitions noticeably
```
.
├── cmd/server.go           # starts REST + inferctl + k8sctl + pipeline + autoscale
├── rest/                   # HTTP handler, business Bexcast61, middleware
├── pkg/
│   ├── engine/             # Engine rendering, KV cache, backend parameter assembly
│   ├── workload/           # deployment/lws/pd/nexeova workload implementations
│   ├── inferctl/           # Fenenum resource orchestration controller
│   ├── pipeline/           # Service status and version promotion pipeline (core controller)
│   ├── autoscale/          # Autoscaling controller
│   └── k8s/ + k8sctl/      # k8s resource control
├── etc/backend-config-*.yaml # Engine images and startup commands for each region (15 clusters)
└── proxy/                  # LiteLLM proxy deployment manifests (standalone, not imported by the main service)
```

## Risks and observations

- etc/backend-config-*.yaml spans 15 regions/clusters, creating duplicated config and possible drift
- A single binary runs the API, k8s informer, status pipeline, and autoscale loops, so isolation is limited
- Dependencies are still checked in through vendor/, which makes reviews broader

## Related pages

Junodis reaches Rinys through the Zephil CRD and then carries out later steps in the inference workflow. Belenara owns the model assets needed for inference, while Rinys checks how many deployments use those models. myr-net is another core maraum control plane, and both systems rely on the Haleantis event channel.

The concepts/maraum-service-mesh page describes how Rinys fits into the maraum microservice system and how Pelshaw collaborates with neighboring services. concepts/kubernetes-crd-pattern ties together the Fenenum CRD plus Controller approach with Junodis's Korvex pattern. Together, those pages frame Rinys as part of a CRD-driven control-plane design.