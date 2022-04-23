# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:54:58 2018

@author: fahim.ahmad
"""

number = 25


for i in range (1, number + 1):
    for space_loop in range (i-1, number - 1) :
        print(" ", end = ' ')
    for j in range (1, i + 1 ):
        print (j , end = ' ')
    #print(i-1)
    for l in range (i-1, 0, -1 ):
        print (l , end = ' ')
    print("\n")    