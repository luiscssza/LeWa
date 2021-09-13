# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 13:47:24 2021

@author: costeros
"""
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
    
      
    # x= input("x:")
# y= input("y:")

# if x > y:
#     print("x is higher as y")
# elif x < y: 
#     print("x is higher")
# else:
#     print("x is equal to y")

# while True:
#     print("hello, world")

# i=3
# while i >0:
#     print("cough \n", end="")
#     i-=1

# for i in [1,2,3]:
#     print("cough")
    
# for i in range(3):
#     print("cough")


from PIL import Image, ImageFilter

before = Image.open("2014-11-02 14.55.54.jpg")
after= before.filter(ImageFilter.BLUR)
after.save("out.jpg")


# x= input("x:")
# y= input("y:")

# if x > y:
#     print("x is higher as y")
# elif x < y: 
#     print("x is higher")
# else:
#     print("x is equal to y")

# while True:
#     print("hello, world")

# i=3
# while i >0:
#     print("cough \n", end="")
#     i-=1

# for i in [1,2,3]:
#     print("cough")
    
# for i in range(3):
#     print("cough")


from PIL import Image, ImageFilter

before = Image.open("2014-11-02 14.55.54.jpg")
after= before.filter(ImageFilter.BLUR)
after.save("out.jpg")
    
    
    
    

# def discounted_price_fun(price, discount):
#     price_reduction = price*discount
#     reduced_price= price - price_reduction
#     return reduced_price
# new_price= discounted_price_fun(12, 0.1)
# print(price_reduction)


#https://realpython.com/python-f-strings/







