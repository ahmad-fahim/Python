# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:48:32 2018

@author: fahim.ahmad
"""

input_number = int(input("Enter a number : "))

num1 = 0
num2 = 1
 
while (input_number > 0):
    print(num1, end=' ')
    temp_num = num1
    num1 = num1 + num2
    num2 = temp_num
    #num1 , num2 = num2 , num1 + num2
    input_number -=1 
    
    #print(num1, end=' ')
