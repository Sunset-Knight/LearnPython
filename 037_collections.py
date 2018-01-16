#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# OrderedDict 实现FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的key

from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
	
	def __init__(self, capacity):
		super(LastUpdatedOrderedDict, self).__init__()
		self._capacity = capacity
	
	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			print('remove:', last)
		if containsKey:
			del self[key]
			print('set:', (key, value))
		else:
			print('add:', (key, value))
		OrderedDict.__setitem__(self, key, value)
	
luod = LastUpdatedOrderedDict(3)
luod['x'] = 1
luod['z'] = 2
luod['y'] = 3
luod['w'] = 33
luod['c'] = 34

# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print(c)