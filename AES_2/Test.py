# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:24:10 2019

@author: fahim.ahmad
"""

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


output = gmul(14,int("B6", 16)) ^ gmul(11,int("8A", 16)) ^ gmul(13,int("34", 16)) ^ gmul(9,int("E8", 16)) 



print(output)