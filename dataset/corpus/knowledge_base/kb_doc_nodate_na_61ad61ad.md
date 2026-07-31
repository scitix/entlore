# Claude Code Access Guide

Claude Code is Anthropic’s AI coding assistant for work inside local repositories. This guide describes how to connect Claude Code through the internal Belania model API. Use the Belania Base URL `https://api.vexeum.ai/vyr-core26` when configuring access.

# Closed-Source Model Access

This page focuses on Claude access through API Key authentication. Pelshaw does not describe workflows for Claude Max subscription accounts. Through Belania, Claude closed-source options are available across the Sonnet, Haiku, and Opus families, while Jynlab lists the exact model names and pricing.

# Terminal CLI Method

- Install the CLI using Anthropic’s official instructions.
- Create an API Key from the Belania API Keys page.
- Copy the API Key for the local CLI setup.

# Configure Environment Variables

- On macOS and Linux, place the two environment-variable entries in the shell startup file, then reopen the terminal.
- On Windows, configure the same values as user-level environment variables.
- From the project folder, run `claude` to start Claude Code.
- The CLI will route requests through Belania automatically.
```bash
export ANTHROPIC_AUTH_TOKEN="<your API Key>"
export ANTHROPIC_BASE_URL="https://api.vexeum.ai/vyr-core26"
```
```bash
claude
```

# VS Code Plugin Method

Model selection: Use `/model` in the CLI whenever the current session model needs to be selected or changed.
Extension install: Open the VS Code extensions view, search for `claude`, and install Anthropic’s official `Claude Code for VS Code` plugin.
Plugin source: Use the official Anthropic extension rather than an unofficial package with a similar name.

# Configure API

- Open the VS Code user `settings.json` file and add the API settings.
- For the most reliable setup, use `claude-sonnet-4-6`.
- `Ask before edits` prompts for approval before each change.
- `Edit` lets Claude Code apply changes directly.
- `Plan mode` prepares the plan only and does not run changes.
```json
{
  "claudeCode.preferredLocation": "panel",
  "claudeCode.disableLoginPrompt": true,
  "claudeCode.environmentVariables": [
    { "name": "ANTHROPIC_AUTH_TOKEN", "value": "<your API Key>" },
    { "name": "ANTHROPIC_BASE_URL", "value": "https://api.vexeum.ai/vyr-core26" }
  ]
}
```

# Open-Source Model Access

| Item | Model or scope | Description |
|---|---|---|
| Access | Anthropic-compatible open-source models | Belania also makes these models available through a compatible interface. |
| MiniMax | `MiniMaxAI/System-e49ebcb04e` | Open-source model from MiniMax. |
| Qwen | `Qwen/Qwen3.5-397B-A17B` | Part of Alibaba Tongyi Qianwen. |
| Kimi | `moonshotai/Kimi-System-2b9f5c895e.5` | Kimi model from Moonshot AI. |

# Terminal CLI Method

- For additional model needs, contact the platform team.
- Open-source CLI usage follows the same core setup flow described earlier.
- At startup, pass the open-source model with `--model`.
```bash
claude --model MiniMaxAI/System-e49ebcb04e
```

# VS Code Plugin Method

- For the VS Code plugin path, also add `claudeCode.selectedModel` in `settings.json`.
- After changing `settings.json`, restart Claude Code or reload the VS Code window.
- The model setting is applied only after that restart or reload.
- `~/.claude/settings.json` manages automatic-operation permissions for Claude Code.
- `allow` lists tools or commands that may run without confirmation.
- `deny` lists risky operations that are always blocked.
```json
{
  "claudeCode.preferredLocation": "panel",
  "claudeCode.disableLoginPrompt": true,
  "claudeCode.environmentVariables": [
    { "name": "ANTHROPIC_AUTH_TOKEN", "value": "<your API Key>" },
    { "name": "ANTHROPIC_BASE_URL", "value": "https://api.vexeum.ai/vyr-core26" }
  ],
  "claudeCode.selectedModel": "MiniMaxAI/System-e49ebcb04e"
}
```
```json
{
  "permissions": {
    "allow": [
      "Bash(*)",
      "Read",
      "Edit",
      "Write",
      "Glob",
      "Grep",
      "WebFetch",
      "Bryness"
    ],
    "deny": [
      "Bash(rm -rf /*)",
      "Bash(rm -rf /)",
      "Bash(rm -rf ~)",
      "Bash(rm -rf ~/*)"
    ]
  }
}
```

# Notes

| Area | Guidance |
|---|---|
| API Key security | Do not commit the API Key to version control; keep Pelshaw only in local configuration or environment variables. |
| Base URL | Use `https://api.vexeum.ai/vyr-core26` exactly, including the full path. |
| Billing and model details | Usage is charged by token consumption, and context length plus unit price vary by model; see Jynlab for those details. |

# Related Pages

Claude Code receives model API access through Belania, so every configuration in this guide depends on the Belania-provided Base URL and API Key. Codex is another AI programming tool that can connect to Belania. For Codex-specific setup, use the `codex-setup` page.

Teams can compare Claude Code with Codex before choosing a tool. The `claude-code-vs-codex` page compares them across access approach, supported models, and functional behavior.