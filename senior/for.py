#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
print (os,'----------------------------------')
li = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for index,item in enumerate(li):
    print (index,item)

# 遍历字典
dic={'a':'你好','b':'世界'}
for k, v in dic.items():
    print (k,v)

# os.listdir可以列出文件和目录
dir=[d for d in os.listdir('.')]
for v in dir:
    print(v)
