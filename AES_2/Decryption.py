# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 00:06:27 2019

@author: fahim.ahmad
"""

import numpy as np
import copy as cp
import math

def get_binary_str( p_single_key ):
    _128_binary_value = ""
    for key_values in range(0, len(p_single_key)) :
        test_value = str(p_single_key[key_values])
        binary_value = bin(int(test_value, 16))[2:].zfill(4)
        _128_binary_value = str(_128_binary_value) + str(binary_value)
        #print (test_value + " = " + binary_value)
        
    return _128_binary_value

def bitwise_xor (p_main_data , p_key_data):
    output_data = ""
    for calc_bit in range(0, len(p_main_data)):
        main_data_bit = p_main_data[calc_bit] 
        key_data_bit = p_key_data[calc_bit] 
        
        if main_data_bit == key_data_bit :
            output_bit = "0"
        else:
            output_bit = "1"
        
        output_data = output_data + output_bit
    return output_data

def gmul(a, b):
    p = 0
    for c in range(8):
        if b & 1:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11b
        b >>= 1
    return p

inv_sBox = (
        "52", "09", "6A", "D5", "30", "36", "A5", "38", "BF", "40", "A3", "9E", "81", "F3", "D7", "FB",
        "7C", "E3", "39", "82", "9B", "2F", "FF", "87", "34", "8E", "43", "44", "C4", "DE", "E9", "CB",
        "54", "7B", "94", "32", "A6", "C2", "23", "3D", "EE", "4C", "95", "0B", "42", "FA", "C3", "4E",
        "08", "2E", "A1", "66", "28", "D9", "24", "B2", "76", "5B", "A2", "49", "6D", "8B", "D1", "25",
        "72", "F8", "F6", "64", "86", "68", "98", "16", "D4", "A4", "5C", "CC", "5D", "65", "B6", "92",
        "6C", "70", "48", "50", "FD", "ED", "B9", "DA", "5E", "15", "46", "57", "A7", "8D", "9D", "84",
        "90", "D8", "AB", "00", "8C", "BC", "D3", "0A", "F7", "E4", "58", "05", "B8", "B3", "45", "06",
        "D0", "2C", "1E", "8F", "CA", "3F", "0F", "02", "C1", "AF", "BD", "03", "01", "13", "8A", "6B",
        "3A", "91", "11", "41", "4F", "67", "DC", "EA", "97", "F2", "CF", "CE", "F0", "B4", "E6", "73",
        "96", "AC", "74", "22", "E7", "AD", "35", "85", "E2", "F9", "37", "E8", "1C", "75", "DF", "6E",
        "47", "F1", "1A", "71", "1D", "29", "C5", "89", "6F", "B7", "62", "0E", "AA", "18", "BE", "1B",
        "FC", "56", "3E", "4B", "C6", "D2", "79", "20", "9A", "DB", "C0", "FE", "78", "CD", "5A", "F4",
        "1F", "DD", "A8", "33", "88", "07", "C7", "31", "B1", "12", "10", "59", "27", "80", "EC", "5F",
        "60", "51", "7F", "A9", "19", "B5", "4A", "0D", "2D", "E5", "7A", "9F", "93", "C9", "9C", "EF",
        "A0", "E0", "3B", "4D", "AE", "2A", "F5", "B0", "C8", "EB", "BB", "3C", "83", "53", "99", "61",
        "17", "2B", "04", "7E", "BA", "77", "D6", "26", "E1", "69", "14", "63", "55", "21", "0C", "7D")

key_file = open("New_Key.txt", "r") 


main_data_full = []

key_list = []
rev_key_list = []

for line in key_file:
    key_list.extend(line.split())
    
for key_ind in range (10, -1, -1):
    #print(key_list[key_ind])
    rev_key_list.append(key_list[key_ind])

main_file = open("Encrypted_data.txt", "r", encoding = 'utf-8') 


ciphertext_in_text_full = ""

decryptKey=main_file.read() 
main_data = []   
main_data_full = str(decryptKey)
in_string = ''.join(main_data_full)

text_in_hex = ""

for data_index in range (0,len(in_string)):
    temp_variable = str(format(ord(in_string[data_index]), "x")).zfill(2)
    text_in_hex = text_in_hex + temp_variable
    
text_in_hex_full = cp.deepcopy( text_in_hex)

for data_index in range (0, int((len(text_in_hex)/32))):
    print(text_in_hex_full[data_index * 32 : (data_index + 1) * 32])
    
    text_in_hex = text_in_hex_full[data_index * 32 : (data_index + 1) * 32]


    ####### Add round key for round 0 ####################    
    print("Round 0 \n")
    main_data_in_binary = get_binary_str(text_in_hex)
    key_data_in_binary = get_binary_str(rev_key_list[0]) 
    
    data_after_adding_round_key = bitwise_xor(main_data_in_binary , key_data_in_binary)
    
    final_hex = str("{0:0>4X}".format(int(data_after_adding_round_key, 2))).zfill(32)
    print("After adding round key")
    print(final_hex)
    
    invCiphertext = np.chararray (shape = (4, 4),itemsize=2, unicode = True)
    
    ind_x = 0
    ind_y = 0
    for matrix_gen in range(0, 16):
        temp_variable = final_hex[matrix_gen * 2 : (matrix_gen+1) * 2]
        invCiphertext [ind_y][ind_x] = temp_variable    
        ind_y = ind_y + 1
        if ind_y > 3 :
            ind_y = 0
            ind_x = ind_x + 1
        
    print(invCiphertext)
        
    invCiphertext_bak = cp.deepcopy( invCiphertext)
    
    for round in range (1, 11):
        print("\nRound " + str(round)+ "\n")
        
        ########## Inverse Shift Row Started ###########
        
        for row_traverse in range (1, 4):
            if row_traverse == 1 :
                for column_traverse in range (0,4):
                    column = (column_traverse + 1) % 4
                    invCiphertext [row_traverse][column] = invCiphertext_bak[row_traverse][column_traverse]
                    
            if row_traverse == 2 :
                for column_traverse in range (0,4):
                    column = (column_traverse + 2) % 4
                    invCiphertext [row_traverse][column] = invCiphertext_bak[row_traverse][column_traverse]
                    
            if row_traverse == 3 :
                for column_traverse in range (0,4):
                    column = (column_traverse + 3) % 4
                    invCiphertext [row_traverse][column] = invCiphertext_bak[row_traverse][column_traverse]
                    
        print ("After Shift Row \n")
        print (invCiphertext)
        
        ############# End of Shift Row ###########
        
        ############# Inverse S box Substitute ##################
        invCiphertext_bak = cp.deepcopy( invCiphertext)
        
        for list_x in range (0,4):
            for list_y in range(0,4):
                single_byte = str(invCiphertext [list_x][list_y])
                inv_SBox_index = int(single_byte[0], 16) * 16 + int(single_byte[1], 16)
                invCiphertext [list_x][list_y] = inv_sBox[inv_SBox_index]
                
        print("After Substitute ")        
        print(invCiphertext)
        
        ################# End of Inverse S box Substitute #############
        
        
        ############# Adding Round Key ################
        
        main_data_in_binary = ""
        for x in range(0,4):
            for y in range(0,4):
                main_data_in_binary = main_data_in_binary + invCiphertext[y][x]
    
        key_data_in_binary = rev_key_list[round]
        
        print (main_data_in_binary , key_data_in_binary )
        
        main_data_in_binary = get_binary_str(main_data_in_binary)
        key_data_in_binary = get_binary_str(key_data_in_binary) 
    
        data_after_adding_round_key = bitwise_xor(main_data_in_binary , key_data_in_binary)
        
        #data_after_adding_round_key = data_after_adding_round_key.zfill(32)
        #print(data_after_adding_round_key)
        final_hex = "{0:0>4X}".format(int(data_after_adding_round_key, 2))
        final_hex = final_hex.zfill(32)
        print("After adding round key ")  
        print(final_hex)
        
        ############# End of Adding Round Key ###############
        
        
        ############### Matrix Conversion #######
        temp_index = 0
        for list_x in range (0,4):
            for list_y in range(0,4):
                invCiphertext [list_y][list_x] = final_hex[temp_index * 2:(temp_index + 1)*2]
                temp_index += 1
        print("In Matrix ")        
        print(invCiphertext)
        ############### Matrix Conversion #######
        
        invCiphertext_bak = cp.deepcopy(invCiphertext)
        
        if round != 10:
            ############ Inverse MixColumn #####################
            for list_x in range (0,4):
                invCiphertext[0][list_x] = str(str(hex(gmul(14, int(invCiphertext_bak [0][list_x], 16) ) ^ gmul(11,int(invCiphertext_bak[1][list_x], 16)) ^ gmul(13,int(invCiphertext_bak[2][list_x], 16)) ^ gmul(9,int(invCiphertext_bak[3][list_x], 16))))[2:4]).zfill(2)
                invCiphertext[1][list_x] = str(str(hex(gmul(9,int(invCiphertext_bak [0][list_x], 16)) ^ gmul(14,int(invCiphertext_bak [1][list_x], 16)) ^ gmul(11,int(invCiphertext_bak [2][list_x], 16)) ^ gmul(13,int(invCiphertext_bak [3][list_x], 16))))[2:4]).zfill(2)            
                invCiphertext[2][list_x] = str(str(hex(gmul(13,int(invCiphertext_bak [0][list_x], 16)) ^ gmul(9,int(invCiphertext_bak [1][list_x], 16)) ^ gmul(14,int(invCiphertext_bak [2][list_x], 16)) ^ gmul(11,int(invCiphertext_bak [3][list_x], 16))))[2:4]).zfill(2)            
                invCiphertext[3][list_x] = str(str(hex(gmul(11,int(invCiphertext_bak [0][list_x], 16)) ^ gmul(13,int(invCiphertext_bak [1][list_x], 16)) ^ gmul(9,int(invCiphertext_bak [2][list_x], 16)) ^ gmul(14,int(invCiphertext_bak [3][list_x], 16))))[2:4]).zfill(2)
            print ("After MixColumn")
            print(invCiphertext)
            invCiphertext_bak = cp.deepcopy( invCiphertext)
            ################# End of Inverse MixColumn #################
    print ("Final Ciphertext in Text ")        
    print (invCiphertext)
    
    ciphertext_in_text = ""
    
    for x in range (0 , 4):
        for y in range(0,4):
            letter_in_hex =   invCiphertext[y][x]
            
            byte_in_text = chr(int(letter_in_hex, 16))
            ciphertext_in_text += byte_in_text
            print(letter_in_hex, byte_in_text)
            
    #print(ciphertext_in_text)
    ciphertext_in_text_full = ciphertext_in_text_full + ciphertext_in_text

ciphertext_in_text_full = ciphertext_in_text_full.strip()    
print(ciphertext_in_text_full)



