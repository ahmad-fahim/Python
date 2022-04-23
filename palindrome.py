# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 20:14:49 2018

@author: fahim.ahmad
"""

user_string = input("Input a string : ")

user_string_len = len(user_string)

last_index = user_string_len - 1
flag = 1
search_upto = int(user_string_len / 2)
for string_traverse in range(0,search_upto):
    if user_string[string_traverse] != user_string[last_index]:
        flag = 0
        break
    else:
        last_index -= 1
    
if flag == 1:
    print("It's a palindrome")
else:
    print("It's not a palindrome")