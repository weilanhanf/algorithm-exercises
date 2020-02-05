# -*- coding: utf-8 -*-
__date__ = '2020/2/5 18:21'



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


def merge_linklist(a_linklist=None, b_linklist=None):
    if a_linklist is None and b_linklist is None:
        return None
    else:
        a_head, b_head = a_linklist.head, b_linklist.head
        res = SingleNode(0)  # 用来模拟不存放数据的头节点
        head = res
        while a_head and b_head:
            if a_head.item <= b_head.item:
                head.next = a_head
                head = head.next
                a_head = a_head.next
            else:
                head.next = b_head
                head = head.next
                b_head = b_head.next
        if a_head:
            head.next = a_head
        if b_head:
            head.next = b_head

    new_linklist = SingleLinkList()
    new_linklist.head = res.next

    return new_linklist  # 返回一个新的合并后的链表


if __name__ == "__main__":
    a_linklist = SingleLinkList()
    b_linklist = SingleLinkList()

    print("a_linklist: ", end="")
    a_linklist.append(1)
    a_linklist.append(3)
    a_linklist.append(7)
    a_linklist.append(10)
    a_linklist.travel()

    print("b_linklist: ", end="")
    b_linklist.append(1)
    b_linklist.append(4)
    b_linklist.append(8)
    b_linklist.append(20)
    b_linklist.travel()

    merged_linklist = merge_linklist(a_linklist, b_linklist)
    print("merged_linklist: ", end="")
    merged_linklist.travel()