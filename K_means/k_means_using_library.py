import numpy as np 
import matplotlib.pyplot as plt 
import cv2 

#%matplotlib inline 

# Read in the image 
image = cv2.imread('2009_02.jpg') 
  
# Change color to RGB (from BGR) 
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
  
plt.imshow(image)

# Reshaping the image into a 2D array of pixels and 3 color values (RGB) 
pixel_vals = image.reshape((-1,3)) 

# Convert to float type 
pixel_vals = np.float32(pixel_vals)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 1000, 0.85) 
k = 5
retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 1000, cv2.KMEANS_RANDOM_CENTERS) 
centers = np.uint8(centers)  
centers = sorted(centers, key = lambda x: (x[1]))
centers = np.array(centers)

segmented_data = centers[labels.flatten()] 

segmented_image = segmented_data.reshape((image.shape)) 

plt.imshow(segmented_image)
height, width, channels = image.shape

print(height, width, channels)

# int((255/user_K) * pixel_values_list[pixel_values_list_loop][3+user_K])

print_pixel = [] 
comp_segmented_data =[]
com_centers = []
for ind in range(0,len(segmented_data)):
    
    width_position = int(ind / width)
    height_position = ind % width
    
    for ind_centers in range(0,len(centers)):
        comp_segmented_data = segmented_data[ind]
        com_centers = centers[ind_centers]
        
        comparison = comp_segmented_data == com_centers 
        equal_arrays = comparison.all() 
        if equal_arrays == True:
            #print(ind,ind_centers, comp_segmented_data, com_centers)
            pixel = ind_centers
            break
            
    R = int((255/k) * pixel)
    G = B = R
    segmented_data[ind][0] = R
    segmented_data[ind][1] = G        
    segmented_data[ind][2] = B 
    
    final_pixel_value = (height_position, width_position, (R,G,B))
    print_pixel.append(final_pixel_value)
    
    
segmented_image = segmented_data.reshape((image.shape)) 

plt.imshow(segmented_image)

unique, counts = np.unique(segmented_data, return_counts=True)   
value_list = list(zip(unique,counts))

for ind in range (0, len(value_list)):
    print(value_list[ind][1])
    
from PIL import Image
output_file = "output_2009_02.bmp"

final_img = Image.new( 'RGB', (width,height), "white")
img_data = final_img.load()
for x, y, color in print_pixel:
    img_data[x,y] = color
    
final_img.save(output_file )
