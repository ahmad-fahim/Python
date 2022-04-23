# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:18:08 2018

@author: fahim.ahmad
"""


from __future__ import print_function
import pandas as pd
import numpy as np
import operator



final_list = []

def get_the_SC_value(p_item_list):
    
    return_sc_value = 0
    
    for final_list_iterator in range(0 , len(final_list)):
        dummy_list = []
        
        if isinstance(final_list[final_list_iterator][0], str):
            dummy_list.append(final_list[final_list_iterator][0])
        else:
            dummy_list = final_list[final_list_iterator][0]
        dummy_list.sort(key=operator.itemgetter(0)) 
        
        #print(dummy_list , p_item_list)
    
        if dummy_list == p_item_list:
            return_sc_value = final_list[final_list_iterator][1]
            return return_sc_value
            
    return return_sc_value

def Number_of_findings(p_search_list) :
    
    p_count = 0
    
    for search_index in range (0 , len(train_data)):
          
        if (all(i in train_data[search_index] for i in p_search_list)) :
            #print("Found\n")
            p_count += 1
            
    return p_count

store_data = pd.read_csv('GroceryStoreDataSet.csv', sep= ',', header= None)

train_data = store_data.values[:,:] 
print(train_data)

C1 = []

for total_row in range (0, len(train_data)):
    for total_column in range (0, 4):
        if str(train_data[total_row][total_column]) != str("nan"):
            C1.append(train_data[total_row][total_column])

unique, counts = np.unique(C1, return_counts=True)

tup = tuple(zip(unique,counts))

C1 = [list(x) for x in tup]

L1 = []

support_count = int(input("Enter the support count : "))

minimum_confidence = int(input("Enter how much minimum confidence required : "))

for C1_list_traverse in range (0, len(C1)):
    if C1[C1_list_traverse][1] >= support_count:
        #C1_list.append()
        L1.append([str(C1[C1_list_traverse][0]), C1[C1_list_traverse][1]])
        
L1 = [list(x) for x in L1]    

L1.sort(key=operator.itemgetter(0))    

for L1_t in range (0, len(L1)):
    final_list.append(list(L1[L1_t]))  
  
L2 = []

for L1_traverse in range(0, len(L1)):
    total_found = 0 
    for L1_traverse_2 in range(L1_traverse + 1 , len(L1)):
        dummy_list = [L1[L1_traverse][0], L1[L1_traverse_2][0]]
        total_found = Number_of_findings(dummy_list)
        

        if total_found >= support_count:
            L2.append((dummy_list, total_found))
            
 
L2 = [list(x) for x in L2]           

final_list = final_list + L2
        
L3 = []

for L2_traverse in range(0, len(L2)):
    total_found = 0 
    for L2_traverse_2 in range(L2_traverse + 1 , len(L2)):
        
        string_1 = L2[L2_traverse][0]
        string_2 = L2[L2_traverse_2][0]
        
        string_1 =  string_1[0]
        string_2 =  string_2[0]
        
        if string_1 == string_2:
                
            
            dummy_list = list(set().union(L2[L2_traverse][0],L2[L2_traverse_2][0] ))
            
            dummy_list.sort() 
            
            total_found = Number_of_findings(dummy_list)

            if total_found >= support_count:
                L3.append((dummy_list, total_found))
L3 = [list(x) for x in L3]                 
final_list = final_list + L3

#print(final_list)

for final_list_traverse in range (0, len(final_list)):
    print(final_list_traverse , final_list[final_list_traverse][0], final_list[final_list_traverse][1])            


while True:
    n_of_user_item_buy = int(input("Number of items the customer bought : "))
    n_of_user_item_would_buy = int(input("Number of items the customer would buy : "))
    
    
    if n_of_user_item_buy == 0 or n_of_user_item_would_buy == 0:
        break
    
    item_bought = []
    item_would_buy = []
    
    for item_index in range(0, n_of_user_item_buy):
        item = input("Enter the item name the customer bought : ")
        item_bought.append(item)
    
    
    
    for item_index in range(0, n_of_user_item_would_buy):
        item = input("Enter the item name the coutomer probabily buy : ")
        item_would_buy.append(item)
        
    #print(item_bought)
    #print(item_would_buy)
    
    comb_item_list = item_bought + item_would_buy
    
    comb_item_list.sort()   
    
    #print(comb_item_list)
    
    #print(get_the_SC_value(comb_item_list))
    
    #print(get_the_SC_value(item_bought))
    
    customer_buy_SC = get_the_SC_value(item_bought)
    
    customer_buy_expected = get_the_SC_value(comb_item_list)
    
    if customer_buy_SC == 0 :
        print("Customer didn't buy any item like this combination\n")
        
    else:
        confidence = round((customer_buy_expected / customer_buy_SC) * 100,2)
        
        print(confidence)
        
        if confidence >= minimum_confidence :
            print("Confidence is" , confidence ,". So, association rule",item_bought, "->" , item_would_buy ,"  is selected.\n")
        else:
            print("Confidence is " , confidence ,"So, association rule",item_bought, "->" , item_would_buy ,"  is Rejected.\n")
        
