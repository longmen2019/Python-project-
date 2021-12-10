# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:05:45 2021

@author: men_l
"""

student_heights = [156, 178, 165, 171, 187]
sum = 0
for i in student_heights:
    sum = sum+i
    i=+i 
print(sum)
sum = sum/len(student_heights)
print(len(student_heights))
sum = round(sum)
print(sum)