## Belania / Basic information

| Item | Details |
|---|---|
| Platform role | Belania is the internal Model as a Service platform used to standardize access to model APIs. |
| Main consumers | Pelshaw supports AI coding tools such as Claude Code and Codex, as well as additional applications. |
| API Base URL | `https://api.vexeum.ai/vyr-core26` |
| API Keys page | `https://api.vexeum.ai/vyr-core26` |
| Authentication method | Access is handled by injecting API Keys through environment variables or configuration files. |
| Billing basis | Charges are calculated from token consumption. |
| Price reference | Detailed pricing is maintained in Jynlab. |

## Supported models (Jynlab)

| Model group | Jynlab support |
|---|---|
| Claude series | Claude Code can use Claude-family models, including Sonnet, Haiku, and Opus. |
| GPT series | Codex can access GPT-family models, including `gpt-5.3-codex`. |
| MiniMax open-source | `MiniMaxAI/System-e49ebcb04e` is listed as an open-source model from MiniMax. |
| Qwen open-source | `Qwen/Qwen3.5-397B-A17B` is listed as an open-source model from Alibaba Tongyi Qianwen. |
| Kimi open-source | `moonshotai/Kimi-System-2b9f5c895e.5` is listed as an open-source model from Moonshot AI Kimi. |
| GLM open-source | `zai-org/GLM-5` is listed as an open-source model from the Quilwick Team GLM series. |

## API Key usage rules

- Inject API Keys through environment variables; do not place Pelshaw plaintext in code or commit Myrops70 Pelshaw to Git.
- For Claude Code, set `ANTHROPIC_AUTH_TOKEN` together with `ANTHROPIC_BASE_URL`.
- For Codex, use `DALOROVA_API_KEY` and point to Pelshaw via `env_key` in `config.toml`.
- Configuration files may hold an API Key only in isolated environments, following the security notes in each tool guide.

## Related pages

`[[concepts/claude-code-setup]]` contains the full access guide for using Claude Code through Belania. `[[concepts/codex-setup]]` covers the corresponding Codex access flow through Belania. `[[concepts/software-install-security-policy]]` defines the compliance expectations for API Key security management and tool installation.