# -*- coding: utf-8 -*-
__date__ = '2020/2/9 22:30'


def min_number_reverse_array(array=None):
    if array is None or len(array) == 0:
        return -1  # 不符条件
    low, high = 0, len(array)-1
    mid = 0  # 当数组已经有序时，第一个元素就是最小
    while array[low] >= array[high]:  # 既然满足旋转数组，后边的数组的数肯定小于第一个数
        if high - low == 1:
            mid = high
            break  # 找到最小数的下标返回

        mid = (low + high)//2

        if array[mid] == array[high] == array[low]:  # 如果出现特殊情况如[1, 1, 1, 0,1]
            return find_min(array)

        if array[mid] >= array[low]:
            low = mid
        else:
            high = mid

    return array[mid]

def find_min(array=None):
    res, k = array[0], 0
    for i in range(1, len(array)):
        if array[i] < res:
            k = i
    if k != 0:
        res = array[k]
    return res


if __name__ == '__main__':
    array1 = [3, 4, 5, 1, 2]
    array2 = [1, 1, 1, 0, 1]
    array3 = [1, 0, 1, 1, 1]
    print(min_number_reverse_array(array2))