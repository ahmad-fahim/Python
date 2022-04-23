# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 21:00:25 2018

@author: fahim.ahmad
"""

def number_of_names(name_of_studens) :
    return len(name_of_studens)
    
    
names = ["Fahim","Uzzal","Sumon","Fahad"]
print(number_of_names(names))
total_names = ''
for idx in names:
    total_names =  total_names + idx
    
print(number_of_names(total_names))