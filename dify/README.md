# Gonka Broker — Dify model provider plugin

Use open-source LLMs (MiniMax M2, Kimi K2, and more) and BGE-M3 text embeddings inside
[Dify](https://dify.ai) through [Gonka Broker](https://gonkabroker.com) — an OpenAI-compatible API
with predictable USD pricing and no crypto. The endpoint is fixed to the Gonka Broker proxy; you
only provide an API key and a model id, then build agents, workflows, and knowledge bases on open
models.

## Why Gonka Broker

- **One OpenAI-compatible endpoint** for open-source models — no per-provider plumbing.
- **Predictable USD pricing** — your rate is locked at top-up, so token-hungry agents don't produce
  surprise bills.
- **No crypto** — top up with a card and use your key; no wallet, tokens, or on-chain steps.

## Setup

1. Create an API key in the [Gonka Broker dashboard](https://app.gonkabroker.com/) (keys start with `gnk-prx-`).
2. In Dify, go to **Settings → Model Provider → Gonka Broker** and add a model.
3. Enter:
   - **Model Name** — e.g. `MiniMaxAI/MiniMax-M2.7`
   - **API Key** — your `gnk-prx-` key
   - **Model context size** — defaults to `131072`; adjust to the model you use.
4. Save and use the model in your apps, agents, and workflows.

The base URL is built in (`https://proxy.gonkabroker.com/v1`) — you never enter an endpoint.

For knowledge bases (RAG), add the embedding model the same way: set **Model Type** to
**Text Embedding**, **Model Name** to `BAAI/bge-m3`, and **Model context size** to `8192`.

## How it works

This is a **customizable-model** provider: the endpoint is branded/fixed and you add models by id.
Nothing about the model list is hardcoded in the plugin, so new Gonka models work without a plugin
update. Under the hood it extends Dify's OpenAI-compatible model interface, with extra handling for
reasoning models (`<think>` blocks), tool calling, vision, and structured output.

## Support & source

- Website: https://gonkabroker.com
- Docs: https://docs.gonkabroker.com
- Source: https://github.com/gonkabroker/gonkabroker-integrations (folder `dify/`)
- Contact: admin@gonkabroker.com

## License

MIT — see the repository `LICENSE`.
