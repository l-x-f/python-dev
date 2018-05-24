#! /usr/bin/env python
# coding:utf-8
# int()方法用于将一个字符串或数字转换为整型。如果不串参数的话默认显示0
# input()方法用于让用户输入文本，第一个参数是提示内容
# print ()方法用于输出内容
length = float(input('请输入身高（m）:'))
weight = float(input('请输入体重（kg）:'))
result=weight/(length**2)
if result<=18.5:
    print ("你的体重过轻")
elif result<=25:
    print ("你的体重正常")
elif result <=28:
    print ("你的体重过重")
elif result <=32:
    print ("肥胖")
else:
    print("严重肥胖")
print ('体重指数',result)