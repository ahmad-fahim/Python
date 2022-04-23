# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 11:01:53 2018

@author: fahim.ahmad
"""
from __future__ import division
import pandas as pd
from sklearn.cross_validation import train_test_split
import math


def Calculate_the_Entropy(Data_set, total_train_count):
    
    distinct_values = ''
    
    list_len = len(Data_set)
    
    for traverse_list in range(1,list_len ):
        #value_int = int(line_word[traverse_list])  
        if Data_set[traverse_list] not in distinct_values:
            distinct_values =  distinct_values + Data_set[traverse_list];
            
    print ("\ndistinct values are :")   
    for distinct_values_print in range (0, len(distinct_values)):
        print(distinct_values[distinct_values_print], " ")
    print ("\n")   
    
    
    total_Entropy = 0 
    
    id_counter = 0 
    for id in distinct_values:
        id_counter = 0
        for traverse_list in range(1,list_len):
            if (  str(id) == Data_set[traverse_list] ):
                id_counter = id_counter + 1
        
        
        # calculate the probability
        
        item_probability = id_counter / total_train_count
        
        #print(item_probability)
        
        item_Entropy = (-1) * item_probability * math.log(item_probability,2)
        
        total_Entropy = total_Entropy + item_Entropy
        
        print ("Entropy of ",str(id) , " = ", item_Entropy)
        
        if id_counter > 0 :
            print("Item ", id , " have " ,id_counter, " entity") 
    
    
    print("Total Entropy is = " ,total_Entropy)
    
    return total_Entropy
    



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
#print (y_test)






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

###### Root node Entropy calculation finished






used_attribute = []


for tree_attribute in range(0, 4):
    

    best_gain = 0
    best_attribute = None
    
    training_data = []
    for attribute_ittarator in range(0, 4): # 4 means the total attribute
        
        if attribute_ittarator not in used_attribute:
            print(used_attribute)
        
            for line in range (1,len(checkpoints_from_file)):
                #print(checkpoints_from_file[line][1])
                append_value = checkpoints_from_file[line][attribute_ittarator]
                append_value = append_value.replace("[","")
                append_value = append_value.replace("]","")
                training_data.append(append_value)
                #print(checkpoints_from_file[line][attribute_ittarator])
            
            #print(training_data)
         
            child_Entropy =  Calculate_the_Entropy(training_data, total_train_count)
            
            print(attribute_ittarator, "th node Entropy is = ", child_Entropy)
            
            gain = parent_Entropy - child_Entropy 
            
            print(attribute_ittarator, "th node gain is = ", gain)
            if gain >= best_gain:
                best_gain, best_attribute, last_used_entropy = gain , attribute_ittarator, child_Entropy
        
    print ("Best gain is ", best_gain , " for attaribute ", best_attribute )
    
    used_attribute.append(best_attribute)
    
    parent_Entropy = last_used_entropy
    
    print("\nlast_used_entropy = ", last_used_entropy)
    
    
    print("\n\n\n\n\n\n Finished an itteration\n\n\n\n\n")


