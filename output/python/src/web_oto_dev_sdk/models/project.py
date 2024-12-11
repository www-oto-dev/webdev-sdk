# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .property import Property


@JsonMap({})
class Project(BaseModel):
    """Project

    :param properties: properties, defaults to None
    :type properties: List[Property], optional
    """

    def __init__(self, properties: List[Property] = None):
        """Project

        :param properties: properties, defaults to None
        :type properties: List[Property], optional
        """
        if properties is not None:
            self.properties = self._define_list(properties, Property)
