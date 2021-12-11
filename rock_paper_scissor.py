# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:26:24 2021

@author: men_l
"""


"""Rock Paper Scissor"""
import random
random_choice = random.randint(0,2)
print(random_choice)
computer_choice = 0
if random_choice == 0:
  computer_choice = "Rock"
elif random_choice == 1:
  computer_choice = "Paper"
else:
  computer_choice = "Scissor"
computer_choice = computer_choice.lower()
# print(computer_choice)

user_choice = input('What is your choice? Type "Rock", "Paper", "Scissor ": \n ')
user_choice = user_choice.lower()
num_attempt = 5

for i in range (num_attempt):
    if user_choice not in ["rock" , "paper" , "scissor"]:
        print(f"You have {num_attempt} attempt left")
        user_choice= input('Wrong input. What is your choice? Type "Rock", "Paper", "Scissor: " \n ')
        user_choice = user_choice.lower()
        num_attempt -= 1
        if num_attempt == 0:         
            print(f"You've {num_attempt} attempt left, Sucker!") 
            break           
   
    elif computer_choice == "rock" and user_choice == "scissor":
      print("The matrix win! ") 
      break
    elif computer_choice == "paper" and user_choice == "rock":
      print("The matrix win!")
      break
    elif computer_choice == "scissor" and user_choice == "paper":
      print("The matrix win")
      break
    elif computer_choice == user_choice:
      print("it is a draw! let's play a gain")
      break
    else:
        print("Human win")
        break
