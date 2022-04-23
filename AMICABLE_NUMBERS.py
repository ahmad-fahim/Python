# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:10:19 2018

@author: fahim.ahmad
"""

def sum_of_divisor(input_number) :
    loop_upto = int((input_number ))
    #print (loop_upto)
    
    new_number = 0
    
    for loop_counter in range(1, loop_upto ):
        #print (input_number,loop_counter, new_number, input_number % loop_counter)
        if input_number % loop_counter == 0 :
            new_number = new_number + loop_counter
            
    return new_number
    
    
input_number1 = int(input("Enter the first Number : "))

return_number1 = sum_of_divisor(input_number1)


input_number2 = int(input("Enter the second Range : "))
return_number2 = sum_of_divisor(input_number2)





if input_number1 == return_number2 and input_number2 == return_number1 :
    print("AMICABLE NUMBERS")
else:
    print ("Not a AMICABLE NUMBERS")




