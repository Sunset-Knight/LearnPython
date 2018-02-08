#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from contextlib import contextmanager
from urllib.request import urlopen

# 在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源的一个方法是使用try...finally：
try:
	f = open('/home/walter/spf13-vim.sh', 'r')
	f.read()
finally:
	if f:
		f.close()
		
# 写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，所以上面的代码可以简化为：
with open('/home/walter/spf13-vim.sh', 'r') as f:
	f.read()
	
class Query(object):
	def __init__(self, name):
		self.name = name
	def __enter__(self):
		print('Begin')
		return self
	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_type:
			print('Error')
		else:
			print('End')
	def query(self):
		print('Query info about %s...' % self.name)
with Query('Bob') as q:
	q.query()
	
class Query2(object):
	def __init__(self, name):
		self.name = name
	def query(self):
		print('Query2 info about %s...' % self.name)
		
@contextmanager
def create_query(name):
	print('Begin')
	q = Query2(name)
	yield q
	print('End')
	
with create_query('Bob') as q:
	q.query()
	
@contextmanager
def tag(name):
	print('<%s>' % name)
	yield
	print('</%s>' % name)
with tag('h1'):
	print('hello')
	print('world')
	


@contextmanager
def closing(thing):
	try:
		yield thing
	finally:
		thing.close()
		
with closing(urlopen('https://www.python.org')) as page:
	for line in page:
		print(line)
