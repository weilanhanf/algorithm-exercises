# -*- coding: utf-8 -*-
__date__ = '2020/2/4 20:53'  # 未完


class SingleNode:
    """单链表节点"""

    def __init__(self, item):
        self.item = item  # 结点存放数据
        self.next = None  # 后继结点

    def __repr__(self):
        return str(self.item)


class SingleLinkList:
    """ 单链表 """

    def __init__(self):
        self.head = None

    def is_empty(self):  # 链表是否为空
        return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur:  # 只要指针不空
            count += 1
            cur = cur.next  # 指针后移
        return count

    def travel(self):
        """ 遍历链表 """
        cur = self.head
        while cur:
            print(cur.item, end='->')
            cur = cur.next
        print(None)  # 链表最后指针指向None

    def add(self, item):
        """ 头插法 """
        node = SingleNode(item)  # 新建一个结点
        node.next = self.head
        self.head = node

    def append(self, item):
        """ 尾插法 """
        node = SingleNode(item)  # 新建一个结点
        if self.is_empty():  # 链表为空
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node



def reverse_linklist(linklist=None):
    pre = linklist.head

    head = None
    while pre:
        cur = pre.next
        pre.next = head
        head = pre
        pre = cur

    linklist.head = head

if __name__ == "__main__":
    linklist = SingleLinkList()

    linklist.append(1)
    linklist.append(2)
    linklist.append(3)
    linklist.append(4)
    linklist.travel()

    reverse_linklist(linklist)
    linklist.travel()