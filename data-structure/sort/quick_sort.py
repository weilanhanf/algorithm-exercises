# -*- coding: utf-8 -*-
__date__ = '2020/1/8 20:39'

from random import randint


def quick_pos(seq, low, high):
    # 返回基准元素位置

    temp = seq[low]
    while low < high:
        while low < high and seq[high] >= temp:
            high -= 1
        if low < high:
            seq[low] = seq[high]
            low += 1
        while low < high and seq[low] < temp:
            low += 1
        if low < high:
            seq[high] = seq[low]
            high -= 1
    seq[low] = temp
    return low


def quick_sort(seq, low, high):
    # 快速排序

    if low < high:
        pos = quick_pos(seq, low, high)
        quick_sort(seq, low, pos-1)
        quick_sort(seq, pos+1, high)


if __name__ == '__main__':
    li = [randint(0, 99) for _ in range(10)]
    print('原序列', li)
    quick_sort(li, 0, len(li)-1)
    print('排序后', li)
