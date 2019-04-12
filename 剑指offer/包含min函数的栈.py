"""
包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""


# -*- coding:utf-8 -*-
class Solution:
    l = []

    def push(self, node):
        # write code here
        self.l.append(node)

    def pop(self):
        # write code here
        d = self.l[-1]
        self.l = self.l[:-1]
        return d

    def top(self):
        # write code here
        return self.l[-1]

    def min(self):
        # write code here
        return min(self.l)