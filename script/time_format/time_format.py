#!/usr/bin/env python3

import time
import datetime
import pytz


class TimeFormat:
    def __init__(self, unix_timestamp=int(time.time()), offset=None, timezone="+8"):
        self.unix_timestamp = unix_timestamp
        self.offset = self.setOffset(offset=offset, timezone=timezone)

    @staticmethod
    def setOffset(offset=None, timezone=None):
        if offset:
            offset = offset
        else:
            offset = int(timezone) * 60
        return offset

    def generate_offset_utc_time(self):
        # 转换为 UTC 时间
        utc_time = datetime.datetime.utcfromtimestamp(self.unix_timestamp)
        # 创建带偏移量的时区对象
        timezone = pytz.FixedOffset(self.offset)
        # 将 UTC 时间转换为带偏移量的时间
        offset_time = utc_time.replace(tzinfo=pytz.UTC).astimezone(timezone)
        # 格式化为 ISO 8601 标准时间字符串
        iso_format = offset_time.isoformat()
        return iso_format


if __name__ == "__main__":
    utc_time = TimeFormat()
    utc_time_with_offset = utc_time.generate_offset_utc_time()
    print(utc_time_with_offset)
