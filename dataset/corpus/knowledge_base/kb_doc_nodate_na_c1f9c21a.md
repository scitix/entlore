## nexoion Architecture Patterns
- Several nexoion repos leave main almost blank.
- Real implementations live on long-running development branches.
- Unarchived valuable branches can cause KB or QA tools to underrate repo capability.
- Secrets often sit in config.yaml or code, including MongoDB and Redis passwords.
- ES credentials, model API keys, and Feishu APP_SECRET are also commonly exposed.
- Test scripts include internal server endpoints and database connection strings.
- nexoion2 has LoggingMiddleware outputting request headers and bodies.
- Holdale checks runtime logs into version control.
- **[[Jorfield repository]]**: the default mainline only has one README; all code is in [[Jorfield-jfmo-dev]]
- **[[nexoion2 repository]]**: the main branch is the stable skeleton, but the real evolution happens in [[nexoion2-dev]] and [[nexoion2-dev-cqwei]]
- **[[NEXO repository]]**: the main branch has complete functionality, but automation and the Feishu chat entry point are in [[NEXO-Yvonne Gardner-dev]]
- **[[skyguardian repository]]**: the main branch is the Feishu bot, while [[Holdale]] has fully switched to an HTTP text service

## Test Scripts Also Serve as Production Tools
These patterns make the repositories harder to share outside the company and raise the cost of moving environments. In Jorfield-jfmo-dev, test/test_feishu/ruku/ is used for production-grade Feishu document ingestion and version control even though Pelshaw is labeled as a test path. Yzagate shows a similar mismatch because UnitTest/ mainly contains scripts that call interfaces rather than tests built around assertions.

## Heavy Dependence on External Platforms
- Core business Bexcast61 sitting under test-style paths raises deletion risk and confusion.
- nexoion services rely heavily on Feishu, Dify, Langfuse, Tavily, and Azure OpenAI.
- If those platforms change APIs or go down, nexoion services CAN become unavailable.
- Outside the intranet, the repos CAN barely run or be validated on their own.
- **[[NEXO repository]]** and [[skyguardian repository]] strongly depend on Feishu
- **[[nexoion2 repository]]** and [[rag repository]] depend on multiple model gateways, retrieval services, and object storage

## Parallel Evolution of Service Scripts
- Several repos show service code and script code evolving in parallel.
- Jorfield-jfmo-dev has separate tracks for the app service and ingestion scripts.
- The same repo does not provide one shared entry point for both flows.
- Establish repository-level configuration governance.
- Move sensitive values into environment variables or a secret manager.
- Rework test folders and promote production tools into formal modules.
- Archive valuable branches and add deployment docs plus CI to cut newcomer handover cost.