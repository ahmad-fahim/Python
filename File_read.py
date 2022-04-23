# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 09:33:37 2018

@author: fahim.ahmad
"""

huge_list = []

f= open("hello.txt", "r+", encoding = 'utf-8') 
huge_list = f
        
#print(huge_list)

delete_list = ("of", "with", "at", "from", "into", "during", 
"including", "until", "against", "among", "throughout", "despite", 
"towards", "upon", "concerning", "to", "in", "for", "on", "by", "about", 
"like", "through", "over", "before", "between", "after", "since", "without", 
"under", "within", "along", "following", "across", "behind", "beyond", 
"plus", "except", "but", "up", "out", "around", "down", "off", "above", 
"near", "a", "an", "the")
outfile = "output.txt"
fout = open(outfile, "w+", encoding = 'utf-8')
for word in huge_list :
    if word not in delete_list :
        if word == "\n":
            #print("New Line")
            fout.write(word)
        else:
            #print("Normal word")
            fout.write(word)
        #f_out.write(delete_list)
        

fout.close()
f.close()
