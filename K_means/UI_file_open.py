# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:02:38 2018

@author: fahim.ahmad
"""

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

print(file_path)

'''
from tkinter import filedialog
from tkinter import *
 
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)

'''