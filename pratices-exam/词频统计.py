# -*- coding: utf-8 -*-
__date__ = '2020/2/23 20:44'

import operator

s = input()
letters_dict = {}

for ch in s:
    if ch in letters_dict.keys():
        letters_dict[ch] += 1
    else:
        letters_dict[ch] = 1

# print(letters_dict.items())
# letters_list = list(letters_dict.items())
# print(letters_list)

sorted_letters_list = sorted(letters_dict.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_letters_list)
