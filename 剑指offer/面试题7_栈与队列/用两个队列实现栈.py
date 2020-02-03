# -*- coding: utf-8 -*-
__date__ = '2020/2/3 22:17'

class Stack:
    '''
    用两个队列表示栈
    用队列的先进先出实现栈的先进后出
    '''
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, item):
        self.queue1.append(item)

    def pop(self):
        if self.queue1 == []:
            return None
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))

        self.queue1, self.queue2 = self.queue2, self.queue1

        return self.queue2.pop(0)

    def show(self):
        print(self.queue1)


if __name__ == "__main__":
    stack = Stack()
    for i in range(10):
        stack.push(i)
    stack.show()
    stack.pop()
    stack.show()