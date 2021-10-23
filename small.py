# -*- coding: utf-8 -*-
"""
Smallest number from alist
"""

def small_num(list):
    small = list[0]
    for a in list:
        if a < small:
            small = a
    return small
print(small_num([2,5,7,9]))