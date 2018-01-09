#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def is_palindrome(n):
	str_n = str(n)
	return str_n == str_n[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))

# 测试代码
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
	print('测试成功')
else:
	print('测试失败')
	
# 排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]
def by_score(t):
	return t[1]

L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score)
print(L2)
print(L3)

	