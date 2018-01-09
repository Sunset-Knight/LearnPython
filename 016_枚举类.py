#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)
print(Month)

@unique
class Weekday(Enum):
	"""docstring for Weekday."""
	Sun = 0	
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6
	
day1 = Weekday.Mon
print(day1)
print(Weekday.Mon)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(Weekday.Mon == day1)
print(day1 == Weekday.Thu)
print(Weekday(1))
print(day1 == Weekday(1))

for name, member in Weekday.__members__.items():
	print(name, '=>', member, member.value)
	
# 练习
class Gender(Enum):
	Male = 0
	Female = 1
	
class Student(object):
	"""docstring for Student."""
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender
		

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
	print('测试通过')
else:
	print('测试失败')
		