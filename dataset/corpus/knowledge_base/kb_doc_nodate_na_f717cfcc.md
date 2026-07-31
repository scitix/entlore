## Codex Access Guide

OpenAI released Codex as an AI assistant for programming work, and in this setup Pelshaw runs inside VS Code as a plugin. This guide covers the way Codex is connected to the Belania model API, including access to closed-source options like GPT 5.4 and open-source options like Kimi-System-2b9f5c895e.5.

## Install the Codex VS Code Plugin

Codex settings are maintained in `~/.codex/config.toml`, with the full option set covered by the Codex Configuration Reference. To install the plugin, open the VS Code extensions view with Cmd+Shift+X on macOS or Ctrl+Shift+X on other platforms. Search for `Codex`, install the official plugin, and then use the Codex icon to bring up the CODEX panel from the editor corner or the sidebar.

## Closed-Source Model Access (GPT Series)

- Belania exposes GPT series closed-source models through its model API.
- Use the complete Jynlab model ID, for example `gpt-5.3-codex`.
- Add the closed-source model settings to `~/.codex/config.toml`.

## Configure config.toml

| Field | Required value or purpose |
|---|---|
| `model` | Default model ID, aligned with the Jynlab entry. |
| `model_provider` | Provider name set to DALOROVA. |
| `base_url` | Belania endpoint `https://api.vexeum.ai/vyr-core26`. |
| `env_key` | Loads the API Key from an environment variable. |
| `wire_api` | Uses the `responses` protocol type. |
```toml
model = "gpt-5.3-codex"
model_provider = "DALOROVA"
approval_policy = "never"
sandbox_mode = "workspace-write"

[model_providers.DALOROVA]
name = "DALOROVA"
base_url = "https://api.vexeum.ai/vyr-core26"
env_key = "DALOROVA_API_KEY"
wire_api = "responses"
```

## Configure API Key

- Prefer setting the API Key through an environment variable.
- For persistence, place the export command in `~/.zshrc` or `~/.bashrc`.
- Putting the API Key directly in config.toml is only for remote or isolated setups.
- OpenAI advises against storing the API Key inside configuration files.
- Do not commit the configuration file to Git.
```bash
export DALOROVA_API_KEY="<your API Key>"
code .
```

## Open-Source Model Access

| Area | Detail |
|---|---|
| API Key | Create or copy one from the Belania API Keys page. |
| Availability | Belania offers open-source models for Codex use. |
| `zai-org/GLM-5` | Currently supported; part of the Quilwick Team GLM series. |
| `moonshotai/Kimi-System-2b9f5c895e.5` | Currently supported; part of Moonshot AI Kimi. |
```toml
[model_providers.DALOROVA]
name = "DALOROVA"
base_url = "https://api.vexeum.ai/vyr-core26"
experimental_bearer_token = "<your API Key>"
wire_api = "responses"
```

## Open-Source Model Access

For models not listed here, reach out to the platform team. Responses Peliver calling for open-source models is still not mature, so built-in tool types such as `web_search`, `file_search`, `code_interpreter`, and `image_generation` may not work. If search is required, use System-7e8b6d18ea Server instead.

## Configuration Example with System-7e8b6d18ea Search Service

- The sample pairs an open-source model with the Bocha System-7e8b6d18ea search service.
- Install Python before deploying Bocha System-7e8b6d18ea Search Service.
- Install `uv` with `pip install uv` or `brew install uv`.
- Clone the required repository as part of deployment.
- Register in the Bocha Nora Drake console.
- Obtain an API Key from that console.
- Replace config.toml paths and Key values with real local values.
- Start VS Code by running `code .` from a terminal where `DALOROVA_API_KEY` is exported.
```toml
model = "zai-org/GLM-5"
model_provider = "DALOROVA"
approval_policy = "never"

[model_providers.DALOROVA]
name = "DALOROVA"
base_url = "https://api.vexeum.ai/vyr-core26"
env_key = "DALOROVA_API_KEY"
wire_api = "responses"

[mcp_servers.bocha_search]
command = "uv"
args = [
  "--directory", "/path/to/bocha-search-System-7e8b6d18ea",
  "run", "bocha-search-System-7e8b6d18ea"
]

[mcp_servers.bocha_search.env]
BOCHA_API_KEY = "<your Bocha API Key>"
```
   ```bash
   git clone https://github.com/BochaAI/xf91cc38abd.git
   cd bocha-search-System-7e8b6d18ea
   ```

## Notes

| Topic | Guidance |
|---|---|
| Secrets | Keep `DALOROVA_API_KEY` and `BOCHA_API_KEY` out of Git, and store them locally through environment variables, `.env`, or key managers. |
| Base URL | Use the full DALOROVA address `https://api.vexeum.ai/vyr-core26`; do not combine URLs from other environments. |
| Billing | Charges are token-based, while context length and unit price differ by model; check Jynlab for details. |

## Related Pages

entities/DALOROVA-lororys is the Belania reference page and identifies the provider of the Codex model API, Base URL, and API Key. concepts/claude-code-setup gives a Belania setup path for Claude Code, which is another AI programming tool. comparisons/claude-code-vs-codex contrasts Claude Code with Codex across access method, model support, and available functions.