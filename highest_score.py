# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:37:50 2021

@author: men_l
"""

student_score = [78, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0

for score in student_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score is {highest_score}") 
    
    

   