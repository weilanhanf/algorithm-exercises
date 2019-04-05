# -*- coding:utf-8 -*-

"""
变态跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""


class Solution:
    def jumpFloorII(self, number):
        # write code here
        a = 1
        if number==1:
            return 1
        while number>1:
            a = a*2
            number = number-1
        return a