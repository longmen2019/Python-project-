# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:30:26 2021

@author: men_l
"""


print("Welcome to Python Pizza Deliveries")
size =input("What size pizza do you want? S , M, or L: ")
bill = 0

if size == "S" :
  print("Small pizza is $15")
  bill += 15
  add_pepporini = input("Do you want pepperoni? Y or N ")
  if add_pepporini == "Y":
    bill = bill + 2    
  extra_cheese = input("Do you want extra cheese? Y or N ")
  if extra_cheese == "Y":
    bill += 1    
  print(f"Your total payment is {bill}")
elif size == "M":
  print ("Medium pizza is $20")
  bill += 20
  add_pepporini = input("Do you want pepperoni? Y or N ")
  if add_pepporini == "Y":
    bill = bill + 3    
  extra_cheese = input("Do you want extra cheese? Y or N ")
  if extra_cheese == "Y":
    bill += 1    
  print(f"Your total payment is {bill}")    
else:
  print("Large pizza is $25")
  bill += 25
  add_pepporini = input("Do you want pepperoni? Y or N ")
  if add_pepporini == "Y":
    bill = bill + 3    
  extra_cheese = input("Do you want extra cheese? Y or N ")
  if extra_cheese == "Y":
    bill += 1    
  print(f"Your total payment is {bill}")  
    