#!/usr/bin/env python3
# -*- coding: utf-8 -*-
list=['aaa','bbb','ccc']
print(len(list))
print(list)
print(list[0])
# 倒数第一个
print(list[-1])
# 报错，索引溢出
# print(list[-4])
# 要删除list末尾的元素，用pop()方法：
print (list.pop(0))
# tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
t=(0,1,23,4,56)
print (t[0])
print (t[-1])
# 只有一个的时候必须加上‘，’ 不加的话默认转成不要括号的变量类型
singleTuple=(1,)
print (singleTuple)
de=(1)
print (de)