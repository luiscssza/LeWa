# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:12:02 2021

@author: costeros
"""
number=15
def print_something(number):
    for j in range(1, number+1):
        if (j%3==0) and (j%5==0):
            print ("PizzaTime")
        elif j % 5==0:
            print("Time")
        elif (j%3==0):
            print("Pizza")
        else:
            print(j)
print_something(number)


#{'name': 'Rebecca', 'age' : 27, 'country':'Scotland','hobbies' :'travel'}

# le_wagon_team = [
#     {'name': 'ben', 'age': 31, 'country': 'france', 'hobbies': ['coding', 'biking']},
#     {'name': 'quinn', 'age': 26, 'country': 'ireland', 'hobbies': ['skiing']},
#     {'name': 'sasha', 'age': 24, 'country': 'lebanon', 'hobbies': ['sports']},
#     {'name': 'alex', 'age': 28, 'country': 'austria', 'hobbies': []}
# ]


    
# for i in range(len(le_wagon_team)):
#     print (f"{le_wagon_team[i]['name']} ({le_wagon_team[i]['age']} years old) ")
    
# a = "Hello"
# b = "world"

# def concatenate_strings(string_one, string_two):
#     return string_one+' '+string_two
# print(concatenate_strings(a,b))

# first_word = "wow"

# second_word = "amazing"
# border_word = "qqqqq"
# def longer_than_five(string):
#     if len(string) <= 5:
#         output= False
#     else:
#         output = True
#     return output
# first_bool=longer_than_five(first_word)
# second_bool=longer_than_five(second_word)
# border_bool = longer_than_five(border_word)

# #The standard deviation measures how wide the grade distribution spreads out taking as reference teh grades average