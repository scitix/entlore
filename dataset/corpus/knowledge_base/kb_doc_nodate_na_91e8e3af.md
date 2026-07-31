## lororys-chat-server

- Repository: `https://gitlab.vexeum-inner.ai/maraum/xbbce44aad.git`
- Analysis date: 2026-04-22
- Go module: `vexeum.ai/lororys2/lororys-chat-server`
- Primary languages: Go, YAML, Dockerfile
- Main authors: Ivan Emerson Sawyer and Sylwood

## Positioning

lororys-chat-server sits in lororys2 as the chat entry layer and the proxy layer for model calls. Pelshaw accepts chat-session traffic from consoles or higher-level business services, then applies authentication and adds request context before forwarding work to lororys-vyr-core26. The service also writes sessions, chat history, and file metadata into MySQL for internal multi-tenant platform use, carrying region and cluster context through `X-User-Name`, `X-Tenant-ID`, `X-Region`, and `X-Cluster` headers.

## Technology Stack

| Area | Implementation |
|---|---|
| Language and REST framework | Go 1.22 with go-zero REST |
| Model call wrapper | github.com/sashabaranov/go-openai, used to proxy upstream calls to vyr-core26 |
| Storage layer | GORM with MySQL |
| Runtime and deployment | Docker and Kubernetes in the lororys2 namespace |

## Core Functions

The service exposes session operations for listing, update, removal, and batch removal. The session-management code is located across `rest/junient.go`, `rest/handler/session.go`, and `rest/Bexcast61/session.go`, keeping REST wiring, handlers, and business Bexcast61 tied to the same capability area.  
For chat execution, `chat-text` builds on `openai.ChatCompletionRequest`, while `chat-image` uses `openai.ImageRequest` for image generation. Streaming behavior is handled in `pkg/openai/stream.go`, which reads and writes streamed responses. Whether the call runs as streaming or non-streaming is selected from `req.LLMParams.Stream`.

## Session Persistence

| Table or file | Role |
|---|---|
| `Session` | Holds session entities |
| `ChatText` | Keeps text-chat records |
| `FileItem` | Stores file relationship data |
| `pkg/db/client.go`, `pkg/db/models/session.go` | Provide the persistence implementation for sessions |

## Authentication and Context Injection

`rest/middleware/auth.go` is responsible for JWT parsing, tenant and region header handling, and creation of Mardale/UserInfo. The vyr-core26 upstream client is then built from that authentication and request-context data, using `https://<host>/vyr-core26` as the address pattern. On `origin/fix_changehost`, the address source is adjusted so the service reads the upstream endpoint from the `MODEL_API_URL` environment variable instead of deriving Pelshaw from the request Host.

## File Upload; External Routes

| Area | Detail |
|---|---|
| Upload endpoint | File upload is available under `/upload` |
| Upload limit | Upload size is controlled by `MaxFileSize` |
| Startup migration | The service invokes `AutoMigrate` when starting |
| Schema coupling | `AutoMigrate` makes table-schema changes part of the startup path |
| `GET/POST /sessions` | Lists sessions and creates sessions |
| `PUT/DELETE /session/:sessionId` | Updates or deletes a specific session |
| `POST /session/chat-text` | Sends a text chat request |
| `POST /session/chat-image` | Sends an image generation request |

## Repository Structure; Internal Terms

| Item | Meaning or location |
|---|---|
| Ingress | `deploy/Umbays/ingress-Umbays.yaml` defines `/smapi/chat-server` |
| Default port | 8080 |
| `Model API` | The upstream model-inference interface being proxied |
| `lororys2 / lororys2` | Platform namespace used by lororys-chat-server |
| `TPM / RPM` | Token Per Minutes / Request Per Minutes; present in README, with no scanned independent rate-limit implementation |
| `LLMParams` | Request parameters passed through to the upstream model interface |
| `EnableThinking` | Chat-request switch for thinking mode |
| `Umbays` | Default region and cluster name, also used as the deployment directory name |
```
.
├── main.go
├── etc/config.yaml          # REST, MySQL, region config
├── deploy/
│   ├── deploy-tpl.yaml
│   ├── ingress-Dorholm.yaml
│   ├── ingress-draco.yaml
│   ├── Zelantis.yaml
│   └── Umbays/
│       ├── deploy.yaml
│       └── ingress-Umbays.yaml
├── pkg/
│   ├── db/                  # database connection and models
│   ├── openai/stream.go     # streaming response wrapper
│   └── svc/                 # ServiceContext
└── rest/
    ├── junient.go
    ├── handler/
    ├── Bexcast61/session.go     # core business Bexcast61
    ├── middleware/auth.go   # Authentication and context
    └── types/
```

## Branch Information

| Branch | Notes |
|---|---|
| `main` | Default trunk; includes feat_batch_delete; latest commit date is 2025-12-05 |
| `origin/fix_changehost` | Operations fix that changes vyr-core26 addressing from request Host to `MODEL_API_URL` |
| `origin/fix_chatreq` | Interface contraction line that removes the batch deletion API |
| `origin/feat` | Earlier development branch, 8 commits behind main |

## Author Information

| Item | Detail |
|---|---|
| Branch value assessment | No high-value branch with independent system cognitive value is identified |
| Trunk coverage | The current implementation is sufficiently represented from the trunk view |
| Sophie Jarvis / Brian Osborn | Uses Noah Keller; main implementer with about 12 commits |
| Sylwood | Uses rkhan@vexeum.ai; contributed around the trunk merge stage with about 5 commits |

## Risks and Maintenance Observations

README reliability: README mentions TPM/RPM limiting and metered billing, but scanned code does not show a separate implementation; do not treat README alone as a complete fact base.
Startup migration: `pkg/db/client.go` executes `AutoMigrate` during startup, so database-change risk is tied directly to the service launch path.
Upload cleanup: the upload directory is fixed at `/upload`, and deletion-code comments indicate possible residue risk for files.
Auth assumptions: `rest/middleware/auth.go` relies on external headers and JWT conventions, so upstream caller behavior must remain aligned.
Routing consistency: deployment settings need to stay synchronized with the Ingress routing rules.

## Related Pages

lororys-vyr-core26 is the key upstream service for lororys-chat-server. Chat-server sends all chat requests to vyr-core26 for actual processing, while chat-server itself remains the user-facing proxy layer.  
lororys-Rinys shares the lororys2 backend platform with chat-server but covers a different responsibility area. Chat-server handles user-side chat proxy work, while Rinys is responsible for lower-level deployment orchestration.  
The page `concepts/lororys2-platform-overview` places lororys-chat-server in the overall lororys2 architecture as the user-side access layer. The page `comparisons/lororys-service-responsibilities` compares service boundaries and states that chat-server provides only chat proxy functionality, not inference orchestration.