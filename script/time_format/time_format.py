#!/usr/bin/env python3

import time
from datetime import datetime, timedelta, timezone


class TimeFormat:
    def __init__(self, unix_timestamp=int(time.time()), time_zone="8"):
        self.unix_timestamp = unix_timestamp
        self.time_zone = time_zone

    # 时间戳（秒）
    def setTimeAsSecondUnixTimestamp(self) -> None:
        print(self.unix_timestamp)

    # 秒（带分隔符）
    def setTimeAsSecondAndT(self) -> None:
        print(time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(self.unix_timestamp)))

    # 秒（带分隔符、时区）
    def setTimeAsSecondAndTZ(self) -> None:
        print(
            time.strftime("%Y-%m-%dT%H:%M:%S %Z", time.localtime(self.unix_timestamp))
        )

    # 日期
    def setTimeAsDay(self) -> None:
        print(time.strftime("%Y-%m-%d", time.localtime(self.unix_timestamp)))
