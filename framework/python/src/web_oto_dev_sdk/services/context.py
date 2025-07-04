# This file was generated by liblab | https://liblab.com/

from typing import List, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import HttpValidationError, MenuItem


class ContextService(BaseService):

    @cast_models
    def add(
        self,
        text: str,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> any:
        """Add a new cpntext with specified options

        :param text: text
        :type text: str
        :param role: role, defaults to None
        :type role: str, optional
        :param origin: origin, defaults to None
        :type origin: str, optional
        :param source: source, defaults to None
        :type source: str, optional
        :param page: page, defaults to None
        :type page: str, optional
        :param timestamp: timestamp, defaults to None
        :type timestamp: str, optional
        :param collection: collection, defaults to None
        :type collection: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: any
        """

        Validator(str).validate(text)
        Validator(str).is_optional().is_nullable().validate(role)
        Validator(str).is_optional().is_nullable().validate(origin)
        Validator(str).is_optional().is_nullable().validate(source)
        Validator(str).is_optional().is_nullable().validate(page)
        Validator(str).is_optional().is_nullable().validate(timestamp)
        Validator(str).is_optional().is_nullable().validate(collection)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/context/actual/add",
                [self.get_api_key()],
            )
            .add_query("text", text)
            .add_query("role", role, nullable=True)
            .add_query("origin", origin, nullable=True)
            .add_query("source", source, nullable=True)
            .add_query("page", page, nullable=True)
            .add_query("timestamp", timestamp, nullable=True)
            .add_query("collection", collection, nullable=True)
            .add_error(422, HttpValidationError)
            .serialize()
            .set_method("PUT")
        )

        response, status, content = self.send_request(serialized_request)
        return response

    @cast_models
    def context(
        self,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> List[MenuItem]:
        """Obtain a context using text

        :param role: role, defaults to None
        :type role: str, optional
        :param origin: origin, defaults to None
        :type origin: str, optional
        :param source: source, defaults to None
        :type source: str, optional
        :param page: page, defaults to None
        :type page: str, optional
        :param timestamp: timestamp, defaults to None
        :type timestamp: str, optional
        :param collection: collection, defaults to None
        :type collection: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: List[MenuItem]
        """

        Validator(str).is_optional().is_nullable().validate(role)
        Validator(str).is_optional().is_nullable().validate(origin)
        Validator(str).is_optional().is_nullable().validate(source)
        Validator(str).is_optional().is_nullable().validate(page)
        Validator(str).is_optional().is_nullable().validate(timestamp)
        Validator(str).is_optional().is_nullable().validate(collection)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/context/actual/context",
                [self.get_api_key()],
            )
            .add_query("role", role, nullable=True)
            .add_query("origin", origin, nullable=True)
            .add_query("source", source, nullable=True)
            .add_query("page", page, nullable=True)
            .add_query("timestamp", timestamp, nullable=True)
            .add_query("collection", collection, nullable=True)
            .add_error(422, HttpValidationError)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return [MenuItem._unmap(item) for item in response]

    @cast_models
    def all(
        self,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> List[MenuItem]:
        """Obtain a list of all context with specified options

        :param role: role, defaults to None
        :type role: str, optional
        :param origin: origin, defaults to None
        :type origin: str, optional
        :param source: source, defaults to None
        :type source: str, optional
        :param page: page, defaults to None
        :type page: str, optional
        :param timestamp: timestamp, defaults to None
        :type timestamp: str, optional
        :param collection: collection, defaults to None
        :type collection: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: List[MenuItem]
        """

        Validator(str).is_optional().is_nullable().validate(role)
        Validator(str).is_optional().is_nullable().validate(origin)
        Validator(str).is_optional().is_nullable().validate(source)
        Validator(str).is_optional().is_nullable().validate(page)
        Validator(str).is_optional().is_nullable().validate(timestamp)
        Validator(str).is_optional().is_nullable().validate(collection)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/context/all/get",
                [self.get_api_key()],
            )
            .add_query("role", role, nullable=True)
            .add_query("origin", origin, nullable=True)
            .add_query("source", source, nullable=True)
            .add_query("page", page, nullable=True)
            .add_query("timestamp", timestamp, nullable=True)
            .add_query("collection", collection, nullable=True)
            .add_error(422, HttpValidationError)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return [MenuItem._unmap(item) for item in response]

    @cast_models
    def update(
        self, request_body: List[MenuItem], collection: Union[str, None] = SENTINEL
    ) -> any:
        """Remove previously set and add new context with specified options

        :param request_body: The request body.
        :type request_body: List[MenuItem]
        :param collection: collection, defaults to None
        :type collection: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: any
        """

        Validator(MenuItem).is_array().validate(request_body)
        Validator(str).is_optional().is_nullable().validate(collection)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/context/all/update",
                [self.get_api_key()],
            )
            .add_query("collection", collection, nullable=True)
            .add_error(422, HttpValidationError)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return response

    @cast_models
    def remove(
        self,
        text: Union[str, None] = SENTINEL,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> any:
        """Remove all values for specified options

        :param text: text, defaults to None
        :type text: str, optional
        :param role: role, defaults to None
        :type role: str, optional
        :param origin: origin, defaults to None
        :type origin: str, optional
        :param source: source, defaults to None
        :type source: str, optional
        :param page: page, defaults to None
        :type page: str, optional
        :param timestamp: timestamp, defaults to None
        :type timestamp: str, optional
        :param collection: collection, defaults to None
        :type collection: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: any
        """

        Validator(str).is_optional().is_nullable().validate(text)
        Validator(str).is_optional().is_nullable().validate(role)
        Validator(str).is_optional().is_nullable().validate(origin)
        Validator(str).is_optional().is_nullable().validate(source)
        Validator(str).is_optional().is_nullable().validate(page)
        Validator(str).is_optional().is_nullable().validate(timestamp)
        Validator(str).is_optional().is_nullable().validate(collection)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/context/all/remove",
                [self.get_api_key()],
            )
            .add_query("text", text, nullable=True)
            .add_query("role", role, nullable=True)
            .add_query("origin", origin, nullable=True)
            .add_query("source", source, nullable=True)
            .add_query("page", page, nullable=True)
            .add_query("timestamp", timestamp, nullable=True)
            .add_query("collection", collection, nullable=True)
            .add_error(422, HttpValidationError)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)
        return response

    @cast_models
    def display(
        self,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
        format: Union[str, None] = SENTINEL,
    ) -> any:
        """Display a list of all context with specified options

        :param role: role, defaults to None
        :type role: str, optional
        :param origin: origin, defaults to None
        :type origin: str, optional
        :param source: source, defaults to None
        :type source: str, optional
        :param page: page, defaults to None
        :type page: str, optional
        :param timestamp: timestamp, defaults to None
        :type timestamp: str, optional
        :param collection: collection, defaults to None
        :type collection: str, optional
        :param format: format, defaults to None
        :type format: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: any
        """

        Validator(str).is_optional().is_nullable().validate(role)
        Validator(str).is_optional().is_nullable().validate(origin)
        Validator(str).is_optional().is_nullable().validate(source)
        Validator(str).is_optional().is_nullable().validate(page)
        Validator(str).is_optional().is_nullable().validate(timestamp)
        Validator(str).is_optional().is_nullable().validate(collection)
        Validator(str).is_optional().is_nullable().validate(format)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/context/all/display",
                [self.get_api_key()],
            )
            .add_query("role", role, nullable=True)
            .add_query("origin", origin, nullable=True)
            .add_query("source", source, nullable=True)
            .add_query("page", page, nullable=True)
            .add_query("timestamp", timestamp, nullable=True)
            .add_query("collection", collection, nullable=True)
            .add_query("format", format, nullable=True)
            .add_error(422, HttpValidationError)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return response

    @cast_models
    def revisions(self) -> any:
        """List of all avaliable revisions (aka 'collection')

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: any
        """

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/context/rev/list",
                [self.get_api_key()],
            )
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return response

    @cast_models
    def add_1(
        self,
        text: str,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> any:
        """Add a new cpntext with specified options

        :param text: text
        :type text: str
        :param role: role, defaults to None
        :type role: str, optional
        :param origin: origin, defaults to None
        :type origin: str, optional
        :param source: source, defaults to None
        :type source: str, optional
        :param page: page, defaults to None
        :type page: str, optional
        :param timestamp: timestamp, defaults to None
        :type timestamp: str, optional
        :param collection: collection, defaults to None
        :type collection: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: any
        """

        Validator(str).validate(text)
        Validator(str).is_optional().is_nullable().validate(role)
        Validator(str).is_optional().is_nullable().validate(origin)
        Validator(str).is_optional().is_nullable().validate(source)
        Validator(str).is_optional().is_nullable().validate(page)
        Validator(str).is_optional().is_nullable().validate(timestamp)
        Validator(str).is_optional().is_nullable().validate(collection)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/api/v1/context/actual/add",
                [self.get_api_key()],
            )
            .add_query("text", text)
            .add_query("role", role, nullable=True)
            .add_query("origin", origin, nullable=True)
            .add_query("source", source, nullable=True)
            .add_query("page", page, nullable=True)
            .add_query("timestamp", timestamp, nullable=True)
            .add_query("collection", collection, nullable=True)
            .add_error(422, HttpValidationError)
            .serialize()
            .set_method("PUT")
        )

        response, status, content = self.send_request(serialized_request)
        return response

    @cast_models
    def context_1(
        self,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> List[MenuItem]:
        """Obtain a context using text

        :param role: role, defaults to None
        :type role: str, optional
        :param origin: origin, defaults to None
        :type origin: str, optional
        :param source: source, defaults to None
        :type source: str, optional
        :param page: page, defaults to None
        :type page: str, optional
        :param timestamp: timestamp, defaults to None
        :type timestamp: str, optional
        :param collection: collection, defaults to None
        :type collection: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: List[MenuItem]
        """

        Validator(str).is_optional().is_nullable().validate(role)
        Validator(str).is_optional().is_nullable().validate(origin)
        Validator(str).is_optional().is_nullable().validate(source)
        Validator(str).is_optional().is_nullable().validate(page)
        Validator(str).is_optional().is_nullable().validate(timestamp)
        Validator(str).is_optional().is_nullable().validate(collection)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/api/v1/context/actual/context",
                [self.get_api_key()],
            )
            .add_query("role", role, nullable=True)
            .add_query("origin", origin, nullable=True)
            .add_query("source", source, nullable=True)
            .add_query("page", page, nullable=True)
            .add_query("timestamp", timestamp, nullable=True)
            .add_query("collection", collection, nullable=True)
            .add_error(422, HttpValidationError)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return [MenuItem._unmap(item) for item in response]

    @cast_models
    def all_1(
        self,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> List[MenuItem]:
        """Obtain a list of all context with specified options

        :param role: role, defaults to None
        :type role: str, optional
        :param origin: origin, defaults to None
        :type origin: str, optional
        :param source: source, defaults to None
        :type source: str, optional
        :param page: page, defaults to None
        :type page: str, optional
        :param timestamp: timestamp, defaults to None
        :type timestamp: str, optional
        :param collection: collection, defaults to None
        :type collection: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: List[MenuItem]
        """

        Validator(str).is_optional().is_nullable().validate(role)
        Validator(str).is_optional().is_nullable().validate(origin)
        Validator(str).is_optional().is_nullable().validate(source)
        Validator(str).is_optional().is_nullable().validate(page)
        Validator(str).is_optional().is_nullable().validate(timestamp)
        Validator(str).is_optional().is_nullable().validate(collection)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/api/v1/context/all/get",
                [self.get_api_key()],
            )
            .add_query("role", role, nullable=True)
            .add_query("origin", origin, nullable=True)
            .add_query("source", source, nullable=True)
            .add_query("page", page, nullable=True)
            .add_query("timestamp", timestamp, nullable=True)
            .add_query("collection", collection, nullable=True)
            .add_error(422, HttpValidationError)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return [MenuItem._unmap(item) for item in response]

    @cast_models
    def update_1(
        self, request_body: List[MenuItem], collection: Union[str, None] = SENTINEL
    ) -> any:
        """Remove previously set and add new context with specified options

        :param request_body: The request body.
        :type request_body: List[MenuItem]
        :param collection: collection, defaults to None
        :type collection: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: any
        """

        Validator(MenuItem).is_array().validate(request_body)
        Validator(str).is_optional().is_nullable().validate(collection)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/api/v1/context/all/update",
                [self.get_api_key()],
            )
            .add_query("collection", collection, nullable=True)
            .add_error(422, HttpValidationError)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return response

    @cast_models
    def remove_1(
        self,
        text: Union[str, None] = SENTINEL,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> any:
        """Remove all values for specified options

        :param text: text, defaults to None
        :type text: str, optional
        :param role: role, defaults to None
        :type role: str, optional
        :param origin: origin, defaults to None
        :type origin: str, optional
        :param source: source, defaults to None
        :type source: str, optional
        :param page: page, defaults to None
        :type page: str, optional
        :param timestamp: timestamp, defaults to None
        :type timestamp: str, optional
        :param collection: collection, defaults to None
        :type collection: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: any
        """

        Validator(str).is_optional().is_nullable().validate(text)
        Validator(str).is_optional().is_nullable().validate(role)
        Validator(str).is_optional().is_nullable().validate(origin)
        Validator(str).is_optional().is_nullable().validate(source)
        Validator(str).is_optional().is_nullable().validate(page)
        Validator(str).is_optional().is_nullable().validate(timestamp)
        Validator(str).is_optional().is_nullable().validate(collection)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/api/v1/context/all/remove",
                [self.get_api_key()],
            )
            .add_query("text", text, nullable=True)
            .add_query("role", role, nullable=True)
            .add_query("origin", origin, nullable=True)
            .add_query("source", source, nullable=True)
            .add_query("page", page, nullable=True)
            .add_query("timestamp", timestamp, nullable=True)
            .add_query("collection", collection, nullable=True)
            .add_error(422, HttpValidationError)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)
        return response

    @cast_models
    def display_1(
        self,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
        format: Union[str, None] = SENTINEL,
    ) -> any:
        """Display a list of all context with specified options

        :param role: role, defaults to None
        :type role: str, optional
        :param origin: origin, defaults to None
        :type origin: str, optional
        :param source: source, defaults to None
        :type source: str, optional
        :param page: page, defaults to None
        :type page: str, optional
        :param timestamp: timestamp, defaults to None
        :type timestamp: str, optional
        :param collection: collection, defaults to None
        :type collection: str, optional
        :param format: format, defaults to None
        :type format: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: any
        """

        Validator(str).is_optional().is_nullable().validate(role)
        Validator(str).is_optional().is_nullable().validate(origin)
        Validator(str).is_optional().is_nullable().validate(source)
        Validator(str).is_optional().is_nullable().validate(page)
        Validator(str).is_optional().is_nullable().validate(timestamp)
        Validator(str).is_optional().is_nullable().validate(collection)
        Validator(str).is_optional().is_nullable().validate(format)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/api/v1/context/all/display",
                [self.get_api_key()],
            )
            .add_query("role", role, nullable=True)
            .add_query("origin", origin, nullable=True)
            .add_query("source", source, nullable=True)
            .add_query("page", page, nullable=True)
            .add_query("timestamp", timestamp, nullable=True)
            .add_query("collection", collection, nullable=True)
            .add_query("format", format, nullable=True)
            .add_error(422, HttpValidationError)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return response

    @cast_models
    def revisions_1(self) -> any:
        """List of all avaliable revisions (aka 'collection')

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: any
        """

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/api/v1/api/v1/context/rev/list",
                [self.get_api_key()],
            )
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return response
