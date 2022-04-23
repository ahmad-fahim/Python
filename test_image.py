# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:26:11 2018

@author: fahim.ahmad
"""

#import nupmy as np
from PIL import Image

image_name = "0292"

test_im = Image.open(image_name + ".JPG", "r")

width, height = test_im.size

final_img = Image.new( 'RGB', (width,height), "white")


#final_img.save("Fahim.bmp") 

print(width, height)

test_pixel_values = list(test_im.getdata())

test_pixel_values_len = len(test_pixel_values)

fout = open("probability_ratio_output.txt", "r") 

huge_list = []

for line in fout:
    huge_list.extend(line.split())
    
#f=open('Fahim.bmp','w')

print_pixel = []


for loop_counter in range (0,test_pixel_values_len):
    tuple_value = test_pixel_values[loop_counter]
    index_value = (tuple_value[0] * (256**2)) + (tuple_value[1] * 256) + tuple_value[2]
    ratio_value = int(eval(huge_list[index_value]))
    
    width_position = int(loop_counter / width)
    height_position = loop_counter % width
    
    
    if ratio_value > 0.2 :
        final_pixel_value = (height_position, width_position, (tuple_value[0],tuple_value[1],tuple_value[2]))
        #final_pixel_value = (height_position, width_position, (255,255,255))
        print_pixel.append(final_pixel_value)
    else:
        final_pixel_value = (height_position, width_position, (255,255,255))
        #final_pixel_value = (height_position, width_position, (0,0,0))
        print_pixel.append(final_pixel_value)
    
    #print_pixel = print_pixel + final_pixel_value

#print(print_pixel)

basic_index = 0


img_data = final_img.load()
for x, y, color in print_pixel:
    img_data[x,y] = color
    
final_img.save(image_name + ".bmp")

'''
for x in range(0, width):
    for y in range(0, height):
        
        list_item = print_pixel[basic_index]
        
        final_img[x][y] = ( list_item[0],list_item[1],list_item[2])
        basic_index += 1
'''
    #print(ratio_value)
#final_img.save("Fahim.bmp")
#f.close()  
fout.close()
      