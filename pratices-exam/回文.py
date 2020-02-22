# -*- coding: utf-8 -*-
__date__ = '2020/2/22 18:36'

s = input()
sign = 1
i, j = 0, len(s)-1
while i<j:
    if(s[i]!=s[j]):
        sign = 0
        break
    else:
        i += 1
        j -= 1

if sign:
    print("yes")
else:
    print("no")