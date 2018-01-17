#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import base64

# 一个能处理去掉 = 的base64解码函数
def safe_base64_decode(s):
	n = len(s) % 4
	if n:
		s = s + b'=' * (4-n)
	return base64.b64decode(s)
	
print(safe_base64_decode(b'YWJjZA'))

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')