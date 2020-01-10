# -*- coding: utf-8 -*-
__date__ = '2020/1/3 13:38'

#
# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
#


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        x, y = 0, 1
        for i in range(2, n+1):
            z = x + y  # z = fib(i-1)+fib(i-2)
            x = y  # x = fib(i-1)
            y = z  # y = z = fib(i-1)+fib(i-2)
        return y


# print(fib(7))
