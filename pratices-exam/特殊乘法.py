# -*- coding: utf-8 -*-
__date__ = '2020/2/21 20:57'

import sys

#  http://codeup.cn/problem.php?cid=100000575&pid=2

while True:
    try:
        a, b = input().split()
        print(sum([int(i) * int(j) for i in a for j in b]))
    except:
        break
    pass
# li = []
# list_new = [] #定义一个空列表
# for line in sys.stdin:
#     #py.3中input（）只能输入一行  sys.stdin按下换行键然后ctrl+d程序结束
#     list_new = line.split()
#     print(list_new)
    # list.extend(list_new) #每一行组成的列表合并

# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break
#     pass