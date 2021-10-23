# -*- coding: utf-8 -*-
"""
Largest number from a list
"""
def larg_num(list):
    larg = list[0]
    for a in list:
        if a>larg:
            larg = a

    return larg

print(larg_num([1,2,5,7]))