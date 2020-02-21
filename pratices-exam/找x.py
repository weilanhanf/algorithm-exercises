# -*- coding: utf-8 -*-
__date__ = '2020/2/21 21:07'

# code up 1934

while True:
    try:
        n = int(input())
        res = input().split()
        res = [int(i) for i in res]
        elem = int(input())
        try:
            key = res.index(elem)
            print(key)
        except:
            print(-1)
    except:
        break
