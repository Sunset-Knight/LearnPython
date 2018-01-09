#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# __getattr__

class Student(object):
	"""docstring for Student."""
	def __init__(self):
		super(Student, self).__init__()
		self.name = 'Michael'		
		
	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		if attr == 'age':
			return lambda: 25
		# 抛出AttributeError
		# raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
	
		
s = Student()
print(s.name)
print(s.score)
print(s.age(), s.age)
# print(s.cc)

# 链式调用
class Chain(object):
	"""docstring for Chain."""
	def __init__(self, path=''):
		self._path = path
		
	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))
	
	def __str__(self):
		return self._path
	
	__repr__ = __str__
	
print(Chain().status.user.timeline.list)

# __call__

class Student(object):
	def __init__(self, name):
		self.name = name
		
	def __call__(self):
		print('My name is %s' % self.name)
		
s = Student('Michael')
s()
print(callable(max))
print(callable([1, 2, 3]))
print(callable('str'))
