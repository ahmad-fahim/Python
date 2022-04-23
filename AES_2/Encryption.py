# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:56:41 2019

@author: fahim.ahmad
"""
import numpy as np
import copy as cp

import math 


    

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


def fn_4_byte_xor(p_1st_byte, p_2nd_byte, p_3rd_byte, p_4th_byte):
    
    
    #print(p_1st_byte, p_2nd_byte, p_3rd_byte, p_4th_byte)
    
    bin_1st_byte = bin(int(str(p_1st_byte), 16))[2:].zfill(8)
    bin_2nd_byte = bin(int(str(p_2nd_byte), 16))[2:].zfill(8)
    bin_3rd_byte = bin(int(str(p_3rd_byte), 16))[2:].zfill(8)
    bin_4th_byte = bin(int(str(p_4th_byte), 16))[2:].zfill(8)
    
    
    resulted_byte = bitwise_xor(bin_1st_byte, bin_2nd_byte)
    resulted_byte = bitwise_xor( resulted_byte, bin_3rd_byte )
    resulted_byte = bitwise_xor( resulted_byte, bin_4th_byte )
    
    resulted_hex = binary_to_hex(resulted_byte)
    
    return resulted_hex

def binary_to_hex (p_bin_value):   
    first_part = p_bin_value[:4]
    temp = int(first_part, 2)
    first_part_in_hex = hex(temp)
    second_part = p_bin_value[4:8]
    temp = int(second_part, 2)
    second_part_in_hex = hex(temp)
    return str(first_part_in_hex[2:]).upper()+ str(second_part_in_hex[2:]).upper()

def binary_to_SBox_index_number (p_bin_value):
    #print (p_bin_value)
    
    first_part = p_bin_value[:4]
    temp = int(first_part, 2)    
    ind_number = temp * 16    
    second_part = p_bin_value[4:8]
    temp = int(second_part, 2)
    ind_number = ind_number + temp
    
    #print(ind_number)   
    
    return ind_number




def get_binary_str( p_single_key ):
    _128_binary_value = ""
    for key_values in range(0, len(p_single_key)) :
        test_value = str(p_single_key[key_values])
        binary_value = bin(int(test_value, 16))[2:].zfill(4)
        _128_binary_value = str(_128_binary_value) + str(binary_value)
        #print (test_value + " = " + binary_value)
        
    return _128_binary_value


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
    
def mul_by_3 (p_byte):
    first_part = mul_by_2(p_byte)
    
    #print(first_part)
    
    decimal_first =int(first_part,16)
    decimal_second=int(p_byte,16)
    
    #print("decimal_first " + str(decimal_first))
    #print("decimal_second " + str(decimal_second))
    
    
    final_decimal = decimal_first ^ decimal_second
    final_decimal = hex(final_decimal).split('x')[-1]
    
    return final_decimal
    
    
    

key_file = open("New_Key.txt", "r", encoding = 'utf-8') 
main_file = open("Main_Text.txt", "r" , encoding = 'utf-8') 


ciphertext_in_text_full = ""
main_data_full = []
for line in main_file:
    main_data_full.extend(line.split("\n"))
    
key_list = []
    
for line in key_file:
    key_list.extend(line.split())


print(main_data_full)

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


main_data_full = str(main_data_full)

main_data_full = main_data_full[2 : len(main_data_full) - 2]

print(main_data_full, int(len(main_data_full) / 16))

for text_traverse in range (0, int(math.ceil (len(main_data_full) / 16)) ):
    print(text_traverse*16, (text_traverse + 1) * 16)
    print("Main data from whole data " + main_data_full[ text_traverse*16 :(text_traverse + 1) * 16])
    main_data = main_data_full[ text_traverse*16 :(text_traverse + 1) * 16]
    
    


    ciphertext = np.chararray(shape = (4, 4),itemsize=2, unicode=True)
    ciphertext_bak = np.chararray(shape = (4, 4),itemsize=2, unicode=True)
    
    
    in_string = ''.join(main_data)
    
    
    in_string = in_string.ljust(16)
    
     
    
    
    
    text_in_hex = in_string.encode("utf-8").hex()
    print("Main Data")
    print(text_in_hex)
    main_data_in_binary = get_binary_str(text_in_hex)
    print(main_data_in_binary)
    
    print("Key Data", key_file)
    
    for round in range(0,11) :
        if round == 0 :
            print(key_list[round] )
            
            single_key = key_list[round]
            
            key_data_in_binary = get_binary_str(single_key) 
            print(key_data_in_binary)
            
            data_after_adding_round_key = bitwise_xor(main_data_in_binary , key_data_in_binary)
            print("\nAfter first adding round key \n")
            print (data_after_adding_round_key)
            print("{0:0>4X}".format(int(data_after_adding_round_key, 2)))
            print(str("{0:0>4X}".format(int(data_after_adding_round_key, 2))).zfill(16))
            
            
            
        else:
             
            print ("\nRound " + str(round) + " started")
            
            ######################## Substitute byte (string divition) ##############
            start = 1
            end = 17
            str_size = 8
            #print("\n")
            matrix_x = 0 
            matrix_y = 0
            Substituted_data = ""
            #print(data_after_adding_round_key + " -------------- ")
            for part_of_bin_data_ind in range(start , end):
                part_of_bin_data = data_after_adding_round_key[start - 1 :str_size * part_of_bin_data_ind ]
    
                start = start + 8
                hex_value = binary_to_hex (part_of_bin_data)
                #print("Main Data -->> " + hex_value)
                
                
                hex_value_ind = binary_to_SBox_index_number(part_of_bin_data)
                
                ciphertext[matrix_x][matrix_y] = str(Sbox[hex_value_ind])
                matrix_x = matrix_x + 1
                if matrix_x > 3 :
                    matrix_x = 0
                    matrix_y = matrix_y + 1
                
            
            ciphertext_bak =  cp.deepcopy(ciphertext)
            print ("\n")
            print ("After Substitute byte \n")
            print (ciphertext)
            
                
            ################## End of Substitute byte ###############
            
            ########## Shift Row Started ###########
            
            for row_traverse in range (1, 4):
                if row_traverse == 1 :
                    for column_traverse in range (0,4):
                        column = (column_traverse + 3) % 4
                        ciphertext [row_traverse][column] = ciphertext_bak[row_traverse][column_traverse]
                        
                if row_traverse == 2 :
                    for column_traverse in range (0,4):
                        column = (column_traverse + 2) % 4
                        ciphertext [row_traverse][column] = ciphertext_bak[row_traverse][column_traverse]
                        
                if row_traverse == 3 :
                    for column_traverse in range (0,4):
                        column = (column_traverse + 1) % 4
                        ciphertext [row_traverse][column] = ciphertext_bak[row_traverse][column_traverse]
                        
            print ("After Shift Row \n")
            print (ciphertext)
            
            ############# End of Shift Row ###########
            
            
            if  round != 10 :
                    
                
                ##### Mix Column Started ############
                
                ciphertext_bak =  cp.deepcopy(ciphertext)
        
                ciphertext[0][0] = fn_4_byte_xor( mul_by_2( ciphertext_bak[0][0]) , mul_by_3( ciphertext_bak[1][0]) , ciphertext_bak[2][0] , ciphertext_bak[3][0])
                ciphertext[0][1] = fn_4_byte_xor( mul_by_2( ciphertext_bak[0][1]) , mul_by_3( ciphertext_bak[1][1]) , ciphertext_bak[2][1] , ciphertext_bak[3][1])
                ciphertext[0][2] = fn_4_byte_xor( mul_by_2( ciphertext_bak[0][2]) , mul_by_3( ciphertext_bak[1][2]) , ciphertext_bak[2][2] , ciphertext_bak[3][2])
                ciphertext[0][3] = fn_4_byte_xor( mul_by_2( ciphertext_bak[0][3]) , mul_by_3( ciphertext_bak[1][3]) , ciphertext_bak[2][3] , ciphertext_bak[3][3])
                ciphertext[1][0] = fn_4_byte_xor( ciphertext_bak[0][0] , mul_by_2( ciphertext_bak[1][0]) , mul_by_3( ciphertext_bak[2][0]) , ciphertext_bak[3][0])
                ciphertext[1][1] = fn_4_byte_xor( ciphertext_bak[0][1] , mul_by_2( ciphertext_bak[1][1]) , mul_by_3( ciphertext_bak[2][1]) , ciphertext_bak[3][1])
                ciphertext[1][2] = fn_4_byte_xor( ciphertext_bak[0][2] , mul_by_2( ciphertext_bak[1][2]) , mul_by_3( ciphertext_bak[2][2]) , ciphertext_bak[3][2])
                ciphertext[1][3] = fn_4_byte_xor( ciphertext_bak[0][3] , mul_by_2( ciphertext_bak[1][3]) , mul_by_3( ciphertext_bak[2][3]) , ciphertext_bak[3][3])
                ciphertext[2][0] = fn_4_byte_xor( ciphertext_bak[0][0] , ciphertext_bak[1][0] , mul_by_2( ciphertext_bak[2][0]) , mul_by_3( ciphertext_bak[3][0]))
                ciphertext[2][1] = fn_4_byte_xor( ciphertext_bak[0][1] , ciphertext_bak[1][1] , mul_by_2( ciphertext_bak[2][1]) , mul_by_3( ciphertext_bak[3][1]))
                ciphertext[2][2] = fn_4_byte_xor( ciphertext_bak[0][2] , ciphertext_bak[1][2] , mul_by_2( ciphertext_bak[2][2]) , mul_by_3( ciphertext_bak[3][2]))
                ciphertext[2][3] = fn_4_byte_xor( ciphertext_bak[0][3] , ciphertext_bak[1][3] , mul_by_2( ciphertext_bak[2][3]) , mul_by_3( ciphertext_bak[3][3]))
                ciphertext[3][0] = fn_4_byte_xor( mul_by_3( ciphertext_bak[0][0]) , ciphertext_bak[1][0] , ciphertext_bak[2][0] , mul_by_2( ciphertext_bak[3][0]))
                ciphertext[3][1] = fn_4_byte_xor( mul_by_3( ciphertext_bak[0][1]) , ciphertext_bak[1][1] , ciphertext_bak[2][1] , mul_by_2( ciphertext_bak[3][1]))
                ciphertext[3][2] = fn_4_byte_xor( mul_by_3( ciphertext_bak[0][2]) , ciphertext_bak[1][2] , ciphertext_bak[2][2] , mul_by_2( ciphertext_bak[3][2]))
                ciphertext[3][3] = fn_4_byte_xor( mul_by_3( ciphertext_bak[0][3]) , ciphertext_bak[1][3] , ciphertext_bak[2][3] , mul_by_2( ciphertext_bak[3][3]))    
                    
                #print("\n")  
                print("\n")
                print("After Mix Column\n") 
                
                print(ciphertext)    
                    
                #################### End of Mix Column #############
                
            
            ################# Adding round key Started #########
            main_data_in_binary = ""
            for x in range(0,4):
                for y in range(0,4):
                    main_data_in_binary = main_data_in_binary + ciphertext[y][x]
                    
            
            key_data_in_binary = key_list[round]
            print("\nmain_data " + main_data_in_binary)
            print("key_data  " + key_data_in_binary)
            main_data_in_binary = get_binary_str(main_data_in_binary)
            key_data_in_binary = get_binary_str(key_data_in_binary) 
            data_after_adding_round_key = bitwise_xor(main_data_in_binary , key_data_in_binary)
            final_hex = "{0:0>4X}".format(int(data_after_adding_round_key, 2))
            print("\nAfter Adding round key \n")
            print("final_hex " + final_hex)
            
            ################# End of Adding round key Started #########

    ciphertext_in_text = ""
    
    for output_traverse in range (0 , 16):
        letter_in_hex =   final_hex[output_traverse * 2: (output_traverse+1) * 2]
        #print(letter_in_hex)       
        byte_in_text = chr(int(letter_in_hex, 16))
        print(int(letter_in_hex, 16), chr(int(letter_in_hex, 16)))
        ciphertext_in_text += byte_in_text
        
    ciphertext_in_text_full = ciphertext_in_text_full + ciphertext_in_text 
    
output_file = open("Encrypted_data.txt", "w+", encoding = 'utf-8')
    
output_file.write(str(ciphertext_in_text_full))

key_file.close()
main_file.close()
output_file.close()
