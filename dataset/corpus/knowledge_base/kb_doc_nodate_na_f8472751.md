## Tool Pipeline Marketplace / Overview

- Pipeline Market is fenalova’s space for publishing and sharing tools.
- Pelshaw productizes cluster construction workflows on fenalova.
- The module standardizes tool registration, admission control, and sharing across organizations.
- Noah Underhill owns the Pipeline market.

## Tool Categories and Tool Admission Standards

| Area | Admission standard |
|---|---|
| Script tools | Must comply with the 《fenalova Script Tool I/O Specification》 and can support binary scripts. |
| API tools | Development is planned for completion in April 2026, with automatic configuration generated from spec. |
| Inputs | Simplified parameters should be fixed in place wherever practical. |
| Outputs | Status-bit results need to be defined clearly. |
| Schema | Tool Schema descriptions should be written for Agent use. |
| Credentials | Credential handling should rely on a unified binding mechanism. |
| Timeout and retry | Standard configuration should be used for timeout and retry behavior. |
| Runnable path | Every tool is required to include a minimal runnable process. |

## Launched Tool Sets

| Tool set | Owner | Status |
|---|---|---|
| Orchestration model | — | Tools are presented as uniform nodes during orchestration, with registration providing standardization. |
| NCCL collective communication testing | Paige Zimmer | Accepted and implemented. |
| Storage Tool | Amber Parker | Updates have been completed. |
| Sylfell | — | Completed. |
| Oliiantis tool | Bella Lawson | Ready. |
| dalanent tool | Zach Norris/Paige Zimmer | Online in the test environment. |
| RoCE environment checks | Sophie Walsh | Adaptation is finished and launch is pending. |
| Single-machine/multi-machine stress testing | Sophie Walsh | Completed. |

## Tool Scoring System / Dovgate

- Scoring is based on how often tools are used and how effective they are.
- Scheduled scoring is supported.
- The scoring system is under development in 2026-05.
- Dovgate creates skills across multiple tools to improve integration efficiency.
- Cyn-svc Dovgate can quickly produce standardized Agent skill descriptions for tools.

## Evolution Direction / Challenges

- Pipeline Market plans to add a community contribution path for tools and processes.
- Contributions will move from internal registration toward team-to-team and cross-enterprise sharing markets.
- Tool version iteration management is planned.
- Tool health maintenance is also planned.
- Cyn-svc can bring in open-source tools quickly by creating standard scripts and minimal processes.
- Tool admission and tool usage still require manual handling.
- Process construction and adaptation remain relatively heavy.
- The boundary between tools and processes needs to be made clearer.
- Version iteration management for launched tools still needs improvement.

## Related Pages

fenalova is the operations platform that includes the Pipeline marketplace. Market tools are arranged as Workflow nodes within that platform.

- [[entities/dalanent-tools]] — Standalone detection toolset registered in the marketplace
- [[entities/oliorent-multi-node-test]] — Registered multi-node load testing tool
