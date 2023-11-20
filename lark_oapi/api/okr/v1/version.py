from .resource import *


class V1(object):
    def __init__(self, config: Config) -> None:
        self.image: Image = Image(config)
        self.okr: Okr = Okr(config)
        self.period: Period = Period(config)
        self.progress_record: ProgressRecord = ProgressRecord(config)
        self.user_okr: UserOkr = UserOkr(config)
