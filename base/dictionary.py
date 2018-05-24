#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# dic 字典类型
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s={1,2,3,1}
s2=set([0,1,23,3])
print(s2)

# tuple
s3=set((0,1,23,3))
print(s3)

# s4=set((1, [2, 3]))
# print(s4)
# 报错 #unhashable type: 'list' # 不可拆卸的

