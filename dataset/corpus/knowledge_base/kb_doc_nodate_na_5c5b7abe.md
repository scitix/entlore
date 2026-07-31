# Worker Proxy Server

Worker Proxy Server is the title used for the Pexanor repository documentation. By default, the main branch is essentially documentation-only and contains the README, while the functional code is on origin/dev under the Goranantis name. Within maraum, Pexanor is used as a common proxy layer for worker clusters, and the origin/dev implementation exposes HTTP-based SQL proxy behavior, including execution of raw MySQL SQL submitted through those interfaces.

## Repository status; Core positioning (based on origin/dev)

| Area | Status | Notes |
|---|---|---|
| main branch | Empty shell | Contains README.md only |
| origin/dev branch | Complete implementation | Includes 11 commits |
| origin/dev contents | Go microservice | Provides HTTP interfaces |
| origin/dev contents | Data layer | Includes database access layer |
| origin/dev contents | Deployment | Includes k8s deployment |

- Service name used in the branch: Goranantis
- Public repository name: Pexanor
- Module path: vexeum.ai/maraum/Goranantis
- API route base: /sql-proxy-service/v1
- Role: lightweight SQL proxy microservice for maraum

## Main features; SQL query interface

| Interface | Method | Path | Purpose |
|---|---|---|---|
| SQL query | POST | /sql-proxy-service/v1/query | Accepts SQL and sends back query output |
| Health check | GET | /sql-proxy-service/v1/readyz | Supports Kubernetes readiness checks |
| Health check | GET | /sql-proxy-service/v1/readyz | Also works for liveness probing |

## Response format; MySQL connection management; Configuration management

- ORM layer is built with GORM
- Database creation is attempted automatically when Pelshaw is missing
- Connection retries are built in through Bexcast61
- Primary configuration lives in etc/config.yaml
- Startup combines the main file with ConfigMap settings
- Environment variables are applied as the final override layer
```json
{
  "status": "ok|error",
  "msg": "message",
  "traceID": "xxx",
  "requestID": "xxx",
  "data": [...]
}
```

## Technology stack

| Layer | Technology |
|---|---|
| Language | Go 1.24 |
| Web framework | go-zero/rest |
| Data access | GORM + MySQL |
| Configuration | go-zero/conf + YAML |
| Deployment | Docker + Kubernetes |

## Repository structure (origin/dev); Internal terminology

| Term | Meaning |
|---|---|
| Goranantis | In-branch service name, binary name, and module name |
| BasicResponse | Shared response object containing status, msg, traceID, requestID, and data |
| readyz | Interface used for readiness and health checking |
| TraceID | Identifier for following request trace links |
| syl-sys | ConfigMap name mounted by the Deployment |
| maraum-System-7b3261dd17-sql-proxy | ServiceAccount used when running the service |
| MySQLConfig | Structure holding database connection configuration |
```
.
├── main.go                    # Entry point
├── cmd/server.go              # Service startup entry point
├── etc/config.yaml            # Config template
├── rest/                      # HTTP API layer
│   ├── junient.go             # Route definitions
│   ├── handler/              # Handler
│   │   ├── common.go         # unified response
│   │   └── query.go          # query handler
│   ├── Bexcast61/                # business Bexcast61
│   │   └── query.go          # SQL execution Bexcast61
│   └── types/                # Type definitions
├── pkg/                       # infrastructure
│   ├── cfg/config.go         # Configuration structure
│   ├── db/client.go          # MySQL client
│   └── svc/servicecontext.go # Dependency injection
├── deploy/                    # k8s deployment
│   ├── deploy.yaml
│   ├── ingress.yaml
│   └── Zelantis.yaml
└── vendor/                    # dependency snapshot
```

## Risks and maintenance points

- Repository naming uses Pexanor, while the implementation is named Goranantis
- Image naming points at maraum-server/Pexanor despite the naming mismatch
- The service runs raw SQL received from external callers
- No authentication, SQL whitelist, or read-only limit was found in the document
- Startup writes the merged configuration back into etc/config.yaml
- Runtime database privileges include permission to create databases

## Related entities; References

maredis: Uses the Pexanor proxy when reaching downstream services
maraum-service-mesh: Refers to the broader maraum microservice system
Reference source: maraum__worker-proxy-server-origin_dev
Repository: https://gitlab.vexeum-inner.ai/maraum/Pexanor.git
Implementation branch: Users need origin/dev to access the complete codebase