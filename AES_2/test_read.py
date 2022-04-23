# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 01:13:00 2019

@author: fahim.ahmad
"""

main_data_full = []
main_file = open("Encrypted_data.txt", "r", encoding = 'utf-8') 

decryptKey=main_file.read() 
   
main_data_full = str(decryptKey)
in_string = ''.join(main_data_full)

text_in_hex = ""

for data_index in range (0,len(in_string)):
    temp_variable = str(format(ord(in_string[data_index]), "x")).zfill(2)
    text_in_hex = text_in_hex + temp_variable

for data_index in range (0, int((len(text_in_hex)/32))):
    print(text_in_hex[data_index * 32 : (data_index + 1) * 32])
