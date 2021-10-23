# -*- coding: utf-8 -*-
"""
A function which sums up a list of numbers
"""
def sum_list(num):
    sum = 0
    for n in num:
        sum += n
    return sum

# Checking the program
print(sum_list((2,4,7,8,9)))

