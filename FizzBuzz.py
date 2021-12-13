# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:35:07 2021

@author: men_l
"""

for i in range (1,101):
    if i % 3 ==0 and i % 5 ==0:
        print("FizzBuzz")
            
    elif i % 3 == 0:
        print("Fizz")
        
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)
    
# print (i)