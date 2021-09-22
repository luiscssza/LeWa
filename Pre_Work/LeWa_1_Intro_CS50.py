# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 13:47:24 2021

@author: costeros
"""

# name = input("Introduce your name: \n")
# print("Hello "+ name + ". How are you?")
# print(f"Hello {name}. How are you?")

###############################################################################

# x= input("x:")
# y= input("y:")

# if x > y:
#     print("x is higher as y")
# elif x < y: 
#     print("x is higher")
# else:
#     print("x is equal to y")

# x = input("Dame una x:")
# y = input("Dame una y:")

# if x>y:
#     print(f"x={x} es mayor que y={y}")
# elif y>x:
#     print(f"y={y} es mayor que x={x}")
# else:
#     print(f"x={x} es igual que y={y}")

###############################################################################

# while True:
#     print("hello, world")
###############################################################################

# i=3
# while i >0:
#     print("cough \n", end="")
#     i-=1
# With the same results:
# i=3
# while i>0:
#     print("cough")
#     i-=1
###############################################################################

# for i in [1,2,3]:
#     print("cough")
    
# for i in range(3):
#     print("cough")


###############################################################################

# from PIL import Image, ImageFilter

# before = Image.open("2014-11-02 14.55.54.jpg")
# after= before.filter(ImageFilter.BLUR)
# after.save("out.jpg")


###############################################################################

# words = set()

# def check(word):
#     if word.lower() in words:
#         return True
#     else:
#         return False

# def load(dictionary):
#     file = open(dictionary, "r")
#     for line in file:
#         words.add(line.rstrip("\n"))
#     file.close()
#     return True

# def size():
#     return len(words)

# def unload():
#     return True

###############################################################################

# s = input("What´s your name?\n")
# #print("hello, " + s)
# print(f"hello, {s}")

# name  = "Eric"
# age = 74
# print("Hello, {name}. You are {age}.")
# f"Hello, {name}. You are {age}."

###############################################################################

# age = int(input("What´s your age?\n"))

# print(f"You are at least {age * 365} days old")

###############################################################################

# s = input("Do you agree?\n")

# # if s=="Y" or s=="y":
# #     print("Agreed.")
# # elif s== "N":
# #     print("Not agreed.")
# # else:
# #     print("I dont understand you")

# # if s in ["Y","y", "yes", "yea", "Yea"]:
# #     print("Agreed.")
# # elif s== "N":
# #     print("Not agreed.")
# # else:
# #     print("I dont understand you")
    
# if s.lower() in ["y","yes", "yea"]:
#     print("Agreed.")
# elif s.lower() in ["n","no", "nope"]:
#     print("Not agreed.")
# else:
#     print("I dont understand you")

###############################################################################


# def main():
#     for i in range(3):
#         cough()

# def cough():
#     print("cough")
    
# main()
###############################################################################
# def main():
#     number_of_cough = int(input("How many times do you want to cough?\n"))
#     cough(number_of_cough)

# def cough(n):
#     for i in range(n):
#         print("cough")
    
# main()

###############################################################################

#print("cough\n"*3)

###############################################################################

# def main():
#     i = get_positive_int()
#     print(i)
    
    
# def get_positive_int():
#     while True:
#         n= int(input("Introduce a positive integer:"))
#         if n > 0:
#             return n
#             break

# main()
    
############################################################################### 
# for i in range(4):
#     print("?", end="")
# print()

# print("?" *4)


# for i in range(3):
#     print("#")

# for i in range(3):
#     print("#")
    
# print("#\n"*3, end="")


# for i in range(3):
#     for j in range(3):
#         print("#", end ="")
#     print()
###############################################################################

# age = int(input("What is your age?: "))
# print(f"Your are at leat {age*365} days old.")

###############################################################################
    
# from time import sleep
# i = 1
# while True:
#     print(i)
#     sleep(0.1)
#     i *=2
###############################################################################
    
# # scores = []
# # scores.append(72)
# # scores.append(73)
# # scores.append(33)   
# scores = [72,73,33]
# print(f"Average: {sum(scores)/len(scores)}")
    
###############################################################################
    
# s = input("Input: ")
# print(f"Output: ", end="")
# # for i in range(len(s)):
# #     print(s[i], end="")
# for c in s:
#     print(c, end="")
# print()
###############################################################################

# s = input("Before: ")
# print(f"After: {s.upper()}", end="\n")
# print(f"After: {s.lower()}", end="")
#print(s.upper())
###############################################################################

# from sys import argv

# # for i in range(len(argv)):
# #     print(argv[i])

# for i in argv:
#     print(i)
###############################################################################
# from sys import argv, exit


# if len(argv) !=2:
#     print("missing command-line argument")
#     exit(1)
# print(f"hello, {argv[1]}")
# exit(0)
###############################################################################

# from sys import exit

# names =["EMMA", "RODRIGO", "BRIAN", "DAVID"]
# if "EMMA" in names:
#     print("FOUND!!!")
#     exit(0)
# print("NOT FOUND!!!")
# exit(1)
###############################################################################    

# from sys import exit

# people = {
#     "EMMA": "0355-69-3301",
#     "RODRIGO": "0355-69-33012",
#     "BRIAN": "0355-69-3303",
#     "DAVID": "0355-69-3304"    
#     }

# whom_call= input("Of whom do you like the phone number?: ").upper()

# if whom_call in people:
#     print(f"The phone number of {whom_call} is {people[whom_call]}")
#     exit(0)
# print("NOT FOUND")
# exit(0)
###############################################################################
# x =1
# y =2

# print(f"x is {x}, y is {y}")
# x,y = y,x
# print(f"x is {x}, y is {y}")
###############################################################################
# import csv

# file = open("phonebook.csv", "a")

# name = input("Name of the person: ")
# number = input("Telephone number: ")

# #file.write("Name, Number\n")

# writer = csv.writer(file)
# writer.writerow((name, number))
# file.close()

###############################################################################
# import csv

# name = input("Name of the person: ")
# number = input("Telephone number: ")

# #file.write("Name, Number\n")

# with open("phonebook.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow((name, number))
###############################################################################
# import re

# s = input("Do you agree?\n")

# if re.search("y(es)?", s, re.IGNORECASE):
#     print("Agreed.")
# elif re.search("^n(o)$", s, re.IGNORECASE):
#     print("Not agreed.")
###############################################################################
# words = input("Say something:\n").lower()
# if "hello" in words:
#     print("Hello to you too!")
# elif "how are you" in words:
#     print("I am well, thanks!")
# elif "goodbye" in words:
#     print("Goodbye to you too!")
# else:
#     print("Huh?")
###############################################################################
# import speech_recognition as sp_rec

# recognizer = sp_rec.Recognizer()
# with sp_rec.Microphone() as source:
#     print("Say something, please!")
#     audio = recognizer.listen(source)
# print("Google Speech Recognition thinks you said:")
# print(recognizer.recognize_google(audio))

# ##############################################################################
#Reference: https://pypi.org/project/SpeechRecognition/

# import speech_recognition as sp_rec
# import re

# # Obtain audio from the microphone
# recognizer = sp_rec.Recognizer()
# with sp_rec.Microphone() as source:
#     print("Say something, please!")
#     audio = recognizer.listen(source)

# # Recognize speech using Google Speech Recognition
# words = recognizer.recognize_google(audio)

# # Respond to speech
# matches = re.search("my name is (.*)", words)

# if matches:
#     print(f"Hey, {matches[1]}.")
# else:
#     print("Hey you.")




# def discounted_price_fun(price, discount):
#     price_reduction = price*discount
#     reduced_price= price - price_reduction
#     return reduced_price
# new_price= discounted_price_fun(12, 0.1)
# print(price_reduction)


#https://realpython.com/python-f-strings/







