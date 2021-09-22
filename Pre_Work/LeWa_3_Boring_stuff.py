# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Lesson 1: 5:12 Automate the boring stuff...
#pastebin.com
#gist.github.com

#-----------------------------------------------------------------------------
# https://automatetheboringstuff.com/2e/chapter2/

##############################################################################
# while True:
#       print('Who are you?')
#       name = input()
#       if name != 'Joe':
#         continue
#       print('Hello, Joe. What is the password? (It is a fish.)')
#       password = input()
#       if password == 'swordfish':
#         print('Access granted.') 
#         break
# # print('Access granted.') here or within the if-condition
# # while loop with a internal if + break
################################################################################ 
# 0, 0.0 and "" are considered False

#################################################################################
# # Importing Modules
# import random
# # using import random it is needed to add the module name prefix "random. ..."
# # Prefered option(***)
# for i in range(5):
#     print(random.randint(1, 10))

# from random import *
# # using ifrom random import * it is NOT needed to add the module name "random. ..."
# # every time

#################################################################################
 
# import sys
# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit(0)
#     print('You typed ' + response + '.')
 
 
#################################################################################
#import random, sys

# print("I am thinking of a number between 1 and 20.")
# secret_number =  random.randint(1, 20)
# num_guess = 0
# while True:
#     guess = int(input("Introduce your guess:"))
#     num_guess += 1
#     if guess < secret_number:
#         print("Your guess is too low")
#     elif guess > secret_number:
#         print("Your guess is too high")
#     else:
#         print(f"Good job! You guessed my number in {num_guess} guesses!")
#         break
# sys.exit(0)
 
# print("I am thinking of a number between 1 and 20. You have only 4 tries")
# secret_number =  random.randint(1, 20)
# num_guess = 0
# while num_guess <4:
#     guess = int(input("Introduce your guess:"))
#     num_guess += 1
#     if guess < secret_number:
#         print("Your guess is too low")
#     elif guess > secret_number:
#         print("Your guess is too high")
#     else:
#         print(f"Good job! You guessed my secret number in {num_guess} guesses!")
#         break
# if num_guess==4:
#     print(f'Unfortunately you have achieved the maximum number of tries. The secret number was {secret_number}')
# sys.exit(0)
 
 
###############################################################################
#-------------------------FUNCTIONS--------------------------------------------
# https://automatetheboringstuff.com/2e/chapter3/
 
# print("cat", "dogs")
# print("cat"*2, "dogs"*3, sep="%", end="#")

# print()
 
# GLOBAL and LOCAL VARIABLES

# Exception Handling

# def spam(divideby):
#     try:
#         return 42/divideby
#     except ZeroDivisionError:
#         print("Error: Invalid argument.")
        
# for i in range(0,11):
#     print(spam(i))

# def spam(divide_by):
#     return 42/divide_by
# try:
#     print(spam(42))
#     print(spam(21))
#     print(spam(10))
#     print(spam(0))
#     print(spam(1))
# except ZeroDivisionError:
#     print('Error: Invalid argument.')

 
# ENUMERATE()
 
# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
 
# for index, item in enumerate(supplies):
#     print("Index "+ str(index) + " in supplies is " + item)
 
# random.choice() randoom.shuffle()

# import random
# pets = ['Dog', 'Cat', 'Moose']  
# print(random.choice(pets))

# people = ['Alice', 'Bob', 'Carol', 'David']
# print(people)
# random.shuffle(people)
# print(people)
 
# Augmented Assignment Operators
 
# *=

# METHODS

# spam = ['hello', 'hi', 'howdy', 'heyas']

# item = spam.index("hello")
  

# del: index known
# remove: value known

# sort()

# spam = [2, 5, 3.14, 1, -7]
# spam.sort()
# spam.sort(reverse = True)

# spam_1 = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']

# spam_1.sort()

# spam_1.sort(key=str.lower)

# spam_animals = ['cat', 'dog', 'moose']
# spam_animals.sort()
# spam_animals.reverse()

# spam = ['apples',
#     'oranges',
#                     'bananas',
# 'cats']
# print(spam)

# Sequence Data Types

# Mutable and Immutable Data Types

# The Tuple Data Type

# Converting Types with the list() and tuple() Functions


























