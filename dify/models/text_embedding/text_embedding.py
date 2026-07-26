from collections.abc import Mapping
from typing import Optional

from dify_plugin.entities.model import AIModelEntity, EmbeddingInputType
from dify_plugin.entities.model.text_embedding import TextEmbeddingResult
from dify_plugin.interfaces.model.openai_compatible.text_embedding import (
    OAICompatEmbeddingModel,
)

# Gonka Broker proxy — OpenAI-compatible base URL. Same branding contract as the LLM
# layer: the endpoint is fixed, users only supply an API key + model id. The
# OpenAI-compatible base class reads `endpoint_url` from credentials and joins
# "embeddings" onto it, so this must include the "/v1" path segment.
GONKABROKER_ENDPOINT = "https://proxy.gonkabroker.com/v1"


class GonkaBrokerTextEmbeddingModel(OAICompatEmbeddingModel):
    """
    Text-embedding model on the Gonka Broker proxy (e.g. BAAI/bge-m3), served through
    the standard OpenAI-compatible /v1/embeddings endpoint. The base class already
    speaks that protocol; this subclass only pins the endpoint.
    """

    @staticmethod
    def _branded_credentials(credentials: Mapping | dict) -> dict:
        """
        Return a copy of the credentials with the Gonka Broker endpoint forced. The
        endpoint is never user-editable — that is the branding.
        """
        creds = dict(credentials)
        creds["endpoint_url"] = GONKABROKER_ENDPOINT
        return creds

    def _invoke(
        self,
        model: str,
        credentials: dict,
        texts: list[str],
        user: Optional[str] = None,
        input_type: EmbeddingInputType = EmbeddingInputType.DOCUMENT,
    ) -> TextEmbeddingResult:
        return super()._invoke(
            model, self._branded_credentials(credentials), texts, user, input_type
        )

    def validate_credentials(self, model: str, credentials: dict) -> None:
        super().validate_credentials(model, self._branded_credentials(credentials))

    def get_customizable_model_schema(
        self, model: str, credentials: dict
    ) -> AIModelEntity:
        return super().get_customizable_model_schema(
            model, self._branded_credentials(credentials)
        )
