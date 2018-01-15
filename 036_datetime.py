#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 常用内建模块
# datetime
import re
from datetime import datetime, timedelta, timezone

# 获取当前时间和日期
now = datetime.now()
print(now)
print(type(now))

# 指定某个日期和时间，
dt = datetime(2016, 4, 5, 12, 23)
print(dt)

# datetime 转换为timestamp
print(dt.timestamp())
print(now.timestamp())
# timestamp 转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))
# timestamp直接转换为UTC标准时区的时间
print(datetime.utcfromtimestamp(t))
print(datetime.utcnow())

# str 转换为datetime
cday = datetime.strptime('2016-9-1 12:33:22', '%Y-%m-%d %H:%M:%S')
print(cday)
print(datetime.timestamp(cday))

# datetime 转换为str

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
print('now = ', now)
print('now + 10hours', now + timedelta(hours=10))
print('now + 1day', now + timedelta(days=1))

# 本地时间转换为UTC时间
tz_utf_8 = timezone(timedelta(hours=8)) # 创建时区UTF+8：00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utf_8) # 强制设置为UTF+8:00
print(dt)

# 时区转换
# 拿到UTC时间，并强制设置时区为UTC+0：00
utf_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utf_dt)
# astimezone()将转换时区为北京时间
bj_dt = utf_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间
tokyo_dt = utf_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换为东京时间
tokyo_dt_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt_dt2)


# 练习
# print(re_tz = re.match(r'UTC([+\-]\d+):00', r‘UTC-09:00’).group(1)
def to_timestamp(dt_str, tz_str):
	c_dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
	re_tz = re.match(r'UTC([\+\-]\d+):00', tz_str).group(1)
	c_tz = timezone(timedelta(hours=int(re_tz)))
	dt = c_dt.replace(tzinfo=c_tz)
	print(dt.timestamp())
	return dt.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')