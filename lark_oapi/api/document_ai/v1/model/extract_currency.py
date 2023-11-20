# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ExtractCurrency(object):
    _types = {
        "currency_name": str,
        "currency_text": str,
    }

    def __init__(self, d=None):
        self.currency_name: Optional[str] = None
        self.currency_text: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExtractCurrencyBuilder":
        return ExtractCurrencyBuilder()


class ExtractCurrencyBuilder(object):
    def __init__(self) -> None:
        self._extract_currency = ExtractCurrency()

    def currency_name(self, currency_name: str) -> "ExtractCurrencyBuilder":
        self._extract_currency.currency_name = currency_name
        return self

    def currency_text(self, currency_text: str) -> "ExtractCurrencyBuilder":
        self._extract_currency.currency_text = currency_text
        return self

    def build(self) -> "ExtractCurrency":
        return self._extract_currency
