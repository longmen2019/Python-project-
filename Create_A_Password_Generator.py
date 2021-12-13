# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:57:51 2021

@author: men_l
"""
import random 
# import strings 
import re

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# creating an array function for letters, numbers and symbols 
def split(word):
    return [char for char in word] #split each character of string into an array 
print(split(letters))

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q'
           ,'r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'
           , 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = "01234567890"
print(split(numbers))
numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = "!@#$%^&*()+"
print(split(symbols))
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

print("Welcome to the PyPassword Generator! ")

nr_letters = int(input("How many leters would you like in your passwords?\n"))
# assert nr_letters > 0,  print("Wrong input")
# assert nr_letters = re.compiler(r'^\?[1-9]*$'), print("Wrong input")
# num_format = re.compile(r'^\-?[1-9][0-9]*$')
# it_is = re.match(num_format,nr_letters)
# if it_is: print("True")
# else: print("False")

nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
password = ""  # leave no space for password otherwise it will also a space in the answer 
# assert nr_letters >= 0, 'wrong input'

for l in range (1, nr_letters+1): # start from 1 and also end the string with + 1
    random_l = random.choice(letters)
    password = password + random_l    
    print(random_l) # add a char of string to the password one at a time 
for s in range (1, nr_symbols+1): 
    random_s = random.choice (symbols)
    password = password + random_s 
    print(random_s)
for n in range (1, nr_numbers+1):
    random_n = random.choice (numbers)
    password = password + random_n
    print(random_n)
print(password)
len_pwd = nr_letters + nr_symbols + nr_numbers # get the length of the pawd for the random.sample funct 
# new_password = ''.join(random.choice(password) for i in range (len_pwd))


# print(type(len_pwd))
temp = random.sample(password,len_pwd) #this is going to shuffle the password and give us an array of char
# print(temp)
new_password ="".join(temp) # adding together the array of char  in the temp into a new password 
print(new_password)
# print(new_password)
