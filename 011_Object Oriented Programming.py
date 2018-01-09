#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Object Oriented Programming

class Student(object):
	
	def __init__(self, name, score, gender):
		self.__name = name
		self.__score = score
		self.__gender = gender
		
	def print_score(self):
		print('%s %s' % (self.__name, self.__score))
	
	def get_name(self):
		return self.__name
	
	def get_gender(self):
		return self.__gender
	
	def get_score(self):
		return self.__score
	
	def set_name(self, name):
		self.__name = name
		
	def set_gender(self, gender):
		self.__gender = gender
	
	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')


bart = Student('Bart simpson', 90, 'male')
bart.print_score()
print(bart._Student__name)
print(bart._Student__score)
bart.set_name('lll')
bart.set_score(100)
print(bart.get_name(), bart.get_score())

if bart.get_gender() != 'male':
	print('测试失败')
else:
	bart.set_gender('female')
	if bart.get_gender() != 'female':
		print('测试失败！')
	else:
		print('测试成功！')
