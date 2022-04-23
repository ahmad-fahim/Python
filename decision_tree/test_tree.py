# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:52:25 2018

@author: fahim.ahmad
"""

from __future__ import print_function
import pandas as pd
from sklearn.cross_validation import train_test_split
import numpy as np
import math 

balance_data = pd.read_csv('balance_scale.csv', sep= ',', header= None)



X = balance_data.values[:, 1:5] # matrix
Y = balance_data.values[:,0] # vector

training_data = []


def unique_vals(rows, col):
    """Find the unique values for a column in a dataset."""
    return set([row[col] for row in rows])


def class_counts(rows):
    """Counts the number of each type of example in a dataset."""
    counts = {}  # a dictionary of label -> count.
    for row in rows:
        # in our dataset format, the label is always the last column
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def is_numeric(value):
    """Test if a value is numeric."""
    return isinstance(value, int) or isinstance(value, float)


class Question:
    """A Question is used to partition a dataset.

    This class just records a 'column number' (e.g., 0 for Color) and a
    'column value' (e.g., Green). The 'match' method is used to compare
    the feature value in an example to the feature value stored in the
    question. See the demo below.
    """

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        # This is just a helper method to print
        # the question in a readable format.
        condition = "=="
        if is_numeric(self.value):
            condition = ">="
        return "Is %s %s %s?" % (header[self.column], condition, str(self.value))
        
def partition(rows, question):
    """Partitions a dataset.

    For each row in the dataset, check if it matches the question. If
    so, add it to 'true rows', otherwise, add it to 'false rows'.
    """
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


def Calculate_the_Entropy(Data_set ):
    
    unique, counts = np.unique(Data_set, return_counts=True)
    
    tup = tuple(zip(unique,counts))
    length = len(Data_set)

    total_entropy = 0 
    
    for item in tup:
        item_probability = item[1]/length
        item_Entropy = (-1)*item_probability*math.log(item_probability,2)
        total_entropy = total_entropy + item_Entropy

    return total_entropy


def info_gain(left, right, current_uncertainty):
    """Information Gain.

    The uncertainty of the starting node, minus the weighted impurity of
    two child nodes.
    """
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * Calculate_the_Entropy(left) - (1 - p) * Calculate_the_Entropy(right)


def find_best_split(rows):
    """Find the best question to ask by iterating over every feature / value
    and calculating the information gain."""
    best_gain = 0  # keep track of the best information gain
    best_question = None  # keep train of the feature / value that produced it
    current_uncertainty = Calculate_the_Entropy(rows)
    n_features = len(rows[0]) - 1  # number of columns

    for col in range(n_features):  # for each feature

        values = set([row[col] for row in rows])  # unique values in the column

        for val in values:  # for each value

            question = Question(col, val)

            # try splitting the dataset
            true_rows, false_rows = partition(rows, question)

            # Skip this split if it doesn't divide the
            # dataset.
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            # Calculate the information gain from this split
            gain = info_gain(true_rows, false_rows, current_uncertainty)

            # You actually can use '>' instead of '>=' here
            # but I wanted the tree to look a certain way for our
            # toy dataset.
            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question


class Leaf:
    """A Leaf node classifies data.

    This holds a dictionary of class (e.g., "Apple") -> number of times
    it appears in the rows from the training data that reach this leaf.
    """

    def __init__(self, rows):
        self.predictions = class_counts(rows)
        
        
class Decision_Node:
    """A Decision Node asks a question.

    This holds a reference to the question, and to the two child nodes.
    """

    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch
        
def build_tree(rows):
    """Builds the tree.

    Rules of recursion: 1) Believe that it works. 2) Start by checking
    for the base case (no further information gain). 3) Prepare for
    giant stack traces.
    """

    # Try partitioing the dataset on each of the unique attribute,
    # calculate the information gain,
    # and return the question that produces the highest gain.
    gain, question = find_best_split(rows)

    # Base case: no further info gain
    # Since we can ask no further questions,
    # we'll return a leaf.
    if gain == 0:
        return Leaf(rows)

    # If we reach here, we have found a useful feature / value
    # to partition on.
    true_rows, false_rows = partition(rows, question)

    # Recursively build the true branch.
    true_branch = build_tree(true_rows)

    # Recursively build the false branch.
    false_branch = build_tree(false_rows)

    # Return a Question node.
    # This records the best feature / value to ask at this point,
    # as well as the branches to follow
    # dependingo on the answer.
    return Decision_Node(question, true_branch, false_branch)

def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        predicter_class = str(node.predictions)
        print (spacing + "Predict",  predicter_class[2])
        return

    # Print the question at this node
    print (spacing + str(node.question))

    # Call this function recursively on the true branch
    print (spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")

    # Call this function recursively on the false branch
    print (spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")



def classify(row, node):
    """See the 'rules of recursion' above."""

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        return node.predictions

    # Decide whether to follow the true-branch or the false-branch.
    # Compare the feature / value stored in the node,
    # to the example we're considering.
    #print
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)


def print_leaf(counts):
    """A nicer way to print the predictions at a leaf."""
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs    

def print_leaf_v2(counts):
    """A nicer way to print the predictions at a leaf."""
    total = sum(counts.values()) * 1.0
    probs = None
    for lbl in counts.keys():
        probs = str(int(counts[lbl] / total * 100))
    return probs 
    
total_accuracy = 0

for traverse_10_times in range(0,10):
    
    X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.1, random_state = None)
    
    training_data_list = []
    tup = []
    for train_data in range(0, len(X_train)):
        first_data = X_train[train_data][0]
        second_data =X_train[train_data][1]
        third_data = X_train[train_data][2]
        forth_data = X_train[train_data][3]
        fifth_data = y_train[train_data]
        
        tup.append((first_data, second_data, third_data,forth_data , fifth_data ))
        
        tup_2 = list(tup)
        
        training_data_list.append(tup_2)
        
    
    
    for item_iterator in range(1, len(training_data_list)):
        training_data = training_data_list[item_iterator]
        
    
    
    header = [ "label", "column1", "column2", "column2", "column4" ]
    
    
    my_tree = build_tree(training_data)
    
    #print_tree(my_tree)
    
    
    #print("\n\n\n End of the tree \n\n\n")
    
    
    test_data_list = []
    tup = []
    for test_data in range(0, len(X_test)):
        first_data = X_test[test_data][0]
        second_data =X_test[test_data][1]
        third_data = X_test[test_data][2]
        forth_data = X_test[test_data][3]
        fifth_data = y_test[test_data]
        
        tup.append((first_data, second_data, third_data,forth_data , fifth_data ))
        
        tup_2 = list(tup)
        
        test_data_list.append(tup_2)
        
        
    #print(training_data_list)    
    #print(len(training_data_list))
    
    for item_iterator in range(1, len(test_data_list)):
        testing_data = test_data_list[item_iterator]
    
    correct_prediction = 0 
    
    for row in testing_data:
        prediction = str(print_leaf(classify(row, my_tree)))
        index_p = prediction.find(':')
        prediction = prediction[2:index_p-1]
        print ("Actual: %s. Predicted: %s" %(row[-1], prediction))
        #print(row[-1] , str(print_leaf(classify(row, my_tree))), index_p)
        if prediction == row[-1] :
            correct_prediction += 1
            
    print("\n\nTotal correct prediction ", correct_prediction , " out of ", len(y_test) , " test data.\n")        
    accuracy = round((correct_prediction / len(y_test)) * 100, 2) 
    
    print("Accuracy is ", accuracy , "%")
    
    total_accuracy = total_accuracy + accuracy
    

print("Average Accuracy is ",round( total_accuracy/10, 2) , "%")

