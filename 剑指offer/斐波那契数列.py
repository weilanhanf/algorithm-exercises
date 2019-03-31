# -*- coding:utf-8 -*-

class Solution:
    def Fibonacci(self, n):
        # write code here
        x, y = 0 , 1
        if n <= 0:
            return 0
        elif n < 2:
            return 1
        for _ in range(n - 1):
            x, y = y, x + y
        return y