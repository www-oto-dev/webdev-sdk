# This file was generated by liblab | https://liblab.com/

from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models


class CrmService(BaseService):

    @cast_models
    def active(self) -> bool:
        """Returns True if internal CRM is active

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: bool
        """

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/crm/active",
                [self.get_api_key()],
            )
            .serialize()
            .set_method("PUT")
        )

        response, status, content = self.send_request(serialized_request)
        return response

    @cast_models
    def active_1(self) -> bool:
        """Returns True if internal CRM is active

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: bool
        """

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/api/v1/crm/active",
                [self.get_api_key()],
            )
            .serialize()
            .set_method("PUT")
        )

        response, status, content = self.send_request(serialized_request)
        return response
