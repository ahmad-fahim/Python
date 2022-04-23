# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:59:43 2019

@author: fahim.ahmad
"""

def Ch (p_e, p_f, p_g ):
    final_result = ""
    for ind in range (0, 1):
        
        temp_e = p_e[ind]
        temp_f = p_f[ind]
        temp_g = p_g[ind]
  
        _1st_part = str(int(temp_e) & int(temp_f))

        if temp_e == "1":
            temp_e = "0"
        else:
            temp_e = "1"
        _2nd_part = str(int(temp_e) & int(temp_g))
        #print(_1st_part , _2nd_part)
        if _1st_part == _2nd_part :
            result = "0"
        else:
            result = "1"
        final_result = final_result + result
    
    return  final_result

def modulo_64(p_1st_number , p_2nd_number):
    v_1st_number_int = int(p_1st_number, 2)
    
    v_2nd_number_int = int(p_2nd_number, 2)
    
    v_2pow_64 = pow (2,64)
    
    
    result = (v_1st_number_int + v_2nd_number_int) % v_2pow_64
    
    
    
    result_in_bin = "{0:b}".format(result)
    print(result_in_bin)
    result_in_bin = result_in_bin.zfill(64)
    print (v_1st_number_int,v_2nd_number_int, result , result_in_bin)

def biswise_circular_right_shift_n_bit(p_str, p_n_bit):

    p_str = str(p_str)
    print(p_str)
    #p_str = p_str[2:len(p_str)-2]
    print(p_str)
    #print(p_str, p_n_bit, len(str(p_str)))
    
    for ind in range (0,p_n_bit):
        p_str = p_str[len(str(p_str)) - 1] + p_str[0:len(str(p_str)) - 1] 
    
    print(p_str)
    #return p_str
    
biswise_circular_right_shift_n_bit("1011001000110111100101101011000100110100100011010100001011101111", 1)



















