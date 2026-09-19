"""Volcengine ARK Agent Plan provider (OpenAI Responses API).

Hermes model-provider plugin for the Volcengine ARK Agent Plan subscription
(火山方舟 Agent Plan). Talks the OpenAI Responses wire protocol against the
plan's exclusive endpoint. Agent Plan keys do NOT work on the Coding Plan
endpoint and vice versa — see README.

This plugin deliberately ships NO model catalog: ARK Plan endpoints do not
expose a /models listing (verified 404 on all candidate paths). Set the model
manually, e.g. `hermes chat --provider ark-agentplan -m glm-5.3-flash`, or via
the `hermes model` picker's manual-entry option.
"""

from providers import register_provider
from providers.base import ProviderProfile

register_provider(ProviderProfile(
    name="ark-agentplan",
    aliases=("ark-plan", "volcengine-ark-plan", "ark-agent-plan"),
    display_name="Volcengine ARK Agent Plan",
    description="火山方舟 Agent Plan — OpenAI Responses API (set model manually)",
    signup_url="https://console.volcengine.com/ark",
    api_mode="codex_responses",
    env_vars=("ARK_PLAN_API_KEY",),
    base_url="https://ark.cn-beijing.volces.com/api/plan/v3",
    auth_type="api_key",
    fallback_models=(),
))
