# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 23:29:04 2018

@author: fahim.ahmad
"""


from __future__ import division
import pandas as pd
from sklearn.cross_validation import train_test_split
import operator
import numpy as np

###### Read the data from the dataset 

balance_data = pd.read_csv('balance_scale.csv', sep= ',', header= None)

total_accuracy = 0


#### input from the user to set the value of K

user_input = int(input("Input the value of K : "))


#### Open a file to write the output

outfile = "output.txt"
fout = open(outfile, "w+")


#### Split the data into attribute and lebel

X = balance_data.values[:, 1:5] # matrix
Y = balance_data.values[:,0] # vector


#### loop for 10 times iteration

for test_data_iterator in range (0,10):

#### Splite the data into 90% train data and 10% test data    
    X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.1, random_state = None)
    
    correct_prediction = 0
#### Loop for traversing the 10% test data one by one
    for test_counter in range(0, len(X_test)):
        
        distance_array = []
        
        title_array = []
#### Loop for traversing the 90% train data one by one to get the distance from each 
#### train data
        for x in range (0,  len(X_train)):
            
            total_dist = 0 
#### Loop to get the distance of the 4 values
            
            for y in range (0, 4):
              
                partial_dist = pow( (X_test[test_counter][y] -  X_train[x][y]) , 2)
                
                total_dist = total_dist + partial_dist

#### square root of the total value
                
            total_dist = pow(total_dist, 0.5)
            
#### Appending the distance as well as the label to a tuple

            distance_array.append((y_train[x], total_dist))

#### Sorting the tuple to get the minimum distance     

            distance_array.sort(key=operator.itemgetter(1))
            
#### getting the lowest distance upto Kth position            
        for item in range (0, user_input):
            title_array.append(distance_array[item][0])

#### Getting how many records are there in each label
        unique, counts = np.unique(title_array, return_counts=True)
        
#### Saving the values in tuple and then sorting the array in descending order to
#### get the testing data         
        tup = tuple(zip(unique,counts))
        #print(tup)
        
        tup_2 = list(tup)
        
        tup_2.sort(key=operator.itemgetter(1), reverse=True)
        
        #print(str(X_test[test_counter]))
        #print(tup_2[0][0])
        #### in the first value of the list the value will
        #### be the output value
        
#### Writing the output into a file for proper visualization
        fout.write("The title of " + str(X_test[test_counter]) + " is " +  tup_2[0][0])
        fout.write("\n")
#### Getting information to get the accuracy
        if y_test[test_counter] == tup_2[0][0]:
            correct_prediction += 1
            
    accuracy = round((correct_prediction / len(y_test)) * 100, 2)
    
    total_accuracy = total_accuracy + accuracy
#### Finding the accuracy of a single test
    fout.write("Accuracy is  " + str(accuracy) + "%" )
    fout.write("\n")
    
    print(accuracy)
        
    print("End of One Test\n\n")
    
    fout.write("\t\t End of One Test\n\n")
#### Finding the total accuracy of 10 tests                       
final_accuracy =  round(total_accuracy / 10, 2)       

fout.write("Final accuracy is  " + str(final_accuracy) + "%" )
fout.write("\n")


fout.close()        
        