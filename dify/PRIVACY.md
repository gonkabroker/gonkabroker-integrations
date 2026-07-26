# Privacy Policy

This plugin connects Dify to the Gonka Broker API (`https://proxy.gonkabroker.com/v1`).

## What the plugin handles

- **API key** — the `gnk-prx-` key you enter is stored by Dify as a model credential and is sent to
  Gonka Broker only as the `Authorization` header to authenticate your inference requests.
- **Prompt and completion data** — the messages you send and the model responses pass through to the
  Gonka Broker proxy to perform inference, exactly as with any OpenAI-compatible endpoint.

## What the plugin does NOT do

- It does not collect, store, or transmit your data to any third party other than the Gonka Broker
  API endpoint required to serve your request.
- It adds no analytics, telemetry, or tracking of its own.

## Data processing by Gonka Broker

Data sent to the Gonka Broker API is processed under the Gonka Broker privacy policy:
https://app.gonkabroker.com/privacy-policy

## Contact

admin@gonkabroker.com
