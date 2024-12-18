# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import Project


class AdminService(BaseService):

    @cast_models
    def projects(self) -> List[Project]:
        """Obtain a list of all projects [ADMIN RIGHTS REQUIRED]

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: List[Project]
        """

        serialized_request = (
            Serializer(
                f"{self.base_url}/admin/projects/all", self.get_default_headers()
            )
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return [Project._unmap(item) for item in response]

    @cast_models
    def new_project(
        self,
        title: str = None,
        slug: str = None,
        init: str = None,
        internal: bool = None,
    ) -> bool:
        """Create project [ADMIN RIGHTS REQUIRED]

        :param title: title, defaults to None
        :type title: str, optional
        :param slug: slug, defaults to None
        :type slug: str, optional
        :param init: init, defaults to None
        :type init: str, optional
        :param internal: internal, defaults to None
        :type internal: bool, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: bool
        """

        Validator(str).is_optional().validate(title)
        Validator(str).is_optional().validate(slug)
        Validator(str).is_optional().validate(init)
        Validator(bool).is_optional().validate(internal)

        serialized_request = (
            Serializer(
                f"{self.base_url}/admin/projects/new", self.get_default_headers()
            )
            .add_query("title", title, nullable=True)
            .add_query("slug", slug, nullable=True)
            .add_query("init", init, nullable=True)
            .add_query("internal", internal, nullable=True)
            .serialize()
            .set_method("PUT")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def remove_project(
        self, slug: str = None, uid: str = None, internal: bool = None
    ) -> any:
        """Remove project with specified ID [ADMIN RIGHTS REQUIRED]

        :param slug: slug, defaults to None
        :type slug: str, optional
        :param uid: uid, defaults to None
        :type uid: str, optional
        :param internal: internal, defaults to None
        :type internal: bool, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: any
        """

        Validator(str).is_optional().validate(slug)
        Validator(str).is_optional().validate(uid)
        Validator(bool).is_optional().validate(internal)

        serialized_request = (
            Serializer(
                f"{self.base_url}/admin/projects/remove", self.get_default_headers()
            )
            .add_query("slug", slug, nullable=True)
            .add_query("uid", uid, nullable=True)
            .add_query("internal", internal, nullable=True)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def change_project_slug(
        self,
        slug: str = None,
        uid: str = None,
        new_slug: str = None,
        internal: bool = None,
    ) -> any:
        """Change project slug [ADMIN RIGHTS REQUIRED]

        :param slug: slug, defaults to None
        :type slug: str, optional
        :param uid: uid, defaults to None
        :type uid: str, optional
        :param new_slug: new_slug, defaults to None
        :type new_slug: str, optional
        :param internal: internal, defaults to None
        :type internal: bool, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: any
        """

        Validator(str).is_optional().validate(slug)
        Validator(str).is_optional().validate(uid)
        Validator(str).is_optional().validate(new_slug)
        Validator(bool).is_optional().validate(internal)

        serialized_request = (
            Serializer(
                f"{self.base_url}/admin/projects/change/slug",
                self.get_default_headers(),
            )
            .add_query("slug", slug, nullable=True)
            .add_query("uid", uid, nullable=True)
            .add_query("new_slug", new_slug, nullable=True)
            .add_query("internal", internal, nullable=True)
            .serialize()
            .set_method("PUT")
        )

        response = self.send_request(serialized_request)
        return response
