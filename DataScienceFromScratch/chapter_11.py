# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 12:14:59 2017

@author: maadland
"""
import random

def split_data(data, prob):
    """Splits data into fractions"""
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results

def train_test_split(x, y, test_pct=.33):
    """Splits training and test where x is the label and y are the features"""
    data = zip(x, y)
    train, test = split_data(data, 1 - test_pct)
    x_train, y_train = zip(*train) #(*zip) neat trick to unzip a file
    x_test, y_test = zip(*test)
    return x_train, x_test, y_train, y_test

def raw_accuracy(tp, fp, fn, tn):
    """Calculates the raw accuracy"""
    correct = tp + tn
    total = sum((tp, fp, fn, tn))
    return correct / total

def precision(tp, fp, fn, tn):
    """Calculates the ratio of true positives to all positives"""
    return tp / (tp + fp)

def recall(tp, fp, fn, tn):
    """Calculates the percentage of all correct positives retreived"""
    return tp / (tp + fn)

def f1_score(tp, fp, fn, tn):
   """Calculates the mean of precision and recall"""
   p = precision(tp, fp, fn, tn)
   r = recall(tp, fp, fn, tn)
   return 2 * p * r / (p + r)

x = [0 if random.random() < 1 else 1 for x in range(1000)]
y = [(1, 0, 1) if random.random() < 1 else (0, 0, 1) for x in range(1000)]

x_train, x_test, y_train, y_test = train_test_split(x, y)
raw_accuracy(10, 2, 2, 10)


