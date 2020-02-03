# -*- coding: utf-8 -*-
__date__ = '2020/2/3 23:01'


class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()
    for i in range(9):
        queue.enqueue(i)
    print(queue.items)

    queue.dequeue()
    queue.dequeue()
    print(queue.items)