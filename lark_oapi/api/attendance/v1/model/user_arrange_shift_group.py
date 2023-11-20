# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .arrange_shift_group import ArrangeShiftGroup


class UserArrangeShiftGroup(object):
    _types = {
        "user_id": str,
        "shift_group": ArrangeShiftGroup,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.shift_group: Optional[ArrangeShiftGroup] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserArrangeShiftGroupBuilder":
        return UserArrangeShiftGroupBuilder()


class UserArrangeShiftGroupBuilder(object):
    def __init__(self) -> None:
        self._user_arrange_shift_group = UserArrangeShiftGroup()

    def user_id(self, user_id: str) -> "UserArrangeShiftGroupBuilder":
        self._user_arrange_shift_group.user_id = user_id
        return self

    def shift_group(self, shift_group: ArrangeShiftGroup) -> "UserArrangeShiftGroupBuilder":
        self._user_arrange_shift_group.shift_group = shift_group
        return self

    def build(self) -> "UserArrangeShiftGroup":
        return self._user_arrange_shift_group
