# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import copy as cp



K_str = [ "428a2f98d728ae22", "7137449123ef65cd", "b5c0fbcfec4d3b2f", "e9b5dba58189dbbc", "3956c25bf348b538", 
          "59f111f1b605d019", "923f82a4af194f9b", "ab1c5ed5da6d8118", "d807aa98a3030242", "12835b0145706fbe", 
          "243185be4ee4b28c", "550c7dc3d5ffb4e2", "72be5d74f27b896f", "80deb1fe3b1696b1", "9bdc06a725c71235", 
          "c19bf174cf692694", "e49b69c19ef14ad2", "efbe4786384f25e3", "0fc19dc68b8cd5b5", "240ca1cc77ac9c65", 
          "2de92c6f592b0275", "4a7484aa6ea6e483", "5cb0a9dcbd41fbd4", "76f988da831153b5", "983e5152ee66dfab", 
          "a831c66d2db43210", "b00327c898fb213f", "bf597fc7beef0ee4", "c6e00bf33da88fc2", "d5a79147930aa725", 
          "06ca6351e003826f", "142929670a0e6e70", "27b70a8546d22ffc", "2e1b21385c26c926", "4d2c6dfc5ac42aed", 
          "53380d139d95b3df", "650a73548baf63de", "766a0abb3c77b2a8", "81c2c92e47edaee6", "92722c851482353b", 
          "a2bfe8a14cf10364", "a81a664bbc423001", "c24b8b70d0f89791", "c76c51a30654be30", "d192e819d6ef5218", 
          "d69906245565a910", "f40e35855771202a", "106aa07032bbd1b8", "19a4c116b8d2d0c8", "1e376c085141ab53", 
          "2748774cdf8eeb99", "34b0bcb5e19b48a8", "391c0cb3c5c95a63", "4ed8aa4ae3418acb", "5b9cca4f7763e373", 
          "682e6ff3d6b2b8a3", "748f82ee5defb2fc", "78a5636f43172f60", "84c87814a1f0ab72", "8cc702081a6439ec", 
          "90befffa23631e28", "a4506cebde82bde9", "bef9a3f7b2c67915", "c67178f2e372532b", "ca273eceea26619c", 
          "d186b8c721c0c207", "eada7dd6cde0eb1e", "f57d4f7fee6ed178", "06f067aa72176fba", "0a637dc5a2c898a6", 
          "113f9804bef90dae", "1b710b35131c471b", "28db77f523047d84", "32caab7b40c72493", "3c9ebe0a15c9bebc", 
          "431d67c49c100d4c", "4cc5d4becb3e42b6", "597f299cfc657e2a", "5fcb6fab3ad6faec", "6c44198c4a475817"]



def modulo_64(p_1st_number , p_2nd_number):
   
    result_in_bin = "{0:b}".format((int(p_1st_number, 2) + int(p_2nd_number, 2)) % (pow (2,64)))
    
    result_in_bin = result_in_bin.zfill(64)
    #print(result_in_bin)
    return result_in_bin


def biswise_circular_right_shift_n_bit(p_str, p_n_bit):

    p_str = str(p_str)
    p_str = p_str[2:len(p_str)-2]
    #print(p_str, p_n_bit, len(str(p_str)))
    
    for ind in range (0,p_n_bit):
        p_str = p_str[len(str(p_str)) - 1] + p_str[0:len(str(p_str)) - 1] 
    
    return p_str

def biswise_circular_left_shift_n_bit(p_str, p_n_bit):
    p_str = str(p_str)
    p_str = p_str[2:len(p_str)-2]
    #print(p_str, p_n_bit, len(str(p_str)))
    for ind in range (0,p_n_bit):
        p_str = p_str[1:len(p_str)]  + "0"
    
    return p_str


def bitwise_xor (p_data1 , p_data2):
    output_data = ""
    
    for calc_bit in range(0, len(p_data1)):
        main_data_bit = p_data1[calc_bit] 
        key_data_bit = p_data2[calc_bit] 
        
        if main_data_bit == key_data_bit :
            output_bit = "0"
        else:
            output_bit = "1"
        
        output_data = output_data + output_bit
        
    return output_data

def fi_0(x):
    data1 = biswise_circular_right_shift_n_bit(x, 1) 
    data2 = biswise_circular_right_shift_n_bit(x, 8)
    data3 = biswise_circular_left_shift_n_bit (x,7)
    final_data = bitwise_xor (data1, data2)
    final_data = bitwise_xor (final_data, data3)
    return final_data
    
def fi_1(x):
    data1 = biswise_circular_right_shift_n_bit(x, 19)
    data2 = biswise_circular_right_shift_n_bit(x, 61)
    data3 = biswise_circular_left_shift_n_bit (x,6)
    final_data = bitwise_xor (data1, data2)
    final_data = bitwise_xor (final_data, data3)
    return final_data


def gen_rest_words():
    for ind in range (16,80):
        w_t_2 = word_array[ind-2]
        w_t_7 = word_array[ind-7]
        w_t_15 = word_array[ind-15]
        w_t_16 = word_array[ind-16]

        w_t_2 = fi_1(w_t_2)
        w_t_15 = fi_0(w_t_15)
        
        w_t_7 = str(w_t_7)
        w_t_7 = w_t_7[2:len(w_t_7)-2]
        final_word = bitwise_xor(w_t_2 , w_t_7)
        final_word = bitwise_xor(final_word , w_t_15)
        w_t_16 = str(w_t_16)
        w_t_16 = w_t_16[2:len(w_t_16)-2]
        final_word = bitwise_xor(final_word , w_t_16)
        word_array[ind] = final_word
        

def padding_bits(p_str ) :
    remaining_bits = ""
    text_in_binary = ''.join( str(format(ord(x), 'b')).zfill(8) for x in p_str)    
    str_len = len(text_in_binary) 
    len_in_128_bit = '{0:0128b}'.format(str_len)
    #print(len_in_128_bit)
    total_len = str_len + 128 + 1
    
    number_of_blocks = int(total_len / 1024) + 1
    
    #print(total_len , number_of_blocks)
    total_remaining_bit = (number_of_blocks * 1024 ) - total_len 
    
    remaining_bits = "1" + "0" * total_remaining_bit
    #print(total_remaining_bit, remaining_bits)

    final_message = text_in_binary + remaining_bits + len_in_128_bit
    
    #print(final_message)
    
    return final_message


def Ch (p_e, p_f, p_g ):
    final_result = ""

    p_e = str(p_e)
    p_f = str(p_f)
    p_g = str(p_g)

    for ind in range (0, 64):
        
        temp_e = str(p_e[ind])
        temp_f = str(p_f[ind])
        temp_g = str(p_g[ind])
        #print(temp_e, temp_f, temp_g)
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
        #print(final_result)
    
    return  final_result
        
        

def sum_512_a0(p_a) :
    a_28 = biswise_circular_right_shift_n_bit(p_a, 28)
    a_34 = biswise_circular_right_shift_n_bit(p_a, 34)
    a_39 = biswise_circular_right_shift_n_bit(p_a, 39)
    
    final_bit = bitwise_xor(bitwise_xor(a_28, a_34), a_39)
    
    return final_bit


def sum_512_e1(p_a) :
    a_14 = biswise_circular_right_shift_n_bit(p_a, 14)
    a_18 = biswise_circular_right_shift_n_bit(p_a, 18)
    a_41 = biswise_circular_right_shift_n_bit(p_a, 41)
    
    final_bit = bitwise_xor(bitwise_xor(a_14, a_18), a_41)
    
    return final_bit
    

def Maj (p_a, p_b, p_c):
    final_bit = bitwise_xor(bitwise_xor(p_a, p_b), p_c)
    
    return final_bit
    


fopen = open ("Main_data.txt", "r")
#word_array = [""]

word_array = np.chararray(shape = (80, 1),itemsize=64, unicode=True)
k_str_binary = np.chararray(shape = (80, 1),itemsize=64, unicode=True)

text = fopen.read()
print (text )

padded_message = padding_bits(text)

print("Full message " + padded_message)

a = "6A09E667F3BCC908"
b = "BB67AE8584CAA73B"
c = "3C6EF372FE94F82B"
d = "A54FF53A5F1D36F1"
e = "510E527FADE682D1"
f = "9B05688C2B3E6C1F"
g = "1F83D9ABFB41BD6B"
h = "5BE0CD19137E2179"

a_bak = cp.deepcopy(a)
b_bak = cp.deepcopy(b)
c_bak = cp.deepcopy(c)
d_bak = cp.deepcopy(d)
e_bak = cp.deepcopy(e)
f_bak = cp.deepcopy(f)
g_bak = cp.deepcopy(g)
h_bak = cp.deepcopy(h)

#init_hash_buffer()


total_block = int(len(padded_message) / 1024)
print(total_block)


for ind in range (0, total_block):
    print("Message Block " + str(ind) )
    M_n = padded_message[ind*1024: (ind+1) * 1024]
    print(M_n)
    #word_array = []
    for bit_ind in range(0, 16):
        word_array[bit_ind] = M_n [ bit_ind * 64 : (bit_ind + 1) * 64 ]
    
    print("Init words " )
    #print(word_array)
    gen_rest_words ()
    #print("Testing WORDS")
    
    #print(word_array)
    
    for k_ind in range (0,80):
        k_str_binary[k_ind] = bin(int(K_str[k_ind], 16))[2:].zfill(64)
        
    
    for round in range (0,80):
    
        result_from_Ch  = Ch(bin(int(e, 16))[2:].zfill(64), bin(int(f, 16))[2:].zfill(64), bin(int(g, 16))[2:].zfill(64))
        result_from_Ch = result_from_Ch.zfill(64)
        #print(result_from_Ch)
        
        
        T1 =  modulo_64(bin(int(h, 16))[2:].zfill(64), result_from_Ch)
        T1 = T1.zfill(64)
        #print("T1")
        #print(T1)
    
        T1 =  modulo_64(T1, sum_512_e1(bin(int(e, 16))[2:].zfill(64)))
        T1 = T1.zfill(64)
    
        temp_word = str(word_array[ind])
        temp_word = temp_word[2:66]
        T1 =  modulo_64(T1, temp_word)
        T1 = T1.zfill(64)
        temp_word = str(k_str_binary[ind])
        temp_word = temp_word[2:66]
        T1 =  modulo_64(T1, temp_word)
        T1 = T1.zfill(64)
        
        temp_maj = Maj(bin(int(a, 16))[2:].zfill(64), bin(int(b, 16))[2:].zfill(64), bin(int(c, 16))[2:].zfill(64))
        temp_maj = temp_maj.zfill(64)
        
        temp_sum_512_a0 = sum_512_a0(bin(int(e, 16))[2:].zfill(64)) 
        temp_sum_512_a0 = temp_sum_512_a0.zfill(64)
        
        T2 = modulo_64(temp_sum_512_a0, temp_maj)
        
        #print(T1, T2)
    
        temp_a = str(hex(int(modulo_64(T1, T2), 2)))
        temp_a = temp_a[2:]
        #bitwise_xor(bin(int(d, 16))[2:].zfill(64), T1)
        temp_e = str(hex(int(modulo_64(bin(int(d, 16))[2:].zfill(64), T1), 2)))
        temp_e = temp_e[2:]
        #print("-----=============-----")
        #print(a, b, c, d, e, f, g, h)
        a, b, c, d, e, f, g, h = temp_a.zfill(16), a.zfill(16), b.zfill(16), c.zfill(16), temp_e.zfill(16) , e.zfill(16), f.zfill(16), g.zfill(16)
        
        print("-----=============-----")
        print("Round : " , round )
        print(a, b, c, d, e, f, g, h)


a = hex(int(modulo_64(bin(int(a, 16))[2:].zfill(64) , bin(int(a_bak, 16))[2:].zfill(64)), 2))
a = a[2:]

b = hex(int(modulo_64(bin(int(b, 16))[2:].zfill(64) , bin(int(b_bak, 16))[2:].zfill(64)), 2))
b = b[2:]

c = hex(int(modulo_64(bin(int(c, 16))[2:].zfill(64) , bin(int(c_bak, 16))[2:].zfill(64)), 2))
c = c[2:]

d = hex(int(modulo_64(bin(int(d, 16))[2:].zfill(64) , bin(int(d_bak, 16))[2:].zfill(64)), 2))
d = d[2:]

e = hex(int(modulo_64(bin(int(e, 16))[2:].zfill(64) , bin(int(e_bak, 16))[2:].zfill(64)), 2))
e = e[2:]

f = hex(int(modulo_64(bin(int(f, 16))[2:].zfill(64) , bin(int(f_bak, 16))[2:].zfill(64)), 2))
f = f[2:]

g = hex(int(modulo_64(bin(int(g, 16))[2:].zfill(64) , bin(int(g_bak, 16))[2:].zfill(64)), 2))
g = g[2:]

h = hex(int(modulo_64(bin(int(h, 16))[2:].zfill(64) , bin(int(h_bak, 16))[2:].zfill(64)), 2))
h = h[2:]

final_hash = a+ b+ c+ d+ e+ f+ g+ h


print("\n Final Hash value \n")
print(final_hash)


