# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 11:01:53 2018

@author: fahim.ahmad
"""
from __future__ import division
import pandas as pd
from sklearn.cross_validation import train_test_split
import math
import numpy as np


def Calculate_the_Entropy(Data_set, total_train_count):
    
    unique, counts = np.unique(Data_set, return_counts=True)
    
    tup = tuple(zip(unique,counts))
    length = len(Data_set)
    print(tup)
    
    
    print(length)
    total_entropy = 0 
    
    for item in tup:
        item_probability = item[1]/length
        item_Entropy = (-1)*item_probability*math.log(item_probability,2)
        total_entropy = total_entropy + item_Entropy
        
        print ("Entropy of ",item[0] , " is = ", item_Entropy)
    
     
    print("Total Entropy is = " ,total_entropy)
    
    return total_entropy
    



balance_data = pd.read_csv('balance_scale.csv', sep= ',', header= None)


X = balance_data.values[:, 1:5] # matrix
Y = balance_data.values[:,0] # vector


X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.1, random_state = None)


#print (X_train)
#print(X_train[0][1])
#print(len(X_train))
#print (X_test)
#print(len(X_test))
#print (y_train)
#print (len(y_train))


outfile = "train_data.txt"
fout = open(outfile, "w+")
for word in X_train :
    fout.write(str(word))
    fout.write("\n")
    
fout.close()
    
checkpoints_from_file = []    
with open("train_data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        checkpoints_from_file.append(line.split(" "))

#print(checkpoints_from_file)
total_train_count = len (checkpoints_from_file)
print(total_train_count)

parent_Entropy = Calculate_the_Entropy(y_train, total_train_count)

print("Parent node Entropy is = ", parent_Entropy)


best_gain = -999990
best_attribute = None

training_data = []
for attribute_ittarator in range(0, 4): 
    training_data = []
    for line in range (0,len(checkpoints_from_file)):
        #print(checkpoints_from_file[line][1])
        append_value = checkpoints_from_file[line][attribute_ittarator]
        append_value = append_value.replace("[","")
        append_value = append_value.replace("]","")
        training_data.append(append_value)
        #print(checkpoints_from_file[line][attribute_ittarator])
    
    #print(training_data)
    #print(training_data)
    child_Entropy =  Calculate_the_Entropy(training_data, total_train_count)
    
    print(attribute_ittarator, "th node Entropy is = ", child_Entropy)
    
    gain = parent_Entropy - child_Entropy 
    
    print(attribute_ittarator, "th node gain is = ", gain)
    if gain >= best_gain:
        best_gain, best_attribute = gain , attribute_ittarator

print ("Best gain is ", best_gain , " for attaribute ", best_attribute  )


