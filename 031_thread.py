#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time, threading

# 新线程执行的代码
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>> %s' % (threading.current_thread().name, n))
	print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')	
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# Lock
# 无Lock
balance = 0
def change_it(n):
	# 先存取，结果应为0
	global balance
	balance = balance + n
	balance = balance - n
	
def run_thread(n):
	for i in range(100000):
		change_it(n)
		
t1 = threading.Thread(target=run_thread, args=(45,))
t2 = threading.Thread(target=run_thread, args=(100,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


# 有锁
balance = 0
lock = threading.Lock()

def run_thread(n):
	for i in range(1000000):
		# 先要获取锁：
		lock.acquire()
		try:
			# 放心地改吧
			change_it(n)
		finally:
			# 改完了一定要释放锁
			lock.release()
			
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)