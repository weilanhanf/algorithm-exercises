# -*- coding: utf-8 -*-
__date__ = '2020/2/9 23:17'


def pow_sign(base, exponent):
    result = 1.0
    for i in range(1, exponent+1):
        result *= base
    return result


def pow(base, exponent):
    if base == 0 and exponent < 0:
        return 0
    abs_exponent = abs(exponent)
    result = pow_sign(base, abs_exponent)
    if exponent < 0:
        result = 1/result
    return result


if __name__ == '__main__':
    print(pow(4, 2))
    print(pow(2, -1))
    print(pow(2, 0))
    print(pow(0, 4))
    print(pow(0, 0))  # 数学上无意义，输出1可以接受