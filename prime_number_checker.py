# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 11:57:53 2021

@author: men_l
"""

n = int(input("Check this number: "))

# def prime_checker(number):
#     assert number > 1, "It's not a prime number."
#     # if number <= 1:
#     #     print("It is not a prime number") 
#     if number in [2,3]:        
#         print("It's a prime number.")    
#     elif number % 2 == 0 or number % 3 == 0:    
#         print("It's not a prime number.")        
    
#     else:  
#         i = 5
#         while i * i <= number :
#             if number % i ==0 or n % (i+2) == 0:
#                 print("It is not a prime number.")
#                 i = i + 6             
#         print("It's a prime number")
def prime_checker(number):
    is_prime = True
    for i in range (2,number):
        if number % i ==0:
            is_prime = False
    if is_prime :
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
        
        
    
prime_checker(number=n)