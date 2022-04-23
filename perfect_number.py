# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:02:10 2018

@author: fahim.ahmad
"""

input_number = int(input("Enter the Number Range : "))

loop_upto = int((input_number ))
#print (loop_upto)

new_number = 0

for loop_counter in range(1, loop_upto ):
    #print (input_number,loop_counter, new_number, input_number % loop_counter)
    if input_number % loop_counter == 0 :
        new_number = new_number + loop_counter
        
if new_number == input_number :
    print("Perfect number")
else:
    print("Not a perfect number")