# -*- coding: utf-8 -*-
__date__ = '2020/1/8 20:25'


'''直接插入排序'''


from random import randint


def insert_sort(seq):
    # 直接插入排序

    n = len(seq)
    for i in range(1, n):
        temp = seq[i]
        j = i - 1
        while j >= 0 and temp < seq[j]:
            seq[j+1] = seq[j]
            j -= 1
        seq[j+1] = temp


if __name__ == '__main__':
    li = [randint(0, 99) for _ in range(10)]
    print('原序列', li)
    insert_sort(li)
    print('排序后', li)
