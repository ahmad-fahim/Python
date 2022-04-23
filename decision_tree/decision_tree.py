# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:21:02 2018

@author: uzzal.hossain
"""
import numpy as np;
import pandas as pd
from sklearn.cross_validation import train_test_split;
from sklearn.tree import DecisionTreeClassifier;
from sklearn.metrics import accuracy_score;
from sklearn import tree;
import random;
from math import log;

def unique_value(array):
    unique, counts = np.unique(array, return_counts=True)
    dic = tuple(zip(unique,counts))
    return dic;


def Entropy_Calculate(array):
    ### Unique Value Count
    #unique_value = pd.unique(array)
    #print(pd.value_counts(pd.Series(array)))
    #new_array = np.asarray(pd.value_counts(pd.Series(array)))
    unique, counts = np.unique(array, return_counts=True)
    tup = tuple(zip(unique,counts))
    length = len(array)
    print(tup)
    print(length)
    entropy = 0;
    item_probability=[]
    item_entropy = []
    for item in tup:
        item_probability.append(item[1]/length)
        ip = item[1]/length
        entropy = entropy + (-1)*ip*log(ip,2)
        #print("Item Probability for ",item[0]," is ",ip)
        
        #print("Item Probability for ",item[0]," is ",item[1]/length)
    print("Item Entropy is ",entropy)
    
    for ip in item_probability:
        item_entropy.append((-1)*ip*log(ip))
        #total_entropy +=
        #print(ip)
    #Entropyitem
    #for pi in item_entropy:
        #print(pi)
    return entropy




balance_data = pd.read_csv('balance_scale.csv',sep=',',header=None);

print("Length of Data : ",len(balance_data));
print("Shape of data : ",balance_data.shape);
print("Balace Data Head\n");
#print(balance_data.head())

A = np.squeeze(np.asarray(balance_data.values[:,1:5]))

X = balance_data.values[:, 1:5];

Y = balance_data.values[:,0];



#print(Y)
#unique_elements, counts_elements = np.unique(Y, return_counts=True)
#print(np.asarray((unique_elements, counts_elements)))
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.1, random_state = None);

parent_entropy = Entropy_Calculate(y_train)

print("Parent entropy is = ", parent_entropy)

best_gain = -999999
bset_attribute = 0


Z = pd.unique(X_train[:,2])
#print(pd.value_counts(pd.Series(X_train[:,0])))
#print(Z[2])
for i in range(0, 4):
    child_entropy = Entropy_Calculate(X_train[:,i])
    child_gain = parent_entropy - child_entropy
    
    if child_gain > best_gain :
        best_gain, bset_attribute = child_gain, i
    
    print("Info gain is = ", child_gain)
    
print(best_gain, i)

print("End")