# -*- coding: utf-8 -*-
__date__ = '2020/2/5 20:44'


def reorder(array=None, length=0):
    """
    将数组中的奇数放到偶数前
    """
    if array is None or length <= 0:
        return None

    left, right = 0, length-1
    while left < right:  # left用来寻找偶数，right用来寻找奇数
        while array[left]%2 == 1 and left < right:
            left += 1
        while array[right]%2 == 0 and left < right:
            right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]

    return array


if __name__ == '__main__':
    from random import randint

    array = [randint(1, 100) for _ in range(10)]
    print("before reorder: ", array)


    print("after reorder: ", reorder(array, len(array)))



