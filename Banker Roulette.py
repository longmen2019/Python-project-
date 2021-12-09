# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:56:56 2021

@author: men_l
"""

import random
names_string = input("Give me everybody's names, separated by a comma. ")
names_string = names_string.split(",")
# print(len(names_string))
random_name = random.randint(0,(len(names_string)-1))
individual = names_string[random_name]
print(f"{individual} is going to buy the meal today!")
