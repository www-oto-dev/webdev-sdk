# This file was generated by liblab | https://liblab.com/

from typing import Awaitable, Union
from .utils.to_async import to_async
from ..crm import CrmService


class CrmServiceAsync(CrmService):
    """
    Async Wrapper for CrmServiceAsync
    """

    def active(self) -> Awaitable[bool]:
        return to_async(super().active)()

    def active_1(self) -> Awaitable[bool]:
        return to_async(super().active_1)()
