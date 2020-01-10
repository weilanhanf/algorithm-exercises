# -*- coding: utf-8 -*-
__date__ = '2020/1/8 19:58'


'''
双向冒泡排序：与冒泡排序的区别在于一次从筛选一个最大，一次筛选一个最小。
'''


from random import randint


def double_bubble_sort(seq):
    # 双向冒泡排序

    n = len(seq)
    left, right = 0, n-1
    while left < right:

        l = left + 1
        r = right - 1

        for i in range(left, right):  # 从左3到右筛选一个最大的元素
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                r = i  # r用来记录下次排序序列的最后一个元素的下标
        right = r

        for j in range(right, left, -1):  # 从右到左筛选一个最小的元素
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]
                l = j
        left = l


if __name__ == '__main__':
    li = [randint(0, 99) for _ in range(10)]
    print('原序列', li)
    double_bubble_sort(li)
    print('排序后', li)


