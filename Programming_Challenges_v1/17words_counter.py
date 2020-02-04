# # lvl 1: using function
#
#
# def word_counter(amount=0):
#     for i in range(len(input().split())):
#         amount += 1
#     return amount
#
#
# print(word_counter())


# lvl 2: using function + regex

import re

wordslist = input()


def word_counter(amount=0):
    res = len(re.findall(r'\w+', wordslist))
    for i in range(res):
        amount += 1
    return amount


print(word_counter())

