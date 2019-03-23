"""
question des
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""

# -*- coding:utf-8 -*-

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next
        l = l[::-1]
        return l
