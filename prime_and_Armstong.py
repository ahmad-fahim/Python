# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 19:11:41 2018

@author: fahim.ahmad
"""

########## User input ################

user_input_number = int(input("Input a Number : "))

#### Check prime #########
prime_flag = 1
check_upto = int(user_input_number/2)+1

#print (user_input_number)
#print (check_upto)

for check_number in range(2, check_upto):
    #print("In loop" , user_input_number % check_number , user_input_number, check_number)
    if user_input_number % check_number == 0 :
        prime_flag = 0
        break
    
##########Prime number result #######    

if prime_flag == 1 :
    print("The number is prime")
else:
    print("The number is not prime")
    
####### End Prime check ##############

    
####### Armstong number ##############

digit_count = 0
temp_user_input_number = user_input_number

while temp_user_input_number > 0 :
    temp_user_input_number = int(temp_user_input_number / 10)
    digit_count += 1;
    
print("Number of digit", digit_count)

result_number = 0
temp_user_input_number = user_input_number

while temp_user_input_number >= 1 :
    mod_user_input_number = temp_user_input_number % 10
    #print("Mod value" , mod_user_input_number)
    temp_user_input_number = int(temp_user_input_number / 10)
    #print("Divisor value" , temp_user_input_number)
    digit_sum = pow(mod_user_input_number, digit_count)
    #print("Digit sum value" , digit_sum)
    result_number = result_number +  digit_sum
    #print (result_number)
    
print("Total digit sum :",result_number)

######## Armstong number Result ######
if result_number == user_input_number :
    print ("It is a Armstong number")
else:
    print ("It is not a Armstong number")

