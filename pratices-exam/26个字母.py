# -*- coding: utf-8 -*-
__date__ = '2020/2/23 20:46'

import string

for ch in string.ascii_lowercase:
    print(ord(ch), ch)

print()
for ch in string.ascii_uppercase:
    print(ord(ch), ch)

print()
for ch in string.ascii_letters:
    print(ord(ch), ch)

print()
for i in range(97, 97+26):
    print(i, chr(i))

letters_list = [chr(i) for i in range(97, 97+26)]
print(letters_list)

letters_string = ''.join([chr(i) for i in range(97, 97+26)])
print(letters_string)