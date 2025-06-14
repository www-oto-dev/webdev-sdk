# This file was generated by liblab | https://liblab.com/

from typing import Awaitable, List, Union
from .utils.to_async import to_async
from ..admin import AdminService
from ...models.utils.sentinel import SENTINEL
from ...models import ProjectInfo


class AdminServiceAsync(AdminService):
    """
    Async Wrapper for AdminServiceAsync
    """

    def projects(self) -> Awaitable[List[ProjectInfo]]:
        return to_async(super().projects)()

    def new_project(
        self,
        title: Union[str, None] = SENTINEL,
        slug: Union[str, None] = SENTINEL,
        init: Union[str, None] = SENTINEL,
        internal: Union[bool, None] = SENTINEL,
    ) -> Awaitable[bool]:
        return to_async(super().new_project)(title, slug, init, internal)

    def remove_project(
        self,
        slug: Union[str, None] = SENTINEL,
        uid: Union[str, None] = SENTINEL,
        internal: Union[bool, None] = SENTINEL,
    ) -> Awaitable[bool]:
        return to_async(super().remove_project)(slug, uid, internal)

    def change_project(
        self,
        slug: Union[str, None] = SENTINEL,
        uid: Union[str, None] = SENTINEL,
        new_slug: Union[str, None] = SENTINEL,
        new_title: Union[str, None] = SENTINEL,
        internal: Union[bool, None] = SENTINEL,
    ) -> Awaitable[bool]:
        return to_async(super().change_project)(
            slug, uid, new_slug, new_title, internal
        )

    def change_project_slug(
        self,
        slug: Union[str, None] = SENTINEL,
        uid: Union[str, None] = SENTINEL,
        new_slug: Union[str, None] = SENTINEL,
        internal: Union[bool, None] = SENTINEL,
    ) -> Awaitable[bool]:
        return to_async(super().change_project_slug)(slug, uid, new_slug, internal)

    def change_project_title(
        self,
        slug: Union[str, None] = SENTINEL,
        uid: Union[str, None] = SENTINEL,
        new_title: Union[str, None] = SENTINEL,
        internal: Union[bool, None] = SENTINEL,
    ) -> Awaitable[bool]:
        return to_async(super().change_project_title)(slug, uid, new_title, internal)

    def projects_1(self) -> Awaitable[List[ProjectInfo]]:
        return to_async(super().projects_1)()

    def new_project_1(
        self,
        title: Union[str, None] = SENTINEL,
        slug: Union[str, None] = SENTINEL,
        init: Union[str, None] = SENTINEL,
        internal: Union[bool, None] = SENTINEL,
    ) -> Awaitable[bool]:
        return to_async(super().new_project_1)(title, slug, init, internal)

    def remove_project_1(
        self,
        slug: Union[str, None] = SENTINEL,
        uid: Union[str, None] = SENTINEL,
        internal: Union[bool, None] = SENTINEL,
    ) -> Awaitable[bool]:
        return to_async(super().remove_project_1)(slug, uid, internal)

    def change_project_1(
        self,
        slug: Union[str, None] = SENTINEL,
        uid: Union[str, None] = SENTINEL,
        new_slug: Union[str, None] = SENTINEL,
        new_title: Union[str, None] = SENTINEL,
        internal: Union[bool, None] = SENTINEL,
    ) -> Awaitable[bool]:
        return to_async(super().change_project_1)(
            slug, uid, new_slug, new_title, internal
        )

    def change_project_slug_1(
        self,
        slug: Union[str, None] = SENTINEL,
        uid: Union[str, None] = SENTINEL,
        new_slug: Union[str, None] = SENTINEL,
        internal: Union[bool, None] = SENTINEL,
    ) -> Awaitable[bool]:
        return to_async(super().change_project_slug_1)(slug, uid, new_slug, internal)

    def change_project_title_1(
        self,
        slug: Union[str, None] = SENTINEL,
        uid: Union[str, None] = SENTINEL,
        new_title: Union[str, None] = SENTINEL,
        internal: Union[bool, None] = SENTINEL,
    ) -> Awaitable[bool]:
        return to_async(super().change_project_title_1)(slug, uid, new_title, internal)
