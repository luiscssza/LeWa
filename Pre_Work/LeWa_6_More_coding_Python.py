#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:27:31 2021

@author: luis
"""
#Source: https://docs.python.org/3/tutorial/controlflow.html


########################################################################
# 4.1 if statements
# x=int(input("Please enter an integer: "))
# if x < 0:
#     print(f"Negative input value, {x**2}, changed to zero")
#     x=0
# elif x==0:
#     print("zero")
# elif x==1:
#     print("Single")
# else:
#     print("More")
###########################################################################
# 4.2 for statements

# words = ["cat", "window", "defenestrate"]
# for i in words:
#     print(i, len(i))
    
# Strategy:  Iterate over a copy
#COULD BE INTERESTING THIS 
# for i in range(5):
#     print(i)

#list(range(5,10))
# list(range(0,10,3))
# list(range(-10, -100, -30))  


########################################################################
# a= ['Mary', 'had', 'a', 'little', 'lamb']

# for i in range(len(a)):
#     print(i, a[i])

# iterable
#sum(range(4))

# 4.4 break and continue statements and else clauses loop

# for n in range(2,10):
#     for x in range(2,n):
#         if n % x ==0:
#             print(n, "equals", x, "*", n//x)
#             break
#     else:
#             print(n, "is a prime number")
        
# for n in range(2,10):
#     for x in range(2,n):

    
#         if n % x == 0:
#             print(f"{n} is not prime {x}")

# for num in range(2,10):
#     if num % 2 == 0:
#         print(f"Found an even number: {num}")
#         continue
#     print(f"Found an odd number: {num}")

#############################################################################
#https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# 5. Data Structures¶
#5.1. More on Lists¶
# fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

# fruits.count("apple")
# fruits.index("banana")
# fruits.index("banana", 4)
# fruits.reverse()
# fruits.append("grape")
# fruits.sort()
##########################################################################
# 5.1.1. Using Lists as Stacks¶
# stack = [3,4,5]
# stack.append(6)
# stack.append(7)
# print(stack)
# stack.pop()
##########################################################################
# 5.1.2. Using Lists as Queues¶
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# queue.append("Graham")
# left = queue.popleft()
# queue.pop()
# print(left)
# print(queue[0])
##########################################################################
# 5.1.3. List Comprehensions¶

# squares =[]
# for x in range(10):
#     squares.append(x**2)
# print(squares)

# squares = list(map(lambda x: x**2, range(10)))
# print(squares)

# squares = [x**2 for x in range(10)]
# print(squares)

# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x,y))
# print(combs)

# combs1=[(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(combs1)

# vect =[-4, -2, 0, 2, 4]
# print(vect)
# dopple = [2*x for x in vect]
# print(dopple)
# only_positive= [x for x in vect if x>=0]
# print(only_positive)
# absolute_values=[abs(x) for x in vect]
# print(absolute_values)

# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# stripped = [weapon.strip() for weapon in freshfruit]
# print(stripped)

# number_and_square = [(x, x**2) for x in range(6)]
# print(number_and_square)

# vec = [[1,2,3], [4,5,6], [7,8,9]]
# flattened_vec = [num for line in vec for num in line ]
# print(flattened_vec)

# from math import pi
# pi_decimals = [str(round(pi, i)) for i in range(1,6)]
# print(pi_decimals)

##########################################################################
#5.1.4. Nested List Comprehensions¶

#matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


# zip 
# https://docs.python.org/3/library/functions.html#zip
# x = [1,2,3]
# y = [4,5,6]
# zipped = zip(x,y)
# zipped_list = list(zipped)
# print(zipped_list)

##########################################################################
# 5.3. Tuples and Sequences¶
# Sequence Types — list, tuple, range https://docs.python.org/3/library/stdtypes.html#typesseq

# t = 12345, 54321, "hello!"
# u = t, (1,2,3,4,5)

# empty = ()
# singleton = "hello",

# t_u =(12345, 54321)
##########################################################################
# 5.4 Sets

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket) # duplicates have been removed
#"orange" in basket
# a = set("abracadabra")
# b = set("alacazam")
# print(a)
# print(b)

# print(f"a-b => letters in \"a\" BUT NOT in \"b\": {sorted(a - b)}" )
# print(f"a|b => letters in \"a\" OR in \"b\" OR in both: {sorted(a | b)}" )
# print(f"a&b => letters in \"a\" AND in \"b\": {sorted(a & b)}" )
# print(f"a^b => letters in \"a\" OR in \"b\" BUT NOT BOTH: {sorted(a ^ b)}" )

# a = { x for x in "abracadabra" if x not in "abc"}
# print(a)


# 5.5. Dictionaries¶

# tel = {"jack":4098, "shape": 4139}
# tel["Guido"] =  4127    # added at the end of the dictionary
# tel["irv"] = 4127
# tel["jack"]= 1234       # not work
# list(tel)               # provide only the keys
# sorted(tel)             # provide a sorted list of the keys 

# pepe = {x: y**2 for x in ["juan", "dani", "nacho"] for y in (0,1,2)}                                                                                                                                                                                                                                                                                                                                           
# print(pepe)
# pepe_1 = {x: y for x, y in ["juan", "dani", "nacho"] and range(3)}                                                                                                                                                                                                                                                                                                                                           
# print(pepe_1) # NOT WORK????

# LeWagon exam:
    
# le_wagon_team = [
#     {"name": "ben", "age": 31, "country": "France", "hobbies": ["coding", "biking"]},
#     {"name": "quinn", "age": 26, "country": "Ireland", "hobbies": ["skiing"]},
#     {"name": "alex", "age": 28, "country": "Austria", "hobbies": []}]
# print(type(le_wagon_team))
# print(type(le_wagon_team[0]))
# print(type(le_wagon_team[0]["hobbies"]))
# print(len(le_wagon_team))
# print(len(le_wagon_team[0]))
# print(len(le_wagon_team[0]["hobbies"]))
# le_wagon_team[-1]["hobbies"] = ["video games"]
# le_wagon_team[-1]["hobbies"].append("football")
# le_wagon_team.append({"name": "Rebecca", "age": 27, "country": "Scotland", "hobbies": ["travel"]})
# print(f"{le_wagon_team[0]['name']} ({le_wagon_team[0]['age']} years old)")

# for i in range(len(le_wagon_team)):
#     print(f"{le_wagon_team[i]['name']} ({le_wagon_team[i]['age']} years old)")


# https://docs.python.org/3/tutorial/datastructures.html#looping-techniques
#5.6. Looping Techniques#####################################################

#knights = {"gallahad": "the pure", "robin": "the brave"}
# for k, v in knights.items():
#     print(k,v)

# for i in range(len(le_wagon_team)):
#     for k, v in le_wagon_team[i].items():
#         print(k,v)

# for i, v in enumerate(le_wagon_team):
#     print(i,v)

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print(f" What is your {q}? It is {a}.")
# #print(f" What is your {questions[0]}? It is {answers[0]}.")

# for i in reversed(range(1,10, 2)):
#     print(i)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in basket:
#     print(i)
# for i in sorted(basket):
#     print(i)
# for i in sorted(set(basket)):
#     print(i)
    
# import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]    
# filtered_data = []

# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)
# filtered_data
    
    
# 5.7. More on Conditions  

# string_1, string_2, string_3 = "", "Trondheim", "Hammer Dance"
# non_null = string_1 or string_2 or string_3


#https://docs.python.org/3/tutorial/stdlib.html
#10. Brief Tour of the Standard Library

# import os

# work_dir = os.getcwd()              # Return the current working directory
# os.chdir("/user/luis....")          # Change current working directory
# os.system("mkdir prueba_en_python") # Run the command mkdir in the system shell

# dir(os)                             # Returns a list of all modle functions
# help(os)                            # Returns an extensive manual page created from the module's docstrings


# import shutil
# # shutil.copyfile('data.db', 'archive.db')
# # shutil.move('/build/executables', 'installdir')
# https://docs.python.org/3/library/shutil.html#module-shutil
# import glob
# glob.glob("*.py")

# import sys
# sys.stderr.write("Esto ha estallado!!!")
    
# import re
# found_f = re.findall(r"\bf[a-z]*", "which foot or hand fell fastest afford")
# found_subpat = re.sub(r'(\b[a-z]+) \1', r'\1', "cat in the the hat")
    
# tea = "tea for too"
# repla = tea.replace("too", "two")    

#10.6 Mathematics
# https://docs.python.org/3/tutorial/stdlib.html

# import math

# value_cos = math.cos(math.pi/4)
# value_log = math.log(1024,2)
# value_log_e = math.log(math.e)
    
# import random
# fruit = random.choice(["aple", "pear", "banana"])
# ran = random.sample(range(100), 10)    
# ran_ran = round(random.random(),2)
# ran_int = random.randrange(10)
    
# import statistics as sta

# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# data_sorted = sorted(data)

# data_mean = sta.mean(data)
# # https://en.wikipedia.org/wiki/Mean

# data_median = sta.median(data)
# # https://en.wikipedia.org/wiki/Median
# data_sorted_set = set(data_sorted)
# data_median_sorted_set = sta.median(data_sorted_set)
# print(f"the median of the sorted & setted data, {data_median_sorted_set}, is different to the median of the original data, {data_median}, because by using set, the repeated values are not taking into account.")

# data_variance = sta.variance(data)
# # https://en.wikipedia.org/wiki/Variance
# data_variance_sorted_set = sta.variance(data_sorted_set)

    
# 10.8. Dates and Times 
    
# from datetime import date

# now = date.today()  # year, month, day
# printed = now.strftime("Year: %y, Month: %m, Day: %d")
# print(printed)
# whole_date = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# print(whole_date)    

# # dates support calendar arithmetic
# birthday = date(1979, 2, 2)
# age = now - birthday
# days = age.days
# print(f"Luis has lived until now {days}")
    
    
# 10.9. Data Compression

# 10.10. Performance Measurement
    
# from timeit import Timer

# time_1 = Timer("t=a; a=b;b=t","a=1; b=2").timeit()
# time_2 = Timer("a,b=b,a", "a=1; b=2").timeit()

# See more info about profile and pstats
# https://docs.python.org/3/library/profile.html#module-pstats
# https://docs.python.org/3/library/profile.html#module-profile

# 10.11. Quality Control
    
# def average(values):
#     """Computes the arithmetic mean of a list of numbers.
#     >>> print(average([20, 30, 70]))
#     40.0 
#     """
#     return sum(values) / len(values)

# import doctest
# doctest.testmod()

# import unittest
    
    
# 10.12. Batteries Included¶
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    