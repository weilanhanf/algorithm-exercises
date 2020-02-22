# -*- coding: utf-8 -*-
__date__ = '2020/2/21 23:18'

ins = input().split()
col, s = int(ins[10]), ins[1]
row = col/2+1 if col%2==1 else col/2
for i in range(int(row)):
    print()
# if col%2==1:
#     row = col/2+1
# else:
#     row = col/2
