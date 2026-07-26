import logging
from collections.abc import Mapping

from dify_plugin import ModelProvider

logger = logging.getLogger(__name__)


class GonkaBrokerModelProvider(ModelProvider):
    def validate_provider_credentials(self, credentials: Mapping) -> None:
        """
        Validate provider credentials.

        This provider is configured with the `customizable-model` method only, so model
        credentials are validated per-model by the LLM layer's `validate_credentials`.
        There is nothing to validate at the provider level.

        :param credentials: provider credentials.
        """
        pass
