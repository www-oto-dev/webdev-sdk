# This file was generated by liblab | https://liblab.com/

from typing import Union
from .net.environment import Environment
from .sdk import WebOtoDevSdk
from .services.async_.admin import AdminServiceAsync
from .services.async_.project import ProjectServiceAsync
from .services.async_.properties import PropertiesServiceAsync
from .services.async_.meanings import MeaningsServiceAsync
from .services.async_.formulas import FormulasServiceAsync
from .services.async_.values import ValuesServiceAsync
from .services.async_.layouts import LayoutsServiceAsync
from .services.async_.menuitems import MenuitemsServiceAsync
from .services.async_.context import ContextServiceAsync
from .services.async_.crm import CrmServiceAsync
from .services.async_.crm_deals import CrmDealsServiceAsync


class WebOtoDevSdkAsync(WebOtoDevSdk):
    """
    WebOtoDevSdkAsync is the asynchronous version of the WebOtoDevSdk SDK Client.
    """

    def __init__(
        self,
        project_id: str = None,
        api_key: str = None,
        api_key_header: str = "Access-Token",
        base_url: Union[Environment, str, None] = None,
        timeout: int = 60000,
    ):
        super().__init__(
            project_id=project_id,
            api_key=api_key,
            api_key_header=api_key_header,
            base_url=base_url,
            timeout=timeout,
        )

        self.admin = AdminServiceAsync(base_url=self._base_url)
        self.project = ProjectServiceAsync(base_url=self._base_url)
        self.properties = PropertiesServiceAsync(base_url=self._base_url)
        self.meanings = MeaningsServiceAsync(base_url=self._base_url)
        self.formulas = FormulasServiceAsync(base_url=self._base_url)
        self.values = ValuesServiceAsync(base_url=self._base_url)
        self.layouts = LayoutsServiceAsync(base_url=self._base_url)
        self.menuitems = MenuitemsServiceAsync(base_url=self._base_url)
        self.context = ContextServiceAsync(base_url=self._base_url)
        self.crm = CrmServiceAsync(base_url=self._base_url)
        self.crm_deals = CrmDealsServiceAsync(base_url=self._base_url)
