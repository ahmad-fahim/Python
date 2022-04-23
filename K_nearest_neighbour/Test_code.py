# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 23:29:04 2018

@author: fahim.ahmad
"""


from __future__ import division
import pandas as pd
from sklearn.cross_validation import train_test_split
import operator
#import math
import numpy as np

balance_data = pd.read_csv('balance_scale.csv', sep= ',', header= None)


X = balance_data.values[:, 1:5] # matrix
Y = balance_data.values[:,0] # vector



X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.1, random_state = None)

#print (X_train, "\n")
#print(X_train[0][1])
#print(len(X_train))
#print (X_test[0], "\n")
#print(len(X_test))
#print (y_train)
#print (len(y_train))


user_input = int(input("Input the value of K : "))

outfile = "output.txt"
fout = open(outfile, "w+")




for test_counter in range(0, len(X_test)):
    
    distance_array = []
    
    title_array = []
    
    for x in range (0,  len(X_train)):
        
        total_dist = 0 
        
        for y in range (0, 4):
            #print(X_train[x][y])
            
            partial_dist = pow( (X_test[test_counter][y] -  X_train[x][y]) , 2)
            
            total_dist = total_dist + partial_dist
            
            #print ( X_test[test_counter][y], X_train[x][y], (X_test[test_counter][y] -  X_train[x][y]), partial_dist, total_dist, "\n")
            
        #print(total_dist, "\n\n")
        
        total_dist = pow(total_dist, 0.5)
        #print(total_dist )
        
        #fout.write("Distance of " + str(X_test[test_counter]) + " from " + str(X_train[x]) + " index " + str(x) + " is " +  str(total_dist))
        #fout.write("\n")
        
        #total_data = zip(y_train[x],str(total_dist))
        
        distance_array.append((y_train[x], total_dist))

        distance_array.sort(key=operator.itemgetter(1))
        
        
    #print(distance_array)
    
    
    for item in range (0, user_input):
        title_array.append(distance_array[item][0])
        
    #print(title_array)
    
    unique, counts = np.unique(title_array, return_counts=True)
    
    
    tup = tuple(zip(unique,counts))
    print(tup)
    
    tup_2 = list(tup)
    
    
    
    tup_2.sort(key=operator.itemgetter(1), reverse=True)
    
    print(tup_2)
    
    print(str(X_test[test_counter]))
    print(tup_2[0][0])
    
    fout.write("The title of " + str(X_test[test_counter]) + " is " +  tup_2[0][0])
    fout.write("\n")
                   
        
fout.close()        
        