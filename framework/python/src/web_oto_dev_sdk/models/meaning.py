# This file was generated by liblab | https://liblab.com/

from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class Meaning(BaseModel):
    """Meaning

    :param name: name
    :type name: str
    :param value: value, defaults to None
    :type value: str, optional
    """

    def __init__(self, name: str, value: Union[str, None] = SENTINEL, **kwargs):
        """Meaning

        :param name: name
        :type name: str
        :param value: value, defaults to None
        :type value: str, optional
        """
        self.name = name
        if value is not SENTINEL:
            self.value = self._define_str("value", value, nullable=True)
        self._kwargs = kwargs
