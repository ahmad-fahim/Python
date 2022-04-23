# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:15:25 2018

@author: fahim.ahmad
"""
from PIL import Image
import numpy as np


from os import listdir
from os.path import isfile, join

from decimal import *




onlyfiles = [f for f in listdir("E:\Personal Information\Python\Sceen_detection\ibtd\ibtd") if isfile(join("E:\Personal Information\Python\Sceen_detection\ibtd\ibtd", f))]

#print(onlyfiles)

file_list = []

for filename in onlyfiles:
    if filename.endswith('.jpg'):
        file_list.append(filename)
        
#print(file_list)
        
mask_dir = "E:\Personal Information\Python\Sceen_detection\ibtd\ibtd\Mask"


#### Initialization of the 3D array with value 0 
skin_value_counter = np.zeros(shape= (256, 256, 256), dtype= int)
non_skin_value_counter = np.zeros(shape= (256, 256, 256), dtype= int)

skin_prob_array = []
non_skin_prob_array = []




total_non_skin_value_counter = 0
total_skin_value_counter = 0


for file in file_list:
        
    print(file)

    im = Image.open(file, 'r')
    width, height = im.size
    
    only_file_name = file.replace(".jpg", ".bmp")
    
    #mask_im = Image.open(mask_dir + only_file_name )
    mask_file_name = mask_dir + "\\"+ only_file_name 
    
    #print(mask_file_name)
    
    mask_im = Image.open(mask_file_name, "r")
    
    
    mask_pixel_values = list(mask_im.getdata())
    
    main_pixel_values = list(im.getdata())
    
    #print(mask_pixel_values)
    
    #print(main_pixel_values)
     
    for loop_counter in range (0,len(mask_pixel_values)):
        
        tuple_value = mask_pixel_values[loop_counter]
        #print(tuple_value)
        
        #print(tuple_value)
        
        if tuple_value[0] > 220 and tuple_value[1] > 220 and tuple_value[2] > 220:
            main_tuple_value = main_pixel_values[loop_counter]
            #print("--------------------non skin", main_tuple_value)
            #print("non skin" , main_pixel_values[loop_counter])
            non_skin_value_counter[main_tuple_value[0]] [main_tuple_value[1]] [main_tuple_value[2]] += 1
            total_non_skin_value_counter += 1
        else:
            main_tuple_value = main_pixel_values[loop_counter]
            #print("--------------------skin" , main_tuple_value)
            #print("skin" , main_pixel_values[loop_counter])
            skin_value_counter[main_tuple_value[0]][main_tuple_value[1]][main_tuple_value[2]] += 1
            total_skin_value_counter += 1
        #value_counter[tuple_value[0]][tuple_value[1]][tuple_value[2]] += 1
    im.close()
    mask_im.close()
    
fout_non_skin = open("non_skin_value_counter.txt", "w+")
fout_skin = open("skin_value_counter.txt", "w+")


for i in range(0,256):
    for j in range(0, 256):
        for k in range (0, 256):
            getcontext().prec = 28
            single_entity_probability = Decimal(non_skin_value_counter[i][j][k] / total_non_skin_value_counter) #non_skin_value_counter[i][j][k] / total_non_skin_value_counter
            non_skin_prob_array.append(single_entity_probability)
            single_entity_probability =  Decimal(skin_value_counter[i][j][k] / total_skin_value_counter)
            skin_prob_array.append(single_entity_probability)
            
            #fout_non_skin.write(str(i) + " " +  str(j) + " " + str(k) + " " + str(non_skin_value_counter[i][j][k]) + " " + str(single_entity_probability) + "\n" )
'''                
for i in range(0,256):
    for j in range(0, 256):
        for k in range (0, 256):
            getcontext().prec = 28
            single_entity_probability =  Decimal(skin_value_counter[i][j][k] / total_skin_value_counter)
            skin_prob_array.append(single_entity_probability)
            #fout_skin.write(str(i) + " " +  str(j) + " " + str(k) + " " + str(skin_value_counter[i][j][k]) + " " + str(single_entity_probability) + "\n")
'''              
print("Sum of non_skin_value_counter = ",total_non_skin_value_counter)               
print("Sum of skin_value_counter = ", total_skin_value_counter)  

final_outfile = open("probability_ratio_output.txt", "w+")

for skin_prob_array_counter, non_skin_prob_array_counter in zip(skin_prob_array, non_skin_prob_array):
    if non_skin_prob_array_counter > 0: 
        final_value = round(float(skin_prob_array_counter) / float(non_skin_prob_array_counter), 2)
    else: 
        final_value = 0.0
    final_outfile.write(str(final_value) + "\n")

fout_non_skin.close()
fout_skin.close()    
final_outfile.close()

print("End")    