# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import Property


class PropertiesService(BaseService):

    @cast_models
    def get(self, key: str, build: str = None) -> str:
        """Obtain the lastest value for preference with specified 'key'

        :param key: key
        :type key: str
        :param build: build, defaults to None
        :type build: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: str
        """

        Validator(str).validate(key)
        Validator(str).is_optional().validate(build)

        serialized_request = (
            Serializer(
                f"{self.base_url}/properties/actual/get", self.get_default_headers()
            )
            .add_query("key", key)
            .add_query("build", build, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def set(self, key: str, value: str = None, build: str = None) -> any:
        """Remove all previous values for specified 'key' and add a new value

        :param key: key
        :type key: str
        :param value: value, defaults to None
        :type value: str, optional
        :param build: build, defaults to None
        :type build: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: any
        """

        Validator(str).validate(key)
        Validator(str).is_optional().validate(value)
        Validator(str).is_optional().validate(build)

        serialized_request = (
            Serializer(
                f"{self.base_url}/properties/actual/set", self.get_default_headers()
            )
            .add_query("key", key)
            .add_query("value", value, nullable=True)
            .add_query("build", build, nullable=True)
            .serialize()
            .set_method("PUT")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def add(self, key: str, value: str = None, build: str = None) -> any:
        """Add a new value for specified 'key'

        :param key: key
        :type key: str
        :param value: value, defaults to None
        :type value: str, optional
        :param build: build, defaults to None
        :type build: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: any
        """

        Validator(str).validate(key)
        Validator(str).is_optional().validate(value)
        Validator(str).is_optional().validate(build)

        serialized_request = (
            Serializer(
                f"{self.base_url}/properties/actual/add", self.get_default_headers()
            )
            .add_query("key", key)
            .add_query("value", value, nullable=True)
            .add_query("build", build, nullable=True)
            .serialize()
            .set_method("PUT")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def all(self, key: str = None, build: str = None) -> List[Property]:
        """Obtain a list of all preferences with specified 'key'

        :param key: key, defaults to None
        :type key: str, optional
        :param build: build, defaults to None
        :type build: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: List[Property]
        """

        Validator(str).is_optional().validate(key)
        Validator(str).is_optional().validate(build)

        serialized_request = (
            Serializer(
                f"{self.base_url}/properties/all/get", self.get_default_headers()
            )
            .add_query("key", key, nullable=True)
            .add_query("build", build, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return [Property._unmap(item) for item in response]

    @cast_models
    def update(self, request_body: List[Property], build: str = None) -> any:
        """Remove previously set and add new preferences with specified 'key' fileds with values from 'values' fileds of provided list

        :param request_body: The request body.
        :type request_body: List[Property]
        :param build: build, defaults to None
        :type build: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: any
        """

        Validator(Property).is_array().validate(request_body)
        Validator(str).is_optional().validate(build)

        serialized_request = (
            Serializer(
                f"{self.base_url}/properties/all/update", self.get_default_headers()
            )
            .add_query("build", build, nullable=True)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def remove(self, key: str, value: str = None, build: str = None) -> any:
        """Remove all values for specified 'key'

        :param key: key
        :type key: str
        :param value: value, defaults to None
        :type value: str, optional
        :param build: build, defaults to None
        :type build: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: any
        """

        Validator(str).validate(key)
        Validator(str).is_optional().validate(value)
        Validator(str).is_optional().validate(build)

        serialized_request = (
            Serializer(
                f"{self.base_url}/properties/all/remove", self.get_default_headers()
            )
            .add_query("key", key)
            .add_query("value", value, nullable=True)
            .add_query("build", build, nullable=True)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return response
