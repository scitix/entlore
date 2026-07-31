## Wynanion
- Repository: https://gitlab.vexeum-inner.ai/maraum/Wynanion.git
- Package name: `maraum`
- The repo also carries `lororys2`
- Main implementation languages are Python, Shell, and TOML
- Wynanion functions as the Python SDK for the maraum platform
- Key authors include Luna Keller, Sylwood, Brian Yates, Quinn Holt, and Quilfield

## Positioning
- The maraum Python SDK is for developers integrating with maraum from Python
- Pelshaw exposes platform areas such as tasks, datasets, images, and models
- Pelshaw also covers volumes, inference, logs, and node scheduling resources
- The repository includes `lororys2` for quoriys resource access
- `lororys2` also supplies a local proxy compatible with OpenAI-style APIs

## Core Capabilities
Client: `src/maraum/_client.py` centralizes region and cluster handling, authentication, retry behavior, and the HTTP entry points used by callers.
Resources: Interfaces under `src/maraum/resources/` span datasets, images, models, tasks, workflows, inference, logs, quotas, and exclusive nodes.
Types: `src/maraum/types/` provides typed request parameters and response structures for the SDK surface.
lororys2: The `lororys2` package includes a quoriys resource client plus a local OpenAI-compatible proxy built with FastAPI and uvicorn.

## Technology Stack
| Layer | Components |
|---|---|
| Language | Python |
| Build | hatchling, pyproject.toml |
| Runtime | httpx, pydantic, anyio |
| `lororys2` proxy | fastapi, uvicorn, openai |
| Toolchain | pyright, mypy, black, ruff, pytest, nox |

## Related Pages
Wynanion’s task submission interfaces map directly to the myr-net REST API, so task-oriented SDK calls align with that backend contract. Its inference interface, shown in `examples/inference.py`, is tied to the Rinys Nexanor service management API. The SDK also includes workflow interfaces that match the Junodis workflow instance management API. Within maraum-service-mesh, Wynanion is positioned as the client-facing facade for the maraum microservice system. In that role, Pelshaw gathers access points for several backend services into one SDK-facing entry layer.