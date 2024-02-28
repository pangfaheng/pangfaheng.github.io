#!/usr/bin/env python3

import time
import datetime
import pytz


class TimeFormat:
    def __init__(self, unix_timestamp=int(time.time()), offset=None, timezone="+8"):
        self.unix_timestamp = unix_timestamp
        self.offset = self.setTimezoneOffset(offset=offset, timezone=timezone)

    def setTimezoneOffset(self, offset=None, timezone=None):
        if offset:
            offset = offset
        elif timezone is not None:
            offset = int(timezone) * 60
        else:
            offset = self.getServerTimezoneOffset()
        return offset

    def getServerTimezoneOffset(self):
        # 获取当前服务器时间
        server_time = datetime.datetime.now(pytz.UTC)
        # 获取服务器时区
        local_timezone = datetime.datetime.now().astimezone().tzinfo
        # 计算时区偏移量
        offset = local_timezone.utcoffset(server_time)
        # 转换为分钟
        offset_minutes = offset.total_seconds() / 60
        # 返回偏移量
        return offset_minutes

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
