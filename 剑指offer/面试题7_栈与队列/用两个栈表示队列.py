# -*- coding: utf-8 -*-
__date__ = '2020/1/3 13:11'


class Queue:
    ''' 用两个栈表示队列 '''
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_full(self):
        if self.stack2 == [] and self.stack1 == []:  # 出队时只有stack2为空，才会去查看stack1
            return True
        else:
            return False

    def is_empty(self):
        """ 一般情况下对列表元素个数不做限制 """
        return False

    def enter_queue(self, item):
        self.stack1.append(item)

    def delete_queue(self):
        if self.is_full():
            return None
        else:
            if self.stack2 == []:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


class Stack:
    ''' 用两个队列表示栈 '''
    def __init__(self):
        self.queue1 = []
        self.queue2 = []



if __name__ == '__main__':
    queue = Queue()
    queue.enter_queue(1)
    print(queue.is_empty())
    print(queue.delete_queue())
