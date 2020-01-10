"""
question des
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


def find_elem(target, array):
    """元素规律排列的二维数组查找数据元素，如果成功返回元素在二维数组中的位置下标，否者返回空"""
    row = len(array)
    col = len(array[0])

    i = 0
    j = col - 1
    while i<= row and j>=0:
        if array[i][j] > target:  # 剔除第j列
            j -= 1
        elif array[i][j] < target:  # 剔除第i行
            i += 1
        else:
            return i, j  # 返回下标


if __name__ == '__main__':
    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13]]
    print(find_elem(7, array))