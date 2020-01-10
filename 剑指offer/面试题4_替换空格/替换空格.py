# -*- coding: utf-8 -*-
__date__ = '2019/12/31 19:27'

# '''问题描述：给定一个字符串比如s为"hello world "，将s中的空格替换为%20的字符串并返回'''
#
#
# def replace_blank1(s):  # 使用方法
#     return s.replace(' ', '%20')


#
# def replace_blank2(s):  # ；列表元素可变
#     str_list = list(s)
#     for i in range(len(s)):
#         if s[i] == ' ':
#             str_list[i] = '%20'
#     return ''.join(str_list)


#
#
# def replace_blank3(s):
#     '''给定一个字符串比如s为"hello world "，将s中的空格替换为%20的字符串并返回'''
#
#     str_len = len(s)
#     blank_num = s.count(' ')  # 获取s的空格个数
#     new_str_len = str_len + blank_num*2  # 新串的长度
#     str_list = [' '] * new_str_len
#     j = 0  # 用j指向新串的待填入位置
#     for i in range(len(s)):  # 用i指向老串的待处理字符
#         if s[i] == ' ':
#             str_list[j] = '%'
#             str_list[j+1] = '2'
#             str_list[j+2] = '0'
#             j += 3  # 空格做替换
#         else:
#             str_list[j] = s[i]
#             j += 1
#
#     return ''.join(str_list)
#
#
# if __name__ == '__main__':
#     # s = input('input a string:')
#     s = 'Hello World'
#     print(replace_blank__(s))
#


# """给定一个字符串，将其中的空格替换为任意字符串"""


# def replace_blank4(s, res):
#     """将s中的空格替换为res"""
#     str_len = len(s)
#     res_len = len(res)
#
#     blank_num = s.count(' ')  # 计算空格的个数
#     new_str_len = str_len + (res_len - 1) * blank_num
#     new_str_list = [' '] * new_str_len
#
#     j = 0
#     for i in range(str_len):
#         if s[i] == ' ':
#             n = 0
#             for k in range(j, j+res_len):
#                 new_str_list[k] = res[n]
#                 n += 1
#             j += res_len
#         else:
#             new_str_list[j] = s[i]
#             j += 1
#
#     return ''.join(new_str_list)
#
#
# if __name__ == '__main__':
#     s = 'hello world'
#     res = '%20'
#     print(replace_blank(s, res))


