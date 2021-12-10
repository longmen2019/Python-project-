# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 11:29:53 2021

@author: men_l
"""
row1 = ["😉",  "😲", "🥱"]
row2 = ["🥺", "😢",  "😭"]
row3 = ["🤧", "😷", "🤒"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
# print(map[1][1])
position = input("How do you feel today? ")
horizontal = position[0]
vertical = position[-1]
treasure = map[int(vertical)-1][int(horizontal)-1]
print(treasure)
