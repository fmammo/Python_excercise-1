# -*- coding: utf-8 -*-
"""
A function which finds/outputs the maximum of three numbers
"""
def max():
    a = input("Please input the first number:    ")
    b = input("Please input the second number:    ")
    c = input("Please input the third number:     ")
    if a > b and a > c:
        print("a is the maximum number")
    elif b > a and b > c:
        print("b is the maximum number")
    elif c > a and c> b:
        print("c is the maximum number")
    else:
        print("Can not determine")
        
# Checking the program
max()


