# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:18:08 2018

@author: fahim.ahmad
"""


from __future__ import print_function
import pandas as pd
import numpy as np
import operator
import itertools


def Number_of_findings(p_search_list) :
    
    p_count = 0
    
    for search_index in range (0 , len(train_data)):
            
        
        #print(p_search_list , train_data[search_index])    
        if (all(i in train_data[search_index] for i in p_search_list)) :
            #print("Found\n")
            p_count += 1
    
    if p_count >= support_count:
        final_list.append((p_search_list, p_count))        
    return p_count

store_data = pd.read_csv('GroceryStoreDataSet.csv', sep= ',', header= None, error_bad_lines=False)



train_data = store_data.values[:,:] 
print(train_data)
#print(train_data[0:len(train_data)])

C1 = []

for total_row in range (0, len(train_data)):
    for total_column in range (0, 4):
        if str(train_data[total_row][total_column]) != str("nan"):
            #print(train_data[total_row][total_column])
            C1.append((train_data[total_row][total_column]).strip())
        
#print(C1)

unique, counts = np.unique(C1, return_counts=True)

print(unique, counts)

tup = tuple(zip(unique,counts))
#print(tup)



C1 = [list(x) for x in tup]

#print(C1)

final_list = []
L1 = []

support_count = int(input("Enter the support count : "))


for C1_list_traverse in range (0, len(C1)):
    if C1[C1_list_traverse][1] >= support_count:
        #C1_list.append()
        L1.append([C1[C1_list_traverse][0], C1[C1_list_traverse][1]])
    
L1.sort(key=operator.itemgetter(0))    
#print(L1)  

'''
L1_dummy = []
for L1_t in range (0, len(L1)):
    L1_dummy = ((L1[0], L1[1]))
    
L1_dummy = list(L1_dummy)     
'''

#print(L1)

final_list = final_list + L1 



L2 = []

for L1_traverse in range(0, len(L1)):
    total_found = 0 
    for L1_traverse_2 in range(L1_traverse + 1 , len(L1)):
        #print(L1[0])
        L1_len = len(L1[0])
        #print(L1_len)
        
        data_from_first_list = L1[L1_traverse][0:1]
        
        data_from_second_list = L1[L1_traverse_2][0:1]
        
        
        #merged = list(itertools.chain(*list2d))
        
        
        dummy_list = [data_from_first_list, data_from_second_list]
        
        dummy_list = list(itertools.chain(*dummy_list))
        
        #print ("Before counting ", dummy_list)
        
        
        total_found = Number_of_findings(dummy_list)
        
        #print(dummy_list)
        #print(total_found)
        if total_found >= support_count:
            L2.append((dummy_list, total_found))
            
#print(L2)
            
L2 = list(L2)            

#final_list = final_list + L2

        
        #if (all(i in a for i in b)) 
#print( L2[0][0] , len(L2[0][0]) )
        
L3 = []

print(L2)
for L2_traverse in range(0, len(L2)):
    total_found = 0 
    for L2_traverse_2 in range(L2_traverse + 1 , len(L2)):
        
        L2_len = len(L2[0][0])
        #print(L2[L2_traverse][:1], L2[L2_traverse_2][:1])
        
        string_1 = L2[L2_traverse][0]
        string_2 = L2[L2_traverse_2][0]
        print(L2[L2_traverse])
        print(string_1, string_2)
        string_1 =  string_1[0:L2_len-1]
        string_2 =  string_2[0:L2_len-1]
        
        print(string_1, string_2)
        if string_1 == string_2:
                
            # >>> results_union = set().union(*results_list)

            print(string_1, string_2)
            
            #dummy_list = [L2[L2_traverse][0] + L2[L2_traverse_2][0]]
            print(L2[L2_traverse][0:L2_len-1] , L2[L2_traverse_2][0:L2_len-1] )
            
            #dummy_list = tuple(set(L2[L2_traverse][0:L2_len-1]  + L2[L2_traverse_2][0:L2_len-1]))
            
            #print (dummy_list)
            
            data_from_first_list =  list(L2[L2_traverse][0:L2_len-1])
            data_from_second_list =  list(L2[L2_traverse_2][0:L2_len-1] )
            
            print (data_from_first_list , data_from_second_list)
            
            dummy_list = list(set().union(data_from_first_list,data_from_second_list ))
            #dummy_list = list(set().union(data_from_first_list,data_from_second_list ))
            total_found = Number_of_findings(dummy_list)
            
            
            #print(dummy_list, total_found )
            #print(total_found)
            
            if total_found >= support_count:
                L3.append((dummy_list, total_found))


                
#final_list = final_list + L3

for final_list_traverse in range (0, len(final_list)):
    print(final_list[final_list_traverse][0], final_list[final_list_traverse][1])            
        
        
    