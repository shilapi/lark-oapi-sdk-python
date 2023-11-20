# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class TwMainlandTravelPermitEntity(object):
    _types = {
        "type": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TwMainlandTravelPermitEntityBuilder":
        return TwMainlandTravelPermitEntityBuilder()


class TwMainlandTravelPermitEntityBuilder(object):
    def __init__(self) -> None:
        self._tw_mainland_travel_permit_entity = TwMainlandTravelPermitEntity()

    def type(self, type: str) -> "TwMainlandTravelPermitEntityBuilder":
        self._tw_mainland_travel_permit_entity.type = type
        return self

    def value(self, value: str) -> "TwMainlandTravelPermitEntityBuilder":
        self._tw_mainland_travel_permit_entity.value = value
        return self

    def build(self) -> "TwMainlandTravelPermitEntity":
        return self._tw_mainland_travel_permit_entity
