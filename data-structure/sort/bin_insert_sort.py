# -*- coding: utf-8 -*-
__date__ = '2020/2/6 13:33'


'''折半插入排序：二分思想'''


from random import randint


def bin_insert_sort(seq):
    # 插入排序

    n = len(seq)
    for i in range(1, n):
        low, high = 0, i-1
        x = seq[i]
        while low <= high:
            mid = (low + high) // 2
            if x < seq[mid]:
                high = mid -1
            else:
                low = mid + 1
        for j in range(i-1, low-1, -1):
            seq[j+1] = seq[j]
        seq[low] = x
    return seq

if __name__ == '__main__':
    li = [randint(0, 99) for _ in range(10)]
    print('原序列', li)
    bin_insert_sort(li)
    print('排序后', li)
