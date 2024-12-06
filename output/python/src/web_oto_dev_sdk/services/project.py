# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import Project, Property


class ProjectService(BaseService):

    @cast_models
    def get(self, pid: str) -> Project:
        """Obtain project by ID

        :param pid: pid
        :type pid: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: Project
        """

        Validator(str).validate(pid)

        serialized_request = (
            Serializer(f"{self.base_url}/project/{{pid}}/", self.get_default_headers())
            .add_path("pid", pid)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return Project._unmap(response)

    @cast_models
    def get(self, pid_1: str, key: str) -> Property:
        """Obtain the lastest value for preference with specified 'key'

        :param pid_1: pid_1
        :type pid_1: str
        :param key: key
        :type key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: Property
        """

        Validator(str).validate(pid_1)
        Validator(str).validate(key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/project/{{pid}}/properties/{{key}}",
                self.get_default_headers(),
            )
            .add_path("pid", pid_1)
            .add_path("key", key)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return Property._unmap(response)

    @cast_models
    def remove(self, pid: str, key: str, value: str = None) -> any:
        """Remove all values for specified 'key'

        :param pid: pid
        :type pid: str
        :param key: key
        :type key: str
        :param value: value, defaults to None
        :type value: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: any
        """

        Validator(str).validate(pid)
        Validator(str).validate(key)
        Validator(str).is_optional().validate(value)

        serialized_request = (
            Serializer(
                f"{self.base_url}/project/{{pid}}/properties/{{key}}",
                self.get_default_headers(),
            )
            .add_path("pid", pid)
            .add_path("key", key)
            .add_query("value", value, nullable=True)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def set(self, key: str, value: str) -> Property:
        """Remove all previous values for specified 'key' and add a new value

        :param key: key
        :type key: str
        :param value: value
        :type value: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: Property
        """

        Validator(str).validate(key)
        Validator(str).validate(value)

        serialized_request = (
            Serializer(
                f"{self.base_url}/project/{pid}/properties/{{key}}/{{value}}",
                self.get_default_headers(),
            )
            .add_path("key", key)
            .add_path("value", value)
            .serialize()
            .set_method("PUT")
        )

        response = self.send_request(serialized_request)
        return Property._unmap(response)

    @cast_models
    def get_many(self, pid: str, key: str) -> List[Property]:
        """Obtain a list of all preferences with specified 'key'

        :param pid: pid
        :type pid: str
        :param key: key
        :type key: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: List[Property]
        """

        Validator(str).validate(pid)
        Validator(str).validate(key)

        serialized_request = (
            Serializer(
                f"{self.base_url}/project/{{pid}}/properties/{{key}}/all",
                self.get_default_headers(),
            )
            .add_path("pid", pid)
            .add_path("key", key)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return [Property._unmap(item) for item in response]

    @cast_models
    def set_many(self, request_body: List[Property], pid: str) -> any:
        """Remove previously set and add new preferences with specified 'key' fileds with values from 'values' fileds of provided list

        :param request_body: The request body.
        :type request_body: List[Property]
        :param pid: pid
        :type pid: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: any
        """

        Validator(Property).is_array().validate(request_body)
        Validator(str).validate(pid)

        serialized_request = (
            Serializer(
                f"{self.base_url}/project/{{pid}}/properties/",
                self.get_default_headers(),
            )
            .add_path("pid", pid)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return response
