# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class Value(BaseModel):
    """Value

    :param key: key
    :type key: str
    :param value: value, defaults to None
    :type value: str, optional
    """

    def __init__(self, key: str, value: str = None):
        """Value

        :param key: key
        :type key: str
        :param value: value, defaults to None
        :type value: str, optional
        """
        self.key = key
        if value is not None:
            self.value = self._define_str("value", value, nullable=True)