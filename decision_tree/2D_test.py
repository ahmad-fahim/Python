# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 21:26:52 2018

@author: fahim.ahmad
"""
from __future__ import division
from string import punctuation
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
#import math



checkpoints_from_file = []

def read_checkpoints():
    global checkpoints_from_file
    with open("balance_scale.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            checkpoints_from_file.append(line.split(" "))
        


if __name__ == '__main__':
    read_checkpoints()
    print (checkpoints_from_file)