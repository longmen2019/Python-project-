# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 12:37:16 2021

@author: men_l


"""
logo= """

   ____     _   _ U _____ u ____    ____          _____    _   _  U _____ u      _   _       _   _   __  __     ____  U _____ u   ____        
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u      |_ " _|  |'| |'| \| ___"|/     | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u     
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/         | |   /| |_| |\ |  _|"      <|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/     
 | |_| |   | |_| | | |___  u___) | u___) |        /| |\  U|  _  |u | |___      U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <       
  \____|  <<\___/  |_____| |____/>>|____/>>      u |_|U   |_| |_|  |_____|      |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\      
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)     _// \\_  //   \\  <<   >>      ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_     
 (__)__)     (__) (__) (__)(__)    (__)         (__) (__)(_") ("_)(__) (__)     (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__)  

"""
print(logo)

print("Welcom to the Number Guessing Game! \nI'm thinking of a number between 1 and 100 ")
import random

random_number = random.randint(0,100)
print(random_number)
game_level = input('Choose a difficulty. Type "easy" or "hard": ')
if game_level == "easy":
    print("You have  10 attempts remaining to guess the game")
    number_of_guess = 10
elif game_level == "hard":
    print("You have 5 attempts remaining to guess the number. ")
    number_of_guess = 5
def guess_game():        
    global random_number
    global number_of_guess    
    player_guess = int(input("Make a guess: ")) 
    
    while number_of_guess > 0:         
        if player_guess > random_number:
            print("Too high\n Guess again ")
            number_of_guess = number_of_guess - 1
            print (number_of_guess)
            break        
        elif player_guess < random_number :
            print("Too low\n Guess gain ")
            number_of_guess = number_of_guess - 1
            print (number_of_guess)
            break
        elif random_number == player_guess:
            # number_of_guess is True 
            print("You've won")
            return 
    if number_of_guess == 0:
        print("You are out of guess") 
        return           
                     
    guess_game()
guess_game()
        
    
    
        # break


   
    #     

    
    


