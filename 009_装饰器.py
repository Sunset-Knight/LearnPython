#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import functools, time
# decorator
def log(func):
	def wrapper(*args, **kw):
		print('Call %s()' % func.__name__)
		return func(*args, **kw)
	return wrapper

def now():
	print('2018')
	
now = log(now)
now()
print(now.__name__)



# true decorator
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('Call %s()' % func.__name__)
		return func(*args, **kw)
	return wrapper

def now():
	print('2018')
	
now = log(now)
now()
print(now.__name__)

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s()' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

def now():
	print('2-000')
	
now = log('llllll')(now)
now()


# exercise
# def metric(fn):
#     print('%s executed in %s ms' % (fn.__name__, 10.24))
#     return fn


def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args, **kw):
		start = time.time()
		result = fn(*args, **kw)
		print('%s executed in %s ms' % (fn.__name__, (time.time()-start)*1000))
		return result
	return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
	
# time
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('start')
		result = func(*args, **kw)
		print('end')
		return result
	return wrapper

@log
def fn():
	print('我在这')
	
fn()
print(fn.__name__)