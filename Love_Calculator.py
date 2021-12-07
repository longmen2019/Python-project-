# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:06:11 2021

@author: men_l
"""

name1 = input("Please enter your name: ")
name2 = input("please enter your name: ")
name1_lowercase = name1.lower()
name2_lowercase = name2.lower()
name = name1_lowercase + name2_lowercase
# print(name)
true = ['t' , 'r' , 'u' , 'e']
count = 0
for i in name:
  if str(i) in true:
    count= count + 1
print(count)

love = ['l' , 'o' , 'v' , 'e']
num = 0
for j in name:
  if str(j) in love:
    num = num +1
print(num)
love_score = str(count) + str(num)
print(f"Your score is {love_score}")

love_score = int(love_score)

if love_score < 10 or love_score> 90:
  print(f"Your score is {love_score}, , you go together like coke and mentos.")
elif love_score >40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}")



