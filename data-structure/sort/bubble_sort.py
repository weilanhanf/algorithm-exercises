# -*- coding: utf-8 -*-
__date__ = '2020/1/8 19:44'


'''冒泡排序'''


from random import randint


def bubble_sort(seq):
    # 冒泡排序

    n = len(seq)
    for i in range(n, 0, -1):
        flag = 0
        for j in range(0, i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
                flag = 1
        if flag == 0:  # 如果序列已经有序排列则直接退出循环
            break


if __name__ == '__main__':
    li = [randint(0, 99) for _ in range(10)]
    print('原序列', li)
    bubble_sort(li)
    print('排序后', li)
