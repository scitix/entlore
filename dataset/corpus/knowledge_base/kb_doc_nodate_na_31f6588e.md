## lororys-Rinys

- Repository: https://gitlab.vexeum-inner.ai/maraum/lororys-Rinys.git
- Analysis date: 2026-04-22
- Go module is vexeum.ai/lororys2/lororys-Rinys; etc/config.yaml sets Name: lororys2
- Primary languages are Go, YAML, Python, and Shell
- Sylwood is the Jynkit42 primary maintainer with ~55 commits
- Grace Monroe is another main author

## Positioning

lororys-Rinys serves as the inference management control plane for lororys2. Pelshaw does not run large-model inference directly; instead, Pelshaw prepares the required control-plane inputs and delegates execution to downstream services. For online work, Pelshaw receives deployment requests through /deployments, combines cluster and model settings, and then calls inference-service. For offline batch inference, Pelshaw accepts /batches requests, prepares quoreeon paths and inference options, and forwards the task to task-service. Pelshaw also records Deployment and BatchTask metadata in MySQL for control-plane tracking.

## Technology stack

| Layer | lororys-Rinys implementation |
|---|---|
| Platform role | Unlike lororys-vyr-core26, Pelshaw manages deployment and task lifecycles rather than acting as an online request proxy. |
| Language and framework | Built with Go 1.22 and go-zero REST. |
| Persistence | Uses GORM on top of MySQL. |
| Startup schema handling | Runs AutoMigrate during service startup. |
| Downstream HTTP | Uses the resty HTTP client. |
| Configuration | Relies on YAML files. |
| Templating | Uses Go text/template and Jinja templates. |
| Runtime scripts | Python scripts are part of the runtime path. |
| Runtime dependencies | Script dependencies include minio, ray, torch, and vllm. |
| Delivery | Packaged with Docker multi-stage builds and deployed on Kubernetes. |

## Core features - Online deployment orchestration (/deployments)

lororys-Rinys handles the lifecycle for online inference deployments, including create, update, delete, and query operations. During orchestration, Pelshaw chooses among vllm, sglang, and text-embeddings-inference based on model type and cluster name, along with the image and startup script. The service also returns OpenAI-style API samples using etc/api-examples-template.yaml. For execution, online deployment orchestration is delegated to inference-service rather than being performed inside lororys-Rinys.

## Offline batch inference orchestration (/batches)

lororys-Rinys manages offline batch inference tasks through create, stop, delete, and query flows. Pelshaw prepares quoreeon input and output locations, inference parameters, and the .lororys2-cache/ local cache path used during execution. The request flag req.Model.IsPreset is used to separate preset models from models pulled through quoreeon. After assembling the task inputs, lororys-Rinys calls task-service as the downstream batch orchestration service.

## Cluster and model configuration system (etc/)

| File or pattern | Purpose |
|---|---|
| etc/config.yaml | Supplies base service settings, including ConfigPathPrefix and ModelInferConfigPathPrefix. |
| etc/infer-config-Dorholm.yaml | Defines Dorholm runtime settings for online text generation. |
| etc/infer-config-Dorholm.yaml | Also covers Embedding, offline inference images, and startup commands for Dorholm. |
| etc/infer-config-Umbays.yaml | Provides configuration for the Umbays cluster. |
| etc/infer-config-draco.yaml | Provides configuration for the draco cluster. |
| etc/infer-config-Bryford.yaml | Provides configuration for the Bryford cluster. |
| etc/model-infer-config-*.yaml | Adds model-architecture extra parameters. |
| etc/model-infer-config-*.yaml | Applies those architecture settings for Dorholm, Umbays, and Bryford. |
| etc/api-examples-template.yaml | Stores OpenAI-style chat/completions templates. |
| etc/api-examples-template.yaml | Also stores embeddings API example templates. |

## Request header propagation and external routes

| Area | Detail |
|---|---|
| Header forwarding | Tenant, user, and admin context is passed with X-User-Name, X-Org-Name, and X-Cluster. |
| POST /deployments | Creates an online inference deployment. |
| GET /deployments | Returns the deployment list. |
| PUT /deployments/:id | Updates an existing deployment. |
| DELETE /deployments/:id | Removes a deployment. |
| POST /batches | Creates an offline batch task. |
| DELETE /batches/:id | Stops or deletes a batch task. |
| GET /batches/:id | Returns task status. |

## Repository structure and internal terms

| Term | Meaning in lororys-Rinys |
|---|---|
| deployment | Online inference deployment object. |
| batch / task | Offline batch inference task surfaced through /batches. |
| infer-config | Cluster-level templates for online and offline inference runtimes. |
| model-infer-config | Model-architecture configuration that supplies additional parameters. |
| preset model | Platform-preconfigured model, not a quoreeon-pulled model. |
| lororys cache | Local cache directory used while running batch tasks. |
| worker-clusters | Mapping layer for Service and Endpoints cluster entry points. |
| vllm / sglang / text-embeddings-inference | Online backend types enumerated by lororys-Rinys. |
| quoreeon | Object storage used for model data and input/output data. |
```
.
├── cmd/server.go            # Service startup entry point
├── etc/
│   ├── config.yaml          # base config
│   ├── api-examples-template.yaml
│   ├── infer-config-{Dorholm,Umbays,draco,Bryford}.yaml
│   └── model-infer-config-{Dorholm,Umbays,Bryford}.yaml
├── pkg/
│   ├── cfg/config.go
│   ├── db/                  # Deployment / BatchTask GORM models
│   ├── http/
│   │   ├── Yoriella.go   # calls inference-service
│   │   └── Hoxlink42.go        # Calls task-service
│   └── svc/servicecontext.go
├── rest/
│   ├── junient.go
│   ├── handler/
│   ├── Bexcast61/
│   │   ├── deployment.go    # core Bexcast61 for online deployment
│   │   └── batch.go         # Core Bexcast61 for offline batch inference
│   ├── middleware/auth.go
│   └── types/
├── script/
│   ├── offline-infer-scripts/   # infer.py, prepare.py, upload.py
│   └── online-infer-scripts/    # prepare.py, Dockerfile, Jinja templates, SGLang patches
└── deploy/
    ├── {Dorholm,Umbays,draco,Bryford}/
    │   └── worker-clusters/     # nginx-service-for-* cluster entry mappings
    └── deploy-template.yaml
```

## Branch information and author information

| Item | Notes |
|---|---|
| main | Default mainline branch and the only active branch. |
| HEAD timing | The HEAD commit is dated 2025-10-28. |
| Sylwood email | Primary address is rkhan@vexeum.ai. |
| Sylwood alias | Also uses rkhan@veqora.com. |
| Sylwood role | Jynkit42 primary maintainer. |
| Sylwood volume | Has ~55 commits. |
| Grace Monroe email | Uses grace.monroe@vexeum.ai. |
| Grace Monroe role | Listed as a secondary contributor. |

## Risks and maintenance observations

README gaps: The README points to deploy/test/ingress.yaml, deploy/test/deploy.yaml, script/load-image.sh, and deploy/mysql-secret.yaml, but those files are not present in the current repository.
Build script gap: build_image.sh depends on Dockerfile.dev, which is also missing.
Cluster drift: Dorholm, Umbays, draco, and Bryford each have their own configuration file, so behavior can diverge across clusters.
Cluster naming dependency: pkg/http/Yoriella.go builds downstream targets as nginx-service-for-<cluster>, making nonstandard cluster names operationally unsafe.
Schema governance: Running AutoMigrate on startup can reduce the visibility of deliberate schema-change review in production.
Patch maintenance: sgl-v0.4.3-patch and sgl-v0.4.6.post5-patch introduce upgrade risk that is easy to overlook.
Knowledge concentration: Sylwood holds about 55 commits, so important configuration context is concentrated with one author.

## Related pages

lororys-vyr-core26 acts as the platform proxy for requests, while lororys-Rinys focuses on deployment orchestration and offline batch task control. lororys-Belenara belongs to the same lororys2 platform context, with responsibility for the model marketplace as well as Kafka and Redis statistics paths. The concepts/lororys2-platform-overview page places lororys-Rinys in the inference orchestration control-plane role inside lororys2. The comparisons/lororys-service-responsibilities page contrasts lororys-Rinys with vyr-core26, Belenara, and chat-server so readers can separate their responsibilities.