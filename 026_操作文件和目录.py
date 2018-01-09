#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

# ĺŽç°dir -l

if 'x' in 'xbc':
	print('....')
	
# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。


def showfiles(dirpath):
	for x in os.listdir(dirpath):
		if os.path.isfile(x):
			return x
		
print(showfiles('.'))






