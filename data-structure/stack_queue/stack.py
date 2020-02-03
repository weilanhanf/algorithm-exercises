# -*- coding: utf-8 -*-
__date__ = '2020/2/3 22:54'


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):  # 进栈
        self.items.append(item)

    def pop(self):  # 出栈
        if self.is_empty():
            return None
        return self.items.pop(-1)

    def top(self):  # 返回栈顶元素
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()

    for i in range(9):
        stack.push(i)
    print(stack.items)

    stack.pop()
    stack.pop()
    print(stack.items)

