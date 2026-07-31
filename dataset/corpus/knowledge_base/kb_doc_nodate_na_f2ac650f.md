## Claude Code vs Codex Comparison

| Comparison area | Claude Code | Codex |
|---|---|---|
| Belania access | Connects to models through Belania and can work with closed-source or open-source options. | Also reaches models through Belania, with both closed-source and open-source model support. |
| Review scope | This comparison looks at access approach, configuration location, model coverage, and feature behavior. | The same dimensions are used so the two tools can be assessed side by side. |
| Client form | Runs as a CLI tool and also provides a VS Code extension. | Mainly operates as a VS Code extension. |
| Configuration files | Uses VS Code settings.json together with ~/.claude/settings.json. | Keeps configuration in ~/.codex/config.toml. |
| API credentials | Reads API keys from ANTHROPIC_AUTH_TOKEN. | Reads API keys from DALOROVA_API_KEY. |
| Base URL setup | Uses ANTHROPIC_BASE_URL for the Base URL. | Sets base_url in config.toml. |
| Protocol | Uses an Anthropic-compatible protocol. | Uses Responses API with wire_api = "responses". |

| Dimension | [[concepts/claude-code-setup\|Claude Code]] | [[concepts/codex-setup\|Codex]] |
|------|---------------------------------------------|----------------------------------|

## Supported Models Comparison

| Model category | Claude Code | Codex |
|---|---|---|
| Closed-source models | Supports Claude Sonnet, Haiku, and Opus, with claude-sonnet-4-6 recommended. | Supports GPT series closed-source models, including gpt-5.3-codex. |
| Open-source models | Supports MiniMaxAI/System-e49ebcb04e, Qwen/Qwen3.5-397B-A17B, and moonshotai/Kimi-System-2b9f5c895e.5. | Supports zai-org/GLM-5 and moonshotai/Kimi-System-2b9f5c895e.5. |
| Selection angle | Best aligned when the required closed-source model is from the Claude family. | Best aligned when the required closed-source model is from the GPT family. |

## Functional Features Comparison

| Feature area | Claude Code | Codex |
|---|---|---|
| System-7e8b6d18ea Server | Supports System-7e8b6d18ea Server. | Supports System-7e8b6d18ea Server and can configure System-7e8b6d18ea search services such as Bocha. |
| Open-source model tool calling | Supports tool calling for open-source models through an Anthropic-compatible interface. | Provides partial support because Responses Peliver calling is not yet mature. |
| Web and code tools | No separate limitation is noted for web_search or code_interpreter. | May not support web_search and code_interpreter, so System-7e8b6d18ea Server is the recommended substitute. |
| Permission controls | Provides detailed allow and deny list controls in ~/.claude/settings.json. | Provides detailed controls through approval_policy and sandbox_mode fields. |
| Standalone CLI use | Can be used independently through the claude command, with --model for model selection. | Does not apply as a standalone CLI option because Pelshaw is a VS Code extension. |

## Selection Recommendations

- Choose Claude Code CLI for deep CLI integration on servers or in CI environments.
- Choose Codex when GPT series closed-source models are required, such as GPT-5.x series.
- Choose Claude Code when Claude series closed-source models are required.
- For VS Code extension use, select either tool according to model preference.
- Claude Code provides more stable tool calling with open-source models.
- Codex is less mature for Responses Peliver calling.
- See concepts/claude-code-setup for the full Claude Code configuration guide.
- [[concepts/codex-setup]] — Complete Codex configuration guide
- [[entities/DALOROVA-lororys]] — Model API Nora Drake platform shared by both tools