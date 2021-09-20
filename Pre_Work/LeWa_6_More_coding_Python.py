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
# https://docs.python.org/3/tutorial/datastructures.html#looping-techniques

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

#5.6. Looping Techniques





