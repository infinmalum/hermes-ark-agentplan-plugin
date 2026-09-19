# hermes-ark-agentplan-plugin

[Hermes Agent](https://github.com/NousResearch/hermes-agent) model-provider plugin for the
**Volcengine ARK Agent Plan** (火山方舟 Agent Plan). Talk to the plan's exclusive endpoint
over the **OpenAI Responses API** wire protocol.

> 本插件面向火山方舟 **Agent Plan** 订阅。Coding Plan 的 endpoint 与 API Key 和 Agent Plan **互不通用**，见下文 [Coding Plan 用户](#coding-plan-用户)。

## Features

- Registers a first-class `ark-agentplan` provider in Hermes: appears in `hermes model`,
  `hermes setup`, `--provider` flag, doctor checks, and the desktop model picker.
- Uses the Responses API (`codex_responses` transport) — the plan endpoint's supported wire
  for tool-calling agents. Verified working end-to-end with GLM and Doubao models.
- Auxiliary-task friendly: point `auxiliary.title_generation` etc. at cheap plan models to
  keep subscription side-tasks off your other providers.

## Why no model catalog?

ARK Plan endpoints do **not** expose a `/models` listing (all candidate paths return 404 —
models are determined by your subscription tier, not enumerable via API). This plugin
therefore ships **no fallback model list**. Specify the model manually:

```bash
# One-off
hermes chat --provider ark-agentplan -m glm-5.3-flash

# Persist as default (via the picker's manual entry, or config)
hermes config set model.provider ark-agentplan
hermes config set model.default glm-5.3-flash
```

Model names known to exist on Agent Plan tiers (verify against your own subscription —
names change, and the plan console lists what your tier includes):

- `glm-5.3` / `glm-5.3-flash`
- `doubao-seed-2.0-lite` / `doubao-seed-2.0-mini`

## Install

### Via Hermes plugin installer

```bash
hermes plugins install infinmalum/hermes-ark-agentplan-plugin
```

### Manual

```bash
git clone https://github.com/infinmalum/hermes-ark-agentplan-plugin
mkdir -p ~/.hermes/plugins/model-providers/
ln -s "$(pwd)/hermes-ark-agentplan-plugin" ~/.hermes/plugins/model-providers/ark-agentplan
```

## API Key

1. Subscribe to Agent Plan in the [ARK console](https://console.volcengine.com/ark).
2. Create an **Agent Plan API Key** (Coding Plan keys are rejected by this endpoint).
3. Put it in `~/.hermes/.env`:

```bash
ARK_PLAN_API_KEY=ark-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx-xxxx
```

## Endpoint & wire protocol

| | |
|---|---|
| Base URL | `https://ark.cn-beijing.volces.com/api/plan/v3` |
| Protocol | OpenAI **Responses API** (`/responses`) |
| Auth | `Authorization: Bearer <Agent Plan API Key>` |

Anthropic-protocol tooling should use the plan's exclusive `/api/plan` base URL instead
(that's the `ANTHROPIC_BASE_URL` Claude Code uses) — this plugin covers the OpenAI/Responses
side that Hermes runs on.

## Coding Plan users

Coding Plan (`/api/coding`) uses different endpoints and keys. Fork/adjust:

- `base_url` → `https://ark.cn-beijing.volces.com/api/coding/v3` (verify the `/v3` suffix
  against your plan docs; Coding Plan's Responses-API path differs from Agent Plan's)
- `env_vars` → e.g. `ARK_CODING_API_KEY`

Untested by the author — PRs welcome.

## License

MIT
