# -*- coding: utf-8 -*-
__date__ = '2020/2/22 16:28'


# 将p进制的x转化为十进制的y
def other_to_ten(x, p):  # p表示进制，num表示需要处理的数
    product, y = 1, 0  # pro表示处理时最低位要乘的数，y用来存储数值
    while x != 0:
        y = y + (x % 10) * product  # 处理最低位
        x = int(x/10)  # 去掉最低位
        product = product*p  # 下一最低位乘pro
    return y


# 将十进制的num转换为b进制的y
def ten_to_other(num, b):
    res = []
    while num != 0:
        res.insert(0,num%b)  # num%b对num取余
        num = int(num/b)
    res = [str(i) for i in res]
    y = int(''.join(res))
    return y

def base_conversion(num, p, b):
    m = other_to_ten(num, p)
    n = ten_to_other(m, b)
    return n


if __name__ == '__main__':
    num, a, b = map(int, input().split())
    print(base_conversion(num, a, b))