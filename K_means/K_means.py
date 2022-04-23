# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:18:26 2018

@author: fahim.ahmad
"""

from PIL import Image
import random
import math
import operator
import numpy as np



def print_new_image():
        
    #### Printing the New Image
            
    print_pixel = []    
    for pixel_values_list_loop in range(0, len(pixel_values_list)):
        #print(pixel_values_list_loop, pixel_values_list[pixel_values_list_loop][3+user_K])
        width_position = int(pixel_values_list_loop / width)
        height_position = pixel_values_list_loop % width
        
        R = int((255/user_K) * pixel_values_list[pixel_values_list_loop][3+user_K])
        G = int((255/user_K) * pixel_values_list[pixel_values_list_loop][3+user_K])
        B = int((255/user_K) * pixel_values_list[pixel_values_list_loop][3+user_K])
        final_pixel_value = (height_position, width_position, (R,G,B))
        print_pixel.append(final_pixel_value)
        
    final_img = Image.new( 'RGB', (width,height), "white")
    img_data = final_img.load()
    for x, y, color in print_pixel:
        img_data[x,y] = color
        
    final_img.save(output_file )
        
    



##### Getting the file name from the User


import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

image_name = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

output_file = image_name[0:-4] + ".bmp"

### Read the image 

#image_name = "IMG_20180120_172824"
im = Image.open(image_name , "r")

pixel_values = list(im.getdata())

#pixel_values_list = list(list(x) for x in pixel_values)

#print(pixel_values_list)

width, height = im.size


### Getting the K value from the User

user_K = int(input("Input the value of K : "))

K_list = []

### Getting the random values
### Putting the random values into a list
for loop_iterator in range(0, user_K ):
    K_list.append((random.randint(0,len(pixel_values))))
    
K_list = sorted(K_list)

### Putting the random RGB values in a list    
dist_pix_value = []
for loop_K in K_list:
    dist_pix_value.append ( pixel_values[loop_K])



print(dist_pix_value)

### Loop to traverse while the distance of previous list and the current list
### Does not match 

while True:
        
    ### Putting all the RGB values in a list
    
    pixel_values_list = list(list(x) for x in pixel_values)
    
    ### Loop for K times to get different distances
    
    for current_Centroid_value in dist_pix_value:
        #### Calculating the distance from each RGB values to the  current_Centroid_value
        for loop_counter in range(0, len(pixel_values)):
            distance = round(math.sqrt(((current_Centroid_value[0] - pixel_values[loop_counter][0]) ** 2) + ((current_Centroid_value[1] - pixel_values[loop_counter][1])**2) + ((current_Centroid_value[2] - pixel_values[loop_counter][2])**2)),2)
            
            ### getting the RGB value of pixel_values_list in a variable    
            init_value = pixel_values_list[loop_counter]
            ### Concatinating the init_value and the distance
            
            merge_value = init_value + [distance]
                    
            #### Finally putting the merge_value in the list again. Lets A RGB value is 
            ### (127, 210, 23) and the distance from the 1st current_Centroid_value is 
            ### 23.52. Then the final value in the pixel_values_list[loop_counter] will be 
            ### (127, 210, 23, 23.52). Again, for the 2nd current_Centroid_value, if the distance 
            ### is 12.76, then in the 2nd loop the value of pixel_values_list[loop_counter] will
            ### be (127, 210, 23, 23.52, 12.76)
            pixel_values_list[loop_counter] = merge_value
            
    
    ######## 
    
    
    for loop_counter in range(0, len(pixel_values)):
        ### Puting only the distances into the dummy_list for a specific RGB
        dummy_list = pixel_values_list[loop_counter][3:3+user_K]
        ### Getting the minimum distance value of the dummy_list to identify the cluster
        min_value_index, min_value = min(enumerate(dummy_list), key=operator.itemgetter(1))
        
        ### Concatinating the cluster(min_value_index) with the items(RGB and the distances)
        ### Let one of our item in the list is (127, 210, 23, 23.52, 12.76) where R = 127
        ### G = 210, B = 23 and Distance0 = 23.52 and Distance1 = 12.76. As Distance1 is smallest
        ### We are putting the 1 with the list and the list will look like 
        ### (127, 210, 23, 23.52, 12.76, 1)
        init_value = pixel_values_list[loop_counter]
        merge_value = init_value + [min_value_index]
        pixel_values_list[loop_counter] = merge_value

        
    cluster_array = []
    
    for item in range (0, len(pixel_values_list)):
        cluster_array.append(pixel_values_list[item][3+user_K])
        
        
    unique, counts = np.unique(cluster_array, return_counts=True)
        

    value_list = list(zip(unique,counts))
    
    R_sum = 0
    G_sum = 0
    B_sum = 0
    
    calculated_pixel_value = []
    
    ### Generating the New RGB value
    
    
    for loop_counter in range(0, len(value_list)):
        
        R_sum = 0 
        G_sum = 0
        B_sum = 0
        
        for pixel_values_list_lookup in range(0, len(pixel_values_list)):
            
            if value_list [loop_counter][0] == pixel_values_list [pixel_values_list_lookup][3+user_K]:
                
                R_sum += pixel_values_list[pixel_values_list_lookup][0]
                G_sum += pixel_values_list[pixel_values_list_lookup][1]
                B_sum += pixel_values_list[pixel_values_list_lookup][2] 
        R_avg_value = round(R_sum / value_list[loop_counter][1], 0)
        G_avg_value = round(G_sum / value_list[loop_counter][1], 0)
        B_avg_value = round(B_sum / value_list[loop_counter][1], 0)
        
        single_item_list = [R_avg_value, G_avg_value, B_avg_value]
        calculated_pixel_value.append(single_item_list)
        
    
    
    ### Sorting the New Centroid_value to compare with the last one
    calculated_pixel_value.sort(key=operator.itemgetter(1))
    ### Sorting the Old Centroid_value to compare with the last one
    dist_pix_value.sort(key=operator.itemgetter(1))
    
    print("New RGB = ", calculated_pixel_value)
    print("Old RGB = ", dist_pix_value)
    
    ### Checking to exit the loop
    
    if calculated_pixel_value == dist_pix_value :
        print("Game Over")
        print_new_image()
        #print(pixel_values_list)
        break
    else:
        print("\nKhela hobe\n")
        print_new_image()
        dist_pix_value = calculated_pixel_value
        #print(dist_pix_value)
        
        #print(value_list[loop_counter], avg_value)
        
'''        
#### Printing the New Image
        
print_pixel = []    
for pixel_values_list_loop in range(0, len(pixel_values_list)):
    #print(pixel_values_list_loop, pixel_values_list[pixel_values_list_loop][3+user_K])
    width_position = int(pixel_values_list_loop / width)
    height_position = pixel_values_list_loop % width
    
    R = int((255/user_K) * pixel_values_list[pixel_values_list_loop][3+user_K])
    G = int((255/user_K) * pixel_values_list[pixel_values_list_loop][3+user_K])
    B = int((255/user_K) * pixel_values_list[pixel_values_list_loop][3+user_K])
    final_pixel_value = (height_position, width_position, (R,G,B))
    print_pixel.append(final_pixel_value)
    
final_img = Image.new( 'RGB', (width,height), "white")
img_data = final_img.load()
for x, y, color in print_pixel:
    img_data[x,y] = color
    
final_img.save(output_file )
'''    