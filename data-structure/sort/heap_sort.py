# -*- coding: utf-8 -*-
__date__ = '2020/2/4 13:57'


from random import randint


def shift(lis, k, m):
    """ 调整堆 """
    x = lis[k]
    i = k
    j = 2*i
    finished = False
    while(j<=m and finished==False):
        if j+1 <= m and lis[j+1] > lis[j]:
            j += 1
        if x >= lis[j]:
            finished = True
        else:
            lis[i] = lis[j]
            i = j
            j = i*2
    lis[i] = x


def creat_heap(lis, length):
    """ 建新堆 """
    end = length  # end表示最后列表最后一个元素的下标
    for i in range((end)//2, 0, -1):
        shift(lis, i, end)  #


def heap_sort(lis, length):
    """ 堆排序 """
    creat_heap(lis, length)
    end = length
    for i in range(end, 1, -1):
        lis[i], lis[1] = lis[1], lis[i]
        shift(lis, 1, i-1)



if __name__ == "__main__":
    lis = [randint(1, 100) for _ in range(10)]
    lis.insert(0, None)  # 顺序表下标为0位置不放置元素
    print("排序前：", lis[1:])

    heap_sort(lis, 10)
    print("排序后：", lis[1:])