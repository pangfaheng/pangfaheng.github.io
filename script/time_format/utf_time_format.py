#!/usr/bin/env python3

import time
import datetime
import pytz


class UTCTimeFormat:
    def __init__(
        self,
        timestamp=int(time.time()),
        offset=None,
        timezone="+8",
        offset_timezone_unit="hour",
    ):
        self.timestamp = timestamp
        self.offset = self.set_timezone_offset(
            offset=offset, timezone=timezone, offset_timezone_unit=offset_timezone_unit
        )

    def set_timezone_offset(
        self, offset=None, timezone=None, offset_timezone_unit=None
    ):
        if offset:
            offset = offset
        elif timezone is not None and offset_timezone_unit == "hour":
            offset = int(timezone) * 60
        elif timezone is not None and offset_timezone_unit == "min":
            offset = int(timezone)
        else:
            offset = self.get_server_timezone_offset()
        return offset

    def get_server_timezone_offset(self):
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

    def generate_offset_utctime(self):
        # 转换为 UTC 时间
        utc_time = datetime.datetime.utcfromtimestamp(self.timestamp)
        # 创建带偏移量的时区对象
        timezone = pytz.FixedOffset(self.offset)
        # 将 UTC 时间转换为带偏移量的时间
        offset_time = utc_time.replace(tzinfo=pytz.UTC).astimezone(timezone)
        # 格式化为 ISO 8601 标准时间字符串
        iso_format = offset_time.isoformat()
        return iso_format

    def get_timpstamp(self):
        return self.timestamp

    def remake_iso8601_to_timestamp(self, iso_8601_time=None):
        # 解析 ISO 8601 标准时间字符串
        if not iso_8601_time:
            dt = datetime.datetime.fromisoformat(self.generate_offset_utctime())
        else:
            dt = datetime.datetime.fromisoformat(iso_8601_time)
        # 转换为时间戳（单位：秒）
        timestamp = dt.timestamp()
        return int(timestamp)


if __name__ == "__main__":
    utc_time = UTCTimeFormat()
    utc_time_with_offset = utc_time.generate_offset_utctime()
    utc_time_with_timestamp = utc_time.remake_iso8601_to_timestamp()
    print(utc_time_with_offset, utc_time_with_timestamp)
