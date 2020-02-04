# -*- coding: utf-8 -*-
__date__ = '2020/2/4 11:52'


class SingleNode:
    """单链表节点"""

    def __init__(self, item):
        self.item = item  # 结点存放数据
        self.next = None  # 后继结点


class SingleLinkList:
    """ 单链表 """

    def __init__(self):
        self.head = None

    def is_empty(self):  # 链表是否为空
        return self.head == None

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

    def search(self, item):
        """ 查找是否存在数据域为item的结点 """
        cur = self.head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            node = SingleNode(item)
            count = 1
            pre = self.head
            while count < pos-1:
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """ 删除值域为item的结点 """
        if self.head.item == item:
            self.head = self.head.next
        else:
            pre = self.head
            cur = pre.next
            while cur != None:
                if cur.item == item:  # 找到则删除
                    pre.next = cur.next
                    cur = pre.next
                else:  # 指针后移
                    pre = cur
                    cur = pre.next


if __name__ == "__main__":
    link_list = SingleLinkList()

    link_list.append(7)
    link_list.append(8)
    link_list.append(8)
    link_list.append(8)
    link_list.append(10)
    link_list.add(6)
    link_list.add(5)
    link_list.add(4)
    link_list.travel()

    link_list.remove(8)
    link_list.travel()

    link_list.insert(5, 8)
    link_list.travel()
