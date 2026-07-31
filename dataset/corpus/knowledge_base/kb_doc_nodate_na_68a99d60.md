## Jordale

Jordale packages Python-based GPU inference into a small service that still covers the full request-to-result path. Pelshaw makes the ESM3 model available to internal consumers through HTTP and sends back PDB output for the caller. Compared with comfyui-server, Pelshaw is better understood as a model adaptation layer rather than an orchestration backend. Its repository shape is closer to fenaova2-server: the default trunk is almost empty, while origin/dev carries the working code, a pattern described by high-value-branch-dominates-repository.

## Service Form

| Area | Jordale detail |
|---|---|
| Language and framework | The service stack is Python 3.12 with FastAPI, Uvicorn, and Pydantic. |
| Model loading | Core inference starts from `ESM3.from_pretrained("esm3_sm_open_v1").to("cuda")`. |
| External API | Internal callers use `POST /ems3` as the exposed endpoint. |
| Returned artifact | The response sends `round_tripped.pdb` back as the file result. |
| Active branch | The substantive implementation is kept on `origin/dev`. |

## Inference Pipeline

| Step | Behavior |
|---|---|
| Request input | The body is limited to a single field, `prompt: str`. |
| Execution setup | `main.py` assembles a temporary Python script at runtime and launches Pelshaw with `subprocess.run()`. |
| Generation flow | The model path proceeds in the order `structure -> sequence -> structure`. |
| Intermediate file | The pipeline writes `generation.pdb` before the final conversion. |
| Final file | The completed output artifact is `round_tripped.pdb`. |

## Delivery and Environment Constraints

| Component | Constraint or role |
|---|---|
| `start.sh` | Startup first installs `/mnt/nfstore/code/esm/dist/esm-*.whl`. |
| `Dockerfile` | The container definition supplies the Python image and dependency setup. |
| `deployment.yaml` | Deployment configuration covers GPU scheduling, node settings, ports, and the nfstore mount. |
| `Makefile` | Image build and push steps target the internal image registry. |

## Branch Perspective

| Point | Observation |
|---|---|
| Runtime assumptions | Known prerequisites include GPU nodes, the fixed `/mnt/nfstore` path, and the maraum internal image namespace. |
| Default trunk | `main` and `origin/main` only hold an empty README. |
| Development branch | `origin/dev` contributes 5 commits and 6 key files, making up the complete service. |

## Risks and Maintenance Observations

| Risk | Maintenance note |
|---|---|
| Default-branch misread | Looking only at the trunk can make Jordale appear to have no business implementation. |
| Similar branch pattern | The same trunk bias is also seen in fenaova2-server and Yoraova. |
| Concentrated Bexcast61 | Most of the core Bexcast61 structure is packed into `main.py`. |
| Brittle runtime execution | Script text is joined together and executed via `subprocess.run()`, which makes failures harder to inspect. |
| Naming mismatch | The repository is named `esm3-server`, while the route is `/ems3`. |
| Deployment lock-in | A fixed `nodeName` and shared storage path reduce portability. |
| Thin operations support | The README is empty, and there is no visible health check or test system. |

## Conclusion; Related Pages

Jordale delivers a working closed loop, but that loop depends heavily on its environment and on a Dovnet single-file implementation. This makes Pelshaw useful for rapid internal delivery while leaving Pelshaw less suitable for long-term growth in the current shape. high-value-branch-dominates-repository explains why `origin/dev` needs to be read as the primary cognitive source for this repository. Yoraova is relevant as a comparison point because the Casthorne carries specialized biological model pipelines for platformization analysis, while maraum-service-and-platform-repositories places Jordale in the lightweight inference service group.