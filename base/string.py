#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 判断语句  len可以获取子字符串和列表的长度
c='000000000'
if len(c)==9:
    print("是9")
else:
    print("不是9")
# 字符串操作 str（）方法可以把数字装换成字符串  .upper（）方法可以把字符串变成大写  .lower()相反
aaa=100
bbb="ggg"
print(str(aaa)+"\n"+bbb+"000")
print(aaa is 100)
ccc=aaa
bbb.upper()
print(ccc)
print(r'''line1
line2
line3''')