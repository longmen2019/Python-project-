# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:56:42 2021

@author: men_l
"""

total = 0
for i in range (0,101):
    if i % 2 ==0:
        total = total + i
print(f"The total even number is {total}")