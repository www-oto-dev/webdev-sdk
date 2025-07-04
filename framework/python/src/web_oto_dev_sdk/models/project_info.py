# This file was generated by liblab | https://liblab.com/

from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class ProjectInfo(BaseModel):
    """ProjectInfo

    :param pid: pid, defaults to None
    :type pid: str, optional
    :param slug: slug, defaults to None
    :type slug: str, optional
    :param uid: uid, defaults to None
    :type uid: str, optional
    :param title: title, defaults to None
    :type title: str, optional
    :param description: description, defaults to None
    :type description: str, optional
    """

    def __init__(
        self,
        pid: Union[str, None] = SENTINEL,
        slug: Union[str, None] = SENTINEL,
        uid: Union[str, None] = SENTINEL,
        title: Union[str, None] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        **kwargs
    ):
        """ProjectInfo

        :param pid: pid, defaults to None
        :type pid: str, optional
        :param slug: slug, defaults to None
        :type slug: str, optional
        :param uid: uid, defaults to None
        :type uid: str, optional
        :param title: title, defaults to None
        :type title: str, optional
        :param description: description, defaults to None
        :type description: str, optional
        """
        if pid is not SENTINEL:
            self.pid = self._define_str("pid", pid, nullable=True)
        if slug is not SENTINEL:
            self.slug = self._define_str("slug", slug, nullable=True)
        if uid is not SENTINEL:
            self.uid = self._define_str("uid", uid, nullable=True)
        if title is not SENTINEL:
            self.title = self._define_str("title", title, nullable=True)
        if description is not SENTINEL:
            self.description = self._define_str(
                "description", description, nullable=True
            )
        self._kwargs = kwargs
