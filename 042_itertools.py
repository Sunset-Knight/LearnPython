#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import itertools

naturals = itertools.count()
for n in naturals:
	print(n)
	if n == 20:
		break
		
cs = itertools.cycle('ABC')
n = 0
for c in cs:
	print(c)
	n = n + 1
	if n == 20:
		break
		
ns = itertools.repeat('A', 4)
for n in ns:
	print(n)
	
naturals = itertools.count()
ns = itertools.takewhile(lambda x: x <= 10, naturals)
print(list(ns))

for c in itertools.chain('ABC', '123'):
	print(c)

for key, group in itertools.groupby('AAABBBCCAAA'):
	print(key, list(group))
	
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
	print(key, list(group))
	
# 练习
def pi(N):
	' 计算pi的值 '
	# step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
	odd = itertools.count(1,2)
	# step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
	odd_n  = itertools.takewhile(lambda x:x<=2*N-1, odd)
	# step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
	numerator = itertools.cycle([4, -4])
	result = [next(numerator)/i for i in odd_n]
	# step 4: 求和:
	return sum(result)
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')