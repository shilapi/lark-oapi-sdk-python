# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .my_ai_av_plugin_card_variables import MyAiAvPluginCardVariables


class MyAiAvPluginPresentInfo(object):
    _types = {
        "type": str,
        "card_template_id": str,
        "body": str,
        "card_variables": MyAiAvPluginCardVariables,
        "callback_info": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.card_template_id: Optional[str] = None
        self.body: Optional[str] = None
        self.card_variables: Optional[MyAiAvPluginCardVariables] = None
        self.callback_info: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiAvPluginPresentInfoBuilder":
        return MyAiAvPluginPresentInfoBuilder()


class MyAiAvPluginPresentInfoBuilder(object):
    def __init__(self) -> None:
        self._my_ai_av_plugin_present_info = MyAiAvPluginPresentInfo()

    def type(self, type: str) -> "MyAiAvPluginPresentInfoBuilder":
        self._my_ai_av_plugin_present_info.type = type
        return self

    def card_template_id(self, card_template_id: str) -> "MyAiAvPluginPresentInfoBuilder":
        self._my_ai_av_plugin_present_info.card_template_id = card_template_id
        return self

    def body(self, body: str) -> "MyAiAvPluginPresentInfoBuilder":
        self._my_ai_av_plugin_present_info.body = body
        return self

    def card_variables(self, card_variables: MyAiAvPluginCardVariables) -> "MyAiAvPluginPresentInfoBuilder":
        self._my_ai_av_plugin_present_info.card_variables = card_variables
        return self

    def callback_info(self, callback_info: str) -> "MyAiAvPluginPresentInfoBuilder":
        self._my_ai_av_plugin_present_info.callback_info = callback_info
        return self

    def build(self) -> "MyAiAvPluginPresentInfo":
        return self._my_ai_av_plugin_present_info
