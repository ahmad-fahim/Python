# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:43:14 2018

@author: fahim.ahmad
"""

def gcd(x, y):
   """This function implements the Euclidian algorithm
   to find G.C.D. of two numbers"""

   while(y):
       #print(x, y, x % y)
       x, y = y, x % y
   #print(x, y)
   return x

def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
   
def lcm_v2(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   lcm = (x*y)//gcd(x,y)
   return lcm
   
num1 = int(input("Input the first number : ") )
num2 = int(input("Input the second number: ") )
   
print("The L.C.M. of", num1,"and", num2,"is", lcm_v2(num1, num2))
print("The G.C.D. of", num1,"and", num2,"is", gcd(num1, num2))