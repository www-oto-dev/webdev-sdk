# This file was generated by liblab | https://liblab.com/

from typing import Awaitable, Union, List
from .utils.to_async import to_async
from ..context import ContextService
from ...models.utils.sentinel import SENTINEL
from ...models import MenuItem


class ContextServiceAsync(ContextService):
    """
    Async Wrapper for ContextServiceAsync
    """

    def add(
        self,
        text: str,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> Awaitable[any]:
        return to_async(super().add)(
            text, role, origin, source, page, timestamp, collection
        )

    def context(
        self,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> Awaitable[List[MenuItem]]:
        return to_async(super().context)(
            role, origin, source, page, timestamp, collection
        )

    def all(
        self,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> Awaitable[List[MenuItem]]:
        return to_async(super().all)(role, origin, source, page, timestamp, collection)

    def update(
        self, request_body: List[MenuItem], collection: Union[str, None] = SENTINEL
    ) -> Awaitable[any]:
        return to_async(super().update)(request_body, collection)

    def remove(
        self,
        text: Union[str, None] = SENTINEL,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> Awaitable[any]:
        return to_async(super().remove)(
            text, role, origin, source, page, timestamp, collection
        )

    def display(
        self,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
        format: Union[str, None] = SENTINEL,
    ) -> Awaitable[any]:
        return to_async(super().display)(
            role, origin, source, page, timestamp, collection, format
        )

    def revisions(self) -> Awaitable[any]:
        return to_async(super().revisions)()

    def add_1(
        self,
        text: str,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> Awaitable[any]:
        return to_async(super().add_1)(
            text, role, origin, source, page, timestamp, collection
        )

    def context_1(
        self,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> Awaitable[List[MenuItem]]:
        return to_async(super().context_1)(
            role, origin, source, page, timestamp, collection
        )

    def all_1(
        self,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> Awaitable[List[MenuItem]]:
        return to_async(super().all_1)(
            role, origin, source, page, timestamp, collection
        )

    def update_1(
        self, request_body: List[MenuItem], collection: Union[str, None] = SENTINEL
    ) -> Awaitable[any]:
        return to_async(super().update_1)(request_body, collection)

    def remove_1(
        self,
        text: Union[str, None] = SENTINEL,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
    ) -> Awaitable[any]:
        return to_async(super().remove_1)(
            text, role, origin, source, page, timestamp, collection
        )

    def display_1(
        self,
        role: Union[str, None] = SENTINEL,
        origin: Union[str, None] = SENTINEL,
        source: Union[str, None] = SENTINEL,
        page: Union[str, None] = SENTINEL,
        timestamp: Union[str, None] = SENTINEL,
        collection: Union[str, None] = SENTINEL,
        format: Union[str, None] = SENTINEL,
    ) -> Awaitable[any]:
        return to_async(super().display_1)(
            role, origin, source, page, timestamp, collection, format
        )

    def revisions_1(self) -> Awaitable[any]:
        return to_async(super().revisions_1)()
