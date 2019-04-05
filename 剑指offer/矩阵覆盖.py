# -*- coding:utf-8 -*-

"""
矩形覆盖:
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""

class Solution:
    def rectCover(self, number):
        # write code here
        if number <=2:
            return number
        a = 1
        b = 2
        c = 0
        for i in range(number-2):
            c = a+b
            a = b
            b = c
        return c