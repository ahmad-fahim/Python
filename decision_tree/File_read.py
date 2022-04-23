# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 09:33:37 2018

@author: fahim.ahmad
"""
import random
huge_list = []
sum= 0 
f = open("balance_scale.txt", "r+")
data = f.read()
#for line in data:
huge_list.extend(data.split('\n'))


#print(huge_list[1][1])


total_line = len(huge_list)

group_len = int(total_line / 10)

print(group_len)

random_number = random.sample(range(0, total_line), group_len)

#print(random_number)
 
for i in random_number :
	print(i, huge_list[i])


print("sadkfhaksd")


for i in range(1,total_line):
	if i not in random_number :
		print(i, huge_list[i])


#for word in huge_list :
#    print(word)
        
f.close()
