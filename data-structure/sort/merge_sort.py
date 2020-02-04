# -*- coding: utf-8 -*-
__date__ = '2020/2/4 12:14'

from random import randint


def merge_sort(lis):
    """ 归并排序 """
    if len(lis) <= 1:
        return lis
    ins = len(lis)//2
    alist = merge_sort(lis[:ins])
    blist= merge_sort(lis[ins:])
    return merge(alist, blist)

def merge(alist, blist):
    l, r = 0, 0
    res = []
    while l < len(alist) and r < len(blist):
        if alist[l] < blist[r]:
            res.append(alist[l])
            l += 1
        else:
            res.append(blist[r])
            r += 1

    res += alist[l:]
    res += blist[r:]
    return res


if  __name__ == "__main__":
    lis = [randint(1, 100) for _ in range(10)]
    print("排序前：", lis)
    print("排序后：", merge_sort(lis))
