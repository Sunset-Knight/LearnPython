#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def createCounter():
	def number():
		num = 0
		while True:
			num = num + 1
			yield(num)
	n = number()
	def counter():
		return next(n)
		
	return counter
ACounter = createCounter()
print(ACounter(), ACounter())
print(ACounter(), ACounter())

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')