# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 21:07:12 2019

@author: fahim.ahmad
"""

import random

def mul_by_2 (p_byte):
    
    #b=hex(p_byte)
    decimal=int(p_byte,16)
    #print(decimal)
    
    decimal = decimal << 1
    #print (decimal)
    if decimal > 255 :
        decimal = (decimal - 256) ^ int('1B', 16)
    #print (decimal)
    
    in_hex = hex(decimal).split('x')[-1]
    
    return in_hex


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

def binary_to_hex (p_bin_value):
    #print (p_bin_value)
    
    first_part = p_bin_value[:4]
    temp = int(first_part, 2)
    
    first_part_in_hex = hex(temp)
    
    second_part = p_bin_value[4:8]
    temp = int(second_part, 2)

    second_part_in_hex = hex(temp)
    
    return str(first_part_in_hex[2:]).upper()+ str(second_part_in_hex[2:]).upper()

Sbox = ("63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76",
        "CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0",
        "B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15",
        "04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75",
        "09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84",
        "53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF",
        "D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8",
        "51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2",
        "CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73",
        "60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB",
        "E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79",
        "E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08",
        "BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A",
        "70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E",
        "E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF",
        "8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"
        )

rcon = None

def g (p_word, p_round_number):
    left_shift_byte = p_word[2:8] + p_word[0:2]
    
    print("\nLeft Shift Value = " + left_shift_byte)
    
    print("\n")
    
    Substitution_Byte = ""
    for traverse_left_shift_byte in range(0,4):
        test_byte = left_shift_byte [traverse_left_shift_byte*2:(traverse_left_shift_byte + 1) * 2]
        print("Main value = " + test_byte)
        test_Substitution_Byte = int(test_byte[0], 16) * 16 + int(test_byte[1], 16)
        #int(test_byte[0], 16)
        print("Substitution value = " + Sbox[test_Substitution_Byte])
        Substitution_Byte = Substitution_Byte + Sbox[test_Substitution_Byte]
    print(Substitution_Byte)
    
    bin_1st_byte = bin(int(str(Substitution_Byte[0:2]), 16))[2:].zfill(8)
    basic_rcon = "01"
    for loop_counter in range (0, p_round_number-1):
        basic_rcon = mul_by_2(basic_rcon)
        
        
    print("basic_rcon " + basic_rcon)
    
    
    bin_2nd_byte = bin(int(str(basic_rcon), 16))[2:].zfill(8)
    print(bin_2nd_byte)
    
    resulted_byte = bitwise_xor(bin_1st_byte, bin_2nd_byte)
    resulted_hex = binary_to_hex(resulted_byte)
    
    final_value = resulted_hex + Substitution_Byte[2:8]
    
    return final_value
        
   
    
key_value = ""
for i in range(16):
    key_value = key_value + (chr(random.randrange(65,90)))
    
print(key_value)

#key_value = "I am Fahim Ahmad"
key_text = key_value.encode("utf-8").hex()

print(key_text)

fout_key = open("New_Key.txt", "w+")
fout_key.write(key_text)
fout_key.write("\n")

for key_gen_round in range (1, 11):
        
    print("Round " + str(key_gen_round))
    print(key_text)
    
    
    w_0 = key_text[ 0 :  8 ]
    w_1 = key_text[ 8 : 16 ]
    w_2 = key_text[16 : 24 ]
    w_3 = key_text[24 : 32 ]
    
    
    print(w_0, w_1, w_2, w_3)
    
    w_4 = g(w_3, key_gen_round)
     
    resulted_byte = bitwise_xor(str(bin(int(str(w_0), 16))[2:].zfill(8)).zfill(32), str(bin(int(str(w_4), 16))[2:].zfill(8)).zfill(32))
    resulted_hex = "{0:0>4X}".format(int(resulted_byte, 2))
    
    w_4 = resulted_hex 
    
    #w_5 = 
    #print(w_4)
    
    resulted_byte = bitwise_xor(str(bin(int(str(w_4), 16))[2:].zfill(8)).zfill(32), str(bin(int(str(w_1), 16))[2:].zfill(8)).zfill(32))
    resulted_hex = "{0:0>4X}".format(int(resulted_byte, 2))
    
    w_5 = resulted_hex 
    #print(w_5)
    
    resulted_byte = bitwise_xor(str(bin(int(str(w_5), 16))[2:].zfill(8)).zfill(32), str(bin(int(str(w_2), 16))[2:].zfill(8)).zfill(32))
    resulted_hex = "{0:0>4X}".format(int(resulted_byte, 2))
    
    w_6 = resulted_hex
    #print(w_6)
    
    resulted_byte = bitwise_xor(str(bin(int(str(w_6), 16))[2:].zfill(8)).zfill(32), str(bin(int(str(w_3), 16))[2:].zfill(8)).zfill(32))
    resulted_hex = "{0:0>4X}".format(int(resulted_byte, 2))
    
    w_7 = resulted_hex
    #print(w_7)
    
    print("------- " + w_4.zfill(8) + w_5.zfill(8) + w_6.zfill(8) + w_7.zfill(8))
    print("\n")
    
    
    key_text = w_4.zfill(8) + w_5.zfill(8) + w_6.zfill(8) + w_7.zfill(8)
    fout_key.write(key_text)
    fout_key.write("\n")
    
    
    
    

fout_key.close() 
