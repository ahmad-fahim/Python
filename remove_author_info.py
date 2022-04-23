# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 20:07:19 2021

@author: fahim.ahmad
"""
import re




main_file = open("paper.txt", "r", encoding = 'utf-8') 
main_data_full = []
for line in main_file:
    main_data_full.append (line)
    
for loop_c in range(0, len(main_data_full)):
    result = re.sub("[\(\[].*?[\)\]]", "", main_data_full[loop_c])
    print(result)