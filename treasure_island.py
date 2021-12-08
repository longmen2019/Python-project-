# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:05:18 2021

@author: men_l
"""


print("welcome to Treasure Island. \n Your mission is to find the treasure.")
# user_input= input("You're at a crossroad , where do you want to go? Type LEFT or RIGHT \n")
user_input = input('You\'re at a crossroad, where do you want to go? Type "left" or "right" \n')
user_input = user_input.lower()
if user_input == "left":
  user_input = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "SWIM" or "WAIT" \n') 
  user_input = user_input.lower()
  if user_input == "wait":
    user_input = input('You\'re at a crossroad , where do you want to go? Type "RED", "BLUE", "YELLOW".\n')    
    user_input = user_input.lower()
    if user_input == "yellow":
      print ("You win!")
      print('''
      
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      
      
      ''')
    elif user_input == "red":
      print("Burned by fire. Game over.")
    elif user_input == "blue":
      print("Eaten by beasts. Game over.")
    else:
      print("Game over.")
  else:  
    print("Attacked by trout. Game Over.")
else:
   print("Fall into a hole. Game Over.") 