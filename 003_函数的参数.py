#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def power(x, n = 2):
	s = 1
	while n > 0	:
		n = n - 1
		s = s * x
	return s

print(power(3,3))
print(power(3))

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

print(calc(1,2,3))
nums = [1, 2, 3, 4]
print(calc(*nums))

# 利用递归函数移动汉诺塔
def move(n ,a , b ,c):
	if n == 1:
		print('move', a, '-->', c)
	else:
		move(n -1, a, c, b)
		move(1, a, b ,c)
		move(n -1, b, a, c)
		
move(3, 'A', 'B', 'C')