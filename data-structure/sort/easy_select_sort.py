# -*- coding: utf-8 -*-
__date__ = '2020/1/9 9:11'


'''简单选择排序'''


from random import randint


def easy_select_sort(seq):
    # 简单选择排序排序
    n = len(seq)
    for i in range(n-1):
        min_ = i  # 共n-1趟排序，用min_记录最小元素的指针
        for j in range(i+1, n):
            if seq[j] < seq[min_]:
                min_ = j
        if min_ != i:  # 找到最小元素，交换位置
            seq[i], seq[min_] = seq[min_], seq[i]


if __name__ == '__main__':
    li = [randint(0, 99) for _ in range(10)]
    print('原序列', li)
    easy_select_sort(li)
    print('排序后', li)
