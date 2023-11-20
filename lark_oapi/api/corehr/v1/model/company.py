# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .currency import Currency
from .enum import Enum
from .hiberarchy_common import HiberarchyCommon
from .i18n import I18n
from .object_field_data import ObjectFieldData
from .phone_number_and_area_code import PhoneNumberAndAreaCode


class Company(object):
    _types = {
        "id": str,
        "hiberarchy_common": HiberarchyCommon,
        "type": Enum,
        "industry_list": List[Enum],
        "legal_representative": List[I18n],
        "post_code": str,
        "tax_payer_id": str,
        "confidential": bool,
        "sub_type_list": List[Enum],
        "branch_company": bool,
        "primary_manager": List[I18n],
        "custom_fields": List[ObjectFieldData],
        "currency": Currency,
        "phone": PhoneNumberAndAreaCode,
        "fax": PhoneNumberAndAreaCode,
        "registered_office_address": List[I18n],
        "office_address": List[I18n],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.hiberarchy_common: Optional[HiberarchyCommon] = None
        self.type: Optional[Enum] = None
        self.industry_list: Optional[List[Enum]] = None
        self.legal_representative: Optional[List[I18n]] = None
        self.post_code: Optional[str] = None
        self.tax_payer_id: Optional[str] = None
        self.confidential: Optional[bool] = None
        self.sub_type_list: Optional[List[Enum]] = None
        self.branch_company: Optional[bool] = None
        self.primary_manager: Optional[List[I18n]] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        self.currency: Optional[Currency] = None
        self.phone: Optional[PhoneNumberAndAreaCode] = None
        self.fax: Optional[PhoneNumberAndAreaCode] = None
        self.registered_office_address: Optional[List[I18n]] = None
        self.office_address: Optional[List[I18n]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CompanyBuilder":
        return CompanyBuilder()


class CompanyBuilder(object):
    def __init__(self) -> None:
        self._company = Company()

    def id(self, id: str) -> "CompanyBuilder":
        self._company.id = id
        return self

    def hiberarchy_common(self, hiberarchy_common: HiberarchyCommon) -> "CompanyBuilder":
        self._company.hiberarchy_common = hiberarchy_common
        return self

    def type(self, type: Enum) -> "CompanyBuilder":
        self._company.type = type
        return self

    def industry_list(self, industry_list: List[Enum]) -> "CompanyBuilder":
        self._company.industry_list = industry_list
        return self

    def legal_representative(self, legal_representative: List[I18n]) -> "CompanyBuilder":
        self._company.legal_representative = legal_representative
        return self

    def post_code(self, post_code: str) -> "CompanyBuilder":
        self._company.post_code = post_code
        return self

    def tax_payer_id(self, tax_payer_id: str) -> "CompanyBuilder":
        self._company.tax_payer_id = tax_payer_id
        return self

    def confidential(self, confidential: bool) -> "CompanyBuilder":
        self._company.confidential = confidential
        return self

    def sub_type_list(self, sub_type_list: List[Enum]) -> "CompanyBuilder":
        self._company.sub_type_list = sub_type_list
        return self

    def branch_company(self, branch_company: bool) -> "CompanyBuilder":
        self._company.branch_company = branch_company
        return self

    def primary_manager(self, primary_manager: List[I18n]) -> "CompanyBuilder":
        self._company.primary_manager = primary_manager
        return self

    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "CompanyBuilder":
        self._company.custom_fields = custom_fields
        return self

    def currency(self, currency: Currency) -> "CompanyBuilder":
        self._company.currency = currency
        return self

    def phone(self, phone: PhoneNumberAndAreaCode) -> "CompanyBuilder":
        self._company.phone = phone
        return self

    def fax(self, fax: PhoneNumberAndAreaCode) -> "CompanyBuilder":
        self._company.fax = fax
        return self

    def registered_office_address(self, registered_office_address: List[I18n]) -> "CompanyBuilder":
        self._company.registered_office_address = registered_office_address
        return self

    def office_address(self, office_address: List[I18n]) -> "CompanyBuilder":
        self._company.office_address = office_address
        return self

    def build(self) -> "Company":
        return self._company
