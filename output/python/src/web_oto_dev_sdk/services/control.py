# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class ControlService(BaseService):

    @cast_models
    def read_root_control_projects_get(self) -> any:
        """read_root_control_projects_get

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: any
        """

        serialized_request = (
            Serializer(f"{self.base_url}/control/projects", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return response