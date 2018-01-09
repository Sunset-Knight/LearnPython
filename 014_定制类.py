#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# __str__

class Student(object):
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__
	
print(Student('Michael'))
s = Student('Michael')


# __iter__
# 斐波那契数列
class Fib(object):
	
	def __init__(self):
		self.a, self.b = 0, 1
		
	def __iter__(self):
		return self
	
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100000:
			raise StopIteration()
		return self.a

for n1 in Fib():
	print(n1)

# __getitem__ 获取第n个元素
class Fib2(object):
	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a

f = Fib2()
print(f[9])

# 切片
class Fib3(object):
	
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice): # n 是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L
		
f = Fib3()
print(f[9])
print(f[10])
print(f[9:12])