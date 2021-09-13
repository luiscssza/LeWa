#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:01:45 2021

@author: luis
"""

# def dna_to_rna(dna):
#     return dna.replace("T", "U")

# #double = lambda x: x*2
# my_list = [1,2,3,4,5,6,7,8,9]
# even = list(filter(lambda x: (x%2==0), my_list))
# print(even)

# double = list(map(lambda x: x*2, my_list))
# print(double)

# DNA_to_RNA = lambda dna: dna.replace("T", "U")

# dna= "TUTUTUTUTUTUTUTUTUTUTUTU"
# print(DNA_to_RNA(dna))

# pepe = "pepe"
# def are_you_playing_banjo(name):
#     # if name[0] == "R" or "r":
#     #     name =  name + "plays banjo"
#     # else:
#     #     name = name + "does not play banjo"
#     # return name
#     return name + (" plays" if name[0].lower() == "r" else " does not play") + " banjo"

# def is_digit(string):
#     return string.isdigit() and len(string)==1

import re

data="q1"
result= bool(re.match("\d", data))