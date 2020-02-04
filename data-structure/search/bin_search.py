# -*- coding: utf-8 -*-
__date__ = '2020/2/4 16:12'



def bin_search(lis, item):
    """ 折半查找（二分），非递归 """
    left, right = 0, len(lis)-1
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] == item:
            return True
        elif lis[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return False  # 如果最终没有找到，则返回False


def bin_search_recur(lis, item):
    """ 递归 """
    if len(lis) < 1:
        return False
    mid = len(lis)//2
    if lis[mid] == item:
        return True
    elif lis[mid] > item:
        return bin_search_recur(lis[:mid], item)
    elif lis[mid] < item:
        return bin_search_recur(lis[mid+1:], item)


if __name__ == "__main__":
    lis = [1, 19, 23, 43, 55, 65, 89, 90]
    print(bin_search(lis, 8))
    print(bin_search_recur(lis, 89))